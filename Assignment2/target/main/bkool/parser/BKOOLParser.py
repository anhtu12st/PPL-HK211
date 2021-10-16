# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\u0200\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\7\2r\n\2\f\2")
        buf.write("\16\2u\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3}\n\3\3\3\3\3\7")
        buf.write("\3\u0081\n\3\f\3\16\3\u0084\13\3\3\3\3\3\3\4\3\4\5\4\u008a")
        buf.write("\n\4\3\5\3\5\5\5\u008e\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("\u0096\n\6\3\7\5\7\u0099\n\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\5\t\u00a6\n\t\3\n\3\n\3\n\3\n\3\n\5")
        buf.write("\n\u00ad\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00c0")
        buf.write("\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00ce\n\16\3\17\3\17\5\17\u00d2\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00d9\n\20\3\20\3\20\3\20\3\21")
        buf.write("\5\21\u00df\n\21\3\21\3\21\3\21\5\21\u00e4\n\21\3\21\3")
        buf.write("\21\3\21\3\22\3\22\5\22\u00eb\n\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u00f5\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\5\26\u00ff\n\26\3\27\3\27\3\27")
        buf.write("\7\27\u0104\n\27\f\27\16\27\u0107\13\27\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u0112\n\31\3\32\3")
        buf.write("\32\3\32\5\32\u0117\n\32\3\33\3\33\3\33\5\33\u011c\n\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0124\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0130")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0138\n\36\3")
        buf.write("\36\5\36\u013b\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u0146\n\37\3 \3 \3 \3 \3 \5 \u014d\n ")
        buf.write("\3!\3!\3!\3!\3!\5!\u0154\n!\3\"\3\"\3\"\3\"\3\"\3\"\7")
        buf.write("\"\u015c\n\"\f\"\16\"\u015f\13\"\3#\3#\3#\3#\3#\3#\7#")
        buf.write("\u0167\n#\f#\16#\u016a\13#\3$\3$\3$\3$\3$\3$\7$\u0172")
        buf.write("\n$\f$\16$\u0175\13$\3%\3%\3%\3%\3%\5%\u017c\n%\3&\3&")
        buf.write("\3&\5&\u0181\n&\3\'\3\'\3\'\5\'\u0186\n\'\3(\3(\3(\3(")
        buf.write("\3(\3(\5(\u018e\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\7)\u019d\n)\f)\16)\u01a0\13)\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\5*\u01a9\n*\3+\3+\3+\3+\3+\5+\u01b0\n+\3,\3,\3,\3,\3")
        buf.write(",\5,\u01b7\n,\3-\3-\3.\3.\3.\5.\u01be\n.\3/\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\5\60\u01d0\n\60\3\61\3\61\3\62\3\62\3\62\3\62\5\62")
        buf.write("\u01d8\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u01df\n\63\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u01ef\n\65\3\66\3\66\3\66\3\66\5")
        buf.write("\66\u01f5\n\66\3\67\3\67\38\38\38\38\38\58\u01fe\n8\3")
        buf.write("8\2\6BDFP9\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\6\3\2")
        buf.write("\31\32\6\2\22\23\25\26.\60\64\64\7\2\3\3\n\n\f\f\16\16")
        buf.write("\64\64\5\2\22\23\25\26.\60\2\u01ff\2s\3\2\2\2\4x\3\2\2")
        buf.write("\2\6\u0089\3\2\2\2\b\u008d\3\2\2\2\n\u0095\3\2\2\2\f\u0098")
        buf.write("\3\2\2\2\16\u009e\3\2\2\2\20\u00a5\3\2\2\2\22\u00ac\3")
        buf.write("\2\2\2\24\u00bf\3\2\2\2\26\u00c1\3\2\2\2\30\u00c4\3\2")
        buf.write("\2\2\32\u00cd\3\2\2\2\34\u00d1\3\2\2\2\36\u00d3\3\2\2")
        buf.write("\2 \u00de\3\2\2\2\"\u00ea\3\2\2\2$\u00ec\3\2\2\2&\u00f4")
        buf.write("\3\2\2\2(\u00f6\3\2\2\2*\u00fe\3\2\2\2,\u0100\3\2\2\2")
        buf.write(".\u010a\3\2\2\2\60\u0111\3\2\2\2\62\u0116\3\2\2\2\64\u011b")
        buf.write("\3\2\2\2\66\u0123\3\2\2\28\u012f\3\2\2\2:\u013a\3\2\2")
        buf.write("\2<\u0145\3\2\2\2>\u014c\3\2\2\2@\u0153\3\2\2\2B\u0155")
        buf.write("\3\2\2\2D\u0160\3\2\2\2F\u016b\3\2\2\2H\u017b\3\2\2\2")
        buf.write("J\u0180\3\2\2\2L\u0185\3\2\2\2N\u018d\3\2\2\2P\u018f\3")
        buf.write("\2\2\2R\u01a8\3\2\2\2T\u01af\3\2\2\2V\u01b6\3\2\2\2X\u01b8")
        buf.write("\3\2\2\2Z\u01bd\3\2\2\2\\\u01bf\3\2\2\2^\u01cf\3\2\2\2")
        buf.write("`\u01d1\3\2\2\2b\u01d7\3\2\2\2d\u01de\3\2\2\2f\u01e0\3")
        buf.write("\2\2\2h\u01ee\3\2\2\2j\u01f4\3\2\2\2l\u01f6\3\2\2\2n\u01fd")
        buf.write("\3\2\2\2pr\5\4\3\2qp\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2")
        buf.write("\2\2tv\3\2\2\2us\3\2\2\2vw\7\2\2\3w\3\3\2\2\2xy\7\5\2")
        buf.write("\2y|\7\64\2\2z{\7\t\2\2{}\7\64\2\2|z\3\2\2\2|}\3\2\2\2")
        buf.write("}~\3\2\2\2~\u0082\7(\2\2\177\u0081\5\6\4\2\u0080\177\3")
        buf.write("\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085")
        buf.write("\u0086\7)\2\2\u0086\5\3\2\2\2\u0087\u008a\5\b\5\2\u0088")
        buf.write("\u008a\5\34\17\2\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2")
        buf.write("\2\u008a\7\3\2\2\2\u008b\u008e\5\f\7\2\u008c\u008e\5\24")
        buf.write("\13\2\u008d\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e\t")
        buf.write("\3\2\2\2\u008f\u0096\7\n\2\2\u0090\u0096\7\f\2\2\u0091")
        buf.write("\u0096\7\3\2\2\u0092\u0096\7\16\2\2\u0093\u0096\7\64\2")
        buf.write("\2\u0094\u0096\5f\64\2\u0095\u008f\3\2\2\2\u0095\u0090")
        buf.write("\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0092\3\2\2\2\u0095")
        buf.write("\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\13\3\2\2\2\u0097")
        buf.write("\u0099\7\30\2\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2")
        buf.write("\2\u0099\u009a\3\2\2\2\u009a\u009b\5\n\6\2\u009b\u009c")
        buf.write("\5\16\b\2\u009c\u009d\7*\2\2\u009d\r\3\2\2\2\u009e\u009f")
        buf.write("\5\20\t\2\u009f\u00a0\5\22\n\2\u00a0\17\3\2\2\2\u00a1")
        buf.write("\u00a6\7\64\2\2\u00a2\u00a3\7\64\2\2\u00a3\u00a4\7#\2")
        buf.write("\2\u00a4\u00a6\5> \2\u00a5\u00a1\3\2\2\2\u00a5\u00a2\3")
        buf.write("\2\2\2\u00a6\21\3\2\2\2\u00a7\u00a8\7-\2\2\u00a8\u00a9")
        buf.write("\5\20\t\2\u00a9\u00aa\5\22\n\2\u00aa\u00ad\3\2\2\2\u00ab")
        buf.write("\u00ad\3\2\2\2\u00ac\u00a7\3\2\2\2\u00ac\u00ab\3\2\2\2")
        buf.write("\u00ad\23\3\2\2\2\u00ae\u00af\7\27\2\2\u00af\u00b0\5\n")
        buf.write("\6\2\u00b0\u00b1\5\26\f\2\u00b1\u00b2\7*\2\2\u00b2\u00c0")
        buf.write("\3\2\2\2\u00b3\u00b4\7\30\2\2\u00b4\u00b5\7\27\2\2\u00b5")
        buf.write("\u00b6\5\n\6\2\u00b6\u00b7\5\26\f\2\u00b7\u00b8\7*\2\2")
        buf.write("\u00b8\u00c0\3\2\2\2\u00b9\u00ba\7\27\2\2\u00ba\u00bb")
        buf.write("\7\30\2\2\u00bb\u00bc\5\n\6\2\u00bc\u00bd\5\26\f\2\u00bd")
        buf.write("\u00be\7*\2\2\u00be\u00c0\3\2\2\2\u00bf\u00ae\3\2\2\2")
        buf.write("\u00bf\u00b3\3\2\2\2\u00bf\u00b9\3\2\2\2\u00c0\25\3\2")
        buf.write("\2\2\u00c1\u00c2\5\30\r\2\u00c2\u00c3\5\32\16\2\u00c3")
        buf.write("\27\3\2\2\2\u00c4\u00c5\7\64\2\2\u00c5\u00c6\7#\2\2\u00c6")
        buf.write("\u00c7\5> \2\u00c7\31\3\2\2\2\u00c8\u00c9\7-\2\2\u00c9")
        buf.write("\u00ca\5\30\r\2\u00ca\u00cb\5\32\16\2\u00cb\u00ce\3\2")
        buf.write("\2\2\u00cc\u00ce\3\2\2\2\u00cd\u00c8\3\2\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00ce\33\3\2\2\2\u00cf\u00d2\5\36\20\2\u00d0")
        buf.write("\u00d2\5 \21\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2")
        buf.write("\u00d2\35\3\2\2\2\u00d3\u00d4\7\30\2\2\u00d4\u00d5\5\"")
        buf.write("\22\2\u00d5\u00d6\7\64\2\2\u00d6\u00d8\7$\2\2\u00d7\u00d9")
        buf.write("\5$\23\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00db\7%\2\2\u00db\u00dc\5,\27\2")
        buf.write("\u00dc\37\3\2\2\2\u00dd\u00df\5\"\22\2\u00de\u00dd\3\2")
        buf.write("\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1")
        buf.write("\7\64\2\2\u00e1\u00e3\7$\2\2\u00e2\u00e4\5$\23\2\u00e3")
        buf.write("\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5\u00e6\7%\2\2\u00e6\u00e7\5,\27\2\u00e7!\3\2\2\2")
        buf.write("\u00e8\u00eb\5\n\6\2\u00e9\u00eb\7\24\2\2\u00ea\u00e8")
        buf.write("\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb#\3\2\2\2\u00ec\u00ed")
        buf.write("\5(\25\2\u00ed\u00ee\5&\24\2\u00ee%\3\2\2\2\u00ef\u00f0")
        buf.write("\7*\2\2\u00f0\u00f1\5(\25\2\u00f1\u00f2\5&\24\2\u00f2")
        buf.write("\u00f5\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00ef\3\2\2\2")
        buf.write("\u00f4\u00f3\3\2\2\2\u00f5\'\3\2\2\2\u00f6\u00f7\5\n\6")
        buf.write("\2\u00f7\u00f8\7\64\2\2\u00f8\u00f9\5*\26\2\u00f9)\3\2")
        buf.write("\2\2\u00fa\u00fb\7-\2\2\u00fb\u00fc\7\64\2\2\u00fc\u00ff")
        buf.write("\5*\26\2\u00fd\u00ff\3\2\2\2\u00fe\u00fa\3\2\2\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00ff+\3\2\2\2\u0100\u0105\7(\2\2\u0101")
        buf.write("\u0104\5h\65\2\u0102\u0104\5.\30\2\u0103\u0101\3\2\2\2")
        buf.write("\u0103\u0102\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3")
        buf.write("\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108\3\2\2\2\u0107\u0105")
        buf.write("\3\2\2\2\u0108\u0109\7)\2\2\u0109-\3\2\2\2\u010a\u010b")
        buf.write("\5\60\31\2\u010b/\3\2\2\2\u010c\u010d\7\21\2\2\u010d\u010e")
        buf.write("\5> \2\u010e\u010f\7*\2\2\u010f\u0112\3\2\2\2\u0110\u0112")
        buf.write("\5\62\32\2\u0111\u010c\3\2\2\2\u0111\u0110\3\2\2\2\u0112")
        buf.write("\61\3\2\2\2\u0113\u0114\7\6\2\2\u0114\u0117\7*\2\2\u0115")
        buf.write("\u0117\5\64\33\2\u0116\u0113\3\2\2\2\u0116\u0115\3\2\2")
        buf.write("\2\u0117\63\3\2\2\2\u0118\u0119\7\4\2\2\u0119\u011c\7")
        buf.write("*\2\2\u011a\u011c\5\66\34\2\u011b\u0118\3\2\2\2\u011b")
        buf.write("\u011a\3\2\2\2\u011c\65\3\2\2\2\u011d\u011e\5Z.\2\u011e")
        buf.write("\u011f\7\"\2\2\u011f\u0120\5> \2\u0120\u0121\7*\2\2\u0121")
        buf.write("\u0124\3\2\2\2\u0122\u0124\58\35\2\u0123\u011d\3\2\2\2")
        buf.write("\u0123\u0122\3\2\2\2\u0124\67\3\2\2\2\u0125\u0126\7\20")
        buf.write("\2\2\u0126\u0127\5`\61\2\u0127\u0128\7\"\2\2\u0128\u0129")
        buf.write("\5> \2\u0129\u012a\t\2\2\2\u012a\u012b\5> \2\u012b\u012c")
        buf.write("\7\7\2\2\u012c\u012d\5.\30\2\u012d\u0130\3\2\2\2\u012e")
        buf.write("\u0130\5:\36\2\u012f\u0125\3\2\2\2\u012f\u012e\3\2\2\2")
        buf.write("\u01309\3\2\2\2\u0131\u0132\7\13\2\2\u0132\u0133\5> \2")
        buf.write("\u0133\u0134\7\17\2\2\u0134\u0137\5.\30\2\u0135\u0136")
        buf.write("\7\b\2\2\u0136\u0138\5.\30\2\u0137\u0135\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u013b\5<\37\2")
        buf.write("\u013a\u0131\3\2\2\2\u013a\u0139\3\2\2\2\u013b;\3\2\2")
        buf.write("\2\u013c\u013d\5> \2\u013d\u013e\7,\2\2\u013e\u013f\7")
        buf.write("\64\2\2\u013f\u0140\7$\2\2\u0140\u0141\5b\62\2\u0141\u0142")
        buf.write("\7%\2\2\u0142\u0143\7*\2\2\u0143\u0146\3\2\2\2\u0144\u0146")
        buf.write("\5,\27\2\u0145\u013c\3\2\2\2\u0145\u0144\3\2\2\2\u0146")
        buf.write("=\3\2\2\2\u0147\u0148\5@!\2\u0148\u0149\7\33\2\2\u0149")
        buf.write("\u014a\5@!\2\u014a\u014d\3\2\2\2\u014b\u014d\5@!\2\u014c")
        buf.write("\u0147\3\2\2\2\u014c\u014b\3\2\2\2\u014d?\3\2\2\2\u014e")
        buf.write("\u014f\5B\"\2\u014f\u0150\7\34\2\2\u0150\u0151\5B\"\2")
        buf.write("\u0151\u0154\3\2\2\2\u0152\u0154\5B\"\2\u0153\u014e\3")
        buf.write("\2\2\2\u0153\u0152\3\2\2\2\u0154A\3\2\2\2\u0155\u0156")
        buf.write("\b\"\1\2\u0156\u0157\5D#\2\u0157\u015d\3\2\2\2\u0158\u0159")
        buf.write("\f\4\2\2\u0159\u015a\7\35\2\2\u015a\u015c\5D#\2\u015b")
        buf.write("\u0158\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2")
        buf.write("\u015d\u015e\3\2\2\2\u015eC\3\2\2\2\u015f\u015d\3\2\2")
        buf.write("\2\u0160\u0161\b#\1\2\u0161\u0162\5F$\2\u0162\u0168\3")
        buf.write("\2\2\2\u0163\u0164\f\4\2\2\u0164\u0165\7\36\2\2\u0165")
        buf.write("\u0167\5F$\2\u0166\u0163\3\2\2\2\u0167\u016a\3\2\2\2\u0168")
        buf.write("\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169E\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016b\u016c\b$\1\2\u016c\u016d\5H%\2\u016d")
        buf.write("\u0173\3\2\2\2\u016e\u016f\f\4\2\2\u016f\u0170\7\37\2")
        buf.write("\2\u0170\u0172\5H%\2\u0171\u016e\3\2\2\2\u0172\u0175\3")
        buf.write("\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174G")
        buf.write("\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0177\5J&\2\u0177\u0178")
        buf.write("\7!\2\2\u0178\u0179\5H%\2\u0179\u017c\3\2\2\2\u017a\u017c")
        buf.write("\5J&\2\u017b\u0176\3\2\2\2\u017b\u017a\3\2\2\2\u017cI")
        buf.write("\3\2\2\2\u017d\u017e\7 \2\2\u017e\u0181\5J&\2\u017f\u0181")
        buf.write("\5L\'\2\u0180\u017d\3\2\2\2\u0180\u017f\3\2\2\2\u0181")
        buf.write("K\3\2\2\2\u0182\u0183\7\36\2\2\u0183\u0186\5L\'\2\u0184")
        buf.write("\u0186\5N(\2\u0185\u0182\3\2\2\2\u0185\u0184\3\2\2\2\u0186")
        buf.write("M\3\2\2\2\u0187\u0188\5P)\2\u0188\u0189\7&\2\2\u0189\u018a")
        buf.write("\5> \2\u018a\u018b\7\'\2\2\u018b\u018e\3\2\2\2\u018c\u018e")
        buf.write("\5P)\2\u018d\u0187\3\2\2\2\u018d\u018c\3\2\2\2\u018eO")
        buf.write("\3\2\2\2\u018f\u0190\b)\1\2\u0190\u0191\5R*\2\u0191\u019e")
        buf.write("\3\2\2\2\u0192\u0193\f\5\2\2\u0193\u0194\7,\2\2\u0194")
        buf.write("\u019d\7\64\2\2\u0195\u0196\f\4\2\2\u0196\u0197\7,\2\2")
        buf.write("\u0197\u0198\7\64\2\2\u0198\u0199\7$\2\2\u0199\u019a\5")
        buf.write("b\62\2\u019a\u019b\7%\2\2\u019b\u019d\3\2\2\2\u019c\u0192")
        buf.write("\3\2\2\2\u019c\u0195\3\2\2\2\u019d\u01a0\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019fQ\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a1\u01a2\7\r\2\2\u01a2\u01a3\7\64\2")
        buf.write("\2\u01a3\u01a4\7$\2\2\u01a4\u01a5\5b\62\2\u01a5\u01a6")
        buf.write("\7%\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a9\5T+\2\u01a8\u01a1")
        buf.write("\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9S\3\2\2\2\u01aa\u01ab")
        buf.write("\7(\2\2\u01ab\u01ac\5j\66\2\u01ac\u01ad\7)\2\2\u01ad\u01b0")
        buf.write("\3\2\2\2\u01ae\u01b0\5V,\2\u01af\u01aa\3\2\2\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0U\3\2\2\2\u01b1\u01b2\7$\2\2\u01b2\u01b3")
        buf.write("\5> \2\u01b3\u01b4\7%\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b7")
        buf.write("\5X-\2\u01b6\u01b1\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7W")
        buf.write("\3\2\2\2\u01b8\u01b9\t\3\2\2\u01b9Y\3\2\2\2\u01ba\u01be")
        buf.write("\7\64\2\2\u01bb\u01be\5\\/\2\u01bc\u01be\5^\60\2\u01bd")
        buf.write("\u01ba\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01be[\3\2\2\2\u01bf\u01c0\5> \2\u01c0\u01c1\7&\2\2\u01c1")
        buf.write("\u01c2\5> \2\u01c2\u01c3\7\'\2\2\u01c3]\3\2\2\2\u01c4")
        buf.write("\u01c5\5> \2\u01c5\u01c6\7,\2\2\u01c6\u01c7\7\64\2\2\u01c7")
        buf.write("\u01d0\3\2\2\2\u01c8\u01c9\5> \2\u01c9\u01ca\7,\2\2\u01ca")
        buf.write("\u01cb\7\64\2\2\u01cb\u01cc\7$\2\2\u01cc\u01cd\5b\62\2")
        buf.write("\u01cd\u01ce\7%\2\2\u01ce\u01d0\3\2\2\2\u01cf\u01c4\3")
        buf.write("\2\2\2\u01cf\u01c8\3\2\2\2\u01d0_\3\2\2\2\u01d1\u01d2")
        buf.write("\7\64\2\2\u01d2a\3\2\2\2\u01d3\u01d4\5> \2\u01d4\u01d5")
        buf.write("\5d\63\2\u01d5\u01d8\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7")
        buf.write("\u01d3\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8c\3\2\2\2\u01d9")
        buf.write("\u01da\7-\2\2\u01da\u01db\5> \2\u01db\u01dc\5d\63\2\u01dc")
        buf.write("\u01df\3\2\2\2\u01dd\u01df\3\2\2\2\u01de\u01d9\3\2\2\2")
        buf.write("\u01de\u01dd\3\2\2\2\u01dfe\3\2\2\2\u01e0\u01e1\t\4\2")
        buf.write("\2\u01e1\u01e2\7&\2\2\u01e2\u01e3\7/\2\2\u01e3\u01e4\7")
        buf.write("\'\2\2\u01e4g\3\2\2\2\u01e5\u01e6\5\n\6\2\u01e6\u01e7")
        buf.write("\5\16\b\2\u01e7\u01e8\7*\2\2\u01e8\u01ef\3\2\2\2\u01e9")
        buf.write("\u01ea\7\27\2\2\u01ea\u01eb\5\n\6\2\u01eb\u01ec\5\26\f")
        buf.write("\2\u01ec\u01ed\7*\2\2\u01ed\u01ef\3\2\2\2\u01ee\u01e5")
        buf.write("\3\2\2\2\u01ee\u01e9\3\2\2\2\u01efi\3\2\2\2\u01f0\u01f1")
        buf.write("\5l\67\2\u01f1\u01f2\5n8\2\u01f2\u01f5\3\2\2\2\u01f3\u01f5")
        buf.write("\3\2\2\2\u01f4\u01f0\3\2\2\2\u01f4\u01f3\3\2\2\2\u01f5")
        buf.write("k\3\2\2\2\u01f6\u01f7\t\5\2\2\u01f7m\3\2\2\2\u01f8\u01f9")
        buf.write("\7-\2\2\u01f9\u01fa\5l\67\2\u01fa\u01fb\5n8\2\u01fb\u01fe")
        buf.write("\3\2\2\2\u01fc\u01fe\3\2\2\2\u01fd\u01f8\3\2\2\2\u01fd")
        buf.write("\u01fc\3\2\2\2\u01feo\3\2\2\2\63s|\u0082\u0089\u008d\u0095")
        buf.write("\u0098\u00a5\u00ac\u00bf\u00cd\u00d1\u00d8\u00de\u00e3")
        buf.write("\u00ea\u00f4\u00fe\u0103\u0105\u0111\u0116\u011b\u0123")
        buf.write("\u012f\u0137\u013a\u0145\u014c\u0153\u015d\u0168\u0173")
        buf.write("\u017b\u0180\u0185\u018d\u019c\u019e\u01a8\u01af\u01b6")
        buf.write("\u01bd\u01cf\u01d7\u01de\u01ee\u01f4\u01fd")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'boolean'", "'break'", "'class'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'new'", "'string'", "'then'", "'for'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'!'", "'^'", 
                     "':='", "'='", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                      "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
                      "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                      "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "OP0", "OP1", "OP2", "OP3", "OP4", "NOT", "CONCAT", 
                      "ASSIGN", "INITASSIGN", "LB", "RB", "LSB", "RSB", 
                      "LP", "RP", "SEMI", "CL", "DOT", "CM", "FLOATLIT", 
                      "INTLIT", "STRLIT", "WS", "COMMENT", "LINECOMMENT", 
                      "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_memdecl = 2
    RULE_attributedecl = 3
    RULE_attrtype = 4
    RULE_vardecl = 5
    RULE_attrlist = 6
    RULE_attr = 7
    RULE_subattrlist = 8
    RULE_constdecl = 9
    RULE_constattrlist = 10
    RULE_constattr = 11
    RULE_subconstattrlist = 12
    RULE_methoddecl = 13
    RULE_staaticmethod = 14
    RULE_instancemethod = 15
    RULE_methodreturntype = 16
    RULE_paramslist = 17
    RULE_subparamslist = 18
    RULE_param = 19
    RULE_idslist = 20
    RULE_blockstatement = 21
    RULE_statement = 22
    RULE_returnstatement = 23
    RULE_continuestatement = 24
    RULE_breakstatement = 25
    RULE_assignstatement = 26
    RULE_forstatement = 27
    RULE_ifstatement = 28
    RULE_callstatement = 29
    RULE_expr = 30
    RULE_expr1 = 31
    RULE_expr2 = 32
    RULE_expr3 = 33
    RULE_expr4 = 34
    RULE_expr5 = 35
    RULE_expr6 = 36
    RULE_expr7 = 37
    RULE_expr8 = 38
    RULE_expr9 = 39
    RULE_expr10 = 40
    RULE_expr11 = 41
    RULE_expr12 = 42
    RULE_operands = 43
    RULE_lhs = 44
    RULE_arraycell = 45
    RULE_fieldaccess = 46
    RULE_scalarvar = 47
    RULE_exprlist = 48
    RULE_subexprlist = 49
    RULE_arraytype = 50
    RULE_attributeinstancedecl = 51
    RULE_literallist = 52
    RULE_literal = 53
    RULE_subliterallist = 54

    ruleNames =  [ "program", "classdecl", "memdecl", "attributedecl", "attrtype", 
                   "vardecl", "attrlist", "attr", "subattrlist", "constdecl", 
                   "constattrlist", "constattr", "subconstattrlist", "methoddecl", 
                   "staaticmethod", "instancemethod", "methodreturntype", 
                   "paramslist", "subparamslist", "param", "idslist", "blockstatement", 
                   "statement", "returnstatement", "continuestatement", 
                   "breakstatement", "assignstatement", "forstatement", 
                   "ifstatement", "callstatement", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "expr9", "expr10", "expr11", "expr12", "operands", "lhs", 
                   "arraycell", "fieldaccess", "scalarvar", "exprlist", 
                   "subexprlist", "arraytype", "attributeinstancedecl", 
                   "literallist", "literal", "subliterallist" ]

    EOF = Token.EOF
    BOOLEAN=1
    BREAK=2
    CLASS=3
    CONTINUE=4
    DO=5
    ELSE=6
    EXTENDS=7
    FLOAT=8
    IF=9
    INT=10
    NEW=11
    STRING=12
    THEN=13
    FOR=14
    RETURN=15
    TRUE=16
    FALSE=17
    VOID=18
    NIL=19
    THIS=20
    FINAL=21
    STATIC=22
    TO=23
    DOWNTO=24
    OP0=25
    OP1=26
    OP2=27
    OP3=28
    OP4=29
    NOT=30
    CONCAT=31
    ASSIGN=32
    INITASSIGN=33
    LB=34
    RB=35
    LSB=36
    RSB=37
    LP=38
    RP=39
    SEMI=40
    CL=41
    DOT=42
    CM=43
    FLOATLIT=44
    INTLIT=45
    STRLIT=46
    WS=47
    COMMENT=48
    LINECOMMENT=49
    ID=50
    UNCLOSE_STRING=51
    ILLEGAL_ESCAPE=52
    ERROR_CHAR=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def classdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ClassdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ClassdeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CLASS:
                self.state = 110
                self.classdecl()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def memdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MemdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MemdeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = BKOOLParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(BKOOLParser.CLASS)
            self.state = 119
            self.match(BKOOLParser.ID)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 120
                self.match(BKOOLParser.EXTENDS)
                self.state = 121
                self.match(BKOOLParser.ID)


            self.state = 124
            self.match(BKOOLParser.LP)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 125
                self.memdecl()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributedecl(self):
            return self.getTypedRuleContext(BKOOLParser.AttributedeclContext,0)


        def methoddecl(self):
            return self.getTypedRuleContext(BKOOLParser.MethoddeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemdecl" ):
                return visitor.visitMemdecl(self)
            else:
                return visitor.visitChildren(self)




    def memdecl(self):

        localctx = BKOOLParser.MemdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memdecl)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.methoddecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ConstdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributedecl" ):
                return visitor.visitAttributedecl(self)
            else:
                return visitor.visitChildren(self)




    def attributedecl(self):

        localctx = BKOOLParser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attributedecl)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.constdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def arraytype(self):
            return self.getTypedRuleContext(BKOOLParser.ArraytypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrtype" ):
                return visitor.visitAttrtype(self)
            else:
                return visitor.visitChildren(self)




    def attrtype(self):

        localctx = BKOOLParser.AttrtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attrtype)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.arraytype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrtype(self):
            return self.getTypedRuleContext(BKOOLParser.AttrtypeContext,0)


        def attrlist(self):
            return self.getTypedRuleContext(BKOOLParser.AttrlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 149
                self.match(BKOOLParser.STATIC)


            self.state = 152
            self.attrtype()
            self.state = 153
            self.attrlist()
            self.state = 154
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(BKOOLParser.AttrContext,0)


        def subattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubattrlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrlist" ):
                return visitor.visitAttrlist(self)
            else:
                return visitor.visitChildren(self)




    def attrlist(self):

        localctx = BKOOLParser.AttrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attrlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.attr()
            self.state = 157
            self.subattrlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INITASSIGN(self):
            return self.getToken(BKOOLParser.INITASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr" ):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)




    def attr(self):

        localctx = BKOOLParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(BKOOLParser.ID)
                self.state = 161
                self.match(BKOOLParser.INITASSIGN)
                self.state = 162
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubattrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def attr(self):
            return self.getTypedRuleContext(BKOOLParser.AttrContext,0)


        def subattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubattrlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_subattrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubattrlist" ):
                return visitor.visitSubattrlist(self)
            else:
                return visitor.visitChildren(self)




    def subattrlist(self):

        localctx = BKOOLParser.SubattrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_subattrlist)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(BKOOLParser.CM)
                self.state = 166
                self.attr()
                self.state = 167
                self.subattrlist()
                pass
            elif token in [BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def attrtype(self):
            return self.getTypedRuleContext(BKOOLParser.AttrtypeContext,0)


        def constattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.ConstattrlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = BKOOLParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constdecl)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(BKOOLParser.FINAL)
                self.state = 173
                self.attrtype()
                self.state = 174
                self.constattrlist()
                self.state = 175
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(BKOOLParser.STATIC)
                self.state = 178
                self.match(BKOOLParser.FINAL)
                self.state = 179
                self.attrtype()
                self.state = 180
                self.constattrlist()
                self.state = 181
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(BKOOLParser.FINAL)
                self.state = 184
                self.match(BKOOLParser.STATIC)
                self.state = 185
                self.attrtype()
                self.state = 186
                self.constattrlist()
                self.state = 187
                self.match(BKOOLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstattrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constattr(self):
            return self.getTypedRuleContext(BKOOLParser.ConstattrContext,0)


        def subconstattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubconstattrlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constattrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstattrlist" ):
                return visitor.visitConstattrlist(self)
            else:
                return visitor.visitChildren(self)




    def constattrlist(self):

        localctx = BKOOLParser.ConstattrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constattrlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.constattr()
            self.state = 192
            self.subconstattrlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstattrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INITASSIGN(self):
            return self.getToken(BKOOLParser.INITASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constattr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstattr" ):
                return visitor.visitConstattr(self)
            else:
                return visitor.visitChildren(self)




    def constattr(self):

        localctx = BKOOLParser.ConstattrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_constattr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(BKOOLParser.ID)
            self.state = 195
            self.match(BKOOLParser.INITASSIGN)
            self.state = 196
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubconstattrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def constattr(self):
            return self.getTypedRuleContext(BKOOLParser.ConstattrContext,0)


        def subconstattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubconstattrlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_subconstattrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubconstattrlist" ):
                return visitor.visitSubconstattrlist(self)
            else:
                return visitor.visitChildren(self)




    def subconstattrlist(self):

        localctx = BKOOLParser.SubconstattrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_subconstattrlist)
        try:
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(BKOOLParser.CM)
                self.state = 199
                self.constattr()
                self.state = 200
                self.subconstattrlist()
                pass
            elif token in [BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def staaticmethod(self):
            return self.getTypedRuleContext(BKOOLParser.StaaticmethodContext,0)


        def instancemethod(self):
            return self.getTypedRuleContext(BKOOLParser.InstancemethodContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = BKOOLParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_methoddecl)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.staaticmethod()
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.instancemethod()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaaticmethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def methodreturntype(self):
            return self.getTypedRuleContext(BKOOLParser.MethodreturntypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstatementContext,0)


        def paramslist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamslistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_staaticmethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaaticmethod" ):
                return visitor.visitStaaticmethod(self)
            else:
                return visitor.visitChildren(self)




    def staaticmethod(self):

        localctx = BKOOLParser.StaaticmethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_staaticmethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(BKOOLParser.STATIC)
            self.state = 210
            self.methodreturntype()
            self.state = 211
            self.match(BKOOLParser.ID)
            self.state = 212
            self.match(BKOOLParser.LB)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 213
                self.paramslist()


            self.state = 216
            self.match(BKOOLParser.RB)
            self.state = 217
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstancemethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstatementContext,0)


        def methodreturntype(self):
            return self.getTypedRuleContext(BKOOLParser.MethodreturntypeContext,0)


        def paramslist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamslistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instancemethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstancemethod" ):
                return visitor.visitInstancemethod(self)
            else:
                return visitor.visitChildren(self)




    def instancemethod(self):

        localctx = BKOOLParser.InstancemethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_instancemethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 219
                self.methodreturntype()


            self.state = 222
            self.match(BKOOLParser.ID)
            self.state = 223
            self.match(BKOOLParser.LB)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 224
                self.paramslist()


            self.state = 227
            self.match(BKOOLParser.RB)
            self.state = 228
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodreturntypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrtype(self):
            return self.getTypedRuleContext(BKOOLParser.AttrtypeContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methodreturntype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodreturntype" ):
                return visitor.visitMethodreturntype(self)
            else:
                return visitor.visitChildren(self)




    def methodreturntype(self):

        localctx = BKOOLParser.MethodreturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_methodreturntype)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.attrtype()
                pass
            elif token in [BKOOLParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(BKOOLParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamslistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def subparamslist(self):
            return self.getTypedRuleContext(BKOOLParser.SubparamslistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramslist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamslist" ):
                return visitor.visitParamslist(self)
            else:
                return visitor.visitChildren(self)




    def paramslist(self):

        localctx = BKOOLParser.ParamslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paramslist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.param()
            self.state = 235
            self.subparamslist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubparamslistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def subparamslist(self):
            return self.getTypedRuleContext(BKOOLParser.SubparamslistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_subparamslist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubparamslist" ):
                return visitor.visitSubparamslist(self)
            else:
                return visitor.visitChildren(self)




    def subparamslist(self):

        localctx = BKOOLParser.SubparamslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_subparamslist)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(BKOOLParser.SEMI)
                self.state = 238
                self.param()
                self.state = 239
                self.subparamslist()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrtype(self):
            return self.getTypedRuleContext(BKOOLParser.AttrtypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def idslist(self):
            return self.getTypedRuleContext(BKOOLParser.IdslistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.attrtype()
            self.state = 245
            self.match(BKOOLParser.ID)
            self.state = 246
            self.idslist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdslistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def idslist(self):
            return self.getTypedRuleContext(BKOOLParser.IdslistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idslist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdslist" ):
                return visitor.visitIdslist(self)
            else:
                return visitor.visitChildren(self)




    def idslist(self):

        localctx = BKOOLParser.IdslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_idslist)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(BKOOLParser.CM)
                self.state = 249
                self.match(BKOOLParser.ID)
                self.state = 250
                self.idslist()
                pass
            elif token in [BKOOLParser.RB, BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def attributeinstancedecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AttributeinstancedeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AttributeinstancedeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockstatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstatement" ):
                return visitor.visitBlockstatement(self)
            else:
                return visitor.visitChildren(self)




    def blockstatement(self):

        localctx = BKOOLParser.BlockstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_blockstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(BKOOLParser.LP)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.OP3) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.STRLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 257
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 255
                    self.attributeinstancedecl()
                    pass

                elif la_ == 2:
                    self.state = 256
                    self.statement()
                    pass


                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 262
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnstatement(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnstatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.returnstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def continuestatement(self):
            return self.getTypedRuleContext(BKOOLParser.ContinuestatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_returnstatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstatement" ):
                return visitor.visitReturnstatement(self)
            else:
                return visitor.visitChildren(self)




    def returnstatement(self):

        localctx = BKOOLParser.ReturnstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_returnstatement)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(BKOOLParser.RETURN)
                self.state = 267
                self.expr()
                self.state = 268
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.continuestatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def breakstatement(self):
            return self.getTypedRuleContext(BKOOLParser.BreakstatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_continuestatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestatement" ):
                return visitor.visitContinuestatement(self)
            else:
                return visitor.visitChildren(self)




    def continuestatement(self):

        localctx = BKOOLParser.ContinuestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continuestatement)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CONTINUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(BKOOLParser.CONTINUE)
                self.state = 274
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.BREAK, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.breakstatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def assignstatement(self):
            return self.getTypedRuleContext(BKOOLParser.AssignstatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_breakstatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstatement" ):
                return visitor.visitBreakstatement(self)
            else:
                return visitor.visitChildren(self)




    def breakstatement(self):

        localctx = BKOOLParser.BreakstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_breakstatement)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(BKOOLParser.BREAK)
                self.state = 279
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.assignstatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def forstatement(self):
            return self.getTypedRuleContext(BKOOLParser.ForstatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assignstatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstatement" ):
                return visitor.visitAssignstatement(self)
            else:
                return visitor.visitChildren(self)




    def assignstatement(self):

        localctx = BKOOLParser.AssignstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignstatement)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.lhs()
                self.state = 284
                self.match(BKOOLParser.ASSIGN)
                self.state = 285
                self.expr()
                self.state = 286
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.forstatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def scalarvar(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarvarContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def ifstatement(self):
            return self.getTypedRuleContext(BKOOLParser.IfstatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_forstatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstatement" ):
                return visitor.visitForstatement(self)
            else:
                return visitor.visitChildren(self)




    def forstatement(self):

        localctx = BKOOLParser.ForstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forstatement)
        self._la = 0 # Token type
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(BKOOLParser.FOR)
                self.state = 292
                self.scalarvar()
                self.state = 293
                self.match(BKOOLParser.ASSIGN)
                self.state = 294
                self.expr()
                self.state = 295
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 296
                self.expr()
                self.state = 297
                self.match(BKOOLParser.DO)
                self.state = 298
                self.statement()
                pass
            elif token in [BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.ifstatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def callstatement(self):
            return self.getTypedRuleContext(BKOOLParser.CallstatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_ifstatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstatement" ):
                return visitor.visitIfstatement(self)
            else:
                return visitor.visitChildren(self)




    def ifstatement(self):

        localctx = BKOOLParser.IfstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ifstatement)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(BKOOLParser.IF)
                self.state = 304
                self.expr()
                self.state = 305
                self.match(BKOOLParser.THEN)
                self.state = 306
                self.statement()
                self.state = 309
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 307
                    self.match(BKOOLParser.ELSE)
                    self.state = 308
                    self.statement()


                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.callstatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_callstatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstatement" ):
                return visitor.visitCallstatement(self)
            else:
                return visitor.visitChildren(self)




    def callstatement(self):

        localctx = BKOOLParser.CallstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_callstatement)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.expr()
                self.state = 315
                self.match(BKOOLParser.DOT)
                self.state = 316
                self.match(BKOOLParser.ID)
                self.state = 317
                self.match(BKOOLParser.LB)
                self.state = 318
                self.exprlist()
                self.state = 319
                self.match(BKOOLParser.RB)
                self.state = 320
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.blockstatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr1Context
            self.right = None # Expr1Context
            self.other = None # Expr1Context

        def OP0(self):
            return self.getToken(BKOOLParser.OP0, 0)

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr1Context,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                localctx.left = self.expr1()
                self.state = 326
                self.match(BKOOLParser.OP0)
                self.state = 327
                localctx.right = self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                localctx.other = self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr2Context
            self.right = None # Expr2Context
            self.other = None # Expr2Context

        def OP1(self):
            return self.getToken(BKOOLParser.OP1, 0)

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr2Context,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr1)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                localctx.left = self.expr2(0)
                self.state = 333
                self.match(BKOOLParser.OP1)
                self.state = 334
                localctx.right = self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                localctx.other = self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr2Context
            self.other = None # Expr3Context
            self.right = None # Expr3Context

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def OP2(self):
            return self.getToken(BKOOLParser.OP2, 0)

        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            localctx.other = self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 343
                    self.match(BKOOLParser.OP2)
                    self.state = 344
                    localctx.right = self.expr3(0) 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr3Context
            self.other = None # Expr4Context
            self.right = None # Expr4Context

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def OP3(self):
            return self.getToken(BKOOLParser.OP3, 0)

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            localctx.other = self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 353
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 354
                    self.match(BKOOLParser.OP3)
                    self.state = 355
                    localctx.right = self.expr4(0) 
                self.state = 360
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr4Context
            self.other = None # Expr5Context
            self.right = None # Expr5Context

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def OP4(self):
            return self.getToken(BKOOLParser.OP4, 0)

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            localctx.other = self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 369
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 364
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 365
                    self.match(BKOOLParser.OP4)
                    self.state = 366
                    localctx.right = self.expr5() 
                self.state = 371
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr6Context
            self.right = None # Expr5Context
            self.other = None # Expr6Context

        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = BKOOLParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr5)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                localctx.left = self.expr6()
                self.state = 373
                self.match(BKOOLParser.CONCAT)
                self.state = 374
                localctx.right = self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                localctx.other = self.expr6()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.right = None # Expr6Context
            self.other = None # Expr7Context

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = BKOOLParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr6)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(BKOOLParser.NOT)
                self.state = 380
                localctx.right = self.expr6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                localctx.other = self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.right = None # Expr7Context
            self.other = None # Expr8Context

        def OP3(self):
            return self.getToken(BKOOLParser.OP3, 0)

        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = BKOOLParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr7)
        try:
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.OP3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(BKOOLParser.OP3)
                self.state = 385
                localctx.right = self.expr7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                localctx.other = self.expr8()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr9Context
            self.right = None # ExprContext
            self.other = None # Expr9Context

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = BKOOLParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr8)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                localctx.left = self.expr9(0)
                self.state = 390
                self.match(BKOOLParser.LSB)
                self.state = 391
                localctx.right = self.expr()
                self.state = 392
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                localctx.other = self.expr9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr9Context
            self.other = None # Expr10Context
            self.right = None # ExprlistContext

        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            localctx.other = self.expr10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 410
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 400
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 401
                        self.match(BKOOLParser.DOT)
                        self.state = 402
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 403
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 404
                        self.match(BKOOLParser.DOT)
                        self.state = 405
                        self.match(BKOOLParser.ID)
                        self.state = 406
                        self.match(BKOOLParser.LB)
                        self.state = 407
                        localctx.right = self.exprlist()
                        self.state = 408
                        self.match(BKOOLParser.RB)
                        pass

             
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprlistContext
            self.other = None # Expr11Context

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def expr11(self):
            return self.getTypedRuleContext(BKOOLParser.Expr11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = BKOOLParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr10)
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.match(BKOOLParser.NEW)
                self.state = 416
                self.match(BKOOLParser.ID)
                self.state = 417
                self.match(BKOOLParser.LB)
                self.state = 418
                localctx.left = self.exprlist()
                self.state = 419
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                localctx.other = self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # LiterallistContext
            self.other = None # Expr12Context

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def literallist(self):
            return self.getTypedRuleContext(BKOOLParser.LiterallistContext,0)


        def expr12(self):
            return self.getTypedRuleContext(BKOOLParser.Expr12Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = BKOOLParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr11)
        try:
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(BKOOLParser.LP)
                self.state = 425
                localctx.left = self.literallist()
                self.state = 426
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                localctx.other = self.expr12()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr12Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprContext
            self.other = None # OperandsContext

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr12

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr12" ):
                return visitor.visitExpr12(self)
            else:
                return visitor.visitChildren(self)




    def expr12(self):

        localctx = BKOOLParser.Expr12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr12)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(BKOOLParser.LB)
                self.state = 432
                localctx.left = self.expr()
                self.state = 433
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                localctx.other = self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def STRLIT(self):
            return self.getToken(BKOOLParser.STRLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = BKOOLParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_operands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.STRLIT) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def arraycell(self):
            return self.getTypedRuleContext(BKOOLParser.ArraycellContext,0)


        def fieldaccess(self):
            return self.getTypedRuleContext(BKOOLParser.FieldaccessContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_lhs)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.arraycell()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                self.fieldaccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraycellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprContext
            self.right = None # ExprContext

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arraycell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraycell" ):
                return visitor.visitArraycell(self)
            else:
                return visitor.visitChildren(self)




    def arraycell(self):

        localctx = BKOOLParser.ArraycellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arraycell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            localctx.left = self.expr()
            self.state = 446
            self.match(BKOOLParser.LSB)
            self.state = 447
            localctx.right = self.expr()
            self.state = 448
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprContext
            self.right = None # ExprlistContext

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_fieldaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldaccess" ):
                return visitor.visitFieldaccess(self)
            else:
                return visitor.visitChildren(self)




    def fieldaccess(self):

        localctx = BKOOLParser.FieldaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_fieldaccess)
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                localctx.left = self.expr()
                self.state = 451
                self.match(BKOOLParser.DOT)
                self.state = 452
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                localctx.left = self.expr()
                self.state = 455
                self.match(BKOOLParser.DOT)
                self.state = 456
                self.match(BKOOLParser.ID)
                self.state = 457
                self.match(BKOOLParser.LB)
                self.state = 458
                localctx.right = self.exprlist()
                self.state = 459
                self.match(BKOOLParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scalarvar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarvar" ):
                return visitor.visitScalarvar(self)
            else:
                return visitor.visitChildren(self)




    def scalarvar(self):

        localctx = BKOOLParser.ScalarvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_scalarvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def subexprlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubexprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_exprlist)
        try:
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.expr()
                self.state = 466
                self.subexprlist()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def subexprlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubexprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_subexprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexprlist" ):
                return visitor.visitSubexprlist(self)
            else:
                return visitor.visitChildren(self)




    def subexprlist(self):

        localctx = BKOOLParser.SubexprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_subexprlist)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.match(BKOOLParser.CM)
                self.state = 472
                self.expr()
                self.state = 473
                self.subexprlist()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = BKOOLParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 479
            self.match(BKOOLParser.LSB)
            self.state = 480
            self.match(BKOOLParser.INTLIT)
            self.state = 481
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeinstancedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrtype(self):
            return self.getTypedRuleContext(BKOOLParser.AttrtypeContext,0)


        def attrlist(self):
            return self.getTypedRuleContext(BKOOLParser.AttrlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def constattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.ConstattrlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributeinstancedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeinstancedecl" ):
                return visitor.visitAttributeinstancedecl(self)
            else:
                return visitor.visitChildren(self)




    def attributeinstancedecl(self):

        localctx = BKOOLParser.AttributeinstancedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_attributeinstancedecl)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.attrtype()
                self.state = 484
                self.attrlist()
                self.state = 485
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.FINAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.match(BKOOLParser.FINAL)
                self.state = 488
                self.attrtype()
                self.state = 489
                self.constattrlist()
                self.state = 490
                self.match(BKOOLParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiterallistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def subliterallist(self):
            return self.getTypedRuleContext(BKOOLParser.SubliterallistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literallist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterallist" ):
                return visitor.visitLiterallist(self)
            else:
                return visitor.visitChildren(self)




    def literallist(self):

        localctx = BKOOLParser.LiterallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_literallist)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.literal()
                self.state = 495
                self.subliterallist()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def STRLIT(self):
            return self.getToken(BKOOLParser.STRLIT, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.STRLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubliterallistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def subliterallist(self):
            return self.getTypedRuleContext(BKOOLParser.SubliterallistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_subliterallist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubliterallist" ):
                return visitor.visitSubliterallist(self)
            else:
                return visitor.visitChildren(self)




    def subliterallist(self):

        localctx = BKOOLParser.SubliterallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_subliterallist)
        try:
            self.state = 507
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 502
                self.match(BKOOLParser.CM)
                self.state = 503
                self.literal()
                self.state = 504
                self.subliterallist()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[32] = self.expr2_sempred
        self._predicates[33] = self.expr3_sempred
        self._predicates[34] = self.expr4_sempred
        self._predicates[39] = self.expr9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




