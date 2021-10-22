from posixpath import expanduser
import unittest
from AST import *
from TestUtils import TestAST

class ASTGenSuite(unittest.TestCase):
    def test_0(self):
        input = """class main { }"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_1(self):
        input = """class main {
            int a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_2(self):
        input = """class main {
            static int a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Static(),VarDecl(Id("a"),IntType()))
            ])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_3(self):
        input = """class main {
            static int a,b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Static(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Static(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_4(self):
        input = """class main {
            final int a=1,b=2;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
             AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_5(self):
        input = """class main {
            final static int a=1,b=1;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
             AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(1)))])]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_6(self):
        input = """
        class XXX { }
        class main {
            final static int a=1,b=1;
            
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),
                [AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(1)))]
            )]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_7(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),
                [AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_8(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(){}
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[],IntType(),Block([],[]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_9(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a,b; float a){}
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),
                [AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                MethodDecl(Static(),Id('method'),[
                    VarDecl(Id('a'),IntType()),
                    VarDecl(Id('b'),IntType()),
                    VarDecl(Id('a'),FloatType()),
                ],IntType(),Block([],[]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_10(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_11(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
            }
            void method1(int a; float a,b){
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),
                [AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                MethodDecl(Static(),Id('method'),[
                    VarDecl(Id('a'),IntType()),
                    VarDecl(Id('a'),FloatType()),
                    VarDecl(Id('b'),FloatType()),
                ],IntType(),Block([
                    ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                    ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                    ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                    ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),IntType()),
                ],[])),
                MethodDecl(Instance(),Id('method1'),[
                    VarDecl(Id('a'),IntType()),
                    VarDecl(Id('a'),FloatType()),
                    VarDecl(Id('b'),FloatType()),
                ],VoidType(),Block([],[]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_12(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                    ],[]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_13(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        Return(Id('a'))
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                    ],[
                        Return(IntLiteral(1))
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_14(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        Return(Id('a'))
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Return(IntLiteral(1))
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_15(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        Return(Id('a'))
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Assign(FieldAccess(SelfLiteral(),Id('myPI')),FloatLiteral(3.14)),
                        Assign(Id('value'),CallExpr(Id('x'),Id('foo'),[IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'),IntLiteral(3)),BinaryOp('/',Id('value'),IntLiteral(2))),
                        Assign(Id('r'),FloatLiteral(2.0)),
                        Assign(Id('s'),BinaryOp('*',BinaryOp('*',Id('r'),Id('r')),FieldAccess(SelfLiteral(),Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,315))
    
    def test_16(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then 
                    a := b;
                else
                    { }
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        If(Id('flag'),Assign(Id('a'),Id('b')),Block([],[])),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Assign(FieldAccess(SelfLiteral(),Id('myPI')),FloatLiteral(3.14)),
                        Assign(Id('value'),CallExpr(Id('x'),Id('foo'),[IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'),IntLiteral(3)),BinaryOp('/',Id('value'),IntLiteral(2))),
                        Assign(Id('r'),FloatLiteral(2.0)),
                        Assign(Id('s'),BinaryOp('*',BinaryOp('*',Id('r'),Id('r')),FieldAccess(SelfLiteral(),Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_17(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then 
                    a := b;
                else if a==b then
                    {}
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        If(Id('flag'),Assign(Id('a'),Id('b')),
                            If(BinaryOp('==',Id('a'),Id('b')),Block([],[]))
                        ),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Assign(FieldAccess(SelfLiteral(),Id('myPI')),FloatLiteral(3.14)),
                        Assign(Id('value'),CallExpr(Id('x'),Id('foo'),[IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'),IntLiteral(3)),BinaryOp('/',Id('value'),IntLiteral(2))),
                        Assign(Id('r'),FloatLiteral(2.0)),
                        Assign(Id('s'),BinaryOp('*',BinaryOp('*',Id('r'),Id('r')),FieldAccess(SelfLiteral(),Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_18(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then 
                    a := b;
                else if a==b then
                    {a := -(b+1);}
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        If(Id('flag'),Assign(Id('a'),Id('b')),
                            If(BinaryOp('==',Id('a'),Id('b')),
                                Block([],[Assign(Id('a'),UnaryOp('-',BinaryOp('+',Id('b'),IntLiteral(1))))]))
                        ),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Assign(FieldAccess(SelfLiteral(),Id('myPI')),FloatLiteral(3.14)),
                        Assign(Id('value'),CallExpr(Id('x'),Id('foo'),[IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'),IntLiteral(3)),BinaryOp('/',Id('value'),IntLiteral(2))),
                        Assign(Id('r'),FloatLiteral(2.0)),
                        Assign(Id('s'),BinaryOp('*',BinaryOp('*',Id('r'),Id('r')),FieldAccess(SelfLiteral(),Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_19(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then 
                    a := b;
                else if a==b then
                    {a := -(b+1);}
                else
                    {}
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        If(Id('flag'),Assign(Id('a'),Id('b')),
                            If(BinaryOp('==',Id('a'),Id('b')),
                                Block([],[Assign(Id('a'),UnaryOp('-',BinaryOp('+',Id('b'),IntLiteral(1))))])
                                ,Block([],[]))
                        ),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Assign(FieldAccess(SelfLiteral(),Id('myPI')),FloatLiteral(3.14)),
                        Assign(Id('value'),CallExpr(Id('x'),Id('foo'),[IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'),IntLiteral(3)),BinaryOp('/',Id('value'),IntLiteral(2))),
                        Assign(Id('r'),FloatLiteral(2.0)),
                        Assign(Id('s'),BinaryOp('*',BinaryOp('*',Id('r'),Id('r')),FieldAccess(SelfLiteral(),Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_20(self):
        input="""
        class XXX {
            int method(){
                for x:=1 to 100 do { }
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                For(Id('x'),IntLiteral(1),IntLiteral(100),True,Block([],[]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_21(self):
        input="""
        class XXX {
            int method(){
                for x:=1 to 100 do x := x \\ 1;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                For(Id('x'),IntLiteral(1),IntLiteral(100),True,
                    Assign(Id('x'),BinaryOp('\\',Id('x'),IntLiteral(1)))
                )
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_22(self):
        input="""
        class XXX {
            int method(){
                for x:=1 to 100 do {
                    io.writeIntLn(i);
                    Intarray[i] := i + 1;
                }
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                For(Id('x'),IntLiteral(1),IntLiteral(100),True,Block([],[
                    CallStmt(Id('io'),Id('writeIntLn'),[Id('i')]),
                    Assign(ArrayCell(Id('Intarray'),Id('i')),BinaryOp('+',Id('i'),IntLiteral(1)))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_23(self):
        input="""
        class XXX {
            int method(){
                for x:=1 to 100 do {
                    if a then { }
                }
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                For(Id('x'),IntLiteral(1),IntLiteral(100),True,Block([],[
                    If(Id('a'),Block([],[]))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_24(self):
        input="""
        class XXX {
            int method(){
                if a then { 
                    for x:=1 to 100 do { }
                }
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                If(Id('a'),Block([],[
                    For(Id('x'),IntLiteral(1),IntLiteral(100),True,Block([],[]))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_25(self):
        input="""
        class XXX {
            int method(){
                break;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                Break()
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_26(self):
        input="""
        class XXX {
            int method(){
                continue;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                Continue()
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_27(self):
        input="""
        class XXX {
            int[5] method(){
                return {1,this,1.1E+1,nil};
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],ArrayType(5,IntType()),Block([],[
                Return(ArrayLiteral([IntLiteral(1),SelfLiteral(),FloatLiteral(1.1e+1),NullLiteral()])),
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_28(self):
        input="""
        class XXX {
            int[5] method(){ }
            static int[5] method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],ArrayType(5,IntType()),Block([],[])),
            MethodDecl(Static(),Id('method'),[],ArrayType(5,IntType()),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_29(self):
        input="""
        class XXX {
            XXX method(){ }
            static XXX method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],ClassType(Id('XXX')),Block([],[])),
            MethodDecl(Static(),Id('method'),[],ClassType(Id('XXX')),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_30(self):
        input="""
        class XXX {
            XXX[5] method(){ }
            static XXX[5] method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],ArrayType(5,ClassType(Id('XXX'))),Block([],[])),
            MethodDecl(Static(),Id('method'),[],ArrayType(5,ClassType(Id('XXX'))),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_31(self):
        input="""
        class XXX {
            float method(){ }
            static float method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],FloatType(),Block([],[])),
            MethodDecl(Static(),Id('method'),[],FloatType(),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_32(self):
        input="""
        class XXX {
            boolean method(){ }
            static boolean method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],BoolType(),Block([],[])),
            MethodDecl(Static(),Id('method'),[],BoolType(),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_33(self):
        input="""
        class XXX {
            string method(){ }
            static string method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],StringType(),Block([],[])),
            MethodDecl(Static(),Id('method'),[],StringType(),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_34(self):
        input="""
        class XXX {
            void method(){ }
            static void method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[])),
            MethodDecl(Static(),Id('method'),[],VoidType(),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_35(self):
        input="""
        class XXX {
            void method(){
                int x;
                float x;
                boolean x;
                string x;
                XXX x;
                int[0] x;
                float[0] x;
                boolean[0] x;
                string[0] x;
                XXX[0] x;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([
                VarDecl(Id('x'),IntType()),
                VarDecl(Id('x'),FloatType()),
                VarDecl(Id('x'),BoolType()),
                VarDecl(Id('x'),StringType()),
                VarDecl(Id('x'),ClassType(Id('XXX'))),
                VarDecl(Id('x'),ArrayType(0,IntType())),
                VarDecl(Id('x'),ArrayType(0,FloatType())),
                VarDecl(Id('x'),ArrayType(0,BoolType())),
                VarDecl(Id('x'),ArrayType(0,StringType())),
                VarDecl(Id('x'),ArrayType(0,ClassType(Id('XXX')))),
            ],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_36(self):
        input="""
        class XXX {
            void method(){
                a := + b;
                a := - b;
                a := a + b;
                a := a - b;
                a := a * b;
                a := a / b;
                a := a \\ b;
                a := a % b;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),UnaryOp('+',Id('b'))),
                Assign(Id('a'),UnaryOp('-',Id('b'))),
                Assign(Id('a'),BinaryOp('+',Id('a'),Id('b'))),
                Assign(Id('a'),BinaryOp('-',Id('a'),Id('b'))),
                Assign(Id('a'),BinaryOp('*',Id('a'),Id('b'))),
                Assign(Id('a'),BinaryOp('/',Id('a'),Id('b'))),
                Assign(Id('a'),BinaryOp('\\',Id('a'),Id('b'))),
                Assign(Id('a'),BinaryOp('%',Id('a'),Id('b'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_37(self):
        input="""
        class XXX {
            void method(){
                a := + - b;
                a := -a + -b;
                a := a * -b;
                a := +a \\ b;
                a := a % --b;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),UnaryOp('+',UnaryOp('-',Id('b')))),
                Assign(Id('a'),BinaryOp('+',UnaryOp('-',Id('a')),UnaryOp('-',Id('b')))),
                Assign(Id('a'),BinaryOp('*',Id('a'),UnaryOp('-',Id('b')))),
                Assign(Id('a'),BinaryOp('\\',UnaryOp('+',Id('a')),Id('b'))),
                Assign(Id('a'),BinaryOp('%',Id('a'),UnaryOp('-',UnaryOp('-',Id('b'))))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_38(self):
        input="""
        class XXX {
            void method(){
                a := +-b+a*b*(-a+b)\\a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp(
                    '+',
                    UnaryOp('+',UnaryOp('-',Id('b'))),
                    BinaryOp(
                        '\\',
                        BinaryOp(
                            '*',
                            BinaryOp('*',Id('a'),Id('b')),
                            BinaryOp('+',UnaryOp('-',Id('a')),Id('b')),
                        ),
                        Id('a')
                    )
                )),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_39(self):
        input="""
        class XXX {
            void method(){
                a := a && a;
                a := a || a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp('&&',Id('a'),Id('a'))),
                Assign(Id('a'),BinaryOp('||',Id('a'),Id('a'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_40(self):
        input="""
        class XXX {
            void method(){
                a := a && a;
                a := a || a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp('&&',Id('a'),Id('a'))),
                Assign(Id('a'),BinaryOp('||',Id('a'),Id('a'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_41(self):
        input="""
        class XXX {
            void method(){
                a := a && a || a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp('||',BinaryOp('&&',Id('a'),Id('a')),Id('a'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_42(self):
        input="""
        class XXX {
            void method(){
                a := a && (a || a);
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp('&&',Id('a'),BinaryOp('||',Id('a'),Id('a')))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_43(self):
        input="""
        class XXX {
            void method(){
                a := new XXX(1);
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'), NewExpr(Id('XXX'),[IntLiteral(1)]))
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_44(self):
        input="""
        class XXX {
            void method(){
                a := a && !a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'), BinaryOp('&&', Id('a'), UnaryOp('!', Id('a'))))
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_45(self):
        input="""
        class XXX {
            void method(){
                a := a ^ a ^ b;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'), BinaryOp('^', Id('a'),BinaryOp('^', Id('a'), Id('b'))))
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_46(self):
        input="""
        class XXX {
            void method(){
                a := a == a;
                a := a != a;
                a := a > a;
                a := a < a;
                a := a >= a;
                a := a <= a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'), BinaryOp('==', Id('a'), Id('a'))),
                Assign(Id('a'), BinaryOp('!=', Id('a'), Id('a'))),
                Assign(Id('a'), BinaryOp('>', Id('a'), Id('a'))),
                Assign(Id('a'), BinaryOp('<', Id('a'), Id('a'))),
                Assign(Id('a'), BinaryOp('>=', Id('a'), Id('a'))),
                Assign(Id('a'), BinaryOp('<=', Id('a'), Id('a'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,346))


    def test_47(self):
        input="""
        class XXX {
            void method(){
                a := a >= a && a+a*a^!-new XXX().xxx[1];
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp('>=', Id('a'),BinaryOp('&&',Id('a'),BinaryOp('+',Id('a'),BinaryOp('*',Id('a'),BinaryOp('^',Id('a'),UnaryOp('!',UnaryOp('-',ArrayCell(FieldAccess(NewExpr(Id('XXX'),[]),Id('xxx')),IntLiteral(1)))))))))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_48(self):
        input="""
        class XXX {
            void method(){
                x.x(1,a+b,a[0]);
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                CallStmt(Id('x'),Id('x'),[
                    IntLiteral(1),
                    BinaryOp('+',Id('a'),Id('b')),
                    ArrayCell(Id('a'),IntLiteral(0)),
                ])
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_49(self):
        input="""
        class XXX {
            void method(){
                a := x.x()[0];
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),ArrayCell(CallExpr(Id('x'),Id('x'),[]),IntLiteral(0))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_50(self):
        input="""
        class XXX {
            void method(){
                a := x.x[0];
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),ArrayCell(FieldAccess(Id('x'),Id('x')),IntLiteral(0))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_51(self):
        input="""
        class XXX {
            void method(){
                x.x[0] := x.x()[0];
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(ArrayCell(FieldAccess(Id('x'),Id('x')),IntLiteral(0)),ArrayCell(CallExpr(Id('x'),Id('x'),[]),IntLiteral(0))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_52(self):
        input="""
        class XXX {
            void method(){
                a[3+x.foo(true)] := a[b[2]] +3;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(
                    ArrayCell(
                        Id('a'),
                        BinaryOp(
                            '+',
                            IntLiteral(3),
                            CallExpr(Id('x'),Id('foo'),[BooleanLiteral(True)]),
                        )
                    ),
                    BinaryOp(
                        '+',
                        ArrayCell(Id('a'),ArrayCell(Id('b'),IntLiteral(2))),
                        IntLiteral(3),
                    )
                ),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_53(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),
                [AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_54(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(){}
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[],IntType(),Block([],[]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_55(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a,b; float a){}
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),
                [AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                MethodDecl(Static(),Id('method'),[
                    VarDecl(Id('a'),IntType()),
                    VarDecl(Id('b'),IntType()),
                    VarDecl(Id('a'),FloatType()),
                ],IntType(),Block([],[]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_56(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_57(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
            }
            void method1(int a; float a,b){
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),
                [AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                MethodDecl(Static(),Id('method'),[
                    VarDecl(Id('a'),IntType()),
                    VarDecl(Id('a'),FloatType()),
                    VarDecl(Id('b'),FloatType()),
                ],IntType(),Block([
                    ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                    ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                    ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                    ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),IntType()),
                ],[])),
                MethodDecl(Instance(),Id('method1'),[
                    VarDecl(Id('a'),IntType()),
                    VarDecl(Id('a'),FloatType()),
                    VarDecl(Id('b'),FloatType()),
                ],VoidType(),Block([],[]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_58(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                    ],[]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_59(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        Return(Id('a'))
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                    ],[
                        Return(IntLiteral(1))
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_60(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        Return(Id('a'))
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Return(IntLiteral(1))
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test_61(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        Return(Id('a'))
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Assign(FieldAccess(SelfLiteral(),Id('myPI')),FloatLiteral(3.14)),
                        Assign(Id('value'),CallExpr(Id('x'),Id('foo'),[IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'),IntLiteral(3)),BinaryOp('/',Id('value'),IntLiteral(2))),
                        Assign(Id('r'),FloatLiteral(2.0)),
                        Assign(Id('s'),BinaryOp('*',BinaryOp('*',Id('r'),Id('r')),FieldAccess(SelfLiteral(),Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,361))
    
    def test_62(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then 
                    a := b;
                else
                    { }
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        If(Id('flag'),Assign(Id('a'),Id('b')),Block([],[])),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Assign(FieldAccess(SelfLiteral(),Id('myPI')),FloatLiteral(3.14)),
                        Assign(Id('value'),CallExpr(Id('x'),Id('foo'),[IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'),IntLiteral(3)),BinaryOp('/',Id('value'),IntLiteral(2))),
                        Assign(Id('r'),FloatLiteral(2.0)),
                        Assign(Id('s'),BinaryOp('*',BinaryOp('*',Id('r'),Id('r')),FieldAccess(SelfLiteral(),Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_63(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then 
                    a := b;
                else if a==b then
                    {}
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        If(Id('flag'),Assign(Id('a'),Id('b')),
                            If(BinaryOp('==',Id('a'),Id('b')),Block([],[]))
                        ),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Assign(FieldAccess(SelfLiteral(),Id('myPI')),FloatLiteral(3.14)),
                        Assign(Id('value'),CallExpr(Id('x'),Id('foo'),[IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'),IntLiteral(3)),BinaryOp('/',Id('value'),IntLiteral(2))),
                        Assign(Id('r'),FloatLiteral(2.0)),
                        Assign(Id('s'),BinaryOp('*',BinaryOp('*',Id('r'),Id('r')),FieldAccess(SelfLiteral(),Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test_64(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then 
                    a := b;
                else if a==b then
                    {a := -(b+1);}
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        If(Id('flag'),Assign(Id('a'),Id('b')),
                            If(BinaryOp('==',Id('a'),Id('b')),
                                Block([],[Assign(Id('a'),UnaryOp('-',BinaryOp('+',Id('b'),IntLiteral(1))))]))
                        ),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Assign(FieldAccess(SelfLiteral(),Id('myPI')),FloatLiteral(3.14)),
                        Assign(Id('value'),CallExpr(Id('x'),Id('foo'),[IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'),IntLiteral(3)),BinaryOp('/',Id('value'),IntLiteral(2))),
                        Assign(Id('r'),FloatLiteral(2.0)),
                        Assign(Id('s'),BinaryOp('*',BinaryOp('*',Id('r'),Id('r')),FieldAccess(SelfLiteral(),Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_65(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then 
                    a := b;
                else if a==b then
                    {a := -(b+1);}
                else
                    {}
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'),[]),
            ClassDecl(
                Id("main"),[
                    AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(Static(),ConstDecl(Id("b"),IntType(),IntLiteral(2))),
                    AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
                    AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),
                    MethodDecl(Static(),Id('method'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],IntType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        ConstDecl(Id("a"),FloatType(),FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"),FloatType(),FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],[
                        If(Id('flag'),Assign(Id('a'),Id('b')),
                            If(BinaryOp('==',Id('a'),Id('b')),
                                Block([],[Assign(Id('a'),UnaryOp('-',BinaryOp('+',Id('b'),IntLiteral(1))))])
                                ,Block([],[]))
                        ),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(),Id('method1'),[
                        VarDecl(Id('a'),IntType()),
                        VarDecl(Id('a'),FloatType()),
                        VarDecl(Id('b'),FloatType()),
                    ],VoidType(),Block([
                        ConstDecl(Id("a"),IntType(),IntLiteral(1)),
                        ConstDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("r"),FloatType()),
                        VarDecl(Id("s"),FloatType()),
                        VarDecl(Id("a"),ArrayType(5,IntType())),
                        VarDecl(Id("b"),ArrayType(5,IntType())),
                    ],[
                        Assign(FieldAccess(SelfLiteral(),Id('myPI')),FloatLiteral(3.14)),
                        Assign(Id('value'),CallExpr(Id('x'),Id('foo'),[IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'),IntLiteral(3)),BinaryOp('/',Id('value'),IntLiteral(2))),
                        Assign(Id('r'),FloatLiteral(2.0)),
                        Assign(Id('s'),BinaryOp('*',BinaryOp('*',Id('r'),Id('r')),FieldAccess(SelfLiteral(),Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test_66(self):
        input="""
        class XXX {
            int method(){
                for x:=1 to 100 do { }
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                For(Id('x'),IntLiteral(1),IntLiteral(100),True,Block([],[]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_67(self):
        input="""
        class XXX {
            int method(){
                for x:=1 to 100 do x := x \\ 1;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                For(Id('x'),IntLiteral(1),IntLiteral(100),True,
                    Assign(Id('x'),BinaryOp('\\',Id('x'),IntLiteral(1)))
                )
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,367))

    def test_68(self):
        input="""
        class XXX {
            int method(){
                for x:=1 to 100 do {
                    io.writeIntLn(i);
                    Intarray[i] := i + 1;
                }
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                For(Id('x'),IntLiteral(1),IntLiteral(100),True,Block([],[
                    CallStmt(Id('io'),Id('writeIntLn'),[Id('i')]),
                    Assign(ArrayCell(Id('Intarray'),Id('i')),BinaryOp('+',Id('i'),IntLiteral(1)))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test_69(self):
        input="""
        class XXX {
            int method(){
                for x:=1 to 100 do {
                    if a then { }
                }
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                For(Id('x'),IntLiteral(1),IntLiteral(100),True,Block([],[
                    If(Id('a'),Block([],[]))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,369))

    def test_70(self):
        input="""
        class XXX {
            int method(){
                if a then { 
                    for x:=1 to 100 do { }
                }
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                If(Id('a'),Block([],[
                    For(Id('x'),IntLiteral(1),IntLiteral(100),True,Block([],[]))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_71(self):
        input="""
        class XXX {
            int method(){
                break;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                Break()
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,71))

    def test_72(self):
        input="""
        class XXX {
            int method(){
                continue;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],IntType(),Block([],[
                Continue()
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_73(self):
        input="""
        class XXX {
            int[5] method(){
                return {1,this,1.1E+1,nil};
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],ArrayType(5,IntType()),Block([],[
                Return(ArrayLiteral([IntLiteral(1),SelfLiteral(),FloatLiteral(1.1e+1),NullLiteral()])),
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_74(self):
        input="""
        class XXX {
            int[5] method(){ }
            static int[5] method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],ArrayType(5,IntType()),Block([],[])),
            MethodDecl(Static(),Id('method'),[],ArrayType(5,IntType()),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_75(self):
        input="""
        class XXX {
            XXX method(){ }
            static XXX method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],ClassType(Id('XXX')),Block([],[])),
            MethodDecl(Static(),Id('method'),[],ClassType(Id('XXX')),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,375))

    def test_76(self):
        input="""
        class XXX {
            XXX[5] method(){ }
            static XXX[5] method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],ArrayType(5,ClassType(Id('XXX'))),Block([],[])),
            MethodDecl(Static(),Id('method'),[],ArrayType(5,ClassType(Id('XXX'))),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_77(self):
        input="""
        class XXX {
            float method(){ }
            static float method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],FloatType(),Block([],[])),
            MethodDecl(Static(),Id('method'),[],FloatType(),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test_78(self):
        input="""
        class XXX {
            boolean method(){ }
            static boolean method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],BoolType(),Block([],[])),
            MethodDecl(Static(),Id('method'),[],BoolType(),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_79(self):
        input="""
        class XXX {
            string method(){ }
            static string method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],StringType(),Block([],[])),
            MethodDecl(Static(),Id('method'),[],StringType(),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_80(self):
        input="""
        class XXX {
            void method(){ }
            static void method(){ }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[])),
            MethodDecl(Static(),Id('method'),[],VoidType(),Block([],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_81(self):
        input="""
        class XXX {
            void method(){
                int x;
                float x;
                boolean x;
                string x;
                XXX x;
                int[0] x;
                float[0] x;
                boolean[0] x;
                string[0] x;
                XXX[0] x;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([
                VarDecl(Id('x'),IntType()),
                VarDecl(Id('x'),FloatType()),
                VarDecl(Id('x'),BoolType()),
                VarDecl(Id('x'),StringType()),
                VarDecl(Id('x'),ClassType(Id('XXX'))),
                VarDecl(Id('x'),ArrayType(0,IntType())),
                VarDecl(Id('x'),ArrayType(0,FloatType())),
                VarDecl(Id('x'),ArrayType(0,BoolType())),
                VarDecl(Id('x'),ArrayType(0,StringType())),
                VarDecl(Id('x'),ArrayType(0,ClassType(Id('XXX')))),
            ],[])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_82(self):
        input="""
        class XXX {
            void method(){
                a := + b;
                a := - b;
                a := a + b;
                a := a - b;
                a := a * b;
                a := a / b;
                a := a \\ b;
                a := a % b;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),UnaryOp('+',Id('b'))),
                Assign(Id('a'),UnaryOp('-',Id('b'))),
                Assign(Id('a'),BinaryOp('+',Id('a'),Id('b'))),
                Assign(Id('a'),BinaryOp('-',Id('a'),Id('b'))),
                Assign(Id('a'),BinaryOp('*',Id('a'),Id('b'))),
                Assign(Id('a'),BinaryOp('/',Id('a'),Id('b'))),
                Assign(Id('a'),BinaryOp('\\',Id('a'),Id('b'))),
                Assign(Id('a'),BinaryOp('%',Id('a'),Id('b'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_83(self):
        input="""
        class XXX {
            void method(){
                a := + - b;
                a := -a + -b;
                a := a * -b;
                a := +a \\ b;
                a := a % --b;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),UnaryOp('+',UnaryOp('-',Id('b')))),
                Assign(Id('a'),BinaryOp('+',UnaryOp('-',Id('a')),UnaryOp('-',Id('b')))),
                Assign(Id('a'),BinaryOp('*',Id('a'),UnaryOp('-',Id('b')))),
                Assign(Id('a'),BinaryOp('\\',UnaryOp('+',Id('a')),Id('b'))),
                Assign(Id('a'),BinaryOp('%',Id('a'),UnaryOp('-',UnaryOp('-',Id('b'))))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_84(self):
        input="""
        class XXX {
            void method(){
                a := +-b+a*b*(-a+b)\\a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp(
                    '+',
                    UnaryOp('+',UnaryOp('-',Id('b'))),
                    BinaryOp(
                        '\\',
                        BinaryOp(
                            '*',
                            BinaryOp('*',Id('a'),Id('b')),
                            BinaryOp('+',UnaryOp('-',Id('a')),Id('b')),
                        ),
                        Id('a')
                    )
                )),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,384))

    def test_85(self):
        input="""
        class XXX {
            void method(){
                a := a && a;
                a := a || a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp('&&',Id('a'),Id('a'))),
                Assign(Id('a'),BinaryOp('||',Id('a'),Id('a'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test_86(self):
        input="""
        class XXX {
            void method(){
                a := a && a;
                a := a || a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp('&&',Id('a'),Id('a'))),
                Assign(Id('a'),BinaryOp('||',Id('a'),Id('a'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_87(self):
        input="""
        class XXX {
            void method(){
                a := a && a || a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp('||',BinaryOp('&&',Id('a'),Id('a')),Id('a'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,387))

    def test_88(self):
        input="""
        class XXX {
            void method(){
                a := a && (a || a);
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp('&&',Id('a'),BinaryOp('||',Id('a'),Id('a')))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,388))

    def test_89(self):
        input="""
        class XXX {
            void method(){
                a := new XXX(1);
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'), NewExpr(Id('XXX'),[IntLiteral(1)]))
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test_90(self):
        input="""
        class XXX {
            void method(){
                a := a && !a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'), BinaryOp('&&', Id('a'), UnaryOp('!', Id('a'))))
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_91(self):
        input="""
        class XXX {
            void method(){
                a := a ^ a ^ b;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'), BinaryOp('^', Id('a'),BinaryOp('^', Id('a'), Id('b'))))
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,391))

    def test_92(self):
        input="""
        class XXX {
            void method(){
                a := a == a;
                a := a != a;
                a := a > a;
                a := a < a;
                a := a >= a;
                a := a <= a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'), BinaryOp('==', Id('a'), Id('a'))),
                Assign(Id('a'), BinaryOp('!=', Id('a'), Id('a'))),
                Assign(Id('a'), BinaryOp('>', Id('a'), Id('a'))),
                Assign(Id('a'), BinaryOp('<', Id('a'), Id('a'))),
                Assign(Id('a'), BinaryOp('>=', Id('a'), Id('a'))),
                Assign(Id('a'), BinaryOp('<=', Id('a'), Id('a'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,392))


    def test_93(self):
        input="""
        class XXX {
            void method(){
                a := a >= a && a+a*a^!-new XXX().xxx[1];
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp('>=', Id('a'),BinaryOp('&&',Id('a'),BinaryOp('+',Id('a'),BinaryOp('*',Id('a'),BinaryOp('^',Id('a'),UnaryOp('!',UnaryOp('-',ArrayCell(FieldAccess(NewExpr(Id('XXX'),[]),Id('xxx')),IntLiteral(1)))))))))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_94(self):
        input="""
        class XXX {
            void method(){
                x.x(1,a+b,a[0]);
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                CallStmt(Id('x'),Id('x'),[
                    IntLiteral(1),
                    BinaryOp('+',Id('a'),Id('b')),
                    ArrayCell(Id('a'),IntLiteral(0)),
                ])
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,394))

    def test_95(self):
        input="""
        class XXX {
            void method(){
                a := x.x()[0];
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),ArrayCell(CallExpr(Id('x'),Id('x'),[]),IntLiteral(0))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test_96(self):
        input="""
        class XXX {
            void method(){
                a := x.x[0];
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),ArrayCell(FieldAccess(Id('x'),Id('x')),IntLiteral(0))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test_97(self):
        input="""
        class XXX {
            void method(){
                x.x[0] := x.x()[0];
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(ArrayCell(FieldAccess(Id('x'),Id('x')),IntLiteral(0)),ArrayCell(CallExpr(Id('x'),Id('x'),[]),IntLiteral(0))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,397))

    def test_98(self):
        input="""
        class XXX {
            void method(){
                a[3+x.foo(true)] := a[b[2]] +3;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(
                    ArrayCell(
                        Id('a'),
                        BinaryOp(
                            '+',
                            IntLiteral(3),
                            CallExpr(Id('x'),Id('foo'),[BooleanLiteral(True)]),
                        )
                    ),
                    BinaryOp(
                        '+',
                        ArrayCell(Id('a'),ArrayCell(Id('b'),IntLiteral(2))),
                        IntLiteral(3),
                    )
                ),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_99(self):
        input="""
        class XXX {
            void method(){
                a := a && a;
                a := a || a;
            }
        }
        """
        expect=str(Program([ClassDecl(Id('XXX'),[
            MethodDecl(Instance(),Id('method'),[],VoidType(),Block([],[
                Assign(Id('a'),BinaryOp('&&',Id('a'),Id('a'))),
                Assign(Id('a'),BinaryOp('||',Id('a'),Id('a'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input,expect,399))
