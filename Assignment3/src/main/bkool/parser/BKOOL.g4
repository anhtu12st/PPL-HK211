grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: classdecl* EOF;

classdecl: CLASS ID (EXTENDS ID)? LP memdecl* RP;
memdecl: attributedecl | methoddecl;

attributedecl: vardecl | constdecl;
attrtype: FLOAT | INT | BOOLEAN | STRING | ID | arraytype;

vardecl: STATIC? attrtype attrlist SEMI;
attrlist: attr subattrlist;
attr: ID | ID INITASSIGN expr;
subattrlist: CM attr subattrlist |;

constdecl:
	FINAL attrtype constattrlist SEMI
	| STATIC FINAL attrtype constattrlist SEMI
	| FINAL STATIC attrtype constattrlist SEMI;
constattrlist: constattr subconstattrlist;
constattr: ID INITASSIGN expr;
subconstattrlist: CM constattr subconstattrlist |;

methoddecl: staaticmethod | instancemethod;
staaticmethod:
	STATIC methodreturntype ID LB paramslist? RB blockstatement;
instancemethod:
	methodreturntype? ID LB paramslist? RB blockstatement; // include constructor
methodreturntype: attrtype | VOID;

paramslist: param subparamslist;
subparamslist: SEMI param subparamslist |;
param: attrtype ID idslist;
idslist: CM ID idslist |;

blockstatement: LP (attributeinstancedecl | statement)* RP;
statement: returnstatement;
returnstatement: RETURN expr SEMI | continuestatement;
continuestatement: CONTINUE SEMI | breakstatement;
breakstatement: BREAK SEMI | assignstatement;
assignstatement: lhs ASSIGN expr SEMI | forstatement;
forstatement:
	FOR scalarvar ASSIGN expr (TO | DOWNTO) expr DO statement
	| ifstatement;
ifstatement:
	IF expr THEN statement (ELSE statement)?
	| callstatement;
callstatement: expr DOT ID LB exprlist RB SEMI | blockstatement;

expr: left = expr1 OP0 right = expr1 | other = expr1;
expr1: left = expr2 OP1 right = expr2 | other = expr2;
expr2: left = expr2 OP2 right = expr3 | other = expr3;
expr3: left = expr3 OP3 right = expr4 | other = expr4;
expr4: left = expr4 OP4 right = expr5 | other = expr5;
expr5: left = expr6 CONCAT right = expr5 | other = expr6;
expr6: NOT right = expr6 | other = expr7;
expr7: OP3 right = expr7 | other = expr8;
expr8: left = expr9 LSB right = expr RSB | other = expr9;
expr9:
	left = expr9 DOT ID
	| left = expr9 DOT ID LB right = exprlist RB
	| other = expr10;
expr10: NEW ID LB left = exprlist RB | other = expr11;
expr11: LP left = literallist RP | other = expr12;
expr12: LB left = expr RB | other = operands;
operands:
	THIS
	| FLOATLIT
	| INTLIT
	| TRUE
	| FALSE
	| NIL
	| ID
	| STRLIT;

lhs: ID | arraycell | fieldaccess;
arraycell: left = expr LSB right = expr RSB;
fieldaccess:
	left = expr DOT ID
	| left = expr DOT ID LB right = exprlist RB;
scalarvar: ID;
exprlist: expr subexprlist |;
subexprlist: CM expr subexprlist |;

arraytype: (FLOAT | INT | BOOLEAN | STRING | ID) LSB INTLIT RSB;
attributeinstancedecl:
	attrtype attrlist SEMI
	| FINAL attrtype constattrlist SEMI;
literallist: literal subliterallist |;
literal: FLOATLIT | INTLIT | TRUE | FALSE | NIL | STRLIT | THIS;
subliterallist: CM literal subliterallist |;

/* KEYWORD */
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FLOAT: 'float';
IF: 'if';
INT: 'int';
NEW: 'new';
STRING: 'string';
THEN: 'then';
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';

/* OPERATOR */
OP0: '>' | '<' | '>=' | '<=';
OP1: '==' | '!=';
OP2: '&&' | '||';
OP3: '+' | '-';
OP4: '*' | '/' | '\\' | '%';

NOT: '!';
CONCAT: '^';
// NEW: 'new'; (defined in KEYWORD)
ASSIGN: ':=';
INITASSIGN: '=';

/* SEPARATOR */
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
LP: '{';
RP: '}';
SEMI: ';';
CL: ':'; // semi-ccolon
DOT: '.';
CM: ','; // comma

/* LITERAL */
FLOATLIT: INTLIT '.' [0-9]* EXPONENT? | INTLIT EXPONENT;
INTLIT: [0-9]+;
STRLIT: '"' CHARACTERS? '"';
// DOUQUOTE: '"';

/* WHITESPACE */
WS: [ \t\r\n\f]+ -> skip; // skip spaces, tabs, newlines
COMMENT: '/*' .*? '*/' -> skip;
LINECOMMENT: '#' ~[\r\n\f]* -> skip;

fragment EXPONENT: [eE][+-]? [0-9]+;
fragment ESC: '\\' [bfrnt"\\];
fragment NONEESC: '\\' ~[bfrnt"\\];
fragment CHARACTERS: (~["\\\r\n\f] | ESC)*;

/* IDENTIFIER */
ID: [_a-zA-Z] [_a-zA-Z0-9]*;

UNCLOSE_STRING: '"' CHARACTERS? {raise UncloseString(self.text)};
ILLEGAL_ESCAPE:
	'"' CHARACTERS? NONEESC {raise IllegalEscape(self.text)};
ERROR_CHAR: . {raise ErrorToken(self.text)};
