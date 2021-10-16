# Generated from /Users/tu/Desktop/PPL/Assignment1/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.8
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
        buf.write("\u01d9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\7\2h")
        buf.write("\n\2\f\2\16\2k\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3s\n\3\3")
        buf.write("\3\3\3\7\3w\n\3\f\3\16\3z\13\3\3\3\3\3\3\4\3\4\5\4\u0080")
        buf.write("\n\4\3\5\3\5\5\5\u0084\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("\u008c\n\6\3\7\5\7\u008f\n\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\5\t\u009c\n\t\3\n\3\n\3\n\3\n\3\n\5")
        buf.write("\n\u00a3\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00b6")
        buf.write("\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00c4\n\16\3\17\3\17\5\17\u00c8\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00cf\n\20\3\20\3\20\3\20\3\21")
        buf.write("\5\21\u00d5\n\21\3\21\3\21\3\21\5\21\u00da\n\21\3\21\3")
        buf.write("\21\3\21\3\22\3\22\5\22\u00e1\n\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u00eb\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\5\26\u00f5\n\26\3\27\3\27\3\27")
        buf.write("\7\27\u00fa\n\27\f\27\16\27\u00fd\13\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u0105\n\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u010c\n\31\3\32\3\32\3\32\5\32\u0111\n\32\3\33")
        buf.write("\3\33\3\33\5\33\u0116\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\5\34\u011e\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u012a\n\35\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\5\36\u0132\n\36\3\36\5\36\u0135\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u013c\n\37\3 \3 \3 \3 \3 \5 \u0143")
        buf.write("\n \3!\3!\3!\3!\3!\3!\7!\u014b\n!\f!\16!\u014e\13!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\7\"\u0156\n\"\f\"\16\"\u0159\13\"")
        buf.write("\3#\3#\3#\3#\3#\3#\7#\u0161\n#\f#\16#\u0164\13#\3$\3$")
        buf.write("\3$\3$\3$\3$\7$\u016c\n$\f$\16$\u016f\13$\3%\3%\3%\5%")
        buf.write("\u0174\n%\3&\3&\3&\5&\u0179\n&\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\5\'\u0181\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write("\7(\u0190\n(\f(\16(\u0193\13(\3)\3)\3)\3)\3)\3)\3)\5)")
        buf.write("\u019c\n)\3*\3*\3*\3*\3*\5*\u01a3\n*\3+\3+\3+\3+\3+\5")
        buf.write("+\u01aa\n+\3,\3,\3-\3-\3-\5-\u01b1\n-\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01c3\n/\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\5\61\u01cb\n\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\5\62\u01d2\n\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\2\7@BDFN\64\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bd\2\5\3\2\31")
        buf.write("\32\6\2\22\23\25\26.\60\64\64\7\2\3\3\n\n\f\f\16\16\64")
        buf.write("\64\2\u01da\2i\3\2\2\2\4n\3\2\2\2\6\177\3\2\2\2\b\u0083")
        buf.write("\3\2\2\2\n\u008b\3\2\2\2\f\u008e\3\2\2\2\16\u0094\3\2")
        buf.write("\2\2\20\u009b\3\2\2\2\22\u00a2\3\2\2\2\24\u00b5\3\2\2")
        buf.write("\2\26\u00b7\3\2\2\2\30\u00ba\3\2\2\2\32\u00c3\3\2\2\2")
        buf.write("\34\u00c7\3\2\2\2\36\u00c9\3\2\2\2 \u00d4\3\2\2\2\"\u00e0")
        buf.write("\3\2\2\2$\u00e2\3\2\2\2&\u00ea\3\2\2\2(\u00ec\3\2\2\2")
        buf.write("*\u00f4\3\2\2\2,\u00f6\3\2\2\2.\u0104\3\2\2\2\60\u010b")
        buf.write("\3\2\2\2\62\u0110\3\2\2\2\64\u0115\3\2\2\2\66\u011d\3")
        buf.write("\2\2\28\u0129\3\2\2\2:\u0134\3\2\2\2<\u013b\3\2\2\2>\u0142")
        buf.write("\3\2\2\2@\u0144\3\2\2\2B\u014f\3\2\2\2D\u015a\3\2\2\2")
        buf.write("F\u0165\3\2\2\2H\u0173\3\2\2\2J\u0178\3\2\2\2L\u0180\3")
        buf.write("\2\2\2N\u0182\3\2\2\2P\u019b\3\2\2\2R\u01a2\3\2\2\2T\u01a9")
        buf.write("\3\2\2\2V\u01ab\3\2\2\2X\u01b0\3\2\2\2Z\u01b2\3\2\2\2")
        buf.write("\\\u01c2\3\2\2\2^\u01c4\3\2\2\2`\u01ca\3\2\2\2b\u01d1")
        buf.write("\3\2\2\2d\u01d3\3\2\2\2fh\5\4\3\2gf\3\2\2\2hk\3\2\2\2")
        buf.write("ig\3\2\2\2ij\3\2\2\2jl\3\2\2\2ki\3\2\2\2lm\7\2\2\3m\3")
        buf.write("\3\2\2\2no\7\5\2\2or\7\64\2\2pq\7\t\2\2qs\7\64\2\2rp\3")
        buf.write("\2\2\2rs\3\2\2\2st\3\2\2\2tx\7(\2\2uw\5\6\4\2vu\3\2\2")
        buf.write("\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2y{\3\2\2\2zx\3\2\2\2{")
        buf.write("|\7)\2\2|\5\3\2\2\2}\u0080\5\b\5\2~\u0080\5\34\17\2\177")
        buf.write("}\3\2\2\2\177~\3\2\2\2\u0080\7\3\2\2\2\u0081\u0084\5\f")
        buf.write("\7\2\u0082\u0084\5\24\13\2\u0083\u0081\3\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\t\3\2\2\2\u0085\u008c\7\n\2\2\u0086\u008c")
        buf.write("\7\f\2\2\u0087\u008c\7\3\2\2\u0088\u008c\7\16\2\2\u0089")
        buf.write("\u008c\7\64\2\2\u008a\u008c\5d\63\2\u008b\u0085\3\2\2")
        buf.write("\2\u008b\u0086\3\2\2\2\u008b\u0087\3\2\2\2\u008b\u0088")
        buf.write("\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c")
        buf.write("\13\3\2\2\2\u008d\u008f\7\30\2\2\u008e\u008d\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091\5\n\6\2")
        buf.write("\u0091\u0092\5\16\b\2\u0092\u0093\7*\2\2\u0093\r\3\2\2")
        buf.write("\2\u0094\u0095\5\20\t\2\u0095\u0096\5\22\n\2\u0096\17")
        buf.write("\3\2\2\2\u0097\u009c\7\64\2\2\u0098\u0099\7\64\2\2\u0099")
        buf.write("\u009a\7#\2\2\u009a\u009c\5<\37\2\u009b\u0097\3\2\2\2")
        buf.write("\u009b\u0098\3\2\2\2\u009c\21\3\2\2\2\u009d\u009e\7-\2")
        buf.write("\2\u009e\u009f\5\20\t\2\u009f\u00a0\5\22\n\2\u00a0\u00a3")
        buf.write("\3\2\2\2\u00a1\u00a3\3\2\2\2\u00a2\u009d\3\2\2\2\u00a2")
        buf.write("\u00a1\3\2\2\2\u00a3\23\3\2\2\2\u00a4\u00a5\7\27\2\2\u00a5")
        buf.write("\u00a6\5\n\6\2\u00a6\u00a7\5\26\f\2\u00a7\u00a8\7*\2\2")
        buf.write("\u00a8\u00b6\3\2\2\2\u00a9\u00aa\7\30\2\2\u00aa\u00ab")
        buf.write("\7\27\2\2\u00ab\u00ac\5\n\6\2\u00ac\u00ad\5\26\f\2\u00ad")
        buf.write("\u00ae\7*\2\2\u00ae\u00b6\3\2\2\2\u00af\u00b0\7\27\2\2")
        buf.write("\u00b0\u00b1\7\30\2\2\u00b1\u00b2\5\n\6\2\u00b2\u00b3")
        buf.write("\5\26\f\2\u00b3\u00b4\7*\2\2\u00b4\u00b6\3\2\2\2\u00b5")
        buf.write("\u00a4\3\2\2\2\u00b5\u00a9\3\2\2\2\u00b5\u00af\3\2\2\2")
        buf.write("\u00b6\25\3\2\2\2\u00b7\u00b8\5\30\r\2\u00b8\u00b9\5\32")
        buf.write("\16\2\u00b9\27\3\2\2\2\u00ba\u00bb\7\64\2\2\u00bb\u00bc")
        buf.write("\7#\2\2\u00bc\u00bd\5<\37\2\u00bd\31\3\2\2\2\u00be\u00bf")
        buf.write("\7-\2\2\u00bf\u00c0\5\30\r\2\u00c0\u00c1\5\32\16\2\u00c1")
        buf.write("\u00c4\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00be\3\2\2\2")
        buf.write("\u00c3\u00c2\3\2\2\2\u00c4\33\3\2\2\2\u00c5\u00c8\5\36")
        buf.write("\20\2\u00c6\u00c8\5 \21\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8\35\3\2\2\2\u00c9\u00ca\7\30\2\2\u00ca\u00cb")
        buf.write("\5\"\22\2\u00cb\u00cc\7\64\2\2\u00cc\u00ce\7$\2\2\u00cd")
        buf.write("\u00cf\5$\23\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d0\3\2\2\2\u00d0\u00d1\7%\2\2\u00d1\u00d2\5")
        buf.write(",\27\2\u00d2\37\3\2\2\2\u00d3\u00d5\5\"\22\2\u00d4\u00d3")
        buf.write("\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("\u00d7\7\64\2\2\u00d7\u00d9\7$\2\2\u00d8\u00da\5$\23\2")
        buf.write("\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\3")
        buf.write("\2\2\2\u00db\u00dc\7%\2\2\u00dc\u00dd\5,\27\2\u00dd!\3")
        buf.write("\2\2\2\u00de\u00e1\5\n\6\2\u00df\u00e1\7\24\2\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1#\3\2\2\2\u00e2")
        buf.write("\u00e3\5(\25\2\u00e3\u00e4\5&\24\2\u00e4%\3\2\2\2\u00e5")
        buf.write("\u00e6\7*\2\2\u00e6\u00e7\5(\25\2\u00e7\u00e8\5&\24\2")
        buf.write("\u00e8\u00eb\3\2\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00e5\3")
        buf.write("\2\2\2\u00ea\u00e9\3\2\2\2\u00eb\'\3\2\2\2\u00ec\u00ed")
        buf.write("\5\n\6\2\u00ed\u00ee\7\64\2\2\u00ee\u00ef\5*\26\2\u00ef")
        buf.write(")\3\2\2\2\u00f0\u00f1\7-\2\2\u00f1\u00f2\7\64\2\2\u00f2")
        buf.write("\u00f5\5*\26\2\u00f3\u00f5\3\2\2\2\u00f4\u00f0\3\2\2\2")
        buf.write("\u00f4\u00f3\3\2\2\2\u00f5+\3\2\2\2\u00f6\u00fb\7(\2\2")
        buf.write("\u00f7\u00fa\5\b\5\2\u00f8\u00fa\5.\30\2\u00f9\u00f7\3")
        buf.write("\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fe\u00ff\7)\2\2\u00ff-\3\2\2\2\u0100")
        buf.write("\u0101\5<\37\2\u0101\u0102\7*\2\2\u0102\u0105\3\2\2\2")
        buf.write("\u0103\u0105\5\60\31\2\u0104\u0100\3\2\2\2\u0104\u0103")
        buf.write("\3\2\2\2\u0105/\3\2\2\2\u0106\u0107\7\21\2\2\u0107\u0108")
        buf.write("\5<\37\2\u0108\u0109\7*\2\2\u0109\u010c\3\2\2\2\u010a")
        buf.write("\u010c\5\62\32\2\u010b\u0106\3\2\2\2\u010b\u010a\3\2\2")
        buf.write("\2\u010c\61\3\2\2\2\u010d\u010e\7\6\2\2\u010e\u0111\7")
        buf.write("*\2\2\u010f\u0111\5\64\33\2\u0110\u010d\3\2\2\2\u0110")
        buf.write("\u010f\3\2\2\2\u0111\63\3\2\2\2\u0112\u0113\7\4\2\2\u0113")
        buf.write("\u0116\7*\2\2\u0114\u0116\5\66\34\2\u0115\u0112\3\2\2")
        buf.write("\2\u0115\u0114\3\2\2\2\u0116\65\3\2\2\2\u0117\u0118\5")
        buf.write("X-\2\u0118\u0119\7\"\2\2\u0119\u011a\5<\37\2\u011a\u011b")
        buf.write("\7*\2\2\u011b\u011e\3\2\2\2\u011c\u011e\58\35\2\u011d")
        buf.write("\u0117\3\2\2\2\u011d\u011c\3\2\2\2\u011e\67\3\2\2\2\u011f")
        buf.write("\u0120\7\20\2\2\u0120\u0121\5^\60\2\u0121\u0122\7\"\2")
        buf.write("\2\u0122\u0123\5<\37\2\u0123\u0124\t\2\2\2\u0124\u0125")
        buf.write("\5<\37\2\u0125\u0126\7\7\2\2\u0126\u0127\5.\30\2\u0127")
        buf.write("\u012a\3\2\2\2\u0128\u012a\5:\36\2\u0129\u011f\3\2\2\2")
        buf.write("\u0129\u0128\3\2\2\2\u012a9\3\2\2\2\u012b\u012c\7\13\2")
        buf.write("\2\u012c\u012d\5<\37\2\u012d\u012e\7\17\2\2\u012e\u0131")
        buf.write("\5.\30\2\u012f\u0130\7\b\2\2\u0130\u0132\5.\30\2\u0131")
        buf.write("\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0135\3\2\2\2")
        buf.write("\u0133\u0135\5,\27\2\u0134\u012b\3\2\2\2\u0134\u0133\3")
        buf.write("\2\2\2\u0135;\3\2\2\2\u0136\u0137\5> \2\u0137\u0138\7")
        buf.write("\33\2\2\u0138\u0139\5> \2\u0139\u013c\3\2\2\2\u013a\u013c")
        buf.write("\5> \2\u013b\u0136\3\2\2\2\u013b\u013a\3\2\2\2\u013c=")
        buf.write("\3\2\2\2\u013d\u013e\5@!\2\u013e\u013f\7\34\2\2\u013f")
        buf.write("\u0140\5@!\2\u0140\u0143\3\2\2\2\u0141\u0143\5@!\2\u0142")
        buf.write("\u013d\3\2\2\2\u0142\u0141\3\2\2\2\u0143?\3\2\2\2\u0144")
        buf.write("\u0145\b!\1\2\u0145\u0146\5B\"\2\u0146\u014c\3\2\2\2\u0147")
        buf.write("\u0148\f\4\2\2\u0148\u0149\7\35\2\2\u0149\u014b\5B\"\2")
        buf.write("\u014a\u0147\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3")
        buf.write("\2\2\2\u014c\u014d\3\2\2\2\u014dA\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014f\u0150\b\"\1\2\u0150\u0151\5D#\2\u0151\u0157")
        buf.write("\3\2\2\2\u0152\u0153\f\4\2\2\u0153\u0154\7\36\2\2\u0154")
        buf.write("\u0156\5D#\2\u0155\u0152\3\2\2\2\u0156\u0159\3\2\2\2\u0157")
        buf.write("\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158C\3\2\2\2\u0159")
        buf.write("\u0157\3\2\2\2\u015a\u015b\b#\1\2\u015b\u015c\5F$\2\u015c")
        buf.write("\u0162\3\2\2\2\u015d\u015e\f\4\2\2\u015e\u015f\7\37\2")
        buf.write("\2\u015f\u0161\5F$\2\u0160\u015d\3\2\2\2\u0161\u0164\3")
        buf.write("\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163E")
        buf.write("\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0166\b$\1\2\u0166")
        buf.write("\u0167\5H%\2\u0167\u016d\3\2\2\2\u0168\u0169\f\4\2\2\u0169")
        buf.write("\u016a\7!\2\2\u016a\u016c\5H%\2\u016b\u0168\3\2\2\2\u016c")
        buf.write("\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016eG\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171\7 \2\2")
        buf.write("\u0171\u0174\5H%\2\u0172\u0174\5J&\2\u0173\u0170\3\2\2")
        buf.write("\2\u0173\u0172\3\2\2\2\u0174I\3\2\2\2\u0175\u0176\7\36")
        buf.write("\2\2\u0176\u0179\5J&\2\u0177\u0179\5L\'\2\u0178\u0175")
        buf.write("\3\2\2\2\u0178\u0177\3\2\2\2\u0179K\3\2\2\2\u017a\u017b")
        buf.write("\5N(\2\u017b\u017c\7&\2\2\u017c\u017d\5<\37\2\u017d\u017e")
        buf.write("\7\'\2\2\u017e\u0181\3\2\2\2\u017f\u0181\5N(\2\u0180\u017a")
        buf.write("\3\2\2\2\u0180\u017f\3\2\2\2\u0181M\3\2\2\2\u0182\u0183")
        buf.write("\b(\1\2\u0183\u0184\5P)\2\u0184\u0191\3\2\2\2\u0185\u0186")
        buf.write("\f\5\2\2\u0186\u0187\7,\2\2\u0187\u0190\7\64\2\2\u0188")
        buf.write("\u0189\f\4\2\2\u0189\u018a\7,\2\2\u018a\u018b\7\64\2\2")
        buf.write("\u018b\u018c\7$\2\2\u018c\u018d\5`\61\2\u018d\u018e\7")
        buf.write("%\2\2\u018e\u0190\3\2\2\2\u018f\u0185\3\2\2\2\u018f\u0188")
        buf.write("\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192O\3\2\2\2\u0193\u0191\3\2\2\2\u0194")
        buf.write("\u0195\7\r\2\2\u0195\u0196\7\64\2\2\u0196\u0197\7$\2\2")
        buf.write("\u0197\u0198\5`\61\2\u0198\u0199\7%\2\2\u0199\u019c\3")
        buf.write("\2\2\2\u019a\u019c\5R*\2\u019b\u0194\3\2\2\2\u019b\u019a")
        buf.write("\3\2\2\2\u019cQ\3\2\2\2\u019d\u019e\7(\2\2\u019e\u019f")
        buf.write("\5`\61\2\u019f\u01a0\7)\2\2\u01a0\u01a3\3\2\2\2\u01a1")
        buf.write("\u01a3\5T+\2\u01a2\u019d\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3")
        buf.write("S\3\2\2\2\u01a4\u01a5\7$\2\2\u01a5\u01a6\5<\37\2\u01a6")
        buf.write("\u01a7\7%\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01aa\5V,\2\u01a9")
        buf.write("\u01a4\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aaU\3\2\2\2\u01ab")
        buf.write("\u01ac\t\3\2\2\u01acW\3\2\2\2\u01ad\u01b1\7\64\2\2\u01ae")
        buf.write("\u01b1\5Z.\2\u01af\u01b1\5\\/\2\u01b0\u01ad\3\2\2\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1Y\3\2\2\2\u01b2")
        buf.write("\u01b3\5<\37\2\u01b3\u01b4\7&\2\2\u01b4\u01b5\5<\37\2")
        buf.write("\u01b5\u01b6\7\'\2\2\u01b6[\3\2\2\2\u01b7\u01b8\5<\37")
        buf.write("\2\u01b8\u01b9\7,\2\2\u01b9\u01ba\7\64\2\2\u01ba\u01c3")
        buf.write("\3\2\2\2\u01bb\u01bc\5<\37\2\u01bc\u01bd\7,\2\2\u01bd")
        buf.write("\u01be\7\64\2\2\u01be\u01bf\7$\2\2\u01bf\u01c0\5`\61\2")
        buf.write("\u01c0\u01c1\7%\2\2\u01c1\u01c3\3\2\2\2\u01c2\u01b7\3")
        buf.write("\2\2\2\u01c2\u01bb\3\2\2\2\u01c3]\3\2\2\2\u01c4\u01c5")
        buf.write("\7\64\2\2\u01c5_\3\2\2\2\u01c6\u01c7\5<\37\2\u01c7\u01c8")
        buf.write("\5b\62\2\u01c8\u01cb\3\2\2\2\u01c9\u01cb\3\2\2\2\u01ca")
        buf.write("\u01c6\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cba\3\2\2\2\u01cc")
        buf.write("\u01cd\7-\2\2\u01cd\u01ce\5<\37\2\u01ce\u01cf\5b\62\2")
        buf.write("\u01cf\u01d2\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01cc\3")
        buf.write("\2\2\2\u01d1\u01d0\3\2\2\2\u01d2c\3\2\2\2\u01d3\u01d4")
        buf.write("\t\4\2\2\u01d4\u01d5\7&\2\2\u01d5\u01d6\7/\2\2\u01d6\u01d7")
        buf.write("\7\'\2\2\u01d7e\3\2\2\2\60irx\177\u0083\u008b\u008e\u009b")
        buf.write("\u00a2\u00b5\u00c3\u00c7\u00ce\u00d4\u00d9\u00e0\u00ea")
        buf.write("\u00f4\u00f9\u00fb\u0104\u010b\u0110\u0115\u011d\u0129")
        buf.write("\u0131\u0134\u013b\u0142\u014c\u0157\u0162\u016d\u0173")
        buf.write("\u0178\u0180\u018f\u0191\u019b\u01a2\u01a9\u01b0\u01c2")
        buf.write("\u01ca\u01d1")
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
    RULE_expr = 29
    RULE_expr1 = 30
    RULE_expr2 = 31
    RULE_expr3 = 32
    RULE_expr4 = 33
    RULE_expr5 = 34
    RULE_expr6 = 35
    RULE_expr7 = 36
    RULE_expr8 = 37
    RULE_expr9 = 38
    RULE_expr10 = 39
    RULE_expr11 = 40
    RULE_expr12 = 41
    RULE_operands = 42
    RULE_lhs = 43
    RULE_arraycell = 44
    RULE_fieldaccess = 45
    RULE_scalarvar = 46
    RULE_exprlist = 47
    RULE_subexprlist = 48
    RULE_arraytype = 49

    ruleNames =  [ "program", "classdecl", "memdecl", "attributedecl", "attrtype", 
                   "vardecl", "attrlist", "attr", "subattrlist", "constdecl", 
                   "constattrlist", "constattr", "subconstattrlist", "methoddecl", 
                   "staaticmethod", "instancemethod", "methodreturntype", 
                   "paramslist", "subparamslist", "param", "idslist", "blockstatement", 
                   "statement", "returnstatement", "continuestatement", 
                   "breakstatement", "assignstatement", "forstatement", 
                   "ifstatement", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", 
                   "expr11", "expr12", "operands", "lhs", "arraycell", "fieldaccess", 
                   "scalarvar", "exprlist", "subexprlist", "arraytype" ]

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
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

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




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CLASS:
                self.state = 100
                self.classdecl()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):

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




    def classdecl(self):

        localctx = BKOOLParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(BKOOLParser.CLASS)
            self.state = 109
            self.match(BKOOLParser.ID)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 110
                self.match(BKOOLParser.EXTENDS)
                self.state = 111
                self.match(BKOOLParser.ID)


            self.state = 114
            self.match(BKOOLParser.LP)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 115
                self.memdecl()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributedecl(self):
            return self.getTypedRuleContext(BKOOLParser.AttributedeclContext,0)


        def methoddecl(self):
            return self.getTypedRuleContext(BKOOLParser.MethoddeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memdecl




    def memdecl(self):

        localctx = BKOOLParser.MemdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memdecl)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ConstdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributedecl




    def attributedecl(self):

        localctx = BKOOLParser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attributedecl)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
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




    def attrtype(self):

        localctx = BKOOLParser.AttrtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attrtype)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 136
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




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 139
                self.match(BKOOLParser.STATIC)


            self.state = 142
            self.attrtype()
            self.state = 143
            self.attrlist()
            self.state = 144
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(BKOOLParser.AttrContext,0)


        def subattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubattrlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrlist




    def attrlist(self):

        localctx = BKOOLParser.AttrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attrlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.attr()
            self.state = 147
            self.subattrlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrContext(ParserRuleContext):

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




    def attr(self):

        localctx = BKOOLParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(BKOOLParser.ID)
                self.state = 151
                self.match(BKOOLParser.INITASSIGN)
                self.state = 152
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




    def subattrlist(self):

        localctx = BKOOLParser.SubattrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_subattrlist)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(BKOOLParser.CM)
                self.state = 156
                self.attr()
                self.state = 157
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




    def constdecl(self):

        localctx = BKOOLParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constdecl)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(BKOOLParser.FINAL)
                self.state = 163
                self.attrtype()
                self.state = 164
                self.constattrlist()
                self.state = 165
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(BKOOLParser.STATIC)
                self.state = 168
                self.match(BKOOLParser.FINAL)
                self.state = 169
                self.attrtype()
                self.state = 170
                self.constattrlist()
                self.state = 171
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(BKOOLParser.FINAL)
                self.state = 174
                self.match(BKOOLParser.STATIC)
                self.state = 175
                self.attrtype()
                self.state = 176
                self.constattrlist()
                self.state = 177
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constattr(self):
            return self.getTypedRuleContext(BKOOLParser.ConstattrContext,0)


        def subconstattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubconstattrlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constattrlist




    def constattrlist(self):

        localctx = BKOOLParser.ConstattrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constattrlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.constattr()
            self.state = 182
            self.subconstattrlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstattrContext(ParserRuleContext):

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




    def constattr(self):

        localctx = BKOOLParser.ConstattrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_constattr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(BKOOLParser.ID)
            self.state = 185
            self.match(BKOOLParser.INITASSIGN)
            self.state = 186
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubconstattrlistContext(ParserRuleContext):

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




    def subconstattrlist(self):

        localctx = BKOOLParser.SubconstattrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_subconstattrlist)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(BKOOLParser.CM)
                self.state = 189
                self.constattr()
                self.state = 190
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def staaticmethod(self):
            return self.getTypedRuleContext(BKOOLParser.StaaticmethodContext,0)


        def instancemethod(self):
            return self.getTypedRuleContext(BKOOLParser.InstancemethodContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methoddecl




    def methoddecl(self):

        localctx = BKOOLParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_methoddecl)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.staaticmethod()
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
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




    def staaticmethod(self):

        localctx = BKOOLParser.StaaticmethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_staaticmethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(BKOOLParser.STATIC)
            self.state = 200
            self.methodreturntype()
            self.state = 201
            self.match(BKOOLParser.ID)
            self.state = 202
            self.match(BKOOLParser.LB)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 203
                self.paramslist()


            self.state = 206
            self.match(BKOOLParser.RB)
            self.state = 207
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstancemethodContext(ParserRuleContext):

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




    def instancemethod(self):

        localctx = BKOOLParser.InstancemethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_instancemethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 209
                self.methodreturntype()


            self.state = 212
            self.match(BKOOLParser.ID)
            self.state = 213
            self.match(BKOOLParser.LB)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 214
                self.paramslist()


            self.state = 217
            self.match(BKOOLParser.RB)
            self.state = 218
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodreturntypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrtype(self):
            return self.getTypedRuleContext(BKOOLParser.AttrtypeContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methodreturntype




    def methodreturntype(self):

        localctx = BKOOLParser.MethodreturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_methodreturntype)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.attrtype()
                pass
            elif token in [BKOOLParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def subparamslist(self):
            return self.getTypedRuleContext(BKOOLParser.SubparamslistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramslist




    def paramslist(self):

        localctx = BKOOLParser.ParamslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paramslist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.param()
            self.state = 225
            self.subparamslist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubparamslistContext(ParserRuleContext):

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




    def subparamslist(self):

        localctx = BKOOLParser.SubparamslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_subparamslist)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(BKOOLParser.SEMI)
                self.state = 228
                self.param()
                self.state = 229
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




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.attrtype()
            self.state = 235
            self.match(BKOOLParser.ID)
            self.state = 236
            self.idslist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdslistContext(ParserRuleContext):

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




    def idslist(self):

        localctx = BKOOLParser.IdslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_idslist)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(BKOOLParser.CM)
                self.state = 239
                self.match(BKOOLParser.ID)
                self.state = 240
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def attributedecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AttributedeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AttributedeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockstatement




    def blockstatement(self):

        localctx = BKOOLParser.BlockstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_blockstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(BKOOLParser.LP)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.OP3) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.STRLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 247
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 245
                    self.attributedecl()
                    pass

                elif la_ == 2:
                    self.state = 246
                    self.statement()
                    pass


                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def returnstatement(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnstatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.expr()
                self.state = 255
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.returnstatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstatementContext(ParserRuleContext):

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




    def returnstatement(self):

        localctx = BKOOLParser.ReturnstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_returnstatement)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(BKOOLParser.RETURN)
                self.state = 261
                self.expr()
                self.state = 262
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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




    def continuestatement(self):

        localctx = BKOOLParser.ContinuestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continuestatement)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CONTINUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(BKOOLParser.CONTINUE)
                self.state = 268
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.BREAK, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
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




    def breakstatement(self):

        localctx = BKOOLParser.BreakstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_breakstatement)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(BKOOLParser.BREAK)
                self.state = 273
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
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




    def assignstatement(self):

        localctx = BKOOLParser.AssignstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignstatement)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.lhs()
                self.state = 278
                self.match(BKOOLParser.ASSIGN)
                self.state = 279
                self.expr()
                self.state = 280
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
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




    def forstatement(self):

        localctx = BKOOLParser.ForstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forstatement)
        self._la = 0 # Token type
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(BKOOLParser.FOR)
                self.state = 286
                self.scalarvar()
                self.state = 287
                self.match(BKOOLParser.ASSIGN)
                self.state = 288
                self.expr()
                self.state = 289
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 290
                self.expr()
                self.state = 291
                self.match(BKOOLParser.DO)
                self.state = 292
                self.statement()
                pass
            elif token in [BKOOLParser.IF, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
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

        def blockstatement(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_ifstatement




    def ifstatement(self):

        localctx = BKOOLParser.IfstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ifstatement)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(BKOOLParser.IF)
                self.state = 298
                self.expr()
                self.state = 299
                self.match(BKOOLParser.THEN)
                self.state = 300
                self.statement()
                self.state = 303
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 301
                    self.match(BKOOLParser.ELSE)
                    self.state = 302
                    self.statement()


                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.blockstatement()
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


    class ExprContext(ParserRuleContext):

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




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                localctx.left = self.expr1()
                self.state = 309
                self.match(BKOOLParser.OP0)
                self.state = 310
                localctx.right = self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
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




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr1)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                localctx.left = self.expr2(0)
                self.state = 316
                self.match(BKOOLParser.OP1)
                self.state = 317
                localctx.right = self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
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



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            localctx.other = self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 330
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
                    self.state = 325
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 326
                    self.match(BKOOLParser.OP2)
                    self.state = 327
                    localctx.right = self.expr3(0) 
                self.state = 332
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



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            localctx.other = self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 341
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
                    self.state = 336
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 337
                    self.match(BKOOLParser.OP3)
                    self.state = 338
                    localctx.right = self.expr4(0) 
                self.state = 343
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



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            localctx.other = self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 352
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
                    self.state = 347
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 348
                    self.match(BKOOLParser.OP4)
                    self.state = 349
                    localctx.right = self.expr5(0) 
                self.state = 354
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr5Context
            self.other = None # Expr6Context
            self.right = None # Expr6Context

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            localctx.other = self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr5Context(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 358
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 359
                    self.match(BKOOLParser.CONCAT)
                    self.state = 360
                    localctx.right = self.expr6() 
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):

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




    def expr6(self):

        localctx = BKOOLParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr6)
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(BKOOLParser.NOT)
                self.state = 367
                localctx.right = self.expr6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
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




    def expr7(self):

        localctx = BKOOLParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr7)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.OP3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.match(BKOOLParser.OP3)
                self.state = 372
                localctx.right = self.expr7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
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




    def expr8(self):

        localctx = BKOOLParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr8)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                localctx.left = self.expr9(0)
                self.state = 377
                self.match(BKOOLParser.LSB)
                self.state = 378
                localctx.right = self.expr()
                self.state = 379
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
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



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            localctx.other = self.expr10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 397
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 387
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 388
                        self.match(BKOOLParser.DOT)
                        self.state = 389
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 390
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 391
                        self.match(BKOOLParser.DOT)
                        self.state = 392
                        self.match(BKOOLParser.ID)
                        self.state = 393
                        self.match(BKOOLParser.LB)
                        self.state = 394
                        localctx.right = self.exprlist()
                        self.state = 395
                        self.match(BKOOLParser.RB)
                        pass

             
                self.state = 401
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




    def expr10(self):

        localctx = BKOOLParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr10)
        try:
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(BKOOLParser.NEW)
                self.state = 403
                self.match(BKOOLParser.ID)
                self.state = 404
                self.match(BKOOLParser.LB)
                self.state = 405
                localctx.left = self.exprlist()
                self.state = 406
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprlistContext
            self.other = None # Expr12Context

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def expr12(self):
            return self.getTypedRuleContext(BKOOLParser.Expr12Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr11




    def expr11(self):

        localctx = BKOOLParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr11)
        try:
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.match(BKOOLParser.LP)
                self.state = 412
                localctx.left = self.exprlist()
                self.state = 413
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
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




    def expr12(self):

        localctx = BKOOLParser.Expr12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr12)
        try:
            self.state = 423
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(BKOOLParser.LB)
                self.state = 419
                localctx.left = self.expr()
                self.state = 420
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
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




    def operands(self):

        localctx = BKOOLParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_operands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
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




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_lhs)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.arraycell()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
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




    def arraycell(self):

        localctx = BKOOLParser.ArraycellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arraycell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            localctx.left = self.expr()
            self.state = 433
            self.match(BKOOLParser.LSB)
            self.state = 434
            localctx.right = self.expr()
            self.state = 435
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldaccessContext(ParserRuleContext):

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




    def fieldaccess(self):

        localctx = BKOOLParser.FieldaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_fieldaccess)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                localctx.left = self.expr()
                self.state = 438
                self.match(BKOOLParser.DOT)
                self.state = 439
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                localctx.left = self.expr()
                self.state = 442
                self.match(BKOOLParser.DOT)
                self.state = 443
                self.match(BKOOLParser.ID)
                self.state = 444
                self.match(BKOOLParser.LB)
                self.state = 445
                localctx.right = self.exprlist()
                self.state = 446
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scalarvar




    def scalarvar(self):

        localctx = BKOOLParser.ScalarvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_scalarvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def subexprlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubexprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_exprlist)
        try:
            self.state = 456
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP3, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.expr()
                self.state = 453
                self.subexprlist()
                pass
            elif token in [BKOOLParser.RB, BKOOLParser.RP]:
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




    def subexprlist(self):

        localctx = BKOOLParser.SubexprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_subexprlist)
        try:
            self.state = 463
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.match(BKOOLParser.CM)
                self.state = 459
                self.expr()
                self.state = 460
                self.subexprlist()
                pass
            elif token in [BKOOLParser.RB, BKOOLParser.RP]:
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




    def arraytype(self):

        localctx = BKOOLParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 466
            self.match(BKOOLParser.LSB)
            self.state = 467
            self.match(BKOOLParser.INTLIT)
            self.state = 468
            self.match(BKOOLParser.RSB)
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
        self._predicates[31] = self.expr2_sempred
        self._predicates[32] = self.expr3_sempred
        self._predicates[33] = self.expr4_sempred
        self._predicates[34] = self.expr5_sempred
        self._predicates[38] = self.expr9_sempred
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
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




