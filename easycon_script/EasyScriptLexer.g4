lexer grammar EasyScript;


/////////////////////////////////////////////////////////////////////////////////////
// 关键词
/////////////////////////////////////////////////////////////////////////////////////

PLUS: '+';
POS: PLUS;
MINUS: '-';
NEG: MINUS;
MUL: '*';
DIV: '/';
MOD: '%';


INC: '++';
DEC: '--';

EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

SHL: '<<';
SHR: '>>';

BITAND: '&';
BITOR: '|';
BITNOT: '~';
BITXOR: '^';


BITAND_EQ: '&=';
BITOR_EQ: '|=';
BITNOT_EQ: '~=';
BITXOR_EQ: '^=';

PLUS_EQ: '+=';
MINUS_EQ: '-=';
MUL_EQ: '*=';
DIV_EQ: '/=';
MOD_EQ: '%=';

SHL_EQ: '<<=';
SHR_EQ: '>>=';

AND_EQ: '&&=';
OR_EQ: '||=';

ASSIGN: '=';
/////////////////////////////////////////////////////////////////////////////////////
// 逻辑运算符
/////////////////////////////////////////////////////////////////////////////////////

AND: '&&';
OR: '||';
NOT: '!';

STRCONCAT: BITAND;

LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';

COMMA: ',';
COMMENT: '#';

/////////////////////////////////////////////////////////////////////////////////////
// 指令
/////////////////////////////////////////////////////////////////////////////////////


CALL: [cC][aA][lL][lL];
PRINT: [pP][rR][iI][nN][tT];
ALERT: [aA][lL][eE][rR][tT];
fragment ABXY: [aA] | [bB] | [xX] | [yY];
fragment SHOULDER: [lL] | [rR] | [zZ][lL] | [zZ][rR] ;
fragment DPAD: [uU][pP] | [dD][oO][wW][nN] | [lL][eE][fF][tT] | [rR][iI][gG][hH][tT];
KEY: (
    ABXY
    | SHOULDER
    | [lL][cC][lL][iI][cC][kK] | [rR][cC][lL][iI][cC][kK]
    | DPAD
    | [hH][oO][mM][eE] | [cC][aA][pP][tT][uU][rR][eE]
    | [pP][lL][uU][sS] | [mM][iI][nN][uU][sS]
    );
DIRECTION: DPAD;
STICK: ([lL][sS] | [rR][sS]);

WAIT: [wW][aA][iI][tT];
RESET: [rR][eE][sS][eE][tT];

FOR: [fF][oO][rR];
TO: [tT][oO];
NEXT: [nN][eE][xX][tT];
BREAK: [bB][rR][eE][aA][kK];
CONTINUE: [cC][oO][nN][tT][iI][nN][uU][eE];

IF: [iI][fF];
ELSE: [eE][lL][sS][eE];
ELIF: [eE][lL][iI][fF];
ENDIF: [eE][nN][dD][iI][fF];


FUNC: [fF][uU][nN][cC];
RETURN: [rR][eE][tT][uU][rR][nN];
ENDFUNC: [eE][nN][dD][fF][uU][nN][cC];

TIME: [tT][iI][mM][eE];
BOOL: [bB][oO][oO][lL];
RAND: [rR][aA][nN][dD];

AMIIBO: [aA][mM][iI][iI][bB][oO];

/////////////////////////////////////////////////////////////////////////////////////
//
/////////////////////////////////////////////////////////////////////////////////////

fragment ID: [a-zA-Z_][a-zA-Z0-9_]*    ;
STRING: (~[\r\n])+   ;
UID: [a-zA-Z_\u4e00-\u9fa5][a-zA-Z0-9_\u4e00-\u9fa5]*    ;
VARIABLE: '$' ID    ;
CONST: '_' UID   ;
INT10: [1-9][0-9]*    ;
INT2: '0'[bB] [01]+    ;
INT8: '0'[oO] [0-7]+    ;
INT16: '0'[xX] [0-9a-fA-F]+    ;
FLOAT: [0-9]+ '.' [0-9]+    ;
BOOLEAN: 'true' | 'false'    ;
IMAGE_LABEL: '@' UID    ;

INT: INT2 | INT8 | INT16 | INT10;
RVAL: VARIABLE | CONST | INT | FLOAT | STRING | BOOLEAN | IMAGE_LABEL;

WS: [ \t]+ -> skip;
