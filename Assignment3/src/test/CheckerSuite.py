import sys
import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):

    def test0(self):
        input = """
        class XXX { }
        class XXX { }
        """
        expect = "Redeclared Class: XXX"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test1(self):
        input = Program([
            ClassDecl(Id('XXX'), [
                AttributeDecl(Instance(), VarDecl(Id('x'), IntType())),
                AttributeDecl(Static(), ConstDecl(
                    Id('x'), FloatType(), FloatLiteral(0.1)))
            ], None)
        ])
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2(self):
        input = """
        class XXX {
            int x;
            int x() { }
        }
        """
        expect = "Redeclared Method: x"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self):
        input = """
        class XXX {
            int x;
            int y(int z, z) { }
        }
        """
        expect = "Redeclared Parameter: z"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test4(self):
        input = """
        class XXX {
            int x;
            int y (int z; float z) { }
        }
        """
        expect = "Redeclared Parameter: z"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test5(self):
        input = """
        class XXX {
            int x;
            int y (int z; float t) { int z = 2; }
        }
        """
        expect = "Redeclared Variable: z"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test6(self):
        input = """
        class XXX {
            int x;
            int y(int z; float t) { final int t = 1; }
        }
        """
        expect = "Redeclared Constant: t"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test7(self):
        input = """
        class XXX {
            int x;
            int y(int z; float t) { 
                {
                    int a;
                    final int a = 1;
                }
            }
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test8(self):
        input = """
        class XXX extends YYY {
            int x (int x){ }
            int x;
        }
        class YYY { }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test9(self):
        input = Program([
            ClassDecl(Id('XXX'), [
                MethodDecl(Instance(), Id('x'), [], IntType(), Block([
                    ConstDecl(Id('y'),IntType(),IntLiteral(1))
                ],[
                    Assign(Id('y'),IntLiteral(1))
                ]))
            ], None)
        ])
        expect = "Cannot Assign To Constant: AssignStmt(Id(y),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test10(self):
        input = Program([
            ClassDecl(Id('XXX'), [
                AttributeDecl(Instance(),ConstDecl(Id('x'),IntType(),IntLiteral(1))),
                MethodDecl(Instance(), Id('y'), [], IntType(), Block([
                    VarDecl(Id('x'),ClassType(Id('XXX')),NewExpr(Id('XXX'),[]))
                ],[
                    Assign(FieldAccess(Id('x'),Id('x')),IntLiteral(1))
                ]))
            ], None)
        ])
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(x),Id(x)),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test11(self):
        input = Program([
            ClassDecl(Id('XXX'), [
                MethodDecl(Instance(), Id('x'), [], IntType(), Block([
                    ConstDecl(Id('x'),ArrayType(3,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(1),IntLiteral(1)]))
                ],[
                    Assign(Id('x'), ArrayLiteral([IntLiteral(1),IntLiteral(1),IntLiteral(1)]))
                ]))
            ], None)
        ])
        expect = "Cannot Assign To Constant: AssignStmt(Id(x),[IntLit(1),IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test12(self):
        input = Program([
            ClassDecl(Id('XXX'), [
                MethodDecl(Instance(), Id('x'), [], IntType(), Block([
                    ConstDecl(Id('x'), IntType(), IntLiteral(1))
                ],[
                    For(Id('x'), IntLiteral(1), IntLiteral(10), True, Assign(Id('x'),BinaryOp('+',Id('x'),Id('x'))))
                ]))
            ], None)
        ])
        expect = "Cannot Assign To Constant: AssignStmt(Id(x),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test13(self):
        input = """
        class XXX {
            int x() {
                int x = 1;
                if x then { }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(Id(x),Block([],[]))"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test14(self):
        input = Program([
            ClassDecl(Id('XXX'), [
                MethodDecl(Instance(), Id('x'), [], IntType(), Block([
                    VarDecl(Id('x'), FloatType(), IntLiteral(1))
                ],[
                    For(Id('x'), IntLiteral(1), IntLiteral(10), True, Assign(Id('x'),BinaryOp('+',Id('x'),Id('x'))))
                ]))
            ], None)
        ])
        expect = "Type Mismatch In Statement: For(Id(x),IntLit(1),IntLit(10),True,AssignStmt(Id(x),BinaryOp(+,Id(x),Id(x)))])"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test15(self):
        input = """
        class XXX {
            int x() {
                int x = 1;
                float y = 1.0;
                boolean z = true;
                string t = "1";
                int[4] g = {1,1,1,1};
                y := x;
                x := y;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test16(self):
        input = """
        class XXX {
            int x() {
                int x = 1;
                float y = 1.0;
                boolean z = true;
                string t = "1";
                int[4] g = {1,1,1,1};
                y := x;
                t := "abc";
                g := {1,2,3,4};
                g := {1,2,3};
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(g),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test17(self):
        input = """
        class XXX {
            int x() {
                int x = 1;
                float y = 1.0;
                boolean z = true;
                string t = "1";
                int[4] g = {1,1,1,1};
                y := x;
                t := "abc";
                g := {1,2,3,4};
                t := z;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(t),Id(z))"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test18(self):
        input = """
        class XXX extends YYY {
            int x() {
                YYY y;
                XXX x;
                XXX z;
                x := z;
                x := y;
            }
        }
        class YYY { }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test19(self):
        input = """
        class XXX {
            int x() {
                int x = 1;
                float y = 1.0;
                boolean z = true;
                string t = "1";
                float[4] g = {1.0,1.0,1.0,1.0};
                y := x;
                t := "abc";
                g := {1,1,3,4};
                g := {true,true,true,true};
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(g),[BooleanLit(True),BooleanLit(True),BooleanLit(True),BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test20(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX[3] x;
                YYY[3] y;
                y := x;
                x := y;
            }
        }
        class YYY { }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test21(self):
        input = """
        class XXX {
            int x() {
                YYY.method2();
                YYY.method();
            }
        }
        class YYY {
            static int method() { }
            static void method2() { }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(YYY),Id(method),[])"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test22(self):
        input = """
        class XXX {
            int x() {
                YYY x;
                x.method2();
                x.method();
            }
        }
        class YYY {
            int method() { }
            void method2() { }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(x),Id(method),[])"
        self.assertTrue(TestChecker.test(input, expect, 422))


    def test23(self):
        input = """
        class XXX {
            int x() {
                YYY x;
                x.method(1, true);
                x.method(1, 0);
            }
        }
        class YYY {
            void method(int x; boolean y) { }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(x),Id(method),[IntLit(1),IntLit(0)])"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test24(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX y;
                YYY x;
                x.method(1, y);
                x.method(1, 1);
            }
        }
        class YYY {
            void method(float x; YYY y) { }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(x),Id(method),[IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test25(self):
        input = """
        class XXX extends YYY {
            int x() {
                int y;
                YYY x;
                x.method(1, 1);
                y.method(1, 1);
            }
        }
        class YYY {
            void method(float x; float y) { }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(y),Id(method),[IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test26(self):
        input = """
        class XXX {
            float x() {
                return 1;
            }
            float y() {
                return true;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test27(self):
        input = """
        class XXX {
            float[5] x() {
                return {1,2,3,4,5};
            }
            float[2] y() {
                return {true,true};
            }
        }
        """
        expect = "Type Mismatch In Statement: Return([BooleanLit(True),BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test28(self):
        input = """
        class XXX {
            int x() {
                int[3] x;
                int y;
                y := x[0];
                y := x[1];
                y := x[true];
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test29(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX[3] x;
                YYY y;
                y := x[0];
                y := x[1];
                y := y[true];
            }
        }
        class YYY { }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(y),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test30(self):
        input = """
        class XXX extends YYY {
            int x() {
                YYY[3] x;
                XXX y;
                x[0] := y;
                y := x[0];
            }
        }
        class YYY { }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y),ArrayCell(Id(x),IntLit(0)))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test31(self):
        input = """
        class XXX extends YYY {
            int x(float a, b; YYY c) {
                XXX x;
                YYY z;
                int y = x.x(1,1,z);
                int t = x.x(1,1,true);
            }
        }
        class YYY { }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(x),Id(x),[IntLit(1),IntLit(1),BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test32(self):
        input = """
        class XXX extends YYY {
            int x(float a, b; YYY c) {
                XXX x;
                YYY z;
                XXX u;
                float y = x.x(1,u.y(),z);
                int t = x.x(1,1,true);
            }
            int y () { }
        }
        class YYY { }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(x),Id(x),[IntLit(1),IntLit(1),BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test33(self):
        input = """
        class XXX extends YYY {
            int x(float a, b; YYY c) {
                XXX x;
                YYY z;
                int y = x.x(1,1,z);
                int t = x.y();
            }
            void y () { }
        }
        class YYY { }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(x),Id(y),[])"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test34(self):
        input = """
        class XXX extends YYY {
            int x(float a, b; YYY c) {
                XXX x;
                YYY z;
                int u;
                int y = x.x(1,1,z);
                int t = u.y();
            }
            void y () { }
        }
        class YYY { }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(u),Id(y),[])"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test35(self):
        input = """
        class XXX {
            int x = x;
        }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test36(self):
        input = """
        class XXX {
            int x () {
                int x = x;
            }
        }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test37(self):
        input = """
        class XXX extends YYY {
            int x(float a, b; YYY c) {
                XXX x;
                float y;
                y := x.y;
                y := XXX.x;
                y := y.p;
            }
        }
        class YYY {
            static int x;
            int y;
        }
        """
        expect = "Type Mismatch In Expression: FieldAccess(Id(y),Id(p))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test38(self):
        input = """
        class XXX extends YYY {
            int x(float a, b; YYY c) {
                final int x = 1;
                YYY z = new XXX();
                final int y = 1.0;
            }
        }
        class YYY {

        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),IntType,FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test39(self):
        input = """
        class XXX extends YYY {
            int x(float a, b; YYY c) {
                float[3] x = {1,2,1.0};
            }
        }
        class YYY { }
        """
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(1.0)]"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test40(self):
        input = """
        class XXX extends YYY {
            int x(float a, b; YYY c) {
                YYY x = new YYY();
                YYY[3] y = {x, x, x};
            }
        }
        class YYY { }
        """
        input = Program([
            ClassDecl(Id('XXX'), [
                MethodDecl(Instance(),Id('x'),[],IntType(),Block([],[
                    VarDecl(
                        Id('y'),
                        ArrayType(2,ClassType(Id('YYY'))),
                        ArrayLiteral([NewExpr(Id('YYY'),[]),NewExpr(Id('XXX'),[])])
                    )
                ]))
            ], Id('YYY')),
            ClassDecl(Id('YYY'),[])
        ])
        expect = "Illegal Array Literal: [NewExpr(Id(YYY),[]),NewExpr(Id(XXX),[])]"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test41(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.method1();
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(a),Id(method1),[])"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test42(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := b.method2();
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(b),Id(method2),[])"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test43(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := b.a;
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test44(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := a.a;
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(a),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test45(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := YYY.method4();
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(YYY),Id(method4),[])"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test46(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := b.method3();
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),Id(method3),[])"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test47(self):
        input = """
        class XXX {
            int x() {
                float x = + 2;
                x := -2;
                x := +2.0;
                x := -2.0;
                x := 1 + 2;
                x := 1 + 2.0;
                x := 1.0 + 2.0;
                x := 1 - 2;
                x := 1 - 2.0;
                x := 1.0 - 2.0;
                x := 1 * 2;
                x := 1 * 2.0;
                x := 1.0 * 2.0;
                x := 1 / 2;
                x := 1 / 2.0;
                x := 1.0 / 2.0;


                int y = 1 \\ 2;
                y := 2 % 2;
                y := 1.0 \\ 2;

            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(\,FloatLit(1.0),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test48(self):
        input = """
        class XXX {
            int x() {
                int y = 1 \\ 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(\,IntLit(1),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test49(self):
        input = """
        class XXX {
            int x() {
                int y = 1.0 \\ 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(\,FloatLit(1.0),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test50(self):
        input = """
        class XXX {
            int x() {
                int y = 1 % 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,IntLit(1),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test51(self):
        input = """
        class XXX {
            int x() {
                int y = 1.0 % 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(1.0),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test52(self):
        input = """
        class XXX {
            int x() {
                int y = 1 / 2;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(y),IntType,BinaryOp(/,IntLit(1),IntLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test53(self):
        input = """
        class XXX {
            int x() {
                int y = 1 / true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test54(self):
        input = """
        class XXX {
            int x() {
                boolean x = true && true;
                x := false || false;
                x := !true;
                x := !1;
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test55(self):
        input = """
        class XXX {
            int x() {
                boolean x = true && true;
                x := false || false;
                x := !true;
                x := 1 || false;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,IntLit(1),BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test56(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 == 2;
                x := 1 != 2;
                x := true == false;
                x := true != false;
                x := 1.0 == 1.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLit(1.0),FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test57(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 == 2;
                x := 1 != 2;
                x := true == false;
                x := true != false;
                x := 1.0 == true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLit(1.0),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test58(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 == 2;
                x := 1 != 2;
                x := true == false;
                x := true != false;
                x := 1.0 != true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,FloatLit(1.0),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test59(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 > 2;
                x := 1.0 < 2;
                x := 1.0 <= 2.0;
                x := 1.0 <= true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,FloatLit(1.0),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test60(self):
        input = """
        class XXX {
            int x() {
                string x = "aaa";
                x := x^"bbb";
                x := x^2;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(^,Id(x),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test61(self):
        input = Program([
            ClassDecl(Id('XXX'), [
                MethodDecl(Instance(),Id('x'),[],IntType(),Block([],[
                    VarDecl(
                        Id('y'),
                        ArrayType(2,ClassType(Id('XXX'))),
                        ArrayLiteral([SelfLiteral(),NewExpr(Id('XXX'),[])])
                    ),
                    VarDecl(
                        Id('z'),
                        ArrayType(2,ClassType(Id('YYY'))),
                        ArrayLiteral([SelfLiteral(),NewExpr(Id('YYY'),[])])
                    )
                ]))
            ], Id('YYY')),
            ClassDecl(Id('YYY'),[])
        ])
        expect = "Illegal Array Literal: [Self(),NewExpr(Id(YYY),[])]"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test62(self):
        input = """
        class XXX {
            int x() {
                int x;
                for x := 1 to 100 do {
                    continue;
                }
                break;                
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test63(self):
        input = """
        class XXX {
            int x() {
                int x;
                for x := 1 to 100 do {
                    break;
                }
                continue;                
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test64(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                final XXX y = new XXX();
            }
        }
        """
        expect = "Illegal Constant Expression: NewExpr(Id(XXX),[])"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test65(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                final XXX z = this;
            }
        }
        """
        expect = "Illegal Constant Expression: Self()"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test66(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                int b;
                final int c = b+1;        
            }
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,Id(b),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test67(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                final float y = YYY.x;       
            }
        }
        class YYY {
            static int x = 1;
            final int y = 1;
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(Id(YYY),Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test68(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                YYY z;
                final float y = z.y;       
            }
        }
        class YYY {
            static final int x = 1;
            int y = 1;
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(Id(z),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test69(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                YYY z;
                final YYY y = z;       
            }
        }
        class YYY {
            static final int x = 1;
            final int y = 1;
        }
        """
        expect = "Illegal Constant Expression: Id(z)"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test70(self):
        input = """
        class XXX extends YYY {
            int x(float a, b; YYY c) {
                YYY x = new YYY();
                YYY[3] y = {x, x, x};
            }
        }
        class YYY { }
        """
        input = Program([
            ClassDecl(Id('XXX'), [
                MethodDecl(Instance(),Id('x'),[],IntType(),Block([],[
                    VarDecl(
                        Id('y'),
                        ArrayType(2,ClassType(Id('YYY'))),
                        ArrayLiteral([NewExpr(Id('YYY'),[]),NewExpr(Id('XXX'),[])])
                    )
                ]))
            ], Id('YYY')),
            ClassDecl(Id('YYY'),[])
        ])
        expect = "Illegal Array Literal: [NewExpr(Id(YYY),[]),NewExpr(Id(XXX),[])]"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test71(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.method1();
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(a),Id(method1),[])"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test72(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := b.method2();
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(b),Id(method2),[])"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test73(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := b.a;
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test74(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := a.a;
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(a),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test75(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := YYY.method4();
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(YYY),Id(method4),[])"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test76(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := b.method3();
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),Id(method3),[])"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test77(self):
        input = """
        class XXX {
            int x() {
                float x = + 2;
                x := -2;
                x := +2.0;
                x := -2.0;
                x := 1 + 2;
                x := 1 + 2.0;
                x := 1.0 + 2.0;
                x := 1 - 2;
                x := 1 - 2.0;
                x := 1.0 - 2.0;
                x := 1 * 2;
                x := 1 * 2.0;
                x := 1.0 * 2.0;
                x := 1 / 2;
                x := 1 / 2.0;
                x := 1.0 / 2.0;


                int y = 1 \\ 2;
                y := 2 % 2;
                y := 1.0 \\ 2;

            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(\,FloatLit(1.0),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test78(self):
        input = """
        class XXX {
            int x() {
                int y = 1 \\ 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(\,IntLit(1),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test79(self):
        input = """
        class XXX {
            int x() {
                int y = 1.0 \\ 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(\,FloatLit(1.0),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test80(self):
        input = """
        class XXX {
            int x() {
                int y = 1 % 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,IntLit(1),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test81(self):
        input = """
        class XXX {
            int x() {
                int y = 1.0 % 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(1.0),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test82(self):
        input = """
        class XXX {
            int x() {
                int y = 1 / 2;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(y),IntType,BinaryOp(/,IntLit(1),IntLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test83(self):
        input = """
        class XXX {
            int x() {
                int y = 1 / true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test84(self):
        input = """
        class XXX {
            int x() {
                boolean x = true && true;
                x := false || false;
                x := !true;
                x := !1;
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test85(self):
        input = """
        class XXX {
            int x() {
                boolean x = true && true;
                x := false || false;
                x := !true;
                x := 1 || false;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,IntLit(1),BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 485))
    
    def test86(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 == 2;
                x := 1 != 2;
                x := true == false;
                x := true != false;
                x := 1.0 == 1.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLit(1.0),FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test87(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 == 2;
                x := 1 != 2;
                x := true == false;
                x := true != false;
                x := 1.0 == true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLit(1.0),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test88(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 == 2;
                x := 1 != 2;
                x := true == false;
                x := true != false;
                x := 1.0 != true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,FloatLit(1.0),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test89(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 > 2;
                x := 1.0 < 2;
                x := 1.0 <= 2.0;
                x := 1.0 <= true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,FloatLit(1.0),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test90(self):
        input = """
        class XXX {
            int x() {
                string x = "aaa";
                x := x^"bbb";
                x := x^2;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(^,Id(x),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test91(self):
        input = Program([
            ClassDecl(Id('XXX'), [
                MethodDecl(Instance(),Id('x'),[],IntType(),Block([],[
                    VarDecl(
                        Id('y'),
                        ArrayType(2,ClassType(Id('XXX'))),
                        ArrayLiteral([SelfLiteral(),NewExpr(Id('XXX'),[])])
                    ),
                    VarDecl(
                        Id('z'),
                        ArrayType(2,ClassType(Id('YYY'))),
                        ArrayLiteral([SelfLiteral(),NewExpr(Id('YYY'),[])])
                    )
                ]))
            ], Id('YYY')),
            ClassDecl(Id('YYY'),[])
        ])
        expect = "Illegal Array Literal: [Self(),NewExpr(Id(YYY),[])]"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test92(self):
        input = """
        class XXX {
            int x() {
                int x;
                for x := 1 to 100 do {
                    continue;
                }
                break;                
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test93(self):
        input = """
        class XXX {
            int x() {
                int x;
                for x := 1 to 100 do {
                    break;
                }
                continue;                
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test94(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                final XXX y = new XXX();
            }
        }
        """
        expect = "Illegal Constant Expression: NewExpr(Id(XXX),[])"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test95(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                final XXX z = this;
            }
        }
        """
        expect = "Illegal Constant Expression: Self()"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test96(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                int b;
                final int c = b+1;        
            }
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,Id(b),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test97(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                final float y = YYY.x;       
            }
        }
        class YYY {
            static int x = 1;
            final int y = 1;
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(Id(YYY),Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test98(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                YYY z;
                final float y = z.z;       
            }
        }
        class YYY {
            static final int x = 1;
            final int y = 1;
            int z;
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(Id(z),Id(z))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test99(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                YYY z;
                final YYY y = z;       
            }
        }
        class YYY {
            static final int x = 1;
            final int y = 1;
        }
        """
        expect = "Illegal Constant Expression: Id(z)"
        self.assertTrue(TestChecker.test(input, expect, 499))
