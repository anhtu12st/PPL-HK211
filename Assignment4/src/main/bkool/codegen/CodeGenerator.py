from Emitter import Emitter
from functools import reduce
from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *

class MType:
  def __init__(self, partype, rettype):
    self.partype = partype
    self.rettype = rettype

class Symbol:
  def __init__(self, name, mtype, value=None, kind=None):
    self.name = name
    self.mtype = mtype
    self.value = value
    self.kind = kind

  def __str__(self):
    return "Symbol("+self.name+","+str(self.mtype)+","+str(self.value)+","+str(self.kind)+")"

@dataclass
class ClassData:
  name: str
  parentname: str
  members: List[Symbol]

class CodeGenerator:
  def __init__(self):
    self.libName = "io"

  def init(self, ast):
    genv = GlobalEnvironment().visitProgram(ast, None)
    ioMembers = [
      Symbol("readInt", MType(list(), IntType()), CName(self.libName), Static()),
      Symbol("writeInt", MType([IntType()], VoidType()), CName(self.libName), Static()),
      Symbol("writeIntLn", MType( [IntType()], VoidType()), CName(self.libName), Static()),

      Symbol("readFloat", MType(list(), FloatType()), CName(self.libName), Static()),
      Symbol("writeFloat", MType( [FloatType()], VoidType()), CName(self.libName), Static()),
      Symbol("writeFloatLn", MType( [FloatType()], VoidType()), CName(self.libName), Static()),

      Symbol("readBool", MType(list(), BoolType()), CName(self.libName), Static()),
      Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName), Static()),
      Symbol("writeBoolLn", MType( [BoolType()], VoidType()), CName(self.libName), Static()),

      Symbol("readStr", MType(list(), StringType()), CName(self.libName), Static()),
      Symbol("writeStr", MType([StringType()], VoidType()), CName(self.libName), Static()),
      Symbol("writeStrLn", MType( [StringType()], VoidType()), CName(self.libName), Static()),
    ]
    genv.append(ClassData('io', None, ioMembers))
    return genv

  def gen(self, ast, path):
    #ast: AST
    #dir_: String

    gl = self.init(ast)
    gc = CodeGenVisitor(ast, gl, path)
    gc.visit(ast, [])


class SubBody():
  def __init__(self, frame: Frame, sym: list):
    self.frame = frame
    self.sym = sym


class Access():
  def __init__(self, frame: Frame, sym: list, isLeft, isFirst=False):
    self.frame = frame
    self.sym = sym
    self.isLeft = isLeft
    self.isFirst = isFirst


class Val(ABC):
  pass


class Index(Val):
  def __init__(self, value):
    self.value = value


class Const(Val):
  def __init__(self, value):
      self.value = value


class CName(Val):
  def __init__(self, value):
    self.value = value


