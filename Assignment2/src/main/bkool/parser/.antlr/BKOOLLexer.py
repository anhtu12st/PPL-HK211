# Generated from /Users/tu/Desktop/PPL/Assignment2/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u0194\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u0100\n\32\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u0106\n\33\3\34\3\34\3\34\3\34\5\34\u010c")
        buf.write("\n\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3-\7-\u0132\n-\f-\16-\u0135\13-\3")
        buf.write("-\5-\u0138\n-\3-\3-\3-\5-\u013d\n-\3.\6.\u0140\n.\r.\16")
        buf.write(".\u0141\3/\3/\5/\u0146\n/\3/\3/\3\60\6\60\u014b\n\60\r")
        buf.write("\60\16\60\u014c\3\60\3\60\3\61\3\61\3\61\3\61\7\61\u0155")
        buf.write("\n\61\f\61\16\61\u0158\13\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\7\62\u0161\n\62\f\62\16\62\u0164\13\62\3\62")
        buf.write("\3\62\3\63\3\63\5\63\u016a\n\63\3\63\6\63\u016d\n\63\r")
        buf.write("\63\16\63\u016e\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66")
        buf.write("\7\66\u0179\n\66\f\66\16\66\u017c\13\66\3\67\3\67\7\67")
        buf.write("\u0180\n\67\f\67\16\67\u0183\13\67\38\38\58\u0187\n8\3")
        buf.write("8\38\39\39\59\u018d\n9\39\39\39\3:\3:\3:\3\u0156\2;\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\2g\2i\2k\2m\64o\65q\66s\67")
        buf.write("\3\2\r\4\2>>@@\4\2--//\6\2\'\',,\61\61^^\3\2\62;\5\2\13")
        buf.write("\f\16\17\"\"\4\2\f\f\16\17\4\2GGgg\t\2$$^^ddhhppttvv\6")
        buf.write("\2\f\f\16\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\2\u01a2\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2m\3\2\2\2\2o\3")
        buf.write("\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3u\3\2\2\2\5}\3\2\2\2\7\u0083")
        buf.write("\3\2\2\2\t\u0089\3\2\2\2\13\u0092\3\2\2\2\r\u0095\3\2")
        buf.write("\2\2\17\u009a\3\2\2\2\21\u00a2\3\2\2\2\23\u00a8\3\2\2")
        buf.write("\2\25\u00ab\3\2\2\2\27\u00af\3\2\2\2\31\u00b3\3\2\2\2")
        buf.write("\33\u00ba\3\2\2\2\35\u00bf\3\2\2\2\37\u00c3\3\2\2\2!\u00ca")
        buf.write("\3\2\2\2#\u00cf\3\2\2\2%\u00d5\3\2\2\2\'\u00da\3\2\2\2")
        buf.write(")\u00de\3\2\2\2+\u00e3\3\2\2\2-\u00e9\3\2\2\2/\u00f0\3")
        buf.write("\2\2\2\61\u00f3\3\2\2\2\63\u00ff\3\2\2\2\65\u0105\3\2")
        buf.write("\2\2\67\u010b\3\2\2\29\u010d\3\2\2\2;\u010f\3\2\2\2=\u0111")
        buf.write("\3\2\2\2?\u0113\3\2\2\2A\u0115\3\2\2\2C\u0118\3\2\2\2")
        buf.write("E\u011a\3\2\2\2G\u011c\3\2\2\2I\u011e\3\2\2\2K\u0120\3")
        buf.write("\2\2\2M\u0122\3\2\2\2O\u0124\3\2\2\2Q\u0126\3\2\2\2S\u0128")
        buf.write("\3\2\2\2U\u012a\3\2\2\2W\u012c\3\2\2\2Y\u013c\3\2\2\2")
        buf.write("[\u013f\3\2\2\2]\u0143\3\2\2\2_\u014a\3\2\2\2a\u0150\3")
        buf.write("\2\2\2c\u015e\3\2\2\2e\u0167\3\2\2\2g\u0170\3\2\2\2i\u0173")
        buf.write("\3\2\2\2k\u017a\3\2\2\2m\u017d\3\2\2\2o\u0184\3\2\2\2")
        buf.write("q\u018a\3\2\2\2s\u0191\3\2\2\2uv\7d\2\2vw\7q\2\2wx\7q")
        buf.write("\2\2xy\7n\2\2yz\7g\2\2z{\7c\2\2{|\7p\2\2|\4\3\2\2\2}~")
        buf.write("\7d\2\2~\177\7t\2\2\177\u0080\7g\2\2\u0080\u0081\7c\2")
        buf.write("\2\u0081\u0082\7m\2\2\u0082\6\3\2\2\2\u0083\u0084\7e\2")
        buf.write("\2\u0084\u0085\7n\2\2\u0085\u0086\7c\2\2\u0086\u0087\7")
        buf.write("u\2\2\u0087\u0088\7u\2\2\u0088\b\3\2\2\2\u0089\u008a\7")
        buf.write("e\2\2\u008a\u008b\7q\2\2\u008b\u008c\7p\2\2\u008c\u008d")
        buf.write("\7v\2\2\u008d\u008e\7k\2\2\u008e\u008f\7p\2\2\u008f\u0090")
        buf.write("\7w\2\2\u0090\u0091\7g\2\2\u0091\n\3\2\2\2\u0092\u0093")
        buf.write("\7f\2\2\u0093\u0094\7q\2\2\u0094\f\3\2\2\2\u0095\u0096")
        buf.write("\7g\2\2\u0096\u0097\7n\2\2\u0097\u0098\7u\2\2\u0098\u0099")
        buf.write("\7g\2\2\u0099\16\3\2\2\2\u009a\u009b\7g\2\2\u009b\u009c")
        buf.write("\7z\2\2\u009c\u009d\7v\2\2\u009d\u009e\7g\2\2\u009e\u009f")
        buf.write("\7p\2\2\u009f\u00a0\7f\2\2\u00a0\u00a1\7u\2\2\u00a1\20")
        buf.write("\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5")
        buf.write("\7q\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7\7v\2\2\u00a7\22")
        buf.write("\3\2\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa\7h\2\2\u00aa\24")
        buf.write("\3\2\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae")
        buf.write("\7v\2\2\u00ae\26\3\2\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\u00b2\7y\2\2\u00b2\30\3\2\2\2\u00b3\u00b4")
        buf.write("\7u\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7i\2\2\u00b9\32")
        buf.write("\3\2\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7j\2\2\u00bc\u00bd")
        buf.write("\7g\2\2\u00bd\u00be\7p\2\2\u00be\34\3\2\2\2\u00bf\u00c0")
        buf.write("\7h\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2\7t\2\2\u00c2\36")
        buf.write("\3\2\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9 \3\2\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc")
        buf.write("\7t\2\2\u00cc\u00cd\7w\2\2\u00cd\u00ce\7g\2\2\u00ce\"")
        buf.write("\3\2\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2")
        buf.write("\7n\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4\7g\2\2\u00d4$\3")
        buf.write("\2\2\2\u00d5\u00d6\7x\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7k\2\2\u00d8\u00d9\7f\2\2\u00d9&\3\2\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7n\2\2\u00dd(\3")
        buf.write("\2\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7j\2\2\u00e0\u00e1")
        buf.write("\7k\2\2\u00e1\u00e2\7u\2\2\u00e2*\3\2\2\2\u00e3\u00e4")
        buf.write("\7h\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7")
        buf.write("\7c\2\2\u00e7\u00e8\7n\2\2\u00e8,\3\2\2\2\u00e9\u00ea")
        buf.write("\7u\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed")
        buf.write("\7v\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7e\2\2\u00ef.\3")
        buf.write("\2\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7q\2\2\u00f2\60")
        buf.write("\3\2\2\2\u00f3\u00f4\7f\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6")
        buf.write("\7y\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9")
        buf.write("\7q\2\2\u00f9\62\3\2\2\2\u00fa\u0100\t\2\2\2\u00fb\u00fc")
        buf.write("\7@\2\2\u00fc\u0100\7?\2\2\u00fd\u00fe\7>\2\2\u00fe\u0100")
        buf.write("\7?\2\2\u00ff\u00fa\3\2\2\2\u00ff\u00fb\3\2\2\2\u00ff")
        buf.write("\u00fd\3\2\2\2\u0100\64\3\2\2\2\u0101\u0102\7?\2\2\u0102")
        buf.write("\u0106\7?\2\2\u0103\u0104\7#\2\2\u0104\u0106\7?\2\2\u0105")
        buf.write("\u0101\3\2\2\2\u0105\u0103\3\2\2\2\u0106\66\3\2\2\2\u0107")
        buf.write("\u0108\7(\2\2\u0108\u010c\7(\2\2\u0109\u010a\7~\2\2\u010a")
        buf.write("\u010c\7~\2\2\u010b\u0107\3\2\2\2\u010b\u0109\3\2\2\2")
        buf.write("\u010c8\3\2\2\2\u010d\u010e\t\3\2\2\u010e:\3\2\2\2\u010f")
        buf.write("\u0110\t\4\2\2\u0110<\3\2\2\2\u0111\u0112\7#\2\2\u0112")
        buf.write(">\3\2\2\2\u0113\u0114\7`\2\2\u0114@\3\2\2\2\u0115\u0116")
        buf.write("\7<\2\2\u0116\u0117\7?\2\2\u0117B\3\2\2\2\u0118\u0119")
        buf.write("\7?\2\2\u0119D\3\2\2\2\u011a\u011b\7*\2\2\u011bF\3\2\2")
        buf.write("\2\u011c\u011d\7+\2\2\u011dH\3\2\2\2\u011e\u011f\7]\2")
        buf.write("\2\u011fJ\3\2\2\2\u0120\u0121\7_\2\2\u0121L\3\2\2\2\u0122")
        buf.write("\u0123\7}\2\2\u0123N\3\2\2\2\u0124\u0125\7\177\2\2\u0125")
        buf.write("P\3\2\2\2\u0126\u0127\7=\2\2\u0127R\3\2\2\2\u0128\u0129")
        buf.write("\7<\2\2\u0129T\3\2\2\2\u012a\u012b\7\60\2\2\u012bV\3\2")
        buf.write("\2\2\u012c\u012d\7.\2\2\u012dX\3\2\2\2\u012e\u012f\5[")
        buf.write(".\2\u012f\u0133\7\60\2\2\u0130\u0132\t\5\2\2\u0131\u0130")
        buf.write("\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2")
        buf.write("\u0136\u0138\5e\63\2\u0137\u0136\3\2\2\2\u0137\u0138\3")
        buf.write("\2\2\2\u0138\u013d\3\2\2\2\u0139\u013a\5[.\2\u013a\u013b")
        buf.write("\5e\63\2\u013b\u013d\3\2\2\2\u013c\u012e\3\2\2\2\u013c")
        buf.write("\u0139\3\2\2\2\u013dZ\3\2\2\2\u013e\u0140\t\5\2\2\u013f")
        buf.write("\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0141\u0142\3\2\2\2\u0142\\\3\2\2\2\u0143\u0145\7$\2")
        buf.write("\2\u0144\u0146\5k\66\2\u0145\u0144\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\7$\2\2\u0148")
        buf.write("^\3\2\2\2\u0149\u014b\t\6\2\2\u014a\u0149\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2")
        buf.write("\u014d\u014e\3\2\2\2\u014e\u014f\b\60\2\2\u014f`\3\2\2")
        buf.write("\2\u0150\u0151\7\61\2\2\u0151\u0152\7,\2\2\u0152\u0156")
        buf.write("\3\2\2\2\u0153\u0155\13\2\2\2\u0154\u0153\3\2\2\2\u0155")
        buf.write("\u0158\3\2\2\2\u0156\u0157\3\2\2\2\u0156\u0154\3\2\2\2")
        buf.write("\u0157\u0159\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\7")
        buf.write(",\2\2\u015a\u015b\7\61\2\2\u015b\u015c\3\2\2\2\u015c\u015d")
        buf.write("\b\61\2\2\u015db\3\2\2\2\u015e\u0162\7%\2\2\u015f\u0161")
        buf.write("\n\7\2\2\u0160\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165\3\2\2\2")
        buf.write("\u0164\u0162\3\2\2\2\u0165\u0166\b\62\2\2\u0166d\3\2\2")
        buf.write("\2\u0167\u0169\t\b\2\2\u0168\u016a\t\3\2\2\u0169\u0168")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c\3\2\2\2\u016b")
        buf.write("\u016d\t\5\2\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016ff\3\2\2")
        buf.write("\2\u0170\u0171\7^\2\2\u0171\u0172\t\t\2\2\u0172h\3\2\2")
        buf.write("\2\u0173\u0174\7^\2\2\u0174\u0175\n\t\2\2\u0175j\3\2\2")
        buf.write("\2\u0176\u0179\n\n\2\2\u0177\u0179\5g\64\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017bl\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017d\u0181\t\13\2\2\u017e\u0180\t\f\2")
        buf.write("\2\u017f\u017e\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182n\3\2\2\2\u0183\u0181")
        buf.write("\3\2\2\2\u0184\u0186\7$\2\2\u0185\u0187\5k\66\2\u0186")
        buf.write("\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188\u0189\b8\3\2\u0189p\3\2\2\2\u018a\u018c\7$\2\2")
        buf.write("\u018b\u018d\5k\66\2\u018c\u018b\3\2\2\2\u018c\u018d\3")
        buf.write("\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\5i\65\2\u018f\u0190")
        buf.write("\b9\4\2\u0190r\3\2\2\2\u0191\u0192\13\2\2\2\u0192\u0193")
        buf.write("\b:\5\2\u0193t\3\2\2\2\25\2\u00ff\u0105\u010b\u0133\u0137")
        buf.write("\u013c\u0141\u0145\u014c\u0156\u0162\u0169\u016e\u0178")
        buf.write("\u017a\u0181\u0186\u018c\6\b\2\2\38\2\39\3\3:\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEAN = 1
    BREAK = 2
    CLASS = 3
    CONTINUE = 4
    DO = 5
    ELSE = 6
    EXTENDS = 7
    FLOAT = 8
    IF = 9
    INT = 10
    NEW = 11
    STRING = 12
    THEN = 13
    FOR = 14
    RETURN = 15
    TRUE = 16
    FALSE = 17
    VOID = 18
    NIL = 19
    THIS = 20
    FINAL = 21
    STATIC = 22
    TO = 23
    DOWNTO = 24
    OP0 = 25
    OP1 = 26
    OP2 = 27
    OP3 = 28
    OP4 = 29
    NOT = 30
    CONCAT = 31
    ASSIGN = 32
    INITASSIGN = 33
    LB = 34
    RB = 35
    LSB = 36
    RSB = 37
    LP = 38
    RP = 39
    SEMI = 40
    CL = 41
    DOT = 42
    CM = 43
    FLOATLIT = 44
    INTLIT = 45
    STRLIT = 46
    WS = 47
    COMMENT = 48
    LINECOMMENT = 49
    ID = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52
    ERROR_CHAR = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
            "'!'", "'^'", "':='", "'='", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
            "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
            "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", 
            "DOWNTO", "OP0", "OP1", "OP2", "OP3", "OP4", "NOT", "CONCAT", 
            "ASSIGN", "INITASSIGN", "LB", "RB", "LSB", "RSB", "LP", "RP", 
            "SEMI", "CL", "DOT", "CM", "FLOATLIT", "INTLIT", "STRLIT", "WS", 
            "COMMENT", "LINECOMMENT", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
                  "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", 
                  "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                  "FINAL", "STATIC", "TO", "DOWNTO", "OP0", "OP1", "OP2", 
                  "OP3", "OP4", "NOT", "CONCAT", "ASSIGN", "INITASSIGN", 
                  "LB", "RB", "LSB", "RSB", "LP", "RP", "SEMI", "CL", "DOT", 
                  "CM", "FLOATLIT", "INTLIT", "STRLIT", "WS", "COMMENT", 
                  "LINECOMMENT", "EXPONENT", "ESC", "NONEESC", "CHARACTERS", 
                  "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.UNCLOSE_STRING_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            actions[56] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise IllegalEscape(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


