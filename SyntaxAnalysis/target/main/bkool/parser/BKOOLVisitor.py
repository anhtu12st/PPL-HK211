# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decllist.
    def visitDecllist(self, ctx:BKOOLParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl.
    def visitDecl(self, ctx:BKOOLParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varlist.
    def visitVarlist(self, ctx:BKOOLParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subvarlist.
    def visitSubvarlist(self, ctx:BKOOLParser.SubvarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcdecl.
    def visitFuncdecl(self, ctx:BKOOLParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#fparam.
    def visitFparam(self, ctx:BKOOLParser.FparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#declarparamlist.
    def visitDeclarparamlist(self, ctx:BKOOLParser.DeclarparamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#fbody.
    def visitFbody(self, ctx:BKOOLParser.FbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bodyitem.
    def visitBodyitem(self, ctx:BKOOLParser.BodyitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#callfunc.
    def visitCallfunc(self, ctx:BKOOLParser.CallfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#fargument.
    def visitFargument(self, ctx:BKOOLParser.FargumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#fargumentlist.
    def visitFargumentlist(self, ctx:BKOOLParser.FargumentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignvar.
    def visitAssignvar(self, ctx:BKOOLParser.AssignvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#freturn.
    def visitFreturn(self, ctx:BKOOLParser.FreturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprlist.
    def visitExprlist(self, ctx:BKOOLParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var.
    def visitVar(self, ctx:BKOOLParser.VarContext):
        return self.visitChildren(ctx)



del BKOOLParser