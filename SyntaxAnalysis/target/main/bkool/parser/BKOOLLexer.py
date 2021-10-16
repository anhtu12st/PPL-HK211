# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\65\n\3\3\4\6\48\n\4\r\4\16\49\3\5\3\5\3\5\5\5?\n\5")
        buf.write("\3\6\6\6B\n\6\r\6\16\6C\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\6\17W\n\17")
        buf.write("\r\17\16\17X\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3")
        buf.write("\22\2\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23\3\2\6\4\2C\\c")
        buf.write("|\3\2\62;\5\2,-//\61\61\5\2\13\f\17\17\"\"\2g\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2")
        buf.write("\5\64\3\2\2\2\7\67\3\2\2\2\t;\3\2\2\2\13A\3\2\2\2\rE\3")
        buf.write("\2\2\2\17G\3\2\2\2\21I\3\2\2\2\23K\3\2\2\2\25M\3\2\2\2")
        buf.write("\27O\3\2\2\2\31Q\3\2\2\2\33S\3\2\2\2\35V\3\2\2\2\37\\")
        buf.write("\3\2\2\2!_\3\2\2\2#a\3\2\2\2%&\7t\2\2&\'\7g\2\2\'(\7v")
        buf.write("\2\2()\7w\2\2)*\7t\2\2*+\7p\2\2+\4\3\2\2\2,-\7k\2\2-.")
        buf.write("\7p\2\2.\65\7v\2\2/\60\7h\2\2\60\61\7n\2\2\61\62\7q\2")
        buf.write("\2\62\63\7c\2\2\63\65\7v\2\2\64,\3\2\2\2\64/\3\2\2\2\65")
        buf.write("\6\3\2\2\2\668\t\2\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2")
        buf.write("\2\29:\3\2\2\2:\b\3\2\2\2;>\5\13\6\2<=\7\60\2\2=?\5\13")
        buf.write("\6\2><\3\2\2\2>?\3\2\2\2?\n\3\2\2\2@B\t\3\2\2A@\3\2\2")
        buf.write("\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\f\3\2\2\2EF\t\4\2\2")
        buf.write("F\16\3\2\2\2GH\7*\2\2H\20\3\2\2\2IJ\7+\2\2J\22\3\2\2\2")
        buf.write("KL\7.\2\2L\24\3\2\2\2MN\7}\2\2N\26\3\2\2\2OP\7\177\2\2")
        buf.write("P\30\3\2\2\2QR\7?\2\2R\32\3\2\2\2ST\7=\2\2T\34\3\2\2\2")
        buf.write("UW\t\5\2\2VU\3\2\2\2WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2YZ\3")
        buf.write("\2\2\2Z[\b\17\2\2[\36\3\2\2\2\\]\13\2\2\2]^\b\20\3\2^")
        buf.write(" \3\2\2\2_`\13\2\2\2`\"\3\2\2\2ab\13\2\2\2b$\3\2\2\2\b")
        buf.write("\2\649>CX\4\b\2\2\3\20\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    MTYPE = 2
    ID = 3
    DECIMAL = 4
    INTLIT = 5
    OP = 6
    LB = 7
    RB = 8
    CM = 9
    LP = 10
    RP = 11
    EQ = 12
    SEMI = 13
    WS = 14
    ERROR_CHAR = 15
    UNCLOSE_STRING = 16
    ILLEGAL_ESCAPE = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'('", "')'", "','", "'{'", "'}'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>",
            "MTYPE", "ID", "DECIMAL", "INTLIT", "OP", "LB", "RB", "CM", 
            "LP", "RP", "EQ", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "MTYPE", "ID", "DECIMAL", "INTLIT", "OP", "LB", 
                  "RB", "CM", "LP", "RP", "EQ", "SEMI", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[14] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