class CodeGenVisitor(BaseVisitor):
  def __init__(self, astTree, env, path):
    self.astTree = astTree
    self.env = env
    self.path = path

  def lookup(self,name,lst,func):
    for x in lst:
      if name == func(x):
        return x
    return None

  def visitProgram(self, ast, c):
    [self.visit(i, c)for i in ast.decl]

  def visitClassDecl(self, ast: ClassDecl, c):
    self.className = ast.classname.name
    self.currentClass = self.lookup(ast.classname.name, self.env, lambda x: x.name)
    parentName = ast.parentname.name if ast.parentname is not None else "java.lang.Object"
    self.emit = Emitter(self.path+"/" + self.className + ".j")
    self.emit.printout(self.emit.emitPROLOG(self.className, parentName))
    # Decl field for class
    [self.visit(ele, None) for ele in ast.memlist if type(ele) == AttributeDecl]
    [self.visit(ele, SubBody(None, list())) for ele in ast.memlist if type(ele) == MethodDecl]
    if "<init>" not in [ele.name.name for ele in ast.memlist if type(ele) == MethodDecl]:
      self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(), None, Block([], [])), c, Frame("<init>", VoidType()))
    self.emit.emitEPILOG()

  def genMETHOD(self, consdecl: MethodDecl, o, frame):
    isInit = consdecl.returnType is None
    isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
    returnType = VoidType() if isInit else consdecl.returnType
    methodName = "<init>" if isInit else consdecl.name.name
    intype = [ArrayType(0, StringType())] if isMain else list(map(lambda x: x.varType, consdecl.param))
    mtype = MType(intype, returnType)
    isStatic = type(consdecl.kind) is Static
    self.emit.printout(self.emit.emitMETHOD(methodName, mtype, isStatic, frame))

    frame.enterScope(True)

    glenv = o

    # Generate code for parameter declarations
    if not isStatic:
      self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(Id(self.className)), frame.getStartLabel(), frame.getEndLabel(), frame))
    elif isMain:
      self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
    else:
      local = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)]+env.sym), consdecl.param, SubBody(frame, []))
      glenv = local.sym+glenv

    body = consdecl.body
    nlenv = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)]+env.sym), body.decl, SubBody(frame, []))
    glenv = nlenv.sym + glenv
    self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
    # Generate code for statements
    if isInit:
      self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
      if self.currentClass.parentname:
        parentclass = self.lookup(self.currentClass.parentname, self.env, lambda x: x.name)
        init = self.lookup("<init>", parentclass.members, lambda x: x.name)
        parentname = self.currentClass.parentname
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame, parentname+"/<init>", init.mtype if init is not None else MType([],VoidType())))
      else:
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
      for x in self.currentClass.members:
        if type(x.mtype) is not MType and type(x.kind) is not Static and x.value is not None:
          # init field value for new instance
          self.visit(Assign(FieldAccess(SelfLiteral(),Id(x.name)),x.value), SubBody(frame, glenv))
    if isMain:
      # init static value for the first time run in main
      for classdata in self.env:
        for mem in classdata.members:
          if type(mem.mtype) is not MType and type(mem.kind) is Static and mem.value is not None:
            self.visit(Assign(FieldAccess(Id(classdata.name),Id(mem.name)),mem.value), SubBody(frame, []))

    # Load init value for vardecl
    for x in body.decl:
      if type(x) is VarDecl:
        if x.varInit is not None:
          self.visit(Assign(x.variable, x.varInit), SubBody(frame, glenv))
    list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

    self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
    if type(returnType) is VoidType:
      self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
    self.emit.printout(self.emit.emitENDMETHOD(frame))
    frame.exitScope()

  def visitMethodDecl(self, ast: MethodDecl, o):
    frame = Frame(ast.name, ast.returnType)
    self.genMETHOD(ast, o.sym, frame)

  def visitAttributeDecl(self, ast: AttributeDecl, ctx):
    kind = ast.kind
    name = ast.decl.variable.name if type(ast.decl) is VarDecl else ast.decl.constant.name
    typ = ast.decl.varType if type(ast.decl) is VarDecl else ast.decl.constType
    isFinal = type(ast.decl) is ConstDecl
    self.emit.printout(self.emit.emitATTRIBUTE(name, typ, isFinal, kind))
  def visitConstDecl(self, ast: ConstDecl, ctx):
    self.emit.printout(self.emit.emitVAR(0, ast.constant.name,\
      ast.constType, ctx.frame.getStartLabel(), ctx.frame.getEndLabel(),\
      ctx.frame))
    return Symbol(ast.constant.name, ast.constType, Const(ast.value))
  def visitVarDecl(self, ast: VarDecl, ctx: SubBody):
    idx = ctx.frame.getNewIndex()
    self.emit.printout(self.emit.emitVAR(idx, ast.variable.name,\
      ast.varType, ctx.frame.getStartLabel(), ctx.frame.getEndLabel(),\
      ctx.frame))
    return Symbol(ast.variable.name, ast.varType, Index(idx))
  def visitBlock(self, ast: Block, ctx: SubBody):
    ctx.frame.enterScope(False)
    nenv = reduce(lambda env, ele: SubBody(ctx.frame, [self.visit(ele, env)]+env.sym), ast.decl, SubBody(ctx.frame, []))
    self.emit.printout(self.emit.emitLABEL(ctx.frame.getStartLabel(), ctx.frame))
    map(lambda x: self.visit(x, SubBody(ctx.frame, ctx.sym+nenv)))
    self.emit.printout(self.emit.emitLABEL(ctx.frame.getEndLabel(), ctx.frame))
    ctx.frame.exitScope()
  def visitAssign(self, ast: Assign, ctx: SubBody):
    elc1, elt1 = self.visit(ast.lhs, Access(ctx.frame, ctx.sym, True, True))
    erc, ert = self.visit(ast.exp, Access(ctx.frame, ctx.sym, False, True))
    elc2, elt2 = self.visit(ast.lhs, Access(ctx.frame, ctx.sym, True, False))
    if elc1 is not None:
      # gen address for field access vs array access
      self.emit.printout(elc1)
    self.emit.printout(erc)
    if isinstance(ert, IntType) and isinstance(elt2, FloatType):
      self.emit.printout(self.emit.emitI2F(ctx.frame))
    self.emit.printout(elc2)
  def visitIf(self, ast: If, ctx: SubBody):
    self.emit.printout(self.visit(ast.expr, Access(ctx.frame, ctx.sym, False, True))[0])
    lb1 = ctx.frame.getNewLabel()
    lb2 = ctx.frame.getNewLabel()
    self.emit.printout(self.emit.emitIFFALSE(lb1, ctx.frame))
    self.visit(ast.thenStmt, SubBody(ctx.frame, ctx.sym))
    self.emit.printout(self.emit.emitGOTO(lb2, ctx.frame))
    self.emit.printout(self.emit.emitLABEL(lb1, ctx.frame))
    self.visit(ast.elseStmt, SubBody(ctx.frame, ctx.sym))
    self.emit.printout(self.emit.emitLABEL(lb2, ctx.frame))

  def visitFor(self, ast: For, ctx: SubBody):
    e1c, _ = self.visit(ast.expr1, Access(ctx.frame, ctx.sym, False, True))
    e2c, _ = self.visit(ast.expr2, Access(ctx.frame, ctx.sym, False, True))
    lwc, _ = self.visit(ast.id, Access(ctx.frame, ctx.sym, True, True))
    lrc, _ = self.visit(ast.id, Access(ctx.frame, ctx.sym, False, False))
    labelS = ctx.frame.getNewLabel()
    labelE = ctx.frame.getNewLabel()
    self.emit.printout(e1c)
    self.emit.printout(lwc)
    ctx.frame.enterLoop()
    self.emit.printout(self.emit.emitLABEL(labelS, ctx.frame))
    self.emit.printout(lrc)
    self.emit.printout(e2c)
    if ast.up:
      self.emit.printout(self.emit.emitIFICMPGT(labelE, ctx.frame))
    else:
      self.emit.printout(self.emit.emitIFICMPLT(labelE, ctx.frame))
    nenv = [x for x in ctx.sym]
    self.visit(ast.loop, SubBody(ctx.frame, nenv))
    self.emit.printout(self.emit.emitLABEL(ctx.frame.getContinueLabel(), ctx.frame))
    self.emit.printout(lrc)
    self.emit.printout(self.emit.emitPUSHICONST(1, ctx.frame))
    self.emit.printout(self.emit.emitADDOP('+' if ast.up else '-', IntType(), ctx.frame))
    self.emit.printout(lwc)
    self.emit.printout(self.emit.emitGOTO(labelS, ctx.frame))
    self.emit.printout(self.emit.emitLABEL(labelE, ctx.frame))
    self.emit.printout(self.emit.emitLABEL(ctx.frame.getBreakLabel(), ctx.frame))
    ctx.frame.exitLoop()
  def visitBreak(self, ast: Break, ctx: SubBody):
    self.emit.printout(self.emit.emitGOTO(ctx.frame.getBreakLabel(), ctx.frame))
  def visitContinue(self, ast: Continue, ctx: SubBody):
    self.emit.printout(self.emit.emitGOTO(ctx.frame.getContinueLabel(), ctx.frame))
  def visitReturn(self, ast: Return, ctx: SubBody):
    if not type(ctx.frame.returnType) is VoidType:
      ec, et = self.visit(ast.expr, Access(ctx.frame, ctx.sym, False, True))
      if type(ctx.frame.returnType) is FloatType and type(et) is IntType:
        ec = ec + self.emit.emitI2F(ctx.frame)
      self.emit.printout(ec)
    # self.emit.printout(self.emit.emitGOTO(ctx.frame.getEndLabel(), ctx.frame))
    self.emit.printout(self.emit.emitRETURN(ctx.frame.returnType, ctx.frame))
  def visitId(self, ast: Id, ctx: Access):
    # id found in ctx.sym (it is an instance or a variable)
    sym = self.lookup(ast.name, ctx.sym, lambda x: x.name)
    if sym is None:
      # attribute of current class
      parentclass = self.lookup(self.currentClass.parentname, self.env, lambda x: x.name)
      sym = self.lookup(ast.name, self.currentClass.members, lambda x: x.name)
      while sym is None and parentclass is not None:
        sym = self.lookup(ast.name, parentclass.members, lambda x: x.name)
        parentclass = self.lookup(parentclass.parentname, self.env, lambda x: x.name)
    if sym is None:
      # return class
      sym = self.lookup(ast.name, self.env, lambda x: x.name)
      return ast.name, ClassType(Id(ast.name))

    if ctx.isLeft:
      if ctx.isFirst:
        return None, None # TODO: update load for field access and array address
      else:
        return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, ctx.frame), sym.mtype
    else:
      # visit rhs (dont care about isFirst or not)
      if type(sym.value) is Index:
        return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, ctx.frame), sym.mtype
      elif type(sym.value) is Const:
        return self.emit.emitREADCONST(sym.value.value, sym.mtype, ctx.frame), sym.mtype
      else:
        # TODO: read static field in current class
        return self.emit.emitGETSTATIC(self.className+"."+ast.name,sym.mtype,ctx.frame), sym.mtype
 
  def visitArrayCell(self, ast: ArrayCell, ctx):
    pass
  def visitFieldAccess(self, ast: FieldAccess, ctx: Access):
    value, typ = self.visit(ast.obj, Access(ctx.frame, ctx.sym, False, True))
    classdata = self.lookup(typ.classname.name, self.env, lambda x: x.name)
    parentclass = self.lookup(classdata.parentname, self.env, lambda x: x.name)
    sym = self.lookup(ast.fieldname.name, classdata.members, lambda x: x.name)
    while sym is None and parentclass is not None:
      classdata = parentclass
      sym = self.lookup(ast.fieldname.name, classdata.members, lambda x: x.name)
      parentclass = self.lookup(classdata.parentname, self.env, lambda x: x.name)
    kind = sym.kind
    if ctx.isLeft == True:
      if ctx.isFirst:
        if type(kind) is not Static:
          return value, typ
        else:
          return None, None
      elif type(kind) is Static:
        return self.emit.emitPUTSTATIC(typ.classname.name+"."+sym.name, sym.mtype, ctx.frame), sym.mtype
      else:
        return self.emit.emitPUTFIELD(typ.classname.name+"."+sym.name, sym.mtype, ctx.frame), sym.mtype
    else:
      if type(kind) is Static:
        return self.emit.emitGETSTATIC(typ.classname.name+"."+sym.name, sym.mtype, ctx.frame), sym.mtype
      else:
        return value + self.emit.emitGETFIELD(typ.classname.name+"."+sym.name, sym.mtype, ctx.frame), sym.mtype

  def visitUnaryOp(self, ast: UnaryOp, ctx: Access):
    c,t = self.visit(ast.body)
    if ast.op == "+":
      return c,t
    if ast.op == "-":
      return c + self.emit.emitNEGOP(t, ctx.frame), t
    if ast.op == "!":
      return c + self.emit.emitNOT(t, ctx.frame), t
  def visitCallExpr(self, ast: CallExpr, ctx: Access):
    # string, typ: ClassType of instance or class
    value, typ = self.visit(ast.obj, Access(ctx.frame, ctx.sym, False, True))
    in_ = ("", [])
    # Get return type of the method
    isCallSpecial = False
    classdata = self.lookup(typ.classname.name, self.env, lambda x: x.name)
    parentclass = self.lookup(classdata.parentname, self.env, lambda x: x.name)
    sym = self.lookup(ast.method.name, classdata.members, lambda x: x.name)
    while sym is None and parentclass is not None:
      isCallSpecial = True
      classdata = parentclass
      sym = self.lookup(ast.method.name, classdata.members, lambda x: x.name)
      parentclass = self.lookup(classdata.parentname, self.env, lambda x: x.name)
    returnType = sym.mtype.rettype
    kind = sym.kind
    # Gen code for param
    for x in ast.param:
      str1, typ1 = self.visit(x, Access(ctx.frame, ctx.sym, False, True))
      in_ = (in_[0] + str1, in_[1] + [typ1])
    mtype = MType(in_[1], returnType)
    # handle static class methods
    if type(kind) is Static:
      return in_[0] + self.emit.emitINVOKESTATIC(typ.classname.name + "/" + ast.method.name, mtype, ctx.frame), mtype.rettype
    elif isCallSpecial:
      return value + in_[0] + self.emit.emitINVOKESPECIAL(ctx.frame, typ.classname.name+"/"+ast.method.name, mtype), mtype.rettype
    else:
      # handle instance method value is Index
      return value + in_[0] + self.emit.emitINVOKEVIRTUAL(typ.classname.name + "/" + ast.method.name, mtype, ctx.frame), mtype.rettype
  def visitNewExpr(self, ast: NewExpr, ctx: Access):
    emit = ""
    emit += self.emit.emitNEW(ctx.frame, ast.classname.name)
    emit += self.emit.emitDUP(ctx.frame)
    in_ = ("", [])
    for x in ast.param:
      str1, typ1 = self.visit(x, Access(ctx.frame, ctx.sym, False, True))
      in_ = (in_[0] + str1, in_[1] + [typ1])
    emit += in_[0]
    emit += self.emit.emitINVOKESPECIAL(ctx.frame, ast.classname.name+"/<init>", MType(in_[1], VoidType()))
    return emit, ClassType(Id(ast.classname.name))

  def visitCallStmt(self, ast: CallStmt, ctx: SubBody):
    # string, typ: ClassType of instance or class
    value, typ = self.visit(ast.obj, Access(ctx.frame, ctx.sym, False, True))
    in_ = ("", [])
    # Get return type of the method
    isCallSpecial = False
    classdata = self.lookup(typ.classname.name, self.env, lambda x: x.name)
    parentclass = self.lookup(classdata.parentname, self.env, lambda x: x.name)
    sym = self.lookup(ast.method.name, classdata.members, lambda x: x.name)
    while sym is None and parentclass is not None:
      isCallSpecial = True
      classdata = parentclass
      sym = self.lookup(ast.method.name, classdata.members, lambda x: x.name)
      parentclass = self.lookup(classdata.parentname, self.env, lambda x: x.name)
    returnType = sym.mtype.rettype
    kind = sym.kind
    # Gen code for param
    for x in ast.param:
      str1, typ1 = self.visit(x, Access(ctx.frame, ctx.sym, False, True))
      in_ = (in_[0] + str1, in_[1] + [typ1])
    mtype = MType(in_[1], returnType)
    # handle static class methods
    if type(kind) is Static:
      self.emit.printout(in_[0] + self.emit.emitINVOKESTATIC(typ.classname.name + "/" + ast.method.name, mtype, ctx.frame))
    elif isCallSpecial:
      self.emit.printout(value + in_[0] + self.emit.emitINVOKESPECIAL(ctx.frame, typ.classname.name+"/"+ast.method.name, mtype))
    else:
      # handle instance method value is Index
      self.emit.printout(value + in_[0] + self.emit.emitINVOKEVIRTUAL(typ.classname.name + "/" + ast.method.name, mtype, ctx.frame))

  def visitBinaryOp(self, ast: BinaryOp, ctx: Access):
    op = ast.op
    e1c, e1t = self.visit(ast.left, ctx)
    e2c, e2t = self.visit(ast.right, ctx)

    typeop = e2t
    if type(e1t) is FloatType or type(e2t) is FloatType or op == "/":
      if type(e1t) is IntType: e1c += self.emit.emitI2F(ctx.frame)
      if type(e2t) is IntType: e2c += self.emit.emitI2F(ctx.frame)
      typeop = FloatType()
    
    if op == "%":
      return e1c + e2c + self.emit.emitMOD(ctx.frame), e1t
    elif op == "\\":
      return e1c + e2c + self.emit.emitDIV(ctx.frame), e1t
    elif op == "/":
      return e1c + e2c + self.emit.emitMULOP(op,typeop,ctx.frame), typeop
    elif op == "+" or op == "-":
      return e1c + e2c + self.emit.emitADDOP(op,typeop,ctx.frame), typeop
    elif op == "*":
      return e1c + e2c + self.emit.emitMULOP(op,typeop,ctx.frame), typeop
    elif op == "&&":
      return e1c + e2c + self.emit.emitANDOP(ctx), BoolType()
    elif op == "||":
      return e1c + e2c + self.emit.emitOROP(ctx), BoolType()
    elif op in ["==", "!=", ">", "<", ">=", "<="]:
      return e1c + e2c + self.emit.emitREOP(op, e1t, ctx.frame), BoolType()
    else:
      left_str = e1c
      right_str = e2c
      return self.emit.emitCONCAT("\""+left_str[6:len(left_str)-2] + right_str[6:len(right_str)-2]+"\"", ctx.frame), StringType()

  def visitIntLiteral(self, ast, o):
    return self.emit.emitPUSHCONST(ast.value, IntType(), o.frame), IntType()
  def visitFloatLiteral(self, ast: FloatLiteral, o):
    return self.emit.emitPUSHCONST(str(ast.value), FloatType(), o.frame), FloatType()
  def visitStringLiteral(self, ast: StringLiteral, o):
    return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()
  def visitBooleanLiteral(self, ast: BooleanLiteral, o):
    return self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame), BoolType()
  def visitNullLiteral(self, ast: NullLiteral, o):
    pass
  def visitSelfLiteral(self, ast: SelfLiteral, ctx: Access):
    return self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, ctx.frame), ClassType(Id(self.className))
  def visitArrayLiteral(self, ast: ArrayLiteral, o):
    pass

class GlobalEnvironment(BaseVisitor):
  def visitProgram(self, ast: Program, o):
    self.classes = [self.visit(x, None) for x in ast.decl]
    return self.classes

  def visitClassDecl(self, ast: ClassDecl, o):
    self.currentClass = ast.classname.name
    classname = ast.classname.name
    parentname = ast.parentname.name if ast.parentname is not None else None
    members = [self.visit(x, o) for x in ast.memlist]
    return ClassData(classname, parentname, members)

  def visitMethodDecl(self, ast: MethodDecl, o):
    name = ast.name.name
    paramType = list(map(lambda x: x.varType, ast.param))
    returnType = ast.returnType
    return Symbol(name, MType(paramType, returnType), CName(self.currentClass), ast.kind)

  def visitAttributeDecl(self, ast: AttributeDecl, o):
    return self.visit(ast.decl, ast.kind)

  def visitVarDecl(self, ast: VarDecl, kind):
    name = ast.variable.name
    type = ast.varType
    value = ast.varInit
    return Symbol(name, type, value, kind)

  def visitConstDecl(self, ast: ConstDecl, kind):
    name = ast.constant.name
    type = ast.constType
    value = ast.value
    return Symbol(name, type, value, kind)
