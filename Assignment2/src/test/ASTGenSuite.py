import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test2(self):
        input = """class main {
            int a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test3(self):
        input = """class main {
            int a;
            int b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))
    
    def test4(self):
        input = """class main {
            int a;
            static final int m =5,c=7,d=9;
            final static int a = 8;
            final int x=7;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Static(),ConstDecl(Id("m"),IntType(),IntLiteral(5))),
             AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(7))),
             AttributeDecl(Static(),ConstDecl(Id("d"),IntType(),IntLiteral(9))),
             AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(8))),
             AttributeDecl(Instance(),ConstDecl(Id("x"),IntType(),IntLiteral(7)))])]))
        self.assertTrue(TestAST.test(input,expect,303))
    
    def test5(self):
        input = """class A {
            final int My1stCons = 1+5, My2ndCons =2;
            static int x,y=0;
        }"""
        expect = str(Program([ClassDecl(Id("A"),
            [AttributeDecl(Instance(),ConstDecl(Id("My1stCons"),IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(5)))),
             AttributeDecl(Instance(),ConstDecl(Id("My2ndCons"),IntType(),IntLiteral(2))),
             AttributeDecl(Static(),VarDecl(Id("x"),IntType())),
             AttributeDecl(Static(),VarDecl(Id("y"),IntType(),IntLiteral(0)))])]))
        self.assertTrue(TestAST.test(input,expect,304))
    
    def test6(self):
        input = """class A {
            int funcA() {

            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(
            Instance(), Id("funcA"), [], IntType(), Block([], []))])]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test7(self):
        input = """class A {
            final int My1stCons = 1+5, My2ndCons =2;
            static int x,y=0;
            int funcA() {

            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[AttributeDecl(Instance(),ConstDecl(Id("My1stCons"),
        IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(5)))),
        AttributeDecl(Instance(),ConstDecl(Id("My2ndCons"),IntType(),IntLiteral(2))),
        AttributeDecl(Static(),VarDecl(Id("x"),IntType(),None)),AttributeDecl(Static(),VarDecl(Id("y"),IntType(),IntLiteral(0))),
        MethodDecl(Instance(),Id("funcA"),[],IntType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,306))
    
    def test8(self):
        input = """class A {
            final int My1stCons = 1+5, My2ndCons =2;
            static int x,y=0;
            int funcA(int x) {
                int a =7;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),
        [AttributeDecl(Instance(),ConstDecl(Id("My1stCons"),IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(5)))),
        AttributeDecl(Instance(),ConstDecl(Id("My2ndCons"),IntType(),IntLiteral(2))),
        AttributeDecl(Static(),VarDecl(Id("x"),IntType(),None)),AttributeDecl(Static(),VarDecl(Id("y"),IntType(),IntLiteral(0))),
        MethodDecl(Instance(),Id("funcA"),[VarDecl(Id("x"),IntType(),None)],IntType(),
        Block([VarDecl(Id("a"),IntType(),IntLiteral(7))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,307))
    
    def test9(self):
        input = """class A {
            final int My1stCons = 1+5, My2ndCons =2;
            static int x,y=0;
            int funcA(int x,a,y; float m,d) {
                int a =7;
                final float b = 7.0;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),
        [AttributeDecl(Instance(),ConstDecl(Id("My1stCons"),IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(5)))),
        AttributeDecl(Instance(),ConstDecl(Id("My2ndCons"),IntType(),IntLiteral(2))),
        AttributeDecl(Static(),VarDecl(Id("x"),IntType())),AttributeDecl(Static(),VarDecl(Id("y"),IntType(),IntLiteral(0))),
        MethodDecl(Instance(),Id("funcA"),[VarDecl(Id("x"),IntType()),VarDecl(Id("a"),IntType()),
        VarDecl(Id("y"),IntType()),VarDecl(Id("m"),FloatType()),VarDecl(Id("d"),FloatType())],IntType(),
        Block([VarDecl(Id("a"),IntType(),IntLiteral(7)),ConstDecl(Id("b"),FloatType(),FloatLiteral(7.0))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,308))
    
    def test10(self):
        input = """class A {
            final int My1stCons = 1+5, My2ndCons =2;
            static int x,y=0;
            A() {
                
            }
            int funcA(int x,a,y; float m,d) {
                int a =7;
                final float b = 7.0;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),
        [AttributeDecl(Instance(),ConstDecl(Id("My1stCons"),IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(5)))),
        AttributeDecl(Instance(),ConstDecl(Id("My2ndCons"),IntType(),IntLiteral(2))),
        AttributeDecl(Static(),VarDecl(Id("x"),IntType())),AttributeDecl(Static(),VarDecl(Id("y"),IntType(),IntLiteral(0))),
        MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),
        MethodDecl(Instance(),Id("funcA"),[VarDecl(Id("x"),IntType()),VarDecl(Id("a"),IntType()),VarDecl(Id("y"),IntType()),VarDecl(Id("m"),FloatType()),VarDecl(Id("d"),FloatType())],IntType(),
        Block([VarDecl(Id("a"),IntType(),IntLiteral(7)),ConstDecl(Id("b"),FloatType(),FloatLiteral(7.0))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,309))
    
    def test11(self):
        input = """class A {
            final int My1stCons = 1+5, My2ndCons =2;
            static int x,y=0;
            A(int x) {

            }
            int funcA(int x,a,y; float m,d) {
                int a =7;
                final float b = 7.0;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),
        [AttributeDecl(Instance(),ConstDecl(Id("My1stCons"),IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(5)))),
        AttributeDecl(Instance(),ConstDecl(Id("My2ndCons"),IntType(),IntLiteral(2))),
        AttributeDecl(Static(),VarDecl(Id("x"),IntType())),AttributeDecl(Static(),VarDecl(Id("y"),IntType(),IntLiteral(0))),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("x"),IntType())],None,Block([],[])),
        MethodDecl(Instance(),Id("funcA"),[VarDecl(Id("x"),IntType()),VarDecl(Id("a"),IntType()),
        VarDecl(Id("y"),IntType()),VarDecl(Id("m"),FloatType()),
        VarDecl(Id("d"),FloatType())],IntType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(7)),
        ConstDecl(Id("b"),FloatType(),FloatLiteral(7.0))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,310))
    
    def test12(self):
        input = """class A {
            final int My1stCons = 1+5, My2ndCons =2;
            static int x,y=0;
            A(int x) {
                this.x := x;
            }
            int funcA(int x,a,y; float m,d) {
                int a =7;
                 final float b = 7.0;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),
        [AttributeDecl(Instance(),ConstDecl(Id("My1stCons"),IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(5)))),
        AttributeDecl(Instance(),ConstDecl(Id("My2ndCons"),IntType(),IntLiteral(2))),
        AttributeDecl(Static(),VarDecl(Id("x"),IntType())),
        AttributeDecl(Static(),VarDecl(Id("y"),IntType(),IntLiteral(0))),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("x"),IntType())],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("x")),Id("x"))])),
        MethodDecl(Instance(),Id("funcA"),[VarDecl(Id("x"),IntType()),VarDecl(Id("a"),IntType()),VarDecl(Id("y"),IntType()),
        VarDecl(Id("m"),FloatType()),VarDecl(Id("d"),FloatType())],IntType(),
        Block([VarDecl(Id("a"),IntType(),IntLiteral(7)),
        ConstDecl(Id("b"),FloatType(),FloatLiteral(7.0))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,311))
    def test13(self):
        input = """
        class Maim {
            void main(){
                string [2] a="Hello world | checker";
                a.boo()[2] := b.boo[a.boo() +3];
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("a"),ArrayType(2,StringType()),StringLiteral('"Hello world | checker"'))],
        [Assign(ArrayCell(CallExpr(Id("a"),Id("boo"),[]),IntLiteral(2)),ArrayCell(FieldAccess(Id("b"),Id("boo")),
        BinaryOp("+",CallExpr(Id("a"),Id("boo"),[]),IntLiteral(3))))]))])]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test14(self):                                     # test19 in parser
        input = """class Tree {
            string Body;
            float height;
            int age;
            static string area = "Afri/*c*/a";
            Tree(string Body; float height) {
                this. Body := Body;
                this.height := height;
            } 
            }
            class Leaves extends Tree {
                static int leaf;
                string treeName;
                static void addLeaf(Tree tree; int leaf){
                    this.leaf := leaf;
                    treeName := "";
                }
                }
                """
        expect = str(Program([ClassDecl(Id("Tree"),
        [AttributeDecl(Instance(),VarDecl(Id("Body"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("height"),FloatType())),
        AttributeDecl(Instance(),VarDecl(Id("age"),IntType())),
        AttributeDecl(Static(),VarDecl(Id("area"),StringType(),StringLiteral('"Afri/*c*/a"'))),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("Body"),StringType()),VarDecl(Id("height"),FloatType())],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("Body")),Id("Body")),
        Assign(FieldAccess(SelfLiteral(),Id("height")),Id("height"))]))]),
        ClassDecl(Id("Leaves"),[AttributeDecl(Static(),VarDecl(Id("leaf"),IntType())),
        AttributeDecl(Instance(),VarDecl(Id("treeName"),StringType())),
        MethodDecl(Static(),Id("addLeaf"),[VarDecl(Id("tree"),ClassType(Id("Tree"))),VarDecl(Id("leaf"),IntType())],VoidType(),
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("leaf")),Id("leaf")),Assign(Id("treeName"),StringLiteral('""'))]))],Id("Tree"))]))
        self.assertTrue(TestAST.test(input,expect,313))
    
    def test15(self):                                     # test21 in parser
        input = """class Example1 {
            static int[10] staticvar;
            int foo(int a) {
                return a*2-+1/50 ^ "89" && true;
            }
            }
            class Example2 {
                void main() {
                    int[10] a = {1,2,3,4};

                }
                }"""
        expect = str(Program([ClassDecl(Id("Example1"),
        [AttributeDecl(Static(),VarDecl(Id("staticvar"),ArrayType(10,IntType()))),
        MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),
        Block([],[Return(BinaryOp("&&",BinaryOp("-",BinaryOp("*",Id("a"),IntLiteral(2)),BinaryOp("/",UnaryOp("+",IntLiteral(1)),
        BinaryOp("^",IntLiteral(50),StringLiteral('"89"')))),
        BooleanLiteral(True)))]))]),
        ClassDecl(Id("Example2"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(10,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),
        IntLiteral(4)]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,314))
    
    def test16(self):                                     # test17 in parser
        input = """class Man {
            int param, obj = 1;
            static void printinfo() {
                System.out.println("Day laf vi du");
            }
            void Alive() {
                if this.obj + 1 * 2 then return "Tui" ^ "Con" ^ "Alive"; else for i := 0 to 10 do {
                    this.obj := " [[]] ";
                }
            }
            void main() {
                Man obj = new Man();
                obj.printinfo();
                obj := obj + 1 - 12.e-13 > 50 ^ "String\\n";
            } 
        }"""
        expect = str(Program([ClassDecl(Id("Man"),
        [AttributeDecl(Instance(),VarDecl(Id("param"),IntType())),
        AttributeDecl(Instance(),VarDecl(Id("obj"),IntType(),IntLiteral(1))),
        MethodDecl(Static(),Id("printinfo"),[],VoidType(),Block([],[CallStmt(FieldAccess(Id("System"),Id("out")),
        Id("println"),[StringLiteral('"Day laf vi du"')])])),
        MethodDecl(Instance(),Id("Alive"),[],VoidType(),
        Block([],[If(BinaryOp("+",FieldAccess(SelfLiteral(),Id("obj")),BinaryOp("*",IntLiteral(1),IntLiteral(2))),
        Return(BinaryOp("^",BinaryOp("^",StringLiteral('"Tui"'),StringLiteral('"Con"')),StringLiteral('"Alive"'))),
        For(Id("i"),IntLiteral(0),IntLiteral(10),True,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("obj")),StringLiteral('" [[]] "'))])))])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("obj"),ClassType(Id("Man")),
        NewExpr(Id("Man"),[]))],[CallStmt(Id("obj"),Id("printinfo"),[]),
        Assign(Id("obj"),BinaryOp(">",BinaryOp("-",BinaryOp("+",Id("obj"),IntLiteral(1)),FloatLiteral(1.2e-12)),
        BinaryOp("^",IntLiteral(50),StringLiteral('"String\\n"'))))]))])]))
        self.assertTrue(TestAST.test(input,expect,315))
    
    def test17(self):                                     # test12 in parser
        input = """class Animal {
            static final int legs = 4;           # normally has 4 legs 
            string nose = "Nose\\t";  
            static void printN(){
                system.out.println(this.nose);
            }
            }
            class PigFish extends Animal {
                static void swim() {
                    io.swimsofar();
                    io.breathalittle();
                    io.keeponswim();
                    io.reachgoal();
                }
                    }
            class Test {
                void main() {
                    PigFish[3] pgf;
                    string[3] noseColor = {  "red\\b"   ,    "blue\\f"   ,   "green\\t"  };
                    for i := 0 to 2 do 
                        pgf[i] := noseColor[i];
                    for j := 2 downto 0 do {
                        pgf[j].printN();
                    }
                }
                }"""
        expect = str(Program([ClassDecl(Id("Animal"),
        [AttributeDecl(Static(),ConstDecl(Id("legs"),IntType(),IntLiteral(4))),
        AttributeDecl(Instance(),VarDecl(Id("nose"),StringType(),StringLiteral('"Nose\\t"'))),
        MethodDecl(Static(),Id("printN"),[],VoidType(),Block([],[CallStmt(FieldAccess(Id("system"),Id("out")),Id("println"),
        [FieldAccess(SelfLiteral(),Id("nose"))])]))]),
        ClassDecl(Id("PigFish"),[MethodDecl(Static(),Id("swim"),[],VoidType(),
        Block([],[CallStmt(Id("io"),Id("swimsofar"),[]),CallStmt(Id("io"),Id("breathalittle"),[]),
        CallStmt(Id("io"),Id("keeponswim"),[]),CallStmt(Id("io"),Id("reachgoal"),[])]))],Id("Animal")),
        ClassDecl(Id("Test"),[MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("pgf"),ArrayType(3,ClassType(Id("PigFish")))),
        VarDecl(Id("noseColor"),ArrayType(3,StringType()),ArrayLiteral([StringLiteral('"red\\b"'),StringLiteral('"blue\\f"'),StringLiteral('"green\\t"')]))],
        [For(Id("i"),IntLiteral(0),IntLiteral(2),True,Assign(ArrayCell(Id("pgf"),Id("i")),ArrayCell(Id("noseColor"),Id("i")))),
        For(Id("j"),IntLiteral(2),IntLiteral(0),False,Block([],[CallStmt(ArrayCell(Id("pgf"),Id("j")),Id("printN"),[])]))]))])]))
        self.assertTrue(TestAST.test(input,expect,316))
    
    def test18(self):                                     # test9 in parser
        input = """class Person {
            int age;
            float height;
            string name;
            string id;
            Person(int age; float height; string name,id){
                this.age := age;
                this.height := height;
                this.name := name;
                this.id := id;
            }
            void setName(string name) {
                this.name := name;
            }
            string getName(){
                return this.name + "LTT is the best";
            }
        }
        class Student extends Person{
            float mark = 10.0e+1;
            string conduct = "Good";
            float getMark() {
                return this.mark + 1.0;
            }
            void setConduct(string conduct){
                this.conduct := conduct;
            }
        }
        class Main {
            static int countST = 0;                               
            void main() {
                Student stu1;
                io.print(stu1.getMark());
                for i := 1 to 10 do {
                    stu1 := stu1 * 2;
                    if stu1 == 10 then break; else continue;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Person"),
        [AttributeDecl(Instance(),VarDecl(Id("age"),IntType())),
        AttributeDecl(Instance(),VarDecl(Id("height"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("name"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("id"),StringType())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("age"),IntType()),
        VarDecl(Id("height"),FloatType()),VarDecl(Id("name"),StringType()),VarDecl(Id("id"),StringType())],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("age")),Id("age")),
        Assign(FieldAccess(SelfLiteral(),Id("height")),Id("height")),Assign(FieldAccess(SelfLiteral(),Id("name")),Id("name")),
        Assign(FieldAccess(SelfLiteral(),Id("id")),Id("id"))])),
        MethodDecl(Instance(),Id("setName"),[VarDecl(Id("name"),StringType())],VoidType(),
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("name")),Id("name"))])),
        MethodDecl(Instance(),Id("getName"),[],StringType(),Block([],[Return(BinaryOp("+",FieldAccess(SelfLiteral(),Id("name")),
        StringLiteral('"LTT is the best"')))]))]),ClassDecl(Id("Student"),
        [AttributeDecl(Instance(),VarDecl(Id("mark"),FloatType(),FloatLiteral(100.0))),
        AttributeDecl(Instance(),VarDecl(Id("conduct"),StringType(),StringLiteral('"Good"'))),MethodDecl(Instance(),Id("getMark"),[],FloatType(),
        Block([],[Return(BinaryOp("+",FieldAccess(SelfLiteral(),Id("mark")),FloatLiteral(1.0)))])),
        MethodDecl(Instance(),Id("setConduct"),[VarDecl(Id("conduct"),StringType())],VoidType(),
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("conduct")),Id("conduct"))]))],Id("Person")),
        ClassDecl(Id("Main"),[AttributeDecl(Static(),VarDecl(Id("countST"),IntType(),IntLiteral(0))),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("stu1"),ClassType(Id("Student")))],
        [CallStmt(Id("io"),Id("print"),[CallExpr(Id("stu1"),Id("getMark"),[])]),For(Id("i"),IntLiteral(1),IntLiteral(10),True,
        Block([],[Assign(Id("stu1"),BinaryOp("*",Id("stu1"),IntLiteral(2))),If(BinaryOp("==",Id("stu1"),IntLiteral(10)),Break(),Continue())]))]))])]))
        self.assertTrue(TestAST.test(input,expect,317))
    
    def test19(self):                                     # test4 in parser
        input ="""class Integer {
            static final float count;
            string str_name = "Lam Thien Toan\\n";
            Integer(float count; string str){
                this.count := count;
                this.str_name := str;
            }
            void increment() {
                this.count := this.count + 1;
            }
        }
        class Example {
            void main() {
                bool x = true;
                int t = 0;
                if t == 0 then x := false; else t := t + 1;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Integer"),
        [AttributeDecl(Static(),ConstDecl(Id("count"),FloatType(),None)),
        AttributeDecl(Instance(),VarDecl(Id("str_name"),StringType(),StringLiteral('"Lam Thien Toan\\n"'))),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("count"),FloatType()),VarDecl(Id("str"),StringType())],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("count")),Id("count")),Assign(FieldAccess(SelfLiteral(),Id("str_name")),Id("str"))])),
        MethodDecl(Instance(),Id("increment"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("count")),
        BinaryOp("+",FieldAccess(SelfLiteral(),Id("count")),IntLiteral(1)))]))]),
        ClassDecl(Id("Example"),[MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("x"),ClassType(Id("bool")),BooleanLiteral(True)),
        VarDecl(Id("t"),IntType(),IntLiteral(0))],[If(BinaryOp("==",Id("t"),IntLiteral(0)),Assign(Id("x"),BooleanLiteral(False)),
        Assign(Id("t"),BinaryOp("+",Id("t"),IntLiteral(1))))]))])]))
        self.assertTrue(TestAST.test(input,expect,318))
    
    def test20(self):                                     # test3 in parser
        input = """class Shape {
                        float length,width;
                        float getArea() {}
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                            } 
                        }
                class Rectangle extends Shape {
                float getArea(){
                return this.length*this.width;
                    } }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    } }     
                class Example2 {
                    void main(){
                        Shape s;
                        s := new Rectangle(3,4);
                        io.writeFloatLn(s.getArea());
                        s := new Triangle(3,4);
                        io.writeFloatLn(s.getArea());
                    } }"""
        expect = str(Program([ClassDecl(Id("Shape"),
        [AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),
        MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[])),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),
        Id("width"))]))]),ClassDecl(Id("Rectangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),
        Block([],[Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape")),
        ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],
        [Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))),IntLiteral(2)))]))],Id("Shape")),
        ClassDecl(Id("Example2"),[MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),ClassType(Id("Shape")))],
        [Assign(Id("s"),NewExpr(Id("Rectangle"),[IntLiteral(3),IntLiteral(4)])),CallStmt(Id("io"),Id("writeFloatLn"),
        [CallExpr(Id("s"),Id("getArea"),[])]),Assign(Id("s"),NewExpr(Id("Triangle"),[IntLiteral(3),IntLiteral(4)])),
        CallStmt(Id("io"),Id("writeFloatLn"),[CallExpr(Id("s"),Id("getArea"),[])])]))])]))
        self.assertTrue(TestAST.test(input,expect,319))
    
    def test21(self):                                     # test23 in parser
        input = """class Example1 {
            static int[10] staticvar;
            int foo(int a) {
                return a*2-+1/50 ^ "89" && true;
            }
            int getVar(){
                return staticvar;
            } 
            }
            class Example2 {
                void main() {
                    Example1 obj = new Example1();
                    int[10] a = {1,2,3,4};
                    if x - 1 != obj.getVar()[3] then return 1; else return "5" / "10";
                }
                }"""
        expect = str(Program([ClassDecl(Id("Example1"),
        [AttributeDecl(Static(),VarDecl(Id("staticvar"),ArrayType(10,IntType()))),
        MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),
        Block([],[Return(BinaryOp("&&",BinaryOp("-",BinaryOp("*",Id("a"),IntLiteral(2)),
        BinaryOp("/",UnaryOp("+",IntLiteral(1)),BinaryOp("^",IntLiteral(50),StringLiteral('"89"')))),
        BooleanLiteral(True)))])),MethodDecl(Instance(),Id("getVar"),[],IntType(),Block([],[Return(Id("staticvar"))]))]),
        ClassDecl(Id("Example2"),[MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("obj"),ClassType(Id("Example1")),
        NewExpr(Id("Example1"),[])),VarDecl(Id("a"),ArrayType(10,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],
        [If(BinaryOp("!=",BinaryOp("-",Id("x"),IntLiteral(1)),ArrayCell(CallExpr(Id("obj"),Id("getVar"),[]),IntLiteral(3))),
        Return(IntLiteral(1)),Return(BinaryOp("/",StringLiteral('"5"'),StringLiteral('"10"'))))]))])]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test22(self):                                     # test24 in parser
        input = """class Example1 {
            static int[10] staticvar;
            int foo(int a) {
                return a*2-+1/50 ^ "89" && true;
            }
            int getVar(){
                return staticvar;
            } 
            }
            class Example2 {
                void main() {
                    Example1 obj = new Example1();
                    int[10] a = {1,2,3,4};
                    if x - 1 != obj.getVar()[3] then return 1; else return "5" / "10";
                    if a[b+ obj.foo(2)*3] - obj.staticvar[7] >= 0 then a[3 + x.foo(2)] := a[b[2]] +3; 
                }
                }"""
        expect = str(Program([ClassDecl(Id("Example1"),
        [AttributeDecl(Static(),VarDecl(Id("staticvar"),ArrayType(10,IntType()))),
        MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),Block([],
        [Return(BinaryOp("&&",BinaryOp("-",BinaryOp("*",Id("a"),IntLiteral(2)),BinaryOp("/",UnaryOp("+",IntLiteral(1)),
        BinaryOp("^",IntLiteral(50),StringLiteral('"89"')))),BooleanLiteral(True)))])),
        MethodDecl(Instance(),Id("getVar"),[],IntType(),Block([],[Return(Id("staticvar"))]))]),
        ClassDecl(Id("Example2"),[MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("obj"),ClassType(Id("Example1")),
        NewExpr(Id("Example1"),[])),VarDecl(Id("a"),ArrayType(10,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],
        [If(BinaryOp("!=",BinaryOp("-",Id("x"),IntLiteral(1)),ArrayCell(CallExpr(Id("obj"),Id("getVar"),[]),IntLiteral(3))),
        Return(IntLiteral(1)),Return(BinaryOp("/",StringLiteral('"5"'),StringLiteral('"10"')))),
        If(BinaryOp(">=",BinaryOp("-",ArrayCell(Id("a"),BinaryOp("+",Id("b"),BinaryOp("*",CallExpr(Id("obj"),Id("foo"),[IntLiteral("2")]),
        IntLiteral(3)))),ArrayCell(FieldAccess(Id("obj"),Id("staticvar")),IntLiteral(7))),IntLiteral(0)),Assign(ArrayCell(Id("a"),BinaryOp("+",IntLiteral(3),CallExpr(Id("x"),Id("foo"),[IntLiteral(2)]))),
        BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))))]))])]))
        self.assertTrue(TestAST.test(input,expect,321))
    
    def test23(self):                                     # test27 in parser
        input = """class Example1 {
            static int[10] staticvar;
            int foo(int a) {
                return a*2-+1/50 ^ "89" && true;
            }
            int getVar(){
                return staticvar;
            } 
            }
            class Example2 {
                void main() {
                    Example1 obj = new Example1();
                    int[10] a = {1,2,3,4};
                    if x - -01 != obj.getVar()[3] then return 1; else a[5] := obj.foo(2);
                    for i := 5 to 10 do {
                        obj.staticvar[i] := 1+"string"-"add";
                        break;
                        {
                            a[i * obj.foo(i)-10] := 5;
                            if x - -01 != obj.getVar()[3] then return 1; else a[5] := obj.foo(2);

                        }
                    }
                }
                }"""
        expect = str(Program([ClassDecl(Id("Example1"),
        [AttributeDecl(Static(),VarDecl(Id("staticvar"),ArrayType(10,IntType()))),
        MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),
        Block([],[Return(BinaryOp("&&",BinaryOp("-",BinaryOp("*",Id("a"),IntLiteral(2)),BinaryOp("/",UnaryOp("+",IntLiteral(1)),
        BinaryOp("^",IntLiteral(50),StringLiteral('"89"')))),BooleanLiteral(True)))])),
        MethodDecl(Instance(),Id("getVar"),[],IntType(),Block([],[Return(Id("staticvar"))]))]),
        ClassDecl(Id("Example2"),[MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("obj"),
        ClassType(Id("Example1")),NewExpr(Id("Example1"),[])),VarDecl(Id("a"),ArrayType(10,IntType()),
        ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],
        [If(BinaryOp("!=",BinaryOp("-",Id("x"),UnaryOp("-",IntLiteral(1))),ArrayCell(CallExpr(Id("obj"),Id("getVar"),[]),IntLiteral(3))),
        Return(IntLiteral(1)),Assign(ArrayCell(Id("a"),IntLiteral(5)),CallExpr(Id("obj"),Id("foo"),[IntLiteral(2)]))),
        For(Id("i"),IntLiteral(5),IntLiteral(10),True,Block([],[Assign(ArrayCell(FieldAccess(Id("obj"),Id("staticvar")),Id("i")),
        BinaryOp("-",BinaryOp("+",IntLiteral(1),StringLiteral('"string"')),StringLiteral('"add"'))),Break(),Block([],
        [Assign(ArrayCell(Id("a"),BinaryOp("-",BinaryOp("*",Id("i"),CallExpr(Id("obj"),Id("foo"),[Id("i")])),IntLiteral(10))),
        IntLiteral(5)),If(BinaryOp("!=",BinaryOp("-",Id("x"),UnaryOp("-",IntLiteral(1))),ArrayCell(CallExpr(Id("obj"),Id("getVar"),[]),
        IntLiteral(3))),Return(IntLiteral(1)),Assign(ArrayCell(Id("a"),IntLiteral(5)),CallExpr(Id("obj"),Id("foo"),[IntLiteral(2)])))])]))]))])]))
        self.assertTrue(TestAST.test(input,expect,322))
    
    def test24(self):                                     # test28 in parser
        input = """class Example1 {
            static int[5] count;
            }
                class Example2 extends Example1 {
                    Example1 obj1;
                    }
                    class Main {
                        void main() {
                            Example2 x;
                            int m = x.obj1.count[0];
                            for i := 0 to 10 do {
                                {
                                    m := x.obj1.count[i];
                                }
                            }
                        }
                        }"""
        expect = str(Program([ClassDecl(Id("Example1"),
        [AttributeDecl(Static(),VarDecl(Id("count"),ArrayType(5,IntType())))]),
        ClassDecl(Id("Example2"),[AttributeDecl(Instance(),VarDecl(Id("obj1"),ClassType(Id("Example1"))))],Id("Example1")),
        ClassDecl(Id("Main"),[MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("x"),ClassType(Id("Example2"))),
        VarDecl(Id("m"),IntType(),ArrayCell(FieldAccess(FieldAccess(Id("x"),Id("obj1")),Id("count")),IntLiteral(0)))],
        [For(Id("i"),IntLiteral(0),IntLiteral(10),True,Block([],[Block([],[Assign(Id("m"),ArrayCell(FieldAccess(FieldAccess(Id("x"),Id("obj1")),
        Id("count")),Id("i")))])]))]))])]))
        self.assertTrue(TestAST.test(input,expect,323))
    
    def test25(self):                                     # test31 in parser
        input = """class Example1 {
            int[5] x;
            }
            class Example2 extends Example1 {
                Example1[5] x; # array \n
                }
            class Example3 extends Example2 {
                Examples2[5] x; 
                }"""
        expect = str(Program([ClassDecl(Id("Example1"),
        [AttributeDecl(Instance(),VarDecl(Id("x"),ArrayType(5,IntType())))]),
        ClassDecl(Id("Example2"),[AttributeDecl(Instance(),VarDecl(Id("x"),ArrayType(5,ClassType(Id("Example1")))))],Id("Example1")),
        ClassDecl(Id("Example3"),[AttributeDecl(Instance(),VarDecl(Id("x"),ArrayType(5,ClassType(Id("Examples2")))))],Id("Example2"))]))
        self.assertTrue(TestAST.test(input,expect,324))
    
    def test26(self):                                     # test38 in parser
        input = """class Animal {
            static int age;
            string name;
            string fur;
            int[10] mong;
            Animal(int age; string name,fur; int[0] mong){
                this.age := age;
                this.fur := fur;
                for i := 0 to 9 do this.mong[i] := mong[i];
            }
            }
            class Cat extends Animal {
                Example1[5] x; # array
                static void foo() {
                    System.out.println("fnsjd");
                    this.x[2].name := "Cat \\n";
                } 
                void main(){
                        Cat m;
                        m.foo();
                    }
                }
                """
        expect = str(Program([ClassDecl(Id("Animal"),
        [AttributeDecl(Static(),VarDecl(Id("age"),IntType())),
        AttributeDecl(Instance(),VarDecl(Id("name"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fur"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("mong"),ArrayType(10,IntType()))),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("age"),IntType()),VarDecl(Id("name"),StringType()),
        VarDecl(Id("fur"),StringType()),VarDecl(Id("mong"),ArrayType(0,IntType()))],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("age")),Id("age")),Assign(FieldAccess(SelfLiteral(),Id("fur")),Id("fur")),
        For(Id("i"),IntLiteral(0),IntLiteral(9),True,Assign(ArrayCell(FieldAccess(SelfLiteral(),Id("mong")),Id("i")),
        ArrayCell(Id("mong"),Id("i"))))]))]),ClassDecl(Id("Cat"),[AttributeDecl(Instance(),VarDecl(Id("x"),ArrayType(5,ClassType(Id("Example1"))))),
        MethodDecl(Static(),Id("foo"),[],VoidType(),Block([],[CallStmt(FieldAccess(Id("System"),Id("out")),Id("println"),
        [StringLiteral('"fnsjd"')]),Assign(FieldAccess(ArrayCell(FieldAccess(SelfLiteral(),Id("x")),IntLiteral(2)),Id("name")),StringLiteral('"Cat \\n"'))])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("m"),ClassType(Id("Cat")))],
        [CallStmt(Id("m"),Id("foo"),[])]))],Id("Animal"))]))
        self.assertTrue(TestAST.test(input,expect,325))
    
    def test27(self):                                     # test39 in parser
        input = """class Animal {
            static int age;
            string name;
            string fur;
            int[10] mong;
            Animal(int age; string name,fur; int[0] mong){
                this.age := age;
                this.fur := fur;
                for i := 0 to 9 do this.mong[i] := mong[i];
            }
            }
            class Cat extends Animal {
                Example1[5] x; # array
                Example1 y;
                static void foo() {
                    System.out.println("fnsjd");
                    this.y.name := "Cat \\n";
                } 
                void main(){
                        Cat m;
                        m.foo();
                    }
                }
                """
        expect = str(Program([ClassDecl(Id("Animal"),
        [AttributeDecl(Static(),VarDecl(Id("age"),IntType())),
        AttributeDecl(Instance(),VarDecl(Id("name"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fur"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("mong"),ArrayType(10,IntType()))),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("age"),IntType()),VarDecl(Id("name"),StringType()),VarDecl(Id("fur"),StringType()),
        VarDecl(Id("mong"),ArrayType(0,IntType()))],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("age")),Id("age")),
        Assign(FieldAccess(SelfLiteral(),Id("fur")),Id("fur")),For(Id("i"),IntLiteral(0),IntLiteral(9),True,
        Assign(ArrayCell(FieldAccess(SelfLiteral(),Id("mong")),Id("i")),ArrayCell(Id("mong"),Id("i"))))]))]),
        ClassDecl(Id("Cat"),[AttributeDecl(Instance(),VarDecl(Id("x"),ArrayType(5,ClassType(Id("Example1"))))),
        AttributeDecl(Instance(),VarDecl(Id("y"),ClassType(Id("Example1")))),
        MethodDecl(Static(),Id("foo"),[],VoidType(),Block([],[CallStmt(FieldAccess(Id("System"),Id("out")),Id("println"),
        [StringLiteral('"fnsjd"')]),Assign(FieldAccess(FieldAccess(SelfLiteral(),Id("y")),Id("name")),StringLiteral('"Cat \\n"'))])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("m"),ClassType(Id("Cat")))],[CallStmt(Id("m"),Id("foo"),[])]))],Id("Animal"))]))
        self.assertTrue(TestAST.test(input,expect,326))
    
    def test28(self):                                     # test40 in parser
        input = """class Animal {
            static int age;
            string name;
            string fur;
            int[10] mong;
            Animal(int age; string name,fur; int[0] mong){
                this.age := age;
                this.fur := fur;
                for i := 0 to 9 do this.mong[i] := mong[i];
            }
            }
            class Cat extends Animal {
                Example1[5] x; # array
                Example1 y;
                static int count = 0;
                static void foo() {
                    System.out.println("fnsjd");
                    this.y.name := "Cat \\n";
                } 
                void main(){
                        Cat m;
                        m.foo();
                        Cat.count := 20*-"snfdjs\\f";
                    }
                }
                """
        expect = str(Program([ClassDecl(Id("Animal"),
        [AttributeDecl(Static(),VarDecl(Id("age"),IntType())),
        AttributeDecl(Instance(),VarDecl(Id("name"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fur"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("mong"),ArrayType(10,IntType()))),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("age"),IntType()),VarDecl(Id("name"),StringType()),VarDecl(Id("fur"),StringType()),
        VarDecl(Id("mong"),ArrayType(0,IntType()))],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("age")),Id("age")),
        Assign(FieldAccess(SelfLiteral(),Id("fur")),Id("fur")),For(Id("i"),IntLiteral(0),IntLiteral(9),True,
        Assign(ArrayCell(FieldAccess(SelfLiteral(),Id("mong")),Id("i")),ArrayCell(Id("mong"),Id("i"))))]))]),
        ClassDecl(Id("Cat"),[AttributeDecl(Instance(),VarDecl(Id("x"),ArrayType(5,ClassType(Id("Example1"))))),
        AttributeDecl(Instance(),VarDecl(Id("y"),ClassType(Id("Example1")))),
        AttributeDecl(Static(),VarDecl(Id("count"),IntType(),IntLiteral(0))),
        MethodDecl(Static(),Id("foo"),[],VoidType(),Block([],[CallStmt(FieldAccess(Id("System"),Id("out")),Id("println"),[StringLiteral('"fnsjd"')]),
        Assign(FieldAccess(FieldAccess(SelfLiteral(),Id("y")),Id("name")),StringLiteral('"Cat \\n"'))])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("m"),ClassType(Id("Cat")))],[CallStmt(Id("m"),Id("foo"),[]),
        Assign(FieldAccess(Id("Cat"),Id("count")),BinaryOp("*",IntLiteral(20),UnaryOp("-",StringLiteral('"snfdjs\\f"'))))]))],Id("Animal"))]))
        self.assertTrue(TestAST.test(input,expect,327))
    
    def test29(self):                                     # test44 in parser
        input = """class Name {
            static final int a;
            static print a() {
                
            }
            }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),None)),
        MethodDecl(Static(),Id("a"),[],ClassType(Id("print")),Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,328))
    
    def test30(self):                                     # test49 in parser
        input ="""class Exmap {
                Example () {
                    (a+b)[3] := 50;
                }
            }"""
        expect = str(Program([ClassDecl(Id("Exmap"),
        [MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Assign(ArrayCell(BinaryOp("+",Id("a"),Id("b")),IntLiteral(3)),IntLiteral(50))]))])]))
        self.assertTrue(TestAST.test(input,expect,329))
    
    def test31(self):                                     # test55 in parser
        input = """class Name{
            string firstName, lastName, fullName;
            static void  printName(void name) {
                this.firstName := name;
            }
            }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),VoidType())],VoidType(),
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name"))]))])]))
        self.assertTrue(TestAST.test(input,expect,330))
    
    def test32(self):                                     # test60 in parser
        input = """class Name{
            string firstName, lastName, fullName;
            static void  printName(int name,    _final) {
                this.firstName := name;
            }
            }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],
        VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name"))]))])]))
        self.assertTrue(TestAST.test(input,expect,331))
    
    def test33(self):                                     # test67 in parser
        input = """class Name{
             string firstName, lastName, fullName;
          static void  printName(int name, _final) {
                final int count = 0;
                this.firstName := name;
                
            }
           }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0))],[Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name"))]))])]))
        self.assertTrue(TestAST.test(input,expect,332))
    
    def test34(self):                                     # test68 in parser
        input = """class Name{
             string firstName, lastName, fullName;
          static void  printName(int name, _final) {
                final int count = 0;
                this.firstName := name;
                
            }
            void main(){
                this.aPI := 3.14;
                value := x.foo(5);
                l[3] := value * 2;
            }
           }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0))],[Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name"))])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14)),
        Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),
        BinaryOp("*",Id("value"),IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input,expect,333))
    
    def test35(self):                                     # test69 in parser
        input = """class Name{
             string firstName, lastName, fullName;
          static void  printName(int name, _final) {
                final int count = 0;
                this.firstName := name;
                
            }
            void main(){
                this.aPI := 3.14;
                value := x.foo(5);
                l[3] := value * 2;
            }
           }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],
        VoidType(),Block([ConstDecl(Id("count"),IntType(),IntLiteral(0))],
        [Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name"))])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14)),
        Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),
        BinaryOp("*",Id("value"),IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input,expect,334))
    
    def test36(self):                                     # test70 in parser
        input = """class Name{
             string firstName, lastName, fullName;
          static void  printName(int name, _final) {
                final int count = 0;
                this.firstName := name;
                if flag then
                    io.writeStrLn("Expression is true");
                else
                    io.writeStrLn ("Expression is false");
                
            }
            void main(){
                this.aPI := 3.14;
                value := x.foo(5);
                l[3] := value * 2;
            }
           }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0))],[Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name")),
        If(Id("flag"),CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is true"')]),
        CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is false"')]))])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14)),
        Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),
        BinaryOp("*",Id("value"),IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input,expect,335))
    
    def test37(self):                                     # test71 in parser
        input =   """class Name{
             string firstName, lastName, fullName;
          static void  printName(int name, _final) {
                final int count = 0;
                this.firstName := name;
                if flag then
                    io.writeStrLn("Expression is true");
                else
                    io.writeStrLn ("Expression is false");
                
            }
            void main(){
                this.aPI := 3.14;
                value := x.foo(5);
                l[3] := value * 2;
                if flag then
                    io.writeStrLn("Expression is true");
                else
                    io.writeStrLn ("Expression is false");
            }
           }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0))],[Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name")),
        If(Id("flag"),CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is true"')]),
        CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is false"')]))])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14)),
        Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),
        BinaryOp("*",Id("value"),IntLiteral(2))),If(Id("flag"),CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is true"')]),
        CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is false"')]))]))])]))
        self.assertTrue(TestAST.test(input,expect,336))
    
    def test38(self):                                     # test75 in parser
        input = """class Name{
             string firstName, lastName, fullName;
          static void  printName(int name, _final) {
                final int count = 0;
                this.firstName := name;
                if flag then
                     {io.writeStrLn("Expression is true");
                     io.writeStrLn ("Expression is false");}
                     else if flag then
                     {io.writeStrLn("Expression is true");
                     io.writeStrLn ("Expression is false");}
            }
            void main(){
                this.aPI := 3.14;
                value := x.foo(5);
                l[3] := value * 2;
            }
           }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0))],[Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name")),
        If(Id("flag"),Block([],[CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is true"')]),
        CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is false"')])]),
        If(Id("flag"),Block([],[CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is true"')]),
        CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is false"')])])))])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14)),
        Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),
        BinaryOp("*",Id("value"),IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input,expect,337))
    
    def test39(self):                                     # test78 in parser
        input = """class Name{
             string firstName, lastName, fullName;
          static void  printName(int name, _final) {
                final int count = 0;
                this.firstName := name;
                {
                if flag then
                     {io.writeStrLn("Expression is true");
                     io.writeStrLn ("Expression is false");}
                     else if flag then
                     {io.writeStrLn("Expression is true");
                     io.writeStrLn ("Expression is false");}}
                     for _ := i to 50 do return _;
            }
            void main(){
                this.aPI := 3.14;
                value := x.foo(5);
                l[3] := value * 2[2];
            }
           }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0))],[Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name")),
        Block([],[If(Id("flag"),Block([],[CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is true"')]),
        CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is false"')])]),
        If(Id("flag"),Block([],[CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is true"')]),
        CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"Expression is false"')])])))]),
        For(Id("_"),Id("i"),IntLiteral(50),True,Return(Id("_")))])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14)),
        Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),
        BinaryOp("*",Id("value"),ArrayCell(IntLiteral(2),IntLiteral(2))))]))])]))
        self.assertTrue(TestAST.test(input,expect,338))
    
    def test40(self):                                     # test84 in parser
        input = """class Name{
             string firstName, lastName, fullName;
          static void  printName(int name, _final) {
                final int count = 0;
                string x ={"rue","flase","1","\\b:\\""};
                this.firstName := name;
                {
                     for _ := i to 50 do return _;}}
            void main(){
                this.aPI := 3.14;
                value := x.foo(5);
                l[3] := value * 2[2];
            }
           }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0)),VarDecl(Id("x"),StringType(),ArrayLiteral([StringLiteral('"rue"'),StringLiteral('"flase"'),
        StringLiteral('"1"'),StringLiteral('"\\b:\\""')]))],[Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name")),
        Block([],[For(Id("_"),Id("i"),IntLiteral(50),True,Return(Id("_")))])])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14)),
        Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),BinaryOp("*",Id("value"),
        ArrayCell(IntLiteral(2),IntLiteral(2))))]))])]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test41(self):                                     # test85 in parser
        input = """class Example1 {
    #         int[5] x;
    #         }
    #         class Example2 extends Example1 {
    #             Example1[5] x; # array \n
    #             }
    #         class Example3 extends Example2 {
    #             Examples2[5] x; 
    #             }
    #             class main {
    #                 void main(){
    #                     Example3[10] x;
    #                     for i := 9 downto 0 do {
    #                         {
    #                             {
    #                                 x[0].x[i].x[j] := 1 == 2 - "3" && 4;
    #                             }
    #                         }
    #                     }
    #                 }
                     }"""
        expect = str(Program([ClassDecl(Id("Example1"),[])]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test42(self):                                     # test88 in parser
        input = """class Name{
              string firstName, lastName, fullName, _string;
           static void  printName(int name, _final) {
                 final int count = 0;
                 string x ={"rue","flase","1","\\b:\\""};
                 this.firstName := name;
                {
                      for _ := i to 50 do return _;}}
             void main(){
                 this.aPI := 3.14;
                 value := x.foo(5);
                 l[3] := value * 2[2];
                 for i := +3 to -10 do return x;
            }
            }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("_string"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0)),VarDecl(Id("x"),StringType(),
        ArrayLiteral([StringLiteral('"rue"'),StringLiteral('"flase"'),StringLiteral('"1"'),StringLiteral('"\\b:\\""')]))],
        [Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name")),Block([],[For(Id("_"),Id("i"),IntLiteral(50),True,
        Return(Id("_")))])])),MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),
        FloatLiteral(3.14)),Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),
        BinaryOp("*",Id("value"),ArrayCell(IntLiteral(2),IntLiteral(2)))),For(Id("i"),UnaryOp("+",IntLiteral(3)),UnaryOp("-",IntLiteral(10)),
        True,Return(Id("x")))]))])]))
        self.assertTrue(TestAST.test(input,expect,341))
    
    def test43(self):                                     # test89 in parser
        input = """class Name{
              string firstName, lastName, fullName, _string;
           static void  printName(int name, _final) {
                 final int count = 0;
                 string x ={"rue","flase","1","\\b:\\""};
                 this.firstName := name;
                {
                      for _ := i to 50 do return _;}}
             void main(){
                 this.aPI := 3.14;
                 value := x.foo(5);
                 l[3] := value * 2[2];
                 for i := +3 to -10 do return x;
            }
            void main() {
                twice twice = 5;
            }
            }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("_string"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0)),VarDecl(Id("x"),StringType(),
        ArrayLiteral([StringLiteral('"rue"'),StringLiteral('"flase"'),StringLiteral('"1"'),StringLiteral('"\\b:\\""')]))],
        [Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name")),
        Block([],[For(Id("_"),Id("i"),IntLiteral(50),True,Return(Id("_")))])])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14)),
        Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),
        BinaryOp("*",Id("value"),ArrayCell(IntLiteral(2),IntLiteral(2)))),For(Id("i"),UnaryOp("+",IntLiteral(3)),
        UnaryOp("-",IntLiteral(10)),True,Return(Id("x")))])),MethodDecl(Instance(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("twice"),ClassType(Id("twice")),IntLiteral(5))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,342))
    
    def test44(self):                                     # test90 in parser
        input = """class Name{
              string firstName, lastName, fullName, _string;
           static void  printName(int name, _final) {
                 final int count = 0;
                 string x ={"rue","flase","1","\\b:\\""};
                 this.firstName := name;
                {
                      for _ := i to 50 do return _;}}
             void main(){
                 this.aPI := 3.14;
                 value := x.foo(5);
                 l[3] := value * 2[2];
                 for i := +3 to -10 do return x;
                 {
                     x := 5;
                     {
                         final string x ={"",""};
                     }
                 }
            }
            void main() {
                twice twice = 5;
            }
            }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("_string"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0)),VarDecl(Id("x"),StringType(),
        ArrayLiteral([StringLiteral('"rue"'),StringLiteral('"flase"'),StringLiteral('"1"'),StringLiteral('"\\b:\\""')]))],
        [Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name")),Block([],[For(Id("_"),Id("i"),IntLiteral(50),True,Return(Id("_")))])])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14)),
        Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),
        BinaryOp("*",Id("value"),ArrayCell(IntLiteral(2),IntLiteral(2)))),For(Id("i"),UnaryOp("+",IntLiteral(3)),
        UnaryOp("-",IntLiteral(10)),True,Return(Id("x"))),Block([],[Assign(Id("x"),IntLiteral(5)),
        Block([ConstDecl(Id("x"),StringType(),ArrayLiteral([StringLiteral('""'),StringLiteral('""')]))],[])])])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("twice"),ClassType(Id("twice")),IntLiteral(5))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,343))
    
    def test45(self):                                     # test92 in parser
        input = """class Name{
              string firstName, lastName, fullName, _string;
           static void  printName(int name, _final) {
                 final int count = 0;
                 string x ={"rue","flase","1","\\b:\\""};
                 this.firstName := name;
                {
                      for _ := i to 50 do return _;}}
             void main(){
                 this.aPI := 3.14;
                 value := x.foo(5);
                 l[3] := value * 2[2];
                 for i := +3 to -10 do return x;
                 {
                     x := 5;
                     {
                         final string x ={"",""};
                     }
                 }
            }
            void main() {
                twice twice = 5;
                if x != 4 then for x := 7 to --8 do return 1;
            }
            }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [AttributeDecl(Instance(),VarDecl(Id("firstName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("lastName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("fullName"),StringType())),
        AttributeDecl(Instance(),VarDecl(Id("_string"),StringType())),
        MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0)),VarDecl(Id("x"),StringType(),
        ArrayLiteral([StringLiteral('"rue"'),StringLiteral('"flase"'),StringLiteral('"1"'),StringLiteral('"\\b:\\""')]))],
        [Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name")),
        Block([],[For(Id("_"),Id("i"),IntLiteral(50),True,Return(Id("_")))])])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14)),
        Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),
        Assign(ArrayCell(Id("l"),IntLiteral(3)),BinaryOp("*",Id("value"),ArrayCell(IntLiteral(2),IntLiteral(2)))),
        For(Id("i"),UnaryOp("+",IntLiteral(3)),UnaryOp("-",IntLiteral(10)),True,Return(Id("x"))),
        Block([],[Assign(Id("x"),IntLiteral(5)),Block([ConstDecl(Id("x"),StringType(),ArrayLiteral([StringLiteral('""'),StringLiteral('""')]))],
        [])])])),MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("twice"),ClassType(Id("twice")),IntLiteral(5))],
        [If(BinaryOp("!=",Id("x"),IntLiteral(4)),For(Id("x"),IntLiteral(7),UnaryOp("-",UnaryOp("-",IntLiteral(8))),True,Return(IntLiteral(1))))]))])]))
        self.assertTrue(TestAST.test(input,expect,344))
    
    def test46(self):                                     # test95 in parser
        input = """class Name{
           static void  printName(int name, _final) {
                 final int count = 0;
                 string x ={"rue","flase","1","\\b:\\""};
                 this.firstName := name;
                {
                      for _ := i to 50 do return _;}}
             void main(){
                 this.aPI := 3.14;
                 value := x.foo(5);
                 l[3] := value * 2[2];
                 for i := +3 to -10 do return x;
                 {
                     x := 5;
                     {
                         final string x ={"",""};
                     }
                 }
            }
            void main() {
                twice twice = 5;
                Name1 na_me = new Name();
                if x != 4 then for x := 7 to --8 do return 1;
                
            }
            }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],VoidType(),
        Block([ConstDecl(Id("count"),IntType(),IntLiteral(0)),VarDecl(Id("x"),StringType(),
        ArrayLiteral([StringLiteral('"rue"'),StringLiteral('"flase"'),StringLiteral('"1"'),StringLiteral('"\\b:\\""')]))],
        [Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name")),Block([],[For(Id("_"),Id("i"),IntLiteral(50),True,Return(Id("_")))])])),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14)),
        Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),
        BinaryOp("*",Id("value"),ArrayCell(IntLiteral(2),IntLiteral(2)))),For(Id("i"),UnaryOp("+",IntLiteral(3)),UnaryOp("-",IntLiteral(10)),True,
        Return(Id("x"))),Block([],[Assign(Id("x"),IntLiteral(5)),Block([ConstDecl(Id("x"),StringType(),ArrayLiteral([StringLiteral('""'),StringLiteral('""')]))],
        [])])])),MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("twice"),ClassType(Id("twice")),IntLiteral(5)),
        VarDecl(Id("na_me"),ClassType(Id("Name1")),NewExpr(Id("Name"),[]))],[If(BinaryOp("!=",Id("x"),IntLiteral(4)),
        For(Id("x"),IntLiteral(7),UnaryOp("-",UnaryOp("-",IntLiteral(8))),True,Return(IntLiteral(1))))]))])]))
        self.assertTrue(TestAST.test(input,expect,345))
    
    def test47(self):                                     # test96 in parser
        input = """class Name{
           static void  printName(int name, _final) {
                 final int count = 0;
                 string x ={"rue","flase","1","\\b:\\""};
                 this.firstName := name;
                {
                      for _ := i to 50 do return _;}}
             void main(){
                 this.aPI := 3.14;
                 value := x.foo(5);
                 l[3] := value * 2[2];
                 for i := +3 to -10 do return x;
                 {
                     x := 5;
                     {
                         final string x ={"",""};
                     }
                 }
            }
            void main(int _7,_3; string[3] args) {
                twice twice = 5;
                Name1 na_me = new Name();
                if x != 4 then for x := 7 to --8 do return 1;
                
            }
            }"""
        expect = str(Program([ClassDecl(Id("Name"),
        [MethodDecl(Static(),Id("printName"),[VarDecl(Id("name"),IntType()),VarDecl(Id("_final"),IntType())],
        VoidType(),Block([ConstDecl(Id("count"),IntType(),IntLiteral(0)),VarDecl(Id("x"),StringType(),
        ArrayLiteral([StringLiteral('"rue"'),StringLiteral('"flase"'),StringLiteral('"1"'),StringLiteral('"\\b:\\""')]))],
        [Assign(FieldAccess(SelfLiteral(),Id("firstName")),Id("name")),Block([],[For(Id("_"),Id("i"),IntLiteral(50),True,
        Return(Id("_")))])])),MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("aPI")),
        FloatLiteral(3.14)),Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),Assign(ArrayCell(Id("l"),IntLiteral(3)),
        BinaryOp("*",Id("value"),ArrayCell(IntLiteral(2),IntLiteral(2)))),For(Id("i"),UnaryOp("+",IntLiteral(3)),UnaryOp("-",IntLiteral(10)),
        True,Return(Id("x"))),Block([],[Assign(Id("x"),IntLiteral(5)),Block([ConstDecl(Id("x"),StringType(),ArrayLiteral([StringLiteral('""'),StringLiteral('""')]))],[])])])),
        MethodDecl(Instance(),Id("main"),[VarDecl(Id("_7"),IntType()),VarDecl(Id("_3"),IntType()),VarDecl(Id("args"),ArrayType(3,StringType()))],
        VoidType(),Block([VarDecl(Id("twice"),ClassType(Id("twice")),IntLiteral(5)),VarDecl(Id("na_me"),ClassType(Id("Name1")),
        NewExpr(Id("Name"),[]))],[If(BinaryOp("!=",Id("x"),IntLiteral(4)),For(Id("x"),IntLiteral(7),UnaryOp("-",UnaryOp("-",IntLiteral(8))),True,
        Return(IntLiteral(1))))]))])]))
        self.assertTrue(TestAST.test(input,expect,346))
        
    def test48(self):                                     # test101 in parser
        input = """
        class Buildng {
            float height,weight;
            int getType() {}
            Buildng(float height,weight){
                this.height := height;
                this.weight := weight;
            }
        }
        class School extends Buildng {
            int getType(){
            if(this.height>300) then return this.weight/1000; 
                else return 0;
            }
        }
        class Skybox extends Buildng {
            int getType(){
            if(this.height>300) then return this.weight/1000.e0; else return 0; 
            }
        }
        class Maim {
            void main(){
            s := new School(3,4);
            (b.coo().d.ass()).o();
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Buildng"),
        [AttributeDecl(Instance(),VarDecl(Id("height"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("weight"),FloatType())),
        MethodDecl(Instance(),Id("getType"),[],IntType(),Block([],[])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("height"),FloatType()),
        VarDecl(Id("weight"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("height")),Id("height")),
        Assign(FieldAccess(SelfLiteral(),Id("weight")),Id("weight"))]))]),ClassDecl(Id("School"),
        [MethodDecl(Instance(),Id("getType"),[],IntType(),Block([],[If(BinaryOp(">",FieldAccess(SelfLiteral(),Id("height")),IntLiteral(300)),
        Return(BinaryOp("/",FieldAccess(SelfLiteral(),Id("weight")),IntLiteral(1000))),
        Return(IntLiteral(0)))]))],Id("Buildng")),ClassDecl(Id("Skybox"),[MethodDecl(Instance(),Id("getType"),[],IntType(),Block([],
        [If(BinaryOp(">",FieldAccess(SelfLiteral(),Id("height")),IntLiteral(300)),Return(BinaryOp("/",FieldAccess(SelfLiteral(),
        Id("weight")),FloatLiteral(1000.0))),Return(IntLiteral(0)))]))],Id("Buildng")),ClassDecl(Id("Maim"),[MethodDecl(Instance(),Id("main"),
        [],VoidType(),Block([],[Assign(Id("s"),NewExpr(Id("School"),[IntLiteral(3),IntLiteral(4)])),CallStmt(CallExpr(
        FieldAccess(CallExpr(Id("b"),Id("coo"),[]),Id("d")),Id("ass"),[]),Id("o"),[])]))])]))
        self.assertTrue(TestAST.test(input,expect,347))
    
    def test49(self):                                     # test104 in parser
        input = """
        class Buildng {
            float height,weight;
            int getType() {}
            Buildng(float height,weight){
                this.height := this.weight \\ 6 /3.0;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Buildng"),
        [AttributeDecl(Instance(),VarDecl(Id("height"),FloatType())),
        AttributeDecl(Instance(),VarDecl(Id("weight"),FloatType())),MethodDecl(Instance(),Id("getType"),[],IntType(),Block([],[])),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("height"),FloatType()),VarDecl(Id("weight"),FloatType())],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("height")),BinaryOp("/",BinaryOp("\\",FieldAccess(SelfLiteral(),Id("weight")),
        IntLiteral(6)),FloatLiteral(3.0)))]))])]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test50(self):                                     # test105 in parser
        input = """
        class Buildng {
        }
        """
        expect = str(Program([ClassDecl(Id("Buildng"),[])]))
        self.assertTrue(TestAST.test(input,expect,349))
    
    def test51(self):                                     # test110 in parser
        input = """
        class Room {
            static int totalNum=0;
            string ID;
            Room(){
                this.ID:=nil;
            }
            Room(string name){
                this.name:=name;
                Room.totalNum := Room.totalNum +1;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Room"),
        [AttributeDecl(Static(),VarDecl(Id("totalNum"),IntType(),IntLiteral(0))),
        AttributeDecl(Instance(),VarDecl(Id("ID"),StringType())),MethodDecl(Instance(),Id("<init>"),[],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("ID")),NullLiteral())])),MethodDecl(Instance(),Id("<init>"),
        [VarDecl(Id("name"),StringType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("name")),Id("name")),
        Assign(FieldAccess(Id("Room"),Id("totalNum")),BinaryOp("+",FieldAccess(Id("Room"),Id("totalNum")),IntLiteral(1)))]))])]))
        self.assertTrue(TestAST.test(input,expect,350))
    
    def test52(self):                                     # test112 in parser
        input = """
        class Maim {
            void main(){
                float a;
                a:=1.;
                io.writeFloatLn(a);
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType())],
        [Assign(Id("a"),FloatLiteral(1.0)),CallStmt(Id("io"),Id("writeFloatLn"),[Id("a")])]))])]))
        self.assertTrue(TestAST.test(input,expect,351))
    
    def test53(self):                                     # test116 in parser
        input = """
        class Maim /* extends */ {
            void main(){
            string[100] a; 
            a := "Hello world";
            } 
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(100,StringType()))],
        [Assign(Id("a"),StringLiteral('"Hello world"'))]))])]))
        self.assertTrue(TestAST.test(input,expect,352))
    
    def test54(self):                                     # test117 in parser
        input = """
        class Room {
            string name;
            Room(){
                this.name:=nil;
            }
            void not(){
               string b;
               b:="I dont know";
               this.name:=this.name^b; 
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Room"),
        [AttributeDecl(Instance(),VarDecl(Id("name"),StringType())),
        MethodDecl(Instance(),Id("<init>"),[],None,Block([],
        [Assign(FieldAccess(SelfLiteral(),Id("name")),NullLiteral())])),
        MethodDecl(Instance(),Id("not"),[],VoidType(),Block([VarDecl(Id("b"),StringType())],
        [Assign(Id("b"),StringLiteral('"I dont know"')),Assign(FieldAccess(SelfLiteral(),Id("name")),
        BinaryOp("^",FieldAccess(SelfLiteral(),Id("name")),Id("b")))]))])]))
        self.assertTrue(TestAST.test(input,expect,353))
    
    def test55(self):                                     # test119 in parser
        input = """
        class Room {
            string name;
            Room(){
                this.name:=nil;
            }
            void not(){
               string b;
               b:="I dont know";
               return this.name^b; 
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Room"),
        [AttributeDecl(Instance(),VarDecl(Id("name"),StringType())),
        MethodDecl(Instance(),Id("<init>"),[],None,Block([],
        [Assign(FieldAccess(SelfLiteral(),Id("name")),NullLiteral())])),
        MethodDecl(Instance(),Id("not"),[],VoidType(),Block([VarDecl(Id("b"),StringType())],
        [Assign(Id("b"),StringLiteral('"I dont know"')),Return(BinaryOp("^",FieldAccess(SelfLiteral(),Id("name")),Id("b")))]))])]))
        self.assertTrue(TestAST.test(input,expect,354))
    
    def test56(self):                                     # test120 in parser
        input = """
        class Room {
            static int[4] total={0,0,0,0};
            string name;
            Room(){
                this.name:=nil;
            }
            Room(string name){
                this.name:=name;
                ID.total[0] := ID.total[0] +1;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Room"),
        [AttributeDecl(Static(),VarDecl(Id("total"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(0),
        IntLiteral(0),IntLiteral(0),IntLiteral(0)]))),AttributeDecl(Instance(),VarDecl(Id("name"),StringType())),
        MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("name")),NullLiteral())])),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("name"),StringType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),
        Id("name")),Id("name")),Assign(ArrayCell(FieldAccess(Id("ID"),Id("total")),IntLiteral(0)),BinaryOp("+",ArrayCell(FieldAccess(
            Id("ID"),Id("total")),IntLiteral(0)),IntLiteral(1)))]))])]))
        self.assertTrue(TestAST.test(input,expect,355))
    
    def test57(self):                                     # test122 in parser
        input = """
        class Maim {
            void main(){
            (b.c[2]).o();
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[CallStmt(ArrayCell(FieldAccess(Id("b"),Id("c")),IntLiteral(2)),Id("o"),[])]))])]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test58(self):                                     # test124 in parser
        input = """
        class printer {
            static void print(int a,b,c; float b){
                io.print(a+b+c+b);
            }
        }
        """
        expect = str(Program([ClassDecl(Id("printer"),
        [MethodDecl(Static(),Id("print"),[VarDecl(Id("a"),IntType()),
        VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType()),VarDecl(Id("b"),FloatType())],VoidType(),Block([],[CallStmt(Id("io"),
        Id("print"),[BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),Id("b"))])]))])]))
        self.assertTrue(TestAST.test(input,expect,357))
    
    def test59(self):                                     # test125 in parser
        input = """
        class printer {
            static void print(int a,b; float b; int c){
                io.print(a+b+c+b);
            }
        }
        """
        expect = str(Program([ClassDecl(Id("printer"),
        [MethodDecl(Static(),Id("print"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("b"),FloatType()),
        VarDecl(Id("c"),IntType())],VoidType(),Block([],[CallStmt(Id("io"),Id("print"),[BinaryOp("+",BinaryOp("+",BinaryOp("+",
        Id("a"),Id("b")),Id("c")),Id("b"))])]))])]))
        self.assertTrue(TestAST.test(input,expect,358))
    
    def test60(self):                                     # test126 in parser
        input = """
        class printer {
            static void print(int a,b; float b; int c){
                if a < b
                    then if b>c
                        then c := a ;
                    else c:= b;
                else c:=a;         
            }
        }
        """
        expect = str(Program([ClassDecl(Id("printer"),
        [MethodDecl(Static(),Id("print"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("b"),FloatType()),
        VarDecl(Id("c"),IntType())],VoidType(),Block([],[If(BinaryOp("<",Id("a"),Id("b")),
        If(BinaryOp(">",Id("b"),Id("c")),Assign(Id("c"),Id("a")),Assign(Id("c"),Id("b"))),Assign(Id("c"),Id("a")))]))])]))
        self.assertTrue(TestAST.test(input,expect,359))
    
    def test61(self):                                     # test129 in parser
        input = """
        class printer {
            static void print(int a; int b; float b; int c){
                io.print(a+b+c+b);
            }
        }
        """
        expect = str(Program([ClassDecl(Id("printer"),
        [MethodDecl(Static(),Id("print"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("b"),FloatType()),
        VarDecl(Id("c"),IntType())],VoidType(),Block([],[CallStmt(Id("io"),Id("print"),[BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),
        Id("b")),Id("c")),Id("b"))])]))])]))
        self.assertTrue(TestAST.test(input,expect,360))
    
    def test62(self):                                     # test133 in parser
        input = """
        class Buildng {
            float height,weight;
            static int getType() {}
            Buildng(float height,weight){
                this.height := "height";
                this.weight := weight;
            }
        }
        class School extends Buildng {
            static int getType(){
            if(this.height>300) then return this.weight/1000; else return 0;
            }
        }
        class Skybox extends Buildng {
            static int getType(){
            return (this.height*this.weight)/2;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Buildng"),
        [AttributeDecl(Instance(),VarDecl(Id("height"),FloatType())),
        AttributeDecl(Instance(),VarDecl(Id("weight"),FloatType())),
        MethodDecl(Static(),Id("getType"),[],IntType(),Block([],[])),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("height"),FloatType()),VarDecl(Id("weight"),FloatType())],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("height")),StringLiteral('"height"')),Assign(FieldAccess(SelfLiteral(),
        Id("weight")),Id("weight"))]))]),ClassDecl(Id("School"),[MethodDecl(Static(),Id("getType"),[],IntType(),
        Block([],[If(BinaryOp(">",FieldAccess(SelfLiteral(),Id("height")),IntLiteral(300)),Return(BinaryOp("/",FieldAccess(SelfLiteral(),
        Id("weight")),IntLiteral(1000))),Return(IntLiteral(0)))]))],Id("Buildng")),ClassDecl(Id("Skybox"),[MethodDecl(Static(),
        Id("getType"),[],IntType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("height")),
        FieldAccess(SelfLiteral(),Id("weight"))),IntLiteral(2)))]))],Id("Buildng"))]))
        self.assertTrue(TestAST.test(input,expect,361))
    
    def test63(self):                                     # test134 in parser
        input = """
        class Buildng {
            float height,weight;
            int getType() {}
            # Buildng(float height,weight){
            #    this.height := "height";
            #    this.weight := weight;
            # }
        }
        class School extends Buildng {
            int getType(){
            if(this.height>300) then return this.weight/1000; else return 0;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Buildng"),
        [AttributeDecl(Instance(),VarDecl(Id("height"),FloatType())),
        AttributeDecl(Instance(),VarDecl(Id("weight"),FloatType())),
        MethodDecl(Instance(),Id("getType"),[],IntType(),Block([],[]))]),
        ClassDecl(Id("School"),[MethodDecl(Instance(),Id("getType"),[],IntType(),Block([],[If(BinaryOp(">",
        FieldAccess(SelfLiteral(),Id("height")),IntLiteral(300)),Return(BinaryOp("/",FieldAccess(SelfLiteral(),Id("weight")),IntLiteral(1000))),
        Return(IntLiteral(0)))]))],Id("Buildng"))]))
        self.assertTrue(TestAST.test(input,expect,362))
    
    def test64(self):                                     # test135 in parser
        input = """
        class Buildng {
            float height,weight;
            int getType() {}
            /* Buildng(float height,weight){
                this.height := "height";
                this.weight := weight;
            } */
        }
        class School extends Buildng {
            int getType(){
                return this.weight/1000; 
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Buildng"),
        [AttributeDecl(Instance(),VarDecl(Id("height"),FloatType())),
        AttributeDecl(Instance(),VarDecl(Id("weight"),FloatType())),
        MethodDecl(Instance(),Id("getType"),[],IntType(),Block([],[]))]),
        ClassDecl(Id("School"),[MethodDecl(Instance(),Id("getType"),[],IntType(),Block([],[Return(BinaryOp("/",FieldAccess(SelfLiteral(),
        Id("weight")),IntLiteral(1000)))]))],Id("Buildng"))]))
        self.assertTrue(TestAST.test(input,expect,363))
    
    def test65(self):                                     # test137 in parser
        input = """
        class array {
            int[4] element;
            array(int a,b; float c){
                element[0]:=a;
                element[1]:=b;
                element[2]:=c;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("array"),
        [AttributeDecl(Instance(),VarDecl(Id("element"),ArrayType(4,IntType()))),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType())],
        None,Block([],[Assign(ArrayCell(Id("element"),IntLiteral(0)),Id("a")),Assign(ArrayCell(Id("element"),IntLiteral(1)),Id("b")),
        Assign(ArrayCell(Id("element"),IntLiteral(2)),Id("c"))]))])]))
        self.assertTrue(TestAST.test(input,expect,364))
    
    def test66(self):                                     # test139 in parser
        input = """
        class Room {
            string name;
            Room(){
                this.name:=nil;
            }
            Room(string name){
                this.name:=name;
            }
        }
        class Maim{
            void main(){
                s:= new Room();
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Room"),
        [AttributeDecl(Instance(),VarDecl(Id("name"),StringType())),
        MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("name")),NullLiteral())])),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("name"),StringType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("name")),
        Id("name"))]))]),ClassDecl(Id("Maim"),[MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(Id("s"),NewExpr(Id("Room"),[]))]))])]))
        self.assertTrue(TestAST.test(input,expect,365))
    
    def test67(self):                                     # test140 in parser
        input = """
        class Room {
            static int totalNum=0;
            string ID;
            Room(){
                this.ID:=nil;
            }
            Room(string name){
                this.name:=name;
                Room.totalNum := Room.totalNum +1;
            }
        }
        class Maim{
            void main(){
                s:= new ID("Hello World");
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Room"),
        [AttributeDecl(Static(),VarDecl(Id("totalNum"),IntType(),IntLiteral(0))),
        AttributeDecl(Instance(),VarDecl(Id("ID"),StringType())),MethodDecl(Instance(),Id("<init>"),[],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("ID")),NullLiteral())])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("name"),StringType())],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("name")),Id("name")),Assign(FieldAccess(Id("Room"),Id("totalNum")),BinaryOp("+",
        FieldAccess(Id("Room"),Id("totalNum")),IntLiteral(1)))]))]),ClassDecl(Id("Maim"),[MethodDecl(Instance(),Id("main"),[],VoidType(),
        Block([],[Assign(Id("s"),NewExpr(Id("ID"),[StringLiteral('"Hello World"')]))]))])]))
        self.assertTrue(TestAST.test(input,expect,366))
    
    def test68(self):                                     # test143 in parser
        input = """
        class Maim {
            void main(){
                int[4] a={1,2,3,4};
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(4,IntType()),
        ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,367))
    
    def test69(self):                                     # test144 in parser
        input = """
        class Maim {
            void main(){
                float[4] a={1.0,2.0,3.0,4.e+1};
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("a"),ArrayType(4,FloatType()),ArrayLiteral([FloatLiteral(1.0),FloatLiteral(2.0),FloatLiteral(3.0),FloatLiteral(40.0)]))],
        []))])]))
        self.assertTrue(TestAST.test(input,expect,368))
    
    def test70(self):                                     # test145 in parser
        input = """
        class Maim {
            void main(){
                float[4] a={1.0,2.0,3.0,4.0};
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(4,FloatType()),
        ArrayLiteral([FloatLiteral(1.0),FloatLiteral(2.0),FloatLiteral(3.0),FloatLiteral(4.0)]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,369))
    
    def test71(self):                                     # test151 in parser
        input = """
        class Employee {
            void print() {
                io.print("Finish work");
            }
        }
        class Employee2 {
            void print(){
                io.print("Create work");
            }
        }
        class Maim {
            void main(){
            s := new Employee2();
            s.print();
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Employee"),
        [MethodDecl(Instance(),Id("print"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("print"),
        [StringLiteral('"Finish work"')])]))]),ClassDecl(Id("Employee2"),[MethodDecl(Instance(),Id("print"),[],VoidType(),
        Block([],[CallStmt(Id("io"),Id("print"),[StringLiteral('"Create work"')])]))]),ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(Id("s"),NewExpr(Id("Employee2"),[])),CallStmt(Id("s"),Id("print"),[])]))])]))
        self.assertTrue(TestAST.test(input,expect,370))
    
    def test72(self):                                     # test153 in parser
        input = """
        class Maim {
            void main(){
            int c;
            c:=(a <= b).coo()[2];
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("c"),IntType())],[Assign(Id("c"),
        ArrayCell(CallExpr(BinaryOp("<=",Id("a"),Id("b")),Id("coo"),[]),IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input,expect,371))
    
    def test73(self):                                     # test154 in parser
        input = """
        class Maim {
            void main(){
            int c;
            c:=c.a(b.d);
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("c"),IntType())],
        [Assign(Id("c"),CallExpr(Id("c"),Id("a"),[FieldAccess(Id("b"),Id("d"))]))]))])]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test74(self):                                     # test155 in parser
        input = """
        class Maim {
            void main(){
            int c;
            c:=a.b.d;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("c"),IntType())],
        [Assign(Id("c"),FieldAccess(FieldAccess(Id("a"),Id("b")),Id("d")))]))])]))
        self.assertTrue(TestAST.test(input,expect,373))
    
    def test75(self):                                     # test157 in parser
        input = """
        class Maim {
            void main(){
            int c;
            c:=a.b().d()[2] || true + false;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("c"),IntType())],[Assign(Id("c"),BinaryOp("||",ArrayCell(CallExpr(CallExpr(Id("a"),Id("b"),[]),
        Id("d"),[]),IntLiteral(2)),BinaryOp("+",BooleanLiteral(True),BooleanLiteral(False))))]))])]))
        self.assertTrue(TestAST.test(input,expect,374))
    
    def test76(self):                                     # test158 in parser
        input = """
        class Maim {
            void main(){
            int c;
            c:=a.b().d()[2] || true + false;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("c"),IntType())],
        [Assign(Id("c"),BinaryOp("||",ArrayCell(CallExpr(CallExpr(Id("a"),Id("b"),[]),Id("d"),[]),
        IntLiteral(2)),BinaryOp("+",BooleanLiteral(True),BooleanLiteral(False))))]))])]))
        self.assertTrue(TestAST.test(input,expect,375))
    
    def test77(self):                                     # test160 in parser
        input = """
        class Room {
            static final int total=0;
            final static string name;
            Room(){
                this.name:=nil;
            }
            Room(string name){
                this.name:=name;
                ID.total := ID.total +1;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Room"),
        [AttributeDecl(Static(),ConstDecl(Id("total"),IntType(),IntLiteral(0))),
        AttributeDecl(Static(),ConstDecl(Id("name"),StringType(),None)),
        MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("name")),NullLiteral())])),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("name"),StringType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("name")),
        Id("name")),Assign(FieldAccess(Id("ID"),Id("total")),BinaryOp("+",FieldAccess(Id("ID"),Id("total")),IntLiteral(1)))]))])]))
        self.assertTrue(TestAST.test(input,expect,376))
    
    def test78(self):                                     # test165 in parser
        input = """
        class Maim {
            void main(){
                string a;
                a := nil;
            } 
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),StringType())],
        [Assign(Id("a"),NullLiteral())]))])]))
        self.assertTrue(TestAST.test(input,expect,377))
    
    def test79(self):                                     # test169 in parser
        input = """
        class Room {
            string name;
            Room(){
                this.name:=nil;
            }
            void not(){
               return this.name^this.name; 
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Room"),
        [AttributeDecl(Instance(),VarDecl(Id("name"),StringType())),
        MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("name")),NullLiteral())])),
        MethodDecl(Instance(),Id("not"),[],VoidType(),Block([],[Return(BinaryOp("^",FieldAccess(SelfLiteral(),Id("name")),FieldAccess(SelfLiteral(),
        Id("name"))))]))])]))
        self.assertTrue(TestAST.test(input,expect,378))
    
    def test80(self):                                     # test172 in parser
        input = """
        class Maim {
            void main(){
            int a;
            a:=0;
            for i := 10 downto 1 do
                a:= a+1;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType())],[Assign(Id("a"),IntLiteral(0)),
        For(Id("i"),IntLiteral(10),IntLiteral(1),False,Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))))]))])]))
        self.assertTrue(TestAST.test(input,expect,379))
    
    def test81(self):                                     # test174 in parser
        input = """
        class Buildng {
            float height,weight;
            int getType() {}
            Buildng(float height,weight){
                this.height := "height";
                this.weight := weight;
            }
            static int num =0;
        }
        """
        expect = str(Program([ClassDecl(Id("Buildng"),
        [AttributeDecl(Instance(),VarDecl(Id("height"),FloatType())),
        AttributeDecl(Instance(),VarDecl(Id("weight"),FloatType())),
        MethodDecl(Instance(),Id("getType"),[],IntType(),Block([],[])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("height"),FloatType()),
        VarDecl(Id("weight"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("height")),StringLiteral('"height"')),
        Assign(FieldAccess(SelfLiteral(),Id("weight")),Id("weight"))])),AttributeDecl(Static(),VarDecl(Id("num"),IntType(),IntLiteral(0)))])]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test82(self):                                     # test177 in parser
        input = """
        class array {
            static int[4] element = {1,2,3,4};
        }
        """
        expect = str(Program([ClassDecl(Id("array"),
        [AttributeDecl(Static(),VarDecl(Id("element"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])))])]))
        self.assertTrue(TestAST.test(input,expect,381))
    
    def test83(self):                                     # test179 in parser
        input = """
        class Room {
            string name;
            Room(){
                this.name:=nil;
            }
            Room(string name){
                this.name:=name;
            }
        }
        class Maim{
            void main(){
                s:= new Room();
                if S.name==nil then
                    break;
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Room"),
        [AttributeDecl(Instance(),VarDecl(Id("name"),StringType())),
        MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("name")),NullLiteral())])),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("name"),StringType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("name")),\
        Id("name"))]))]),ClassDecl(Id("Maim"),[MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],[Assign(Id("s"),
        NewExpr(Id("Room"),[])),If(BinaryOp("==",FieldAccess(Id("S"),Id("name")),NullLiteral()),Break())]))])]))
        self.assertTrue(TestAST.test(input,expect,382))
    
    def test84(self):                                     # test185 in parser
        input = """
        class Maim {
            void main(){
                float[4] a /* ={1.0,2.0,3.0,4.0} */; 
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(4,FloatType()))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,383))
    
    def test85(self):                                     # test188 in parser
        input = """
        class Maim {
            void main(){
                boolean [4]a="Helloworld"^a.boo[4];
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(4,BoolType()),
        BinaryOp("^",StringLiteral('"Helloworld"'),ArrayCell(FieldAccess(Id("a"),Id("boo")),IntLiteral(4))))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,384))
    
    def test86(self):                                     # test192 in parser
        input = """
        class Maim {
            void main(){
                int[2] a; #Check comment 
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(2,IntType()))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,385))
    
    def test87(self):                                     # test194 in parser
        input = """
        class Maim {
            void main(){
                a:=1.e+3-4.e+1-1.0+e.coo();
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([],
        [Assign(Id("a"),BinaryOp("+",BinaryOp("-",BinaryOp("-",FloatLiteral(1000.0),FloatLiteral(40.0)),FloatLiteral(1.0)),
        CallExpr(Id("e"),Id("coo"),[])))]))])]))
        self.assertTrue(TestAST.test(input,expect,386))
    
    def test88(self):                                     # test195 in parser
        input = """
        class Maim {
            void main(){
                float[4] a;
                this.print(a); 
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(4,FloatType()))],[CallStmt(SelfLiteral(),Id("print"),[Id("a")])]))])]))
        self.assertTrue(TestAST.test(input,expect,387))
    
    def test89(self):                                     # test198 in parser
        input = """
        class Maim {
            void main(){
                boolean [4]a="Helloworld /* ";
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("a"),ArrayType(4,BoolType()),StringLiteral('"Helloworld /* "'))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,388))

    def test90(self):                                     # test199 in parser
        input = """
        class Maim {
            void main(){
                string [2] a="Hello world | checker";
                a.boo()[2] := b.boo[a.boo() +3];
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(2,StringType()),
        StringLiteral('"Hello world | checker"'))],[Assign(ArrayCell(CallExpr(Id("a"),Id("boo"),[]),IntLiteral(2)),
        ArrayCell(FieldAccess(Id("b"),Id("boo")),BinaryOp("+",CallExpr(Id("a"),Id("boo"),[]),IntLiteral(3))))]))])]))
        self.assertTrue(TestAST.test(input,expect,389))
    
    def test91(self):                                     # test31 in parser
        input = """class rec{
        int w,b;
        int main(){
        io.readInt(this.w);
        io.readInt(this.b);
        io.writeInt(w*b);
        }}"""
        expect = str(Program([ClassDecl(Id("rec"),
        [AttributeDecl(Instance(),VarDecl(Id("w"),IntType())),
        AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),
        MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[CallStmt(Id("io"),Id("readInt"),[FieldAccess(SelfLiteral(),
        Id("w"))]),CallStmt(Id("io"),Id("readInt"),[FieldAccess(SelfLiteral(),Id("b"))]),CallStmt(Id("io"),Id("writeInt"),
        [BinaryOp("*",Id("w"),Id("b"))])]))])]))
        self.assertTrue(TestAST.test(input,expect,390))
    
    def test92(self):                                     # test31 in parser
        input = """class A{
        void main(){
        bool x;
        if x then x:={1,2,  3};
        }}"""
        expect = str(Program([ClassDecl(Id("A"),
        [MethodDecl(Instance(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("x"),ClassType(Id("bool")))],
        [If(Id("x"),Assign(Id("x"),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])))]))])]))
        self.assertTrue(TestAST.test(input,expect,391))
    
    def test93(self):                                     # test31 in parser
        input = """class _ {
                final float x;
                void main(){
                    _ _ ;
                }
            }"""
        expect = str(Program([ClassDecl(Id("_"),
        [AttributeDecl(Instance(),ConstDecl(Id("x"),FloatType(),None)),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("_"),ClassType(Id("_")))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,392))
    
    def test94(self):                                     # test31 in parser
        input = """class _ {
                final float x;
                void main(){
                    _ _ ;
                }
                static string voi(_ __){

                }
            }"""
        expect = str(Program([ClassDecl(Id("_"),
        [AttributeDecl(Instance(),ConstDecl(Id("x"),FloatType(),None)),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("_"),ClassType(Id("_")))],[])),
        MethodDecl(Static(),Id("voi"),[VarDecl(Id("__"),ClassType(Id("_")))],StringType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,393))
    
    def test95(self):                                     # test31 in parser
        input = """class _ {
                final float x;
                void main(){
                    _ _ ;
                }
                static string voi(_ __){
                    __ := "__" + ___ ^ 23 --7;
                }
            }"""
        expect = str(Program([ClassDecl(Id("_"),
        [AttributeDecl(Instance(),ConstDecl(Id("x"),FloatType(),None)),
        MethodDecl(Instance(),Id("main"),[],VoidType(),Block([VarDecl(Id("_"),ClassType(Id("_")))],[])),
        MethodDecl(Static(),Id("voi"),[VarDecl(Id("__"),ClassType(Id("_")))],StringType(),
        Block([],[Assign(Id("__"),BinaryOp("-",BinaryOp("+",StringLiteral('"__"'),BinaryOp("^",Id("___"),IntLiteral(23))),
        UnaryOp("-",IntLiteral(7))))]))])]))
        self.assertTrue(TestAST.test(input,expect,394))
    
    def test96(self):                                     # test31 in parser
        input = """class Example1 extends extend {
            int[5] x;
                Example1(Example1 Example1){}
            }
            """
        expect = str(Program([ClassDecl(Id("Example1"),
        [AttributeDecl(Instance(),VarDecl(Id("x"),ArrayType(5,IntType()))),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("Example1"),ClassType(Id("Example1")))],None,Block([],[]))],Id("extend"))]))
        self.assertTrue(TestAST.test(input,expect,395))
    
    def test97(self):                                     # test31 in parser
        input = """class Example1 extends extends_ {
            int[5] x;
                Example1(Example1 Example1){
                    Example1 Example1;
                }
            }
            """
        expect = str(Program([ClassDecl(Id("Example1"),[AttributeDecl(Instance(),VarDecl(Id("x"),ArrayType(5,IntType()))),
        MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("Example1"),ClassType(Id("Example1")))],None,
        Block([VarDecl(Id("Example1"),ClassType(Id("Example1")))],[]))],Id("extends_"))]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test98(self):                                     # test31 in parser
        input = """class Example1 extends _extends {
            #int[5] x;
                Example1(Example1 Example1){
                    Example1 Example1 = this.mnil;
                }
            }
            """
        expect = str(Program([ClassDecl(Id("Example1"),
        [MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("Example1"),
        ClassType(Id("Example1")))],None,Block([VarDecl(Id("Example1"),ClassType(Id("Example1")),FieldAccess(SelfLiteral(),Id("mnil")))],[]))],Id("_extends"))]))
        self.assertTrue(TestAST.test(input,expect,397))
    
    def test99(self):                                     # test31 in parser
        input = """class Example1 extends _extends {
            #int[5] x;
                Example1(Example1 Example1){
                    Example1 Example1 = this.nilx;
                    example1 := nil + nil;
                }
            }
            """
        expect = str(Program([ClassDecl(Id("Example1"),
        [MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("Example1"),ClassType(Id("Example1")))],None,
        Block([VarDecl(Id("Example1"),ClassType(Id("Example1")),FieldAccess(SelfLiteral(),Id("nilx")))],
        [Assign(Id("example1"),BinaryOp("+",NullLiteral(),NullLiteral()))]))],Id("_extends"))]))
        self.assertTrue(TestAST.test(input,expect,398))
    
    def test100(self):                                     # test31 in parser
        input = """class Example1 extends _extends {
            #int[5] x;
                Example1(Example1 Example1){
                    Example1 Example1 = this.nilx - nilx.thiss;
                    example1 := a.foo7()[10];
                }
            }
            """
        expect = str(Program([ClassDecl(Id("Example1")
        ,[MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("Example1"),ClassType(Id("Example1")))],None,
        Block([VarDecl(Id("Example1"),ClassType(Id("Example1")),BinaryOp("-",FieldAccess(SelfLiteral(),Id("nilx")),
        FieldAccess(Id("nilx"),Id("thiss"))))],[Assign(Id("example1"),ArrayCell(CallExpr(Id("a"),Id("foo7"),[]),IntLiteral(10)))]))],Id("_extends"))]))
        self.assertTrue(TestAST.test(input,expect,399))
    
        
    
