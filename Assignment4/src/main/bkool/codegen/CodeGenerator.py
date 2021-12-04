from Emitter import Emitter
from functools import reduce
import sys
from Frame import Frame
from abc import ABC
# from Visitor import *
# from AST import *

if not './main/bkool/utils/' in sys.path:
  from main.bkool.utils.Visitor import *
  from main.bkool.utils.AST import *
else:
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
    return "Symbol("+self.name+","+str(self.mtype)+","+str(self.kind)+")"

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
    parentName = ast.parentname.name if ast.parentname is not None else "java.lang.Object"
    self.emit = Emitter(self.path+"/" + self.className + ".j")
    self.emit.printout(self.emit.emitPROLOG(self.className, parentName))
    #TODO: assume that class have only methods for now, need to update for attribute
    [self.visit(ele, SubBody(None, list())) for ele in ast.memlist if type(ele) == MethodDecl]
    if "<init>" not in list(map(lambda x: x.name.name, ast.memlist)):
      self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(), None, Block([], [])), c, Frame("<init>", VoidType()))
    self.emit.emitEPILOG()

  def genMETHOD(self, consdecl: MethodDecl, o, frame):
    isInit = consdecl.returnType is None
    isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
    returnType = VoidType() if isInit else consdecl.returnType
    methodName = "<init>" if isInit else consdecl.name.name
    intype = [ArrayType(0, StringType())] if isMain else list(map(lambda x: x.varType, consdecl.param))
    mtype = MType(intype, returnType)

    self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

    frame.enterScope(True)

    glenv = o

    # Generate code for parameter declarations
    if isInit:
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
      self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
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
    # pass this one be
    pass
  def visitConstDecl(self, ast: ConstDecl, ctx):
    self.emit.printout(self.emit.emitVAR(0, ast.constant.name,\
      ast.constType, ctx.frame.getStartLabel(), ctx.frame.getEndLabel(),\
      ctx.frame))
    ctx.sym.append(Symbol(ast.constant.name, ast.constType, Const(ast.value)))
  def visitVarDecl(self, ast: VarDecl, ctx: SubBody):
    idx = ctx.frame.getNewIndex()
    self.emit.printout(self.emit.emitVAR(0, ast.variable.name,\
      ast.varType, ctx.frame.getStartLabel(), ctx.frame.getEndLabel(),\
      ctx.frame))
    ctx.sym.append(Symbol(ast.variable.name, ast.varType, Index(idx)))
  def visitBlock(self, ast: Block, ctx: SubBody):
    ctx.frame.enterScope(False)
    nenv = reduce(lambda env, ele: SubBody(ctx.frame, [self.visit(ele, env)]+env.sym), ast.decl, SubBody(ctx.frame, []))
    self.emit.printout(self.emit.emitLABEL(ctx.frame.getStartLabel(), ctx.frame))
    map(lambda x: self.visit(x, SubBody(ctx.frame, ctx.sym+nenv)))
    self.emit.printout(self.emit.emitLABEL(ctx.frame.getEndLabel(), ctx.frame))
    ctx.frame.exitScope()
  def visitAssign(self, ast: Assign, ctx: SubBody):
    #TODO: update visit left first for field access and array
    erc, ert = self.visit(ast.exp, Access(ctx.frame, ctx.sym, False, True))
    elc, elt = self.visit(ast.lhs, Access(ctx.frame, ctx.sym, True, True))
    self.emit.printout(erc)
    if isinstance(ert, IntType) and isinstance(elt, FloatType):
      self.emit.printout(self.emit.emitI2F(ctx.frame))
    self.emit.printout(elc)

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

  def visitFor(self, ast: For, ctx):
    pass
  def visitBreak(self, ast: Break, ctx: SubBody):
    self.emit.printout(self.emit.emitGOTO(ctx.frame.getBreakLabel(), ctx.frame))
  def visitContinue(self, ast: Continue, ctx: SubBody):
    self.emit.printout(self.emit.emitGOTO(ctx.frame.getContinueLabel(), ctx.frame))
  def visitReturn(self, ast: Return, ctx):
    pass
  def visitId(self, ast: Id, ctx: Access):
    sym = self.lookup(ast.name, ctx.sym, lambda x: x.name)
    if sym is not None:
      # handle if id is found in ctx.sym (it is an instance)
      pass
    sym = self.lookup(ast.name, self.env, lambda x: x.name)
    return ast.name, ClassType(Id(ast.name))
  def visitArrayCell(self, ast: ArrayCell, ctx):
    pass
  def visitFieldAccess(self, ast: FieldAccess, ctx: Access):
    ec, et = self.visit(ast.fieldname, Access(ctx.frame, ctx.sym, True, False))
    classname = type(et).__name__
    fields = None
    for key, value in self.genv.items():
      if key == classname:
        fields = value["members"]
    field = self.lookup(ast.fieldname.name, fields, lambda x: x.name)
    if ctx.isLeft == True:
      return self.emit.emitPUTSTATIC(classname+"."+field.name, field.mtype, ctx.frame), field.mtype
    if field.value is not None:
      return self.emit.emitPUSHCONST(self.emit.emitEXPR(field.value.value, field.mtype), StringType(), ctx.frame), field.mtype
    return self.emit.emitGETSTATIC(classname+"."+field.name,field.mtype,ctx.frame),field.mtype

  def visitUnaryOp(self, ast: UnaryOp, ctx: Access):
    c,t = self.visit(ast.body)
    if ast.op == "+":
      return c,t
    if ast.op == "-":
      return c + self.emit.emitNEGOP(t, ctx.frame), t
    if ast.op == "!":
      return c + self.emit.emitNOT(t, ctx.frame), t
  def visitCallExpr(self, ast: CallExpr, ctx: Access):
    # TODO: update to call from parent class
    # string, typ: ClassType of instance or class
    value, typ = self.visit(ast.obj, Access(ctx.frame, ctx.sym, False, True))
    in_ = ("", list())
    # Get return type of the method
    sym = self.lookup(typ.classname.name, self.env, lambda x: x.name)
    sym = sym.members
    sym = self.lookup(ast.method.name, sym, lambda x: x.name)
    returnType = sym.mtype.rettype
    kind = sym.kind
    # Gen code for param
    for x in ast.param:
      str1, typ1 = self.visit(x, Access(ctx.frame, ctx.sym, False, True))
      in_ = (in_[0] + str1, in_[1].append(typ1))
    self.emit.printout(in_[0])
    mtype = MType(in_[1], returnType)
    # handle static class methods
    if type(kind) is Static():
      return in_[0] + self.emit.emitINVOKESTATIC(value + "/" + ast.method.name, mtype, ctx.frame), mtype.rettype
    else:
      # handle instance method value is Index
      return in_[0] + self.emit.emitINVOKEVIRTUAL(value + "/" + ast.method.name, mtype, ctx.frame), mtype.rettype
  def visitNewExpr(self, ast: NewExpr, ctx: Access):
    pass

  def visitCallStmt(self, ast: CallStmt, ctx: SubBody):
    # TODO: update to call from parent class
    # string, typ: ClassType of instance or class
    value, typ = self.visit(ast.obj, Access(ctx.frame, ctx.sym, False, True))
    in_ = ("", list())
    # Get return type of the method
    sym = self.lookup(typ.classname.name, self.env, lambda x: x.name)
    sym = sym.members
    sym = self.lookup(ast.method.name, sym, lambda x: x.name)
    mtype = sym.mtype
    kind = sym.kind
    # Gen code for param
    for x in ast.param:
      str1, typ1 = self.visit(x, Access(ctx.frame, ctx.sym, False, True))
      in_ = (in_[0] + str1, in_[1].append(typ1))
    self.emit.printout(in_[0])
    # handle static class methods
    if type(kind) is Static:
      self.emit.printout(self.emit.emitINVOKESTATIC(value + "/" + ast.method.name, mtype, ctx.frame))
    else:
      # handle instance method value is Index
      self.emit.printout(self.emit.emitINVOKEVIRTUAL(value + "/" + ast.method.name, mtype, ctx.frame))

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
      raise "TODO update concat string" 

  def visitIntLiteral(self, ast, o):
    return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()
  def visitFloatLiteral(self, ast: FloatLiteral, o):
    return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()
  def visitStringLiteral(self, ast: StringLiteral, o):
    return self.emit.emitPUSHCONST(str(ast.value), StringType(), o.frame), StringType()
  def visitBooleanLiteral(self, ast: BooleanLiteral, o):
    return self.emit.emitPUSHICONST(str(ast.value), o.frame), BoolType()
  def visitNullLiteral(self, ast: NullLiteral, o):
    pass
  def visitSelfLiteral(self, ast: SelfLiteral, o):
    pass
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
