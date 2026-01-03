grammar EasyScript;

import EasyScriptLexer;


program: (statement)* EOF;

statement: (
    comment | print_statement | alert_statement
    | key_statement | stick_statement | wait_statement
    | for_statement | break_statement | continue_statement
    | assignment | function_definition | function_call
    | complex_assignment | if_statement | return_statement
    | tool_statement | amiibo_statement
    ) ;

expression: 
    (POS | NEG | BITNOT | NOT) expression
    | expression (MUL | DIV | MOD) expression
    | expression (PLUS | MINUS) expression
    | expression (SHL | SHR) expression
    | expression (BITAND | BITOR | BITXOR) expression
    | expression (AND | OR) expression
    | expression (EQ | NEQ | LT | GT | LTE | GTE) expression
    | RVAL
    | LPAREN expression RPAREN
    ;

comment: COMMENT ~('\n'|'\r')* '\r'? '\n' ;

print_statement: PRINT expression (STRCONCAT expression)*;
alert_statement: ALERT expression;
key_statement: KEY (VARIABLE)?;
stick_statement: STICK ((VARIABLE | DIRECTION) ? (',' VARIABLE)? | RESET);
wait_statement: (WAIT)? expression;
for_statement: FOR (expression | VARIABLE ASSIGN INT TO INT)?
    (statement)*
    NEXT;

break_statement: BREAK (INT)?;
continue_statement: CONTINUE (INT)?;

assignment: (VARIABLE | CONST) ASSIGN expression;
function_definition: FUNC UID
    (statement)*
    ENDFUNC;
function_call: CALL UID ;

complex_assignment: VARIABLE (PLUS_EQ | MINUS_EQ | MUL_EQ | DIV_EQ | MOD_EQ | AND_EQ | OR_EQ | SHL_EQ | SHR_EQ | BITAND_EQ | BITOR_EQ | BITXOR_EQ) expression;
if_statement: IF expression
    (statement)*
    ((ELIF expression)
        (statement)*
    )
    (ELSE 
        (statement)*
    )?
    ENDIF;

return_statement: RETURN;
tool_statement: ( TIME | BOOL | RAND ) VARIABLE;
amiibo_statement: AMIIBO expression;

