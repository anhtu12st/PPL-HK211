from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):

    '''
    program: classdecl* EOF;
    '''
    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])

    '''
    classdecl: CLASS ID (EXTENDS ID)? LP memdecl* RP;
    '''
    def visitClassdecl(self,ctx:BKOOLParser.ClassdeclContext):
        memdecl_lst = [self.visit(x) for x in ctx.memdecl()]
        lst = []
        for mem in memdecl_lst:
            try:
                if len(mem) > 0: lst = lst + mem
            except:
                lst.append(mem)
        return ClassDecl(Id(ctx.ID(0).getText()),
                        lst,
                        Id(ctx.ID(1).getText()) if len(ctx.ID())>1 else None)

    '''
    memdecl: attributedecl | methoddecl;
    '''
    def visitMemdecl(self,ctx:BKOOLParser.MemdeclContext):
        if ctx.attributedecl():
            return self.visit(ctx.attributedecl())
        else:
            return self.visit(ctx.methoddecl())

    '''
    attributedecl: vardecl | constdecl;
    '''
    def visitAttributedecl(self, ctx: BKOOLParser.AttributedeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else:
            return self.visit(ctx.constdecl())

    '''
    attrtype:
        FLOAT
        | INT
        | BOOLEAN
        | STRING
        | ID
        | arraytype;
    '''
    def visitAttrtype(self, ctx: BKOOLParser.AttrtypeContext):
        if ctx.FLOAT():
            return FloatType()
        elif ctx.INT():
            return IntType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        else:
            return self.visit(ctx.arraytype())

    '''
    vardecl: STATIC? attrtype attrlist SEMI;
    '''
    def visitVardecl(self, ctx: BKOOLParser.VardeclContext):
        attrlist = self.visit(ctx.attrlist())
        type = self.visit(ctx.attrtype())
        if ctx.STATIC():
            return [AttributeDecl(Static(),VarDecl(id, type, expr)) for (id,expr) in attrlist]
        else:
            return [AttributeDecl(Instance(),VarDecl(id, type, expr)) for (id,expr) in attrlist]


    '''
    attrlist: attr subattrlist;
    '''
    def visitAttrlist(self, ctx: BKOOLParser.AttrlistContext):
        return [self.visit(ctx.attr())] + self.visit(ctx.subattrlist())

    '''
    attr: ID | ID INITASSIGN expr;
    '''
    def visitAttr(self, ctx: BKOOLParser.AttrContext):
        if ctx.INITASSIGN():
            return (Id(ctx.ID().getText()), self.visit(ctx.expr()))
        else:
            return (Id(ctx.ID().getText()), None)

    '''
    subattrlist: CM attr subattrlist |;
    '''
    def visitSubattrlist(self, ctx: BKOOLParser.SubattrlistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.attr())] + self.visit(ctx.subattrlist())

    '''
    constdecl:
	FINAL attrtype constattrlist SEMI
	| STATIC FINAL attrtype constattrlist
	| FINAL STATIC attrtype constattrlist;
    '''
    def visitConstdecl(self, ctx: BKOOLParser.ConstdeclContext):
        constattrlist = self.visit(ctx.constattrlist())
        type = self.visit(ctx.attrtype())
        if ctx.STATIC():
            return [AttributeDecl(Static(),ConstDecl(id, type, expr)) for (id,expr) in constattrlist]
        else:
            return [AttributeDecl(Instance(),ConstDecl(id, type, expr)) for (id,expr) in constattrlist]
    
    '''
    constattrlist: constattr subconstattrlist;
    '''
    def visitConstattrlist(self, ctx: BKOOLParser.ConstattrlistContext):
        return [self.visit(ctx.constattr())] + self.visit(ctx.subconstattrlist())

    '''
    constattr: ID INITASSIGN expr;
    '''
    def visitConstattr(self, ctx: BKOOLParser.ConstattrContext):
        return (Id(ctx.ID().getText()), self.visit(ctx.expr()))

    '''
    subconstattrlist: CM constattr subconstattrlist |;
    '''
    def visitSubconstattrlist(self, ctx: BKOOLParser.SubconstattrlistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.constattr())] + self.visit(ctx.subconstattrlist())

    '''
    methoddecl: staaticmethod | instancemethod;
    '''
    def visitMethoddecl(self, ctx: BKOOLParser.MethoddeclContext):
        return self.visit(ctx.staaticmethod()) if ctx.staaticmethod() else self.visit(ctx.instancemethod())
    
    '''
    staaticmethod: STATIC methodreturntype ID LB paramslist? RB blockstatement;
    '''
    def visitStaaticmethod(self, ctx: BKOOLParser.StaaticmethodContext):
        return MethodDecl(Static(),Id(ctx.ID().getText()),
                            self.visit(ctx.paramslist()) if ctx.paramslist() else [],
                            self.visit(ctx.methodreturntype()),
                            self.visit(ctx.blockstatement()))

    '''
    instancemethod: methodreturntype? ID LB paramslist? RB blockstatement;
    '''
    def visitInstancemethod(self, ctx: BKOOLParser.InstancemethodContext):
        return MethodDecl(Instance(),Id(ctx.ID().getText()) if ctx.methodreturntype() else Id("<init>"),
                            self.visit(ctx.paramslist()) if ctx.paramslist() else [],
                            self.visit(ctx.methodreturntype()) if ctx.methodreturntype() else None,
                            self.visit(ctx.blockstatement()))

    '''
    methodreturntype: attrtype | VOID;
    '''
    def visitMethodreturntype(self, ctx: BKOOLParser.MethodreturntypeContext):
        return VoidType() if ctx.VOID() else self.visit(ctx.attrtype())

    '''
    paramslist: param subparamslist;
    '''
    def visitParamslist(self, ctx: BKOOLParser.ParamslistContext):
        return self.visit(ctx.param()) + self.visit(ctx.subparamslist())

    '''
    subparamslist: SEMI param subparamslist |;
    '''
    def visitSubparamslist(self, ctx: BKOOLParser.SubparamslistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.param()) + self.visit(ctx.subparamslist())

    '''
    param: attrtype ID idslist;
    '''
    def visitParam(self, ctx: BKOOLParser.ParamContext):
        type = self.visit(ctx.attrtype())
        ids_list = [Id(ctx.ID().getText())] + self.visit(ctx.idslist())
        return [VarDecl(id,type,None) for id in ids_list]

    '''
    idslist: CM ID idslist |;
    '''
    def visitIdslist(self, ctx: BKOOLParser.IdslistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [Id(ctx.ID().getText())] + self.visit(ctx.idslist())

    '''
    blockstatement: LP (attributedecl | statement)* RP;
    '''
    def visitBlockstatement(self, ctx: BKOOLParser.BlockstatementContext):
        lst = [self.visit(x) for x in ctx.attributeinstancedecl()]
        storedecl_lst = []
        for mem in lst:
            try:
                if len(mem) > 0: storedecl_lst = storedecl_lst + mem
            except:
                storedecl_lst.append(mem)
        stmt_lst = [self.visit(x) for x in ctx.statement()]
        return Block(storedecl_lst,stmt_lst)


    '''
    statement: expr SEMI | returnstatement;
    '''
    def visitStatement(self, ctx: BKOOLParser.StatementContext):
        return self.visit(ctx.returnstatement())

    '''
    returnstatement: RETURN expr SEMI | continuestatement;
    '''
    def visitReturnstatement(self, ctx: BKOOLParser.ReturnstatementContext):
        if ctx.continuestatement():
            return self.visit(ctx.continuestatement())
        else:
            return Return(self.visit(ctx.expr()))

    '''
    continuestatement: CONTINUE SEMI | breakstatement;
    '''
    def visitContinuestatement(self, ctx: BKOOLParser.ContinuestatementContext):
        if ctx.breakstatement():
            return self.visit(ctx.breakstatement())
        else:
            return Continue()

    '''
    breakstatement: BREAK SEMI | assignstatement;
    '''
    def visitBreakstatement(self, ctx: BKOOLParser.BreakstatementContext):
        if ctx.assignstatement():
            return self.visit(ctx.assignstatement())
        else:
            return Break()

    '''
    assignstatement: lhs ASSIGN expr SEMI | forstatement;
    '''
    def visitAssignstatement(self, ctx: BKOOLParser.AssignstatementContext):
        if ctx.forstatement():
            return self.visit(ctx.forstatement())
        else:
            return Assign(self.visit(ctx.lhs()),self.visit(ctx.expr()))

    '''
    forstatement:
	FOR scalarvar ASSIGN expr (TO | DOWNTO) expr DO statement
	| ifstatement;
    '''
    def visitForstatement(self, ctx: BKOOLParser.ForstatementContext):
        if ctx.ifstatement():
            return self.visit(ctx.ifstatement())
        else:
            return For(self.visit(ctx.scalarvar()),self.visit(ctx.expr(0)),
                    self.visit(ctx.expr(1)),True if ctx.TO() else False,
                    self.visit(ctx.statement()))

    '''
    ifstatement:
	IF expr THEN statement (ELSE statement)?
	| blockstatement;
    '''
    def visitIfstatement(self, ctx: BKOOLParser.IfstatementContext):
        if ctx.callstatement():
            return self.visit(ctx.callstatement())
        else:
            return If(self.visit(ctx.expr()),self.visit(ctx.statement(0)),
                    self.visit(ctx.statement(1)) if ctx.ELSE() else None)

    '''
    '''
    def visitCallstatement(self, ctx: BKOOLParser.CallstatementContext):
        if ctx.blockstatement():
            return self.visit(ctx.blockstatement())
        else:
            return CallStmt(self.visit(ctx.expr()),Id(ctx.ID().getText()),self.visit(ctx.exprlist()))

    '''
    Expression
    '''
    '''
    BINARY OPERATION
    '''
    def visitExpr(self, ctx: BKOOLParser.ExprContext):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return BinaryOp(ctx.OP0().getText(),self.visit(ctx.left),self.visit(ctx.right))

    def visitExpr1(self, ctx: BKOOLParser.Expr1Context):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return BinaryOp(ctx.OP1().getText(),self.visit(ctx.left),self.visit(ctx.right))

    def visitExpr2(self, ctx: BKOOLParser.Expr2Context):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return BinaryOp(ctx.OP2().getText(),self.visit(ctx.left),self.visit(ctx.right))
    
    def visitExpr3(self, ctx: BKOOLParser.Expr3Context):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return BinaryOp(ctx.OP3().getText(),self.visit(ctx.left),self.visit(ctx.right))
    
    def visitExpr4(self, ctx: BKOOLParser.Expr4Context):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return BinaryOp(ctx.OP4().getText(),self.visit(ctx.left),self.visit(ctx.right))
    
    def visitExpr5(self, ctx: BKOOLParser.Expr5Context):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return BinaryOp(ctx.CONCAT().getText(),self.visit(ctx.left),self.visit(ctx.right))

    '''
    UNARY OPERATION
    '''
    def visitExpr6(self, ctx: BKOOLParser.Expr6Context):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.right))

    def visitExpr7(self, ctx: BKOOLParser.Expr7Context):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return UnaryOp(ctx.OP3().getText(),self.visit(ctx.right))

    '''
    CALL OPERATION
    '''
    def visitExpr8(self, ctx: BKOOLParser.Expr8Context):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return ArrayCell(self.visit(ctx.left),self.visit(ctx.right))

    def visitExpr9(self, ctx: BKOOLParser.Expr9Context):
        if ctx.other:
            return self.visit(ctx.other)
        elif ctx.right:
            return CallExpr(self.visit(ctx.left),Id(ctx.ID().getText()),self.visit(ctx.right))
        else:
            return FieldAccess(self.visit(ctx.left),Id(ctx.ID().getText()))

    def visitExpr10(self, ctx: BKOOLParser.Expr10Context):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return NewExpr(Id(ctx.ID().getText()),self.visit(ctx.left))
    
    def visitExpr11(self, ctx: BKOOLParser.Expr11Context):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return ArrayLiteral(self.visit(ctx.left))

    def visitExpr12(self, ctx: BKOOLParser.Expr12Context):
        if ctx.other:
            return self.visit(ctx.other)
        else:
            return self.visit(ctx.left)

    def visitOperands(self, ctx: BKOOLParser.OperandsContext):
        if ctx.THIS():
            return SelfLiteral()
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NullLiteral()
        elif ctx.STRLIT():
            return StringLiteral(ctx.STRLIT().getText())
        else:
            return Id(ctx.ID().getText())

    '''
    lhs: ID | arraycell | fieldaccess;
    '''
    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.arraycell():
            return self.visit(ctx.arraycell())
        else:
            return self.visit(ctx.fieldaccess())

    '''
    arraycell: expr LSB expr RSB;
    '''
    def visitArraycell(self, ctx: BKOOLParser.ArraycellContext):
        return ArrayCell(self.visit(ctx.left),self.visit(ctx.right))

    '''
    fieldaccess: expr DOT ID | expr DOT ID LB exprlist RB;
    '''
    def visitFieldaccess(self, ctx: BKOOLParser.FieldaccessContext):
        if ctx.right:
            return CallExpr(self.visit(ctx.left),Id(ctx.ID().getText()),
                            self.visit(ctx.right))
        else:
            return FieldAccess(self.visit(ctx.left),Id(ctx.ID().getText()))

    '''
    scalarvar: ID;
    '''
    def visitScalarvar(self, ctx: BKOOLParser.ScalarvarContext):
        return Id(ctx.ID().getText())

    '''
    exprlist: expr subexprlist |;
    '''
    def visitExprlist(self, ctx: BKOOLParser.ExprlistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.subexprlist())

    '''
    subexprlist: CM expr subexprlist |;
    '''
    def visitSubexprlist(self, ctx: BKOOLParser.SubexprlistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.subexprlist())

    '''
    arraytype: (FLOAT | INT | BOOLEAN | STRING | ID) LSB INTLIT RSB;
    '''
    def visitArraytype(self, ctx: BKOOLParser.ArraytypeContext):
        size = int(ctx.INTLIT().getText())
        if ctx.FLOAT():
            return ArrayType(size,FloatType())
        elif ctx.INT():
            return ArrayType(size,IntType())
        elif ctx.BOOLEAN():
            return ArrayType(size,BoolType())
        elif ctx.STRING():
            return ArrayType(size,StringType())
        else:
            return ArrayType(size,ClassType(Id(ctx.ID().getText())))

    '''
    attributeinstancedecl: attrtype attrlist SEMI | FINAL attrtype constattrlist SEMI;
    '''
    def visitAttributeinstancedecl(self, ctx: BKOOLParser.AttributeinstancedeclContext):
        if ctx.FINAL():
            constattrlist = self.visit(ctx.constattrlist())
            type = self.visit(ctx.attrtype())
            return [ConstDecl(id, type, expr) for (id,expr) in constattrlist]
        else:
            attrlist = self.visit(ctx.attrlist())
            type = self.visit(ctx.attrtype())
            return [VarDecl(id, type, expr) for (id,expr) in attrlist]

    def visitLiterallist(self, ctx: BKOOLParser.LiterallistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.literal())] + self.visit(ctx.subliterallist())

    def visitSubliterallist(self, ctx: BKOOLParser.SubliterallistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.literal())] + self.visit(ctx.subliterallist())

    def visitLiteral(self, ctx: BKOOLParser.LiteralContext):
        if ctx.THIS():
            return SelfLiteral()
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NullLiteral()
        else:
            return StringLiteral(ctx.STRLIT().getText())