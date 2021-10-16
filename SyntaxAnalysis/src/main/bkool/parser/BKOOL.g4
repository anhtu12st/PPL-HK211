grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : decl decllist EOF ;

decllist: decl decllist | ;

decl: vardecl SEMI | funcdecl ;

vardecl: MTYPE varlist;
varlist: ID subvarlist;
subvarlist: CM ID subvarlist | ;

funcdecl: MTYPE ID LB fparam RB LP fbody RP;
fparam: MTYPE varlist declarparamlist | ;
declarparamlist: SEMI MTYPE varlist declarparamlist | ;

fbody: bodyitem fbody | ;
bodyitem: (vardecl | assignvar | callfunc | freturn) SEMI;

callfunc: ID LB fargument RB;
fargument: expr fargumentlist | ;
fargumentlist: CM expr fargumentlist | ;
assignvar: ID EQ expr;
freturn: 'return' expr;
expr: var exprlist;
exprlist: OP var exprlist | ;

var: ID | DECIMAL | callfunc;
MTYPE: 'int' | 'float';
ID: [a-zA-Z]+;
DECIMAL: INTLIT ('.'INTLIT)?;
INTLIT: [0-9]+;
OP: '+' | '-' | '*' | '/' ;
LB: '(';
RB: ')';
CM: ',';
LP: '{';
RP: '}';
EQ: '=';
SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;