import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    #======================================= 0-9 ==========================================
    # test ID
    def test_id_1(self):
        self.assertTrue(TestLexer.test("aA09 A12a","aA09,A12a,<EOF>",100))
    def test_id_2(self):
        self.assertTrue(TestLexer.test("_acd1~cd", "_acd1,Error Token ~", 101))
    def test_id_3(self):
        self.assertTrue(TestLexer.test("_Abc001 ?_ac","_Abc001,Error Token ?",102))
    def test_id_4(self):
        self.assertTrue(TestLexer.test("p_pl_211 dnc_1k_2s0","p_pl_211,dnc_1k_2s0,<EOF>",103))
    def test_id_5(self):
        self.assertTrue(TestLexer.test("abc @a2_1","abc,Error Token @",104))
    def test_id_6(self):
        self.assertTrue(TestLexer.test("a _ bc _012 cd_012","a,_,bc,_012,cd_012,<EOF>",105))
    # test comment
    def test_cmt_1(self):
        self.assertTrue(TestLexer.test("abc#123\nabc","abc,abc,<EOF>",106))
    def test_cmt_2(self):
        self.assertTrue(TestLexer.test("abc #123   asc agc abc", "abc,<EOF>", 107))
    def test_cmt_3(self):
        self.assertTrue(TestLexer.test("abc/*123*/ abc","abc,abc,<EOF>",108))
    def test_cmt_4(self):
        self.assertTrue(TestLexer.test("abc /*123\nabc*/ a012 _ 123","abc,a012,_,123,<EOF>",109))
    #======================================= 10 - 19 ==========================================
    def test_cmt_5(self):
        self.assertTrue(TestLexer.test("_1ab2 /* cAA end abc","_1ab2,/,*,cAA,end,abc,<EOF>",110))
    # test string
    def test_str1(self):
        self.assertTrue(TestLexer.test(""" "Test string in this" """,""""Test string in this",<EOF>""",111))
    def test_str2(self):
        self.assertTrue(TestLexer.test(""" "Bob talk: \\"Hi, I'm Bop.\\" " """,""""Bob talk: \\"Hi, I'm Bop.\\" ",<EOF>""",112))
    def test_str3(self):
        self.assertTrue(TestLexer.test(""" "String have \\" " """,""""String have \\" ",<EOF>""",113))
    def test_str4(self):
        self.assertTrue(TestLexer.test(""" "Escape \\b\\f\\r\\t" """,""""Escape \\b\\f\\r\\t",<EOF>""",114))
    def test_str5(self):
        self.assertTrue(TestLexer.test(""" "Backslash \\\\" """,""""Backslash \\\\",<EOF>""",115))
    def test_str6(self):
        self.assertTrue(TestLexer.test(""" "Escape error \\." ""","""Illegal Escape In String: "Escape error \.""",116))
    def test_str7(self):
        self.assertTrue(TestLexer.test(""" " Use \\n in string. Is OK! " ""","""" Use \\n in string. Is OK! ",<EOF>""",117))
    def test_str8(self):
        self.assertTrue(TestLexer.test(""" "String with EOF""","""Unclosed String: "String with EOF""",118))
    def test_str9(self):
        self.assertTrue(TestLexer.test(""" "" """,""""",<EOF>""", 119))
    #======================================= 20 - 29 ==========================================
    def test_str10(self):
        self.assertTrue(TestLexer.test(""" "String with newline\nafter newline" """, """Unclosed String: "String with newline""", 120))
    def test_str11(self):
        self.assertTrue(TestLexer.test(""" "Escape \\a" ""","""Illegal Escape In String: "Escape \\a""", 121))
    # test exp with literal
    def test_el_1(self):
        self.assertTrue(TestLexer.test("a + 2020 - c * d","a,+,2020,-,c,*,d,<EOF>",122))
    def test_el_2(self):
        self.assertTrue(TestLexer.test("12 + 22 - (-2020)*(+110)","12,+,22,-,(,-,2020,),*,(,+,110,),<EOF>",123))
    def test_el_3(self):
        self.assertTrue(TestLexer.test("1.0001 + 2 - c * 1.9e123","1.0001,+,2,-,c,*,1.9e123,<EOF>",124))
    def test_el_4(self):
        self.assertTrue(TestLexer.test("0e123 / 0E123 \\ 0e-123 * 0E+123","0e123,/,0E123,\\,0e-123,*,0E+123,<EOF>",125))
    def test_el_5(self):
        self.assertTrue(TestLexer.test("123 + 0.1e12","123,+,0.1e12,<EOF>",126))
    def test_el_6(self):
        self.assertTrue(TestLexer.test("2 + animal.cat.height","2,+,animal,.,cat,.,height,<EOF>",127))
    def test_el_7(self):
        self.assertTrue(TestLexer.test("(true || A && false) == (1 + 2 * pi > 15)", "(,true,||,A,&&,false,),==,(,1,+,2,*,pi,>,15,),<EOF>", 128))
    def test_el_8(self):
        self.assertTrue(TestLexer.test("!(a <= b) != !!((_f - (af * 1.0e-12 + 123)) > 22)","!,(,a,<=,b,),!=,!,!,(,(,_f,-,(,af,*,1.0e-12,+,123,),),>,22,),<EOF>",129))
    #======================================= 30 - 39 ==========================================
    # test array literal
    def test_arrlit_1(self):
        self.assertTrue(TestLexer.test("{}","{,},<EOF>",130))
    def test_arrlit_2(self):
        self.assertTrue(TestLexer.test("{1}","{,1,},<EOF>",131))
    def test_arrlit_3(self):
        self.assertTrue(TestLexer.test("{1,2,3}","{,1,,,2,,,3,},<EOF>",132))
    def test_arrlit_4(self):
        self.assertTrue(TestLexer.test("{1, 1 + 2 * 3, 34}","{,1,,,1,+,2,*,3,,,34,},<EOF>",133))
    def test_arrlit_5(self):
        self.assertTrue(TestLexer.test("{1.001, 1.2E-12, 0e+23}","{,1.001,,,1.2E-12,,,0e+23,},<EOF>",134))
    def test_arrlit_6(self):
        self.assertTrue(TestLexer.test("{true, false, true, true, a && b || c}","{,true,,,false,,,true,,,true,,,a,&&,b,||,c,},<EOF>",135))
    def test_arrlit_7(self):
        self.assertTrue(TestLexer.test("{a + b * 2, dc - -_123}","{,a,+,b,*,2,,,dc,-,-,_123,},<EOF>",136))
    def test_arrlit_8(self):
        self.assertTrue(TestLexer.test("{a > b, (a + c) <= 22, 2 != -_123, -(-23) == _as * pi}","{,a,>,b,,,(,a,+,c,),<=,22,,,2,!=,-,_123,,,-,(,-,23,),==,_as,*,pi,},<EOF>",137))
    def test_arrlit_9(self):
        self.assertTrue(TestLexer.test("""{"abc cd? as;", "\\"Hi.!\\" Bob said."}""","""{,"abc cd? as;",,,"\\"Hi.!\\" Bob said.",},<EOF>""",138))
    def test_arrlit_10(self):
        self.assertTrue(TestLexer.test("""{"abc" ^ "123 !!", "\n"}""",'''{,"abc",^,"123 !!",,,Unclosed String: "''',139))
    #======================================= 40 - 49 ==========================================
    # test variable declaration
    def test_var_de_1(self):
        self.assertTrue(TestLexer.test("int a = 2;","int,a,=,2,;,<EOF>",140))
    def test_var_de_2(self):
        self.assertTrue(TestLexer.test("float a, b = 2;","float,a,,,b,=,2,;,<EOF>",141))
    def test_var_de_3(self):
        self.assertTrue(TestLexer.test("int _z = 2 + 2 * a - (-12) + a / 2;","int,_z,=,2,+,2,*,a,-,(,-,12,),+,a,/,2,;,<EOF>",142))
    def test_var_de_4(self):
        self.assertTrue(TestLexer.test("boolean x=true;\nboolean z =false;","boolean,x,=,true,;,boolean,z,=,false,;,<EOF>",143))
    def test_var_de_5(self):
        self.assertTrue(TestLexer.test("int[4] a;","int,[,4,],a,;,<EOF>",144))
    def test_var_de_6(self):
        self.assertTrue(TestLexer.test("boolean[2] x={true && a || b, (false == z) || t};","boolean,[,2,],x,=,{,true,&&,a,||,b,,,(,false,==,z,),||,t,},;,<EOF>",145))
    def test_var_de_7(self):
        self.assertTrue(TestLexer.test("""string a = "abc", b= "x a!", c ="a \\z" ""","""string,a,=,"abc",,,b,=,"x a!",,,c,=,Illegal Escape In String: "a \\z""",146))
    def test_var_de_8(self):
        self.assertTrue(TestLexer.test("int a =0;\nfloat b = 0.22e-12;\nboolean z = a !=b;","int,a,=,0,;,float,b,=,0.22e-12,;,boolean,z,=,a,!=,b,;,<EOF>",147))
    # check WS and NEWLINE -> SKIP
    def test_ws_1(self):
        self.assertTrue(TestLexer.test("abc\t\t\fabc","abc,abc,<EOF>",148))
    def test_ws_2(self):
        self.assertTrue(TestLexer.test("a\n\nb\tc\fd\r\r\t\f\tac+123?","a,b,c,d,ac,+,123,Error Token ?",149))
    #======================================= 50 - 59 ==========================================
    # test stmt
    def test_stmt_1(self):
        self.assertTrue(TestLexer.test("break;","break,;,<EOF>",150))
    def test_stmt_2(self):
        self.assertTrue(TestLexer.test("continue;","continue,;,<EOF>",151))
    def test_stmt_3(self):
        self.assertTrue(TestLexer.test("if(a != b)\nthen a=a+1;\nelse b=0;","if,(,a,!=,b,),then,a,=,a,+,1,;,else,b,=,0,;,<EOF>",152))
    def test_stmt_4(self):
        self.assertTrue(TestLexer.test("return new animal(a,b + c);","return,new,animal,(,a,,,b,+,c,),;,<EOF>",153))
    def test_stmt_5(self):
        self.assertTrue(TestLexer.test("callFunction(a + b*c % (d+2));","callFunction,(,a,+,b,*,c,%,(,d,+,2,),),;,<EOF>",154))
    def test_stmt_6(self):
        self.assertTrue(TestLexer.test("a[7+9]:=12;\nfor i:=0-1 to 7+b do {\na[i]:=a[i]+1;\ncalFunction(i);}",
                                       "a,[,7,+,9,],:=,12,;,for,i,:=,0,-,1,to,7,+,b,do,{,a,[,i,],:=,a,[,i,],+,1,;,calFunction,(,i,),;,},<EOF>", 155))
    def test_stmt_7(self):
        self.assertTrue(TestLexer.test("a:=1;\nb[1+c]:=(true && !f || _z)!=false;","a,:=,1,;,b,[,1,+,c,],:=,(,true,&&,!,f,||,_z,),!=,false,;,<EOF>",156))
    def test_stmt_8(self):
        self.assertTrue(TestLexer.test("""animal.cat.talk(s + "abc");""","""animal,.,cat,.,talk,(,s,+,"abc",),;,<EOF>""",157))
    def test_stmt_9(self):
        self.assertTrue(TestLexer.test("return abc.getArea(1 + 2) - (new obj()).arr[1];","return,abc,.,getArea,(,1,+,2,),-,(,new,obj,(,),),.,arr,[,1,],;,<EOF>",158))
    def test_stmt_10(self):
        self.assertTrue(TestLexer.test("for i:=10 downto 0 do {\ncallFunction(); if a == arr[1] then break; else callF();}",
                                       "for,i,:=,10,downto,0,do,{,callFunction,(,),;,if,a,==,arr,[,1,],then,break,;,else,callF,(,),;,},<EOF>", 159))
    # #======================================= 60 - 69 ==========================================
    # test method declaration
    def test_met_de_1(self):
        self.assertTrue(TestLexer.test("void function(){}","void,function,(,),{,},<EOF>",160))
    def test_met_de_2(self):
        self.assertTrue(TestLexer.test("int cacul(int a,b) {return a +b;}","int,cacul,(,int,a,,,b,),{,return,a,+,b,;,},<EOF>",161))
    def test_met_de_3(self):
        self.assertTrue(TestLexer.test("float classCheck(int a,b; float c) { if (a < b) then return c; else return a + b;}",
                                       "float,classCheck,(,int,a,,,b,;,float,c,),{,if,(,a,<,b,),then,return,c,;,else,return,a,+,b,;,},<EOF>",162))
    def test_met_de_4(self):
        self.assertTrue(TestLexer.test("float ?_Function() {}","float,Error Token ?",163))
    def test_met_de_5(self):
        self.assertTrue(TestLexer.test("""void function_test(int a) {/*comment at here*/ getString("input\n");}""",
                                       """void,function_test,(,int,a,),{,getString,(,Unclosed String: "input""",164))
    def test_met_de_6(self):
        self.assertTrue(TestLexer.test("int add(int a,b) {return a+b;}\nfloat add(float a,b) {return a+b;}",
                                       "int,add,(,int,a,,,b,),{,return,a,+,b,;,},float,add,(,float,a,,,b,),{,return,a,+,b,;,},<EOF>", 165))
    def test_met_de_7(self):
        self.assertTrue(TestLexer.test("dog makeDog(int h,t) {#make new dog with h and t\nif(h > t) then return new dog(h,t); else return nil;}#end function",
                                       "dog,makeDog,(,int,h,,,t,),{,if,(,h,>,t,),then,return,new,dog,(,h,,,t,),;,else,return,nil,;,},<EOF>", 166))
    def test_met_de_8(self):
        self.assertTrue(TestLexer.test("string getString(string input; int l) {classSTR.getData(input);\nif (l > 0) then return getS()^input; else return input;}",
                                       "string,getString,(,string,input,;,int,l,),{,classSTR,.,getData,(,input,),;,if,(,l,>,0,),then,return,getS,(,),^,input,;,else,return,input,;,},<EOF>", 167))
    def test_met_de_9(self):
        self.assertTrue(TestLexer.test("int getData(){int data=?getINPUT();return data;}\nint[5] getArray(int l){int[5] arr;\nfor i:=0 to l do arr[i] := getData();\nreturn arr;}",
                                       "int,getData,(,),{,int,data,=,Error Token ?",168))
    def test_met_de_10(self):
        self.assertTrue(TestLexer.test(""" string get_Special_String(){return "abc\\g!!";}""",
                                       """string,get_Special_String,(,),{,return,Illegal Escape In String: "abc\\g""",169))
    #======================================= 70 - 79 ==========================================
    # test class
    def test_class_1(self):
        self.assertTrue(TestLexer.test("class A{}","class,A,{,},<EOF>",170))
    def test_class_2(self):
        self.assertTrue(TestLexer.test("class A extends B {}","class,A,extends,B,{,},<EOF>",171))
    def test_class_3(self):
        self.assertTrue(TestLexer.test("class A{final int a = 5;/*this is cmt*/}","class,A,{,final,int,a,=,5,;,},<EOF>",172))
    def test_class_4(self):
        self.assertTrue(TestLexer.test("""class str{final static string[3] a_str= {"abc","a\nb","xyz "}}""",
                                       """class,str,{,final,static,string,[,3,],a_str,=,{,"abc",,,Unclosed String: "a""", 173))
    def test_class_5(self):
        self.assertTrue(TestLexer.test("class A {A(int a,b; float c) { callFunction(a + b - c);}}",
                                       "class,A,{,A,(,int,a,,,b,;,float,c,),{,callFunction,(,a,+,b,-,c,),;,},},<EOF>", 174))
    def test_class_6(self):
        self.assertTrue(TestLexer.test("""class A {void foo() {print("abc")}}\nclass B extends A {int[5] arr;}""",
                                       """class,A,{,void,foo,(,),{,print,(,"abc",),},},class,B,extends,A,{,int,[,5,],arr,;,},<EOF>""", 175))
    def test_class_7(self):
        self.assertTrue(TestLexer.test("class A {B makeNew@B() { return new B();}}","class,A,{,B,makeNew,Error Token @",176))
    def test_class_8(self):
        self.assertTrue(TestLexer.test("class A{} class B {} class C extends A{/*cmt}","class,A,{,},class,B,{,},class,C,extends,A,{,/,*,cmt,},<EOF>",177))
    def test_class_9(self):
        self.assertTrue(TestLexer.test("class A{for i := 1 downto 1.0E+123 do x := x + 2;#abc}",
                                       "class,A,{,for,i,:=,1,downto,1.0E+123,do,x,:=,x,+,2,;,<EOF>", 178))
    def test_class_10(self):
        self.assertTrue(TestLexer.test("""class obj_zz {if a == b them "string\\"\\"\\"" else "string\\s"}""",
                                       """class,obj_zz,{,if,a,==,b,them,"string\\"\\"\\"",else,Illegal Escape In String: "string\\s""",179))
    #======================================= 80 - 89 ==========================================
    # test random form
    def test_random_1(self):
        self.assertTrue(TestLexer.test("ascn cxlz ask +nad xmmc skc / 223 2.341 + sad - asc ___asint Initlit C++",
                        "ascn,cxlz,ask,+,nad,xmmc,skc,/,223,2.341,+,sad,-,asc,___asint,Initlit,C,+,+,<EOF>", 180))
    def test_random_2(self):
        self.assertTrue(TestLexer.test("check type ant int void ++ 2030/12 if a == b: z++; ",
                                       "check,type,ant,int,void,+,+,2030,/,12,if,a,==,b,:,z,+,+,;,<EOF>", 181))
    def test_random_3(self):
        self.assertTrue(TestLexer.test("#include <stdio.h>\nint main(){}","int,main,(,),{,},<EOF>",182))
    def test_random_4(self):
        self.assertTrue(TestLexer.test("# include <stdio.h>\n#include <stdlib.h>\n#include <assert.h>\n#include <pthread.h>\n#include <time.h>\nstatic volatile long long incircle=0;\npthread_mutex_t lock;",
                                       "static,volatile,long,long,incircle,=,0,;,pthread_mutex_t,lock,;,<EOF>", 183))
    def test_random_5(self):
        self.assertTrue(TestLexer.test("1x  1z\n3y  3t(x + z + y + 1) % 3(x + z + t + 1) % 3(x + y + t + 3) % 3(y + t + z + 3) % 3",
                                       "1,x,1,z,3,y,3,t,(,x,+,z,+,y,+,1,),%,3,(,x,+,z,+,t,+,1,),%,3,(,x,+,y,+,t,+,3,),%,3,(,y,+,t,+,z,+,3,),%,3,<EOF>", 184))
    def test_random_6(self):
        self.assertTrue(TestLexer.test(
            "class,A,{,void,foo,(,),{,print,(,abc,),},},class,B,extends,A,{,int,[,5,],arr,;,}",
            "class,,,A,,,{,,,void,,,foo,,,(,,,),,,{,,,print,,,(,,,abc,,,),,,},,,},,,class,,,B,,,extends,,,A,,,{,,,int,,,[,,,5,,,],,,arr,,,;,,,},<EOF>", 185))
    def test_random_7(self):
        self.assertTrue(TestLexer.test("""#include <iostream>
using namespace std;
int main() {
    for (int x = 1; x < 10; x++)
        for (int y = 1; y < 10; y++)
            for (int @z = 1; z < 10; z++)
                for (int t = 1; t < 10; t++) {
                    if ((x + z + y) % 2 == 0 && (x + z + t) % 2 == 0 && (x + y + t + 2) % 2 == 0 && (y + t + z + 2) % 2 == 0) {
                        cout << x << y << z << t;
                        return 0;
                    }
                }
}""", "using,namespace,std,;,int,main,(,),{,for,(,int,x,=,1,;,x,<,10,;,x,+,+,),for,(,int,y,=,1,;,y,<,10,;,y,+,+,),for,(,int,Error Token @", 186))
    def test_random_8(self):
        self.assertTrue(TestLexer.test("""if (N >= 10000)	num_of_thread = 1000;
	                                      else if (N >= 1000)	num_of_thread = 100;
	                                      else if (N >= 100)	num_of_thread = 10;
	                                      else  num_of_thread = 1;""",
                                          "if,(,N,>=,10000,),num_of_thread,=,1000,;,else,if,(,N,>=,1000,),num_of_thread,=,100,;,else,if,(,N,>=,100,),num_of_thread,=,10,;,else,num_of_thread,=,1,;,<EOF>", 187))
    def test_random_9(self):
        input = """printf("PI = %f\n", 4.0 * incircle / N);
	printf("TIME = %d sec\n", (unsigned int)(time(NULL) - start));
	pthread_mutex_destroy(&lock);
	pthread_exit(NULL);"""
        output = """printf,(,Unclosed String: "PI = %f"""
        self.assertTrue(TestLexer.test(input,output,188))
    def test_random_10(self):
        input = """for(long long i = 0; i <= num_of_thread; i++) {
		if (i != num_of_thread)
			pthread_create(&threads[i], NULL, runner, (void *) loop_per_thread);
		else
			pthread_create(&threads[i], NULL, runner, (void *) (N % num_of_thread));
	}
		
	for(long long i = 0; i <= num_of_thread; i++)
		pthread_join(threads[i], NULL);"""
        output = """for,(,long,long,i,=,0,;,i,<=,num_of_thread,;,i,+,+,),{,if,(,i,!=,num_of_thread,),pthread_create,(,Error Token &"""
        self.assertTrue(TestLexer.test(input, output, 189))
    # #======================================= 90 - 99 ==========================================
    def test_random_11(self):
        input ="""
        void add(int s, int t) {
        Interval newBus;
        newBus.start = s;
        newBus.end = t;
        if (max == 0) {
            bus.push_back(newBus);
            in.push_back(s);
            out.push_back(t);
            findMax();
        }
        else if (insertBus(newBus)) {
            insertData(1, s);
            insertData(0, t);
            findMax();
        }
    }"""
        output = "void,add,(,int,s,,,int,t,),{,Interval,newBus,;,newBus,.,start,=,s,;,newBus,.,end,=,t,;,if,(,max,==,0,),{,bus,.,push_back,(,newBus,),;,in,.,push_back,(,s,),;,out,.,push_back,(,t,),;,findMax,(,),;,},else,if,(,insertBus,(,newBus,),),{,insertData,(,1,,,s,),;,insertData,(,0,,,t,),;,findMax,(,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input,output,190))
    def test_random_12(self):
        input = """    void remove(int s, int t) {
        Interval deleteBus;
        deleteBus.start = s;
        deleteBus.end = t;
        if (max == 0)    return;
        else if (insertBus(deleteBus)) {
            insertData(1, s);
            insertData(0, t);
            findMax();
        }
    }
    int minPark() {
        return max;
    }"""
        output = "void,remove,(,int,s,,,int,t,),{,Interval,deleteBus,;,deleteBus,.,start,=,s,;,deleteBus,.,end,=,t,;,if,(,max,==,0,),return,;,else,if,(,insertBus,(,deleteBus,),),{,insertData,(,1,,,s,),;,insertData,(,0,,,t,),;,findMax,(,),;,},},int,minPark,(,),{,return,max,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 191))
    def test_random_13(self):
        input = """/*cmt cmt cmt##### /*/* abcd #123123\n\\z\t \\" 123 abc##### \\" \n"""
        output = """*,abcd,\\,z,\\,Unclosed String: " 123 abc##### \\" """
        self.assertTrue(TestLexer.test(input, output, 192))
    def test_random_14(self):
        input = """Interval(int start = 0, int end = 0) {
            this->start = start;
            this->end = end;
        }
        bool operator<(Interval &a) {
            if (this->start < a.start)    return 1;
            if (this->start > a.start)    return 0;
            if (this->end < a.end)    return 1;
            return 0;
        }
        bool operator>(Interval &a) {
            if (this->start > a.start)    return 1;
            if (this->start < a.start)    return 0;
            if (this->end > a.end)    return 1;
            return 0;
        }
        bool operator==(Interval &a) {
            return (this->start == a.start && this->end == a.end);
        }
        bool operator!=(Interval &a) {
            return (this->start != a.start || this->end != a.end);
        }
        bool operator>=(Interval &a) {
            if (this->start >= a.start)    return 1;
            if (this->start < a.start)    return 0;
            if (this->end >= a.end)    return 1;
            return 0;
        }
        bool operator<=(Interval &a) {
            if (this->start <= a.start)    return 1;
            if (this->start > a.start)    return 0;
            if (this->end <= a.end)    return 1;
            return 0;
        }"""
        output = "Interval,(,int,start,=,0,,,int,end,=,0,),{,this,-,>,start,=,start,;,this,-,>,end,=,end,;,},bool,operator,<,(,Interval,Error Token &"
        self.assertTrue(TestLexer.test(input, output, 193))
    def test_random_15(self):
        input = """void create_button_skill() {
        Instantiate(button_skill, new Vector3(-6.5f,-4f,0f), transform.rotation);
    }
    void create_skill() {
        can_skill = false;
        have_button = false;
        Instantiate(water_skill, new Vector3(-10f,0f,0f), transform.rotation);  
        skill_Audio.Play(0);   
    }
    void shootWater() {
        for (int i = 0; i < num_bullet; i++) {
            Instantiate(bullet_water, fire_point.position, fire_point.rotation);  
            shoot_Audio.Play(0);       
        }
    }
    void shootMask() {
        for (int i = 0; i < num_bullet; i++) {
            Instantiate(bullet_mask, fire_point.position, fire_point.rotation);  
            shoot_Audio.Play(0);       
        }
    }"""
        output = "void,create_button_skill,(,),{,Instantiate,(,button_skill,,,new,Vector3,(,-,6.5,f,,,-,4,f,,,0,f,),,,transform,.,rotation,),;,},void,create_skill,(,),{,can_skill,=,false,;,have_button,=,false,;,Instantiate,(,water_skill,,,new,Vector3,(,-,10,f,,,0,f,,,0,f,),,,transform,.,rotation,),;,skill_Audio,.,Play,(,0,),;,},void,shootWater,(,),{,for,(,int,i,=,0,;,i,<,num_bullet,;,i,+,+,),{,Instantiate,(,bullet_water,,,fire_point,.,position,,,fire_point,.,rotation,),;,shoot_Audio,.,Play,(,0,),;,},},void,shootMask,(,),{,for,(,int,i,=,0,;,i,<,num_bullet,;,i,+,+,),{,Instantiate,(,bullet_mask,,,fire_point,.,position,,,fire_point,.,rotation,),;,shoot_Audio,.,Play,(,0,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 194))
    def test_random_16(self):
        input = """void GameOver() {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 1);
        /*  UPDATE LATE
        **  WHEN GAMEOVER, DESTROY UFO
        **  EXPLOSION :))
        */
    }"""
        output = "void,GameOver,(,),{,SceneManager,.,LoadScene,(,SceneManager,.,GetActiveScene,(,),.,buildIndex,-,1,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 195))
    def test_random_17(self):
        input = """using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class move : MonoBehaviour"""
        output = "using,System,.,Collections,;,using,System,.,Collections,.,Generic,;,using,UnityEngine,;,using,UnityEngine,.,SceneManagement,;,using,UnityEngine,.,UI,;,public,class,move,:,MonoBehaviour,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 196))
    def test_random_18(self):
        input = """n = int(input("Nhap n = "))
count  = 0
for i in range(n) :
    count += i*i
count3 = 0.0
for i in range(1,n + 1):
    count3 += 1/i
print("bai 3 :",count3)
count5 = 0.0
for i in range(n + 1):
    count5 += 1/(2 * i +1)
print("bai 5 :",count5)
s =  0
fac = 1
for i in range(1,n+1):
    fac *= i
    s += fac"""
        output = '''n,=,int,(,input,(,"Nhap n = ",),),count,=,0,for,i,in,range,(,n,),:,count,+,=,i,*,i,count3,=,0.0,for,i,in,range,(,1,,,n,+,1,),:,count3,+,=,1,/,i,print,(,"bai 3 :",,,count3,),count5,=,0.0,for,i,in,range,(,n,+,1,),:,count5,+,=,1,/,(,2,*,i,+,1,),print,(,"bai 5 :",,,count5,),s,=,0,fac,=,1,for,i,in,range,(,1,,,n,+,1,),:,fac,*,=,i,s,+,=,fac,<EOF>'''
        self.assertTrue(TestLexer.test(input, output, 197))
    def test_random_19(self):
        input = """num  = float(input("Moi ban nhap so :"))
fl = num - int(num)
#[0,0.25)    => 0
#[0.25,0.75) => 0.5
#[0.75,1]    => 1
fl = int(fl * 4)
myroud = {0 : 0 ,1 : 0.5, 2 : 0.5, 3 : 1}
print("So lam tron :",float(int(num) + myroud[fl]))"""
        output = """num,=,float,(,input,(,"Moi ban nhap so :",),),fl,=,num,-,int,(,num,),fl,=,int,(,fl,*,4,),myroud,=,{,0,:,0,,,1,:,0.5,,,2,:,0.5,,,3,:,1,},print,(,"So lam tron :",,,float,(,int,(,num,),+,myroud,[,fl,],),),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 198))
    def test_random_20(self):
        input = """money = int(input("nhap vao so tien can doi"))
#naive
print(f"{money//50} to 50 ,{money%50//20} to 20 ,{money%50%20//10} to 10 ,{money%50%20%10//5} to 5,{money%50%20%10%5//2} to 2,{money%50%20%10%5%2} to 1")"""
        output = """money,=,int,(,input,(,"nhap vao so tien can doi",),),print,(,f,"{money//50} to 50 ,{money%50//20} to 20 ,{money%50%20//10} to 10 ,{money%50%20%10//5} to 5,{money%50%20%10%5//2} to 2,{money%50%20%10%5%2} to 1",),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 199))

