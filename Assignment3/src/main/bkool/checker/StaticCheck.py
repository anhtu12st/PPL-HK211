
"""
 * @author nhphung
"""
import sys
# from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

if not './main/bkool/utils/' in sys.path:
    from main.bkool.utils.AST import *
    from main.bkool.utils.Visitor import *
    from main.bkool.utils.Utils import Utils
else:
    from AST import *
    from Visitor import *
    from Utils import Utils


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ctx, o):
        lst = []
        for x in ctx.decl:
            if x.classname.name in lst:
                raise Redeclared(Class(), x.classname.name)
            lst += [x.classname.name]

