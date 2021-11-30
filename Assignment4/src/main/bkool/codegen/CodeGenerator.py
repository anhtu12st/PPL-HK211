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
  def __init__(self, name, mtype, value=None):
    self.name = name
    self.mtype = mtype
    self.value = value

  def __str__(self):
    return "Symbol("+self.name+","+str(self.mtype)+")"


class CodeGenerator:
  def __init__(self):
    self.libName = "io"

  def init(self, ast):
    genv = GlobalEnvironment().visitProgram(ast, None)
    genv["io"] = {}
    genv["io"]['members'] = [
      Symbol("readInt", MType(list(), IntType()), CName(self.libName)),
      Symbol("writeInt", MType([IntType()], VoidType()), CName(self.libName)),
      Symbol("writeIntLn", MType( [IntType()], VoidType()), CName(self.libName)),

      Symbol("readFloat", MType(list(), FloatType()), CName(self.libName)),
      Symbol("writeFloat", MType( [FloatType()], VoidType()), CName(self.libName)),
      Symbol("writeFloatLn", MType( [FloatType()], VoidType()), CName(self.libName)),

      Symbol("readBool", MType(list(), BoolType()), CName(self.libName)),
      Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
      Symbol("writeBoolLn", MType( [BoolType()], VoidType()), CName(self.libName)),

      Symbol("readStr", MType(list(), StringType()), CName(self.libName)),
      Symbol("writeStr", MType([StringType()], VoidType()), CName(self.libName)),
      Symbol("writeStrLn", MType( [StringType()], VoidType()), CName(self.libName)),
    ]
    temp = list()
    for key, value in genv.items():
      temp += value["members"]
    return temp

  def gen(self, ast, path):
    #ast: AST
    #dir_: String

    gl = self.init(ast)
    gc = CodeGenVisitor(ast, gl, path)
    gc.visit(ast, None)


class SubBody():
  def __init__(self, frame, sym):
    self.frame = frame
    self.sym = sym


class Access():
  def __init__(self, frame, sym, isLeft, isFirst=False):
    self.frame = frame
    self.sym = sym
    self.isLeft = isLeft
    self.isFirst = isFirst


class Val(ABC):
  pass


class Index(Val):
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

  def visitProgram(self, ast, c):
    [self.visit(i, c)for i in ast.decl]

  def visitClassDecl(self, ast: ClassDecl, c):
    self.className = ast.classname.name
    parentName = ast.parentname if ast.parentname is not None else "java.lang.Object"
    self.emit = Emitter(self.path+"/" + self.className + ".j")
    self.emit.printout(self.emit.emitPROLOG(self.className, parentName))
    #TODO: assume that class have only methods for now, need to update for attribute
    [self.visit(ele, SubBody(None, self.env)) for ele in ast.memlist if type(ele) == MethodDecl]
    if "<init>" not in list(map(lambda x: x.name.name, ast.memlist)):
      self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(), None, Block([], [])), c, Frame("<init>", VoidType()))
    self.emit.emitEPILOG()

  def genMETHOD(self, consdecl, o, frame):
    isInit = consdecl.returnType is None
    isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
    returnType = VoidType() if isInit else consdecl.returnType
    methodName = "<init>" if isInit else consdecl.name.name
    intype = [ArrayType(0, StringType())] if isMain else list(map(lambda x: x.typ, consdecl.param))
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
    pass
  def visitConstDecl(self, ast: ConstDecl, ctx):
    pass
  def visitVarDecl(self, ast: VarDecl, ctx):
    pass
  def visitBlock(self, ast: Block, ctx):
    pass
  def visitAssign(self, ast: Assign, ctx):
    pass
  def visitIf(self, ast: If, ctx):
    pass
  def visitFor(self, ast: For, ctx):
    pass
  def visitBreak(self, ast: Break, ctx):
    pass
  def visitContinue(self, ast: Continue, ctx):
    pass
  def visitReturn(self, ast: Return, ctx):
    pass
  def visitCallStmt(self, ast: CallStmt, ctx):
    pass
  def visitId(self, ast: Id, ctx):
    pass
  def visitArrayCell(self, ast: ArrayCell, ctx):
    pass
  def visitFieldAccess(self, ast: FieldAccess, ctx):
    pass
  def visitUnaryOp(self, ast: UnaryOp, ctx):
    pass
  def visitCallExpr(self, ast: CallExpr, ctx):
    pass
  def visitNewExpr(self, ast: NewExpr, ctx):
    pass

  def visitCallStmt(self, ast: CallStmt, o):
    ctxt = o
    frame = ctxt.frame
    nenv = ctxt.sym
    sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
    cname = sym.value.value
    ctype = sym.mtype
    in_ = ("", list())
    for x in ast.param:
      str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
      in_ = (in_[0] + str1, in_[1].append(typ1))
    self.emit.printout(in_[0])
    self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

  def visitBinaryOp(self, ast, o):
    e1c, e1t = self.visit(ast.left, o)
    e2c, e2t = self.visit(ast.right, o)
    return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t

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
  """
  classes: {
    [className]:{
      parentname: string,
      members: [Symbol]
    }
  }
  """
  def visitProgram(self, ast: Program, o):
    self.classes = {}
    for decl in ast.decl:
      class_name = decl.classname.name
      self.classes[class_name] = {}
    for decl in ast.decl:
      class_name = decl.classname.name
      parent_name = decl.parentname.name if decl.parentname is not None else None
      self.classes[class_name]['parentname'] = parent_name
    [self.visit(x, self.classes) for x in ast.decl]
    return self.classes

  def visitClassDecl(self, ast: ClassDecl, o):
    members = []
    o[ast.classname.name]['members'] = members
    self.currentClass = ast.classname.name
    [self.visit(x, members) for x in ast.memlist]

  def visitMethodDecl(self, ast: MethodDecl, members):
    name = ast.name.name
    paramType = list(map(lambda x: x.varType, ast.param))
    returnType = ast.returnType
    members.append(
      Symbol(name, MType(paramType, returnType), CName(self.currentClass)))
    return name

  def visitAttributeDecl(self, ast: AttributeDecl, members):
    name, type = self.visit(ast.decl, members)
    members.append(Symbol(name, type, CName(self.currentClass)))
    return name

  def visitVarDecl(self, ast: VarDecl, members):
    name = ast.variable.name
    type = str(ast.varType)
    return name, type

  def visitConstDecl(self, ast: ConstDecl, members):
    name = ast.constant.name
    type = ast.constType
    return name, type
