import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_0(self):
        input = """class BKoolClass {
            static void main() {io.writeInt(1);}
            }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_1(self):
        input = """class BKoolClass {static void main() {io.writeInt(1+3);}}"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_2(self):
    	input = Program([ClassDecl(Id("BKoolClass"),
                            [MethodDecl(Static(),Id("main"),[],VoidType(),
                                Block([],[CallStmt(Id("io"),Id("writeInt"),[IntLiteral(1)])]))])])
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_3(self):
        input = Program([ClassDecl(Id("BKoolClass"),
                    [MethodDecl(Static(),Id("main"),[],VoidType(),
                        Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_4(self):
        input = """class BKoolClass {
            static void main() {io.writeFloat(1.1);}
            }"""
        expect = "1.1"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_5(self):
        input = """class BKoolClass {
            static void main() { int x = 1; io.writeInt(x);}
            }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_6(self):
        input = """class BKoolClass {
            static void main() { 
                int x = 1;
                x := x+100;
                io.writeInt(x);}
            }"""
        expect = "101"
        self.assertTrue(TestCodeGen.test(input,expect,506))