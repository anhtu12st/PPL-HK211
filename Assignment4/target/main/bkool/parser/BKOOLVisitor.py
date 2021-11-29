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


    # Visit a parse tree produced by BKOOLParser#classdecl.
    def visitClassdecl(self, ctx:BKOOLParser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memdecl.
    def visitMemdecl(self, ctx:BKOOLParser.MemdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributedecl.
    def visitAttributedecl(self, ctx:BKOOLParser.AttributedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrtype.
    def visitAttrtype(self, ctx:BKOOLParser.AttrtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrlist.
    def visitAttrlist(self, ctx:BKOOLParser.AttrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attr.
    def visitAttr(self, ctx:BKOOLParser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subattrlist.
    def visitSubattrlist(self, ctx:BKOOLParser.SubattrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constdecl.
    def visitConstdecl(self, ctx:BKOOLParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constattrlist.
    def visitConstattrlist(self, ctx:BKOOLParser.ConstattrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constattr.
    def visitConstattr(self, ctx:BKOOLParser.ConstattrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subconstattrlist.
    def visitSubconstattrlist(self, ctx:BKOOLParser.SubconstattrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methoddecl.
    def visitMethoddecl(self, ctx:BKOOLParser.MethoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#staaticmethod.
    def visitStaaticmethod(self, ctx:BKOOLParser.StaaticmethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#instancemethod.
    def visitInstancemethod(self, ctx:BKOOLParser.InstancemethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodreturntype.
    def visitMethodreturntype(self, ctx:BKOOLParser.MethodreturntypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramslist.
    def visitParamslist(self, ctx:BKOOLParser.ParamslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subparamslist.
    def visitSubparamslist(self, ctx:BKOOLParser.SubparamslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idslist.
    def visitIdslist(self, ctx:BKOOLParser.IdslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockstatement.
    def visitBlockstatement(self, ctx:BKOOLParser.BlockstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnstatement.
    def visitReturnstatement(self, ctx:BKOOLParser.ReturnstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continuestatement.
    def visitContinuestatement(self, ctx:BKOOLParser.ContinuestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakstatement.
    def visitBreakstatement(self, ctx:BKOOLParser.BreakstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignstatement.
    def visitAssignstatement(self, ctx:BKOOLParser.AssignstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forstatement.
    def visitForstatement(self, ctx:BKOOLParser.ForstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifstatement.
    def visitIfstatement(self, ctx:BKOOLParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#callstatement.
    def visitCallstatement(self, ctx:BKOOLParser.CallstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr6.
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr7.
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr8.
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr9.
    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr10.
    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr11.
    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr12.
    def visitExpr12(self, ctx:BKOOLParser.Expr12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operands.
    def visitOperands(self, ctx:BKOOLParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraycell.
    def visitArraycell(self, ctx:BKOOLParser.ArraycellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#fieldaccess.
    def visitFieldaccess(self, ctx:BKOOLParser.FieldaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scalarvar.
    def visitScalarvar(self, ctx:BKOOLParser.ScalarvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprlist.
    def visitExprlist(self, ctx:BKOOLParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subexprlist.
    def visitSubexprlist(self, ctx:BKOOLParser.SubexprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraytype.
    def visitArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributeinstancedecl.
    def visitAttributeinstancedecl(self, ctx:BKOOLParser.AttributeinstancedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literallist.
    def visitLiterallist(self, ctx:BKOOLParser.LiterallistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subliterallist.
    def visitSubliterallist(self, ctx:BKOOLParser.SubliterallistContext):
        return self.visitChildren(ctx)



del BKOOLParser