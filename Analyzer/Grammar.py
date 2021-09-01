from Instruction.Print import *
from Instruction.Sentencia import *
from Instruction.If import *

from Expresiones.Literal import *
from Expresiones.Aritmetico import *
from Expresiones.Relacional import *

rw = {
    "NULO": "NULO", "INT64": "INT64", "FLOAT64": "FLOAT64", "BOOL": "BOOL", "CHAR": "CHAR", "STRING": "STRING",
    "TRUE": "TRUE", "FALSE": "FALSE", "IF": "IF", "ELSE": "ELSE", "ELSEIF": "ELSEIF", "PRINT": "PRINT",
    "PRINTLN": "PRINTLN "
}

tokens = [
             "ID", "INTID", "FLOATID", "STRINGID",
             "IGUAL", "PUNTO", "COMA", "DOSPUNTOS", "PUNTOCOMA", "PARIZQ", "PARDER",
             "MAS", "MENOS", "MULT", "DIV",
             "AND", "OR", "NOT",
             "MAYOR", "MENOR", "MAYORIGUAL", "MENORIGUAL", "IGUALES", "DISTINTOS",
         ] + list(rw.values())

t_IGUAL = r'='
t_PUNTO = r'.'
t_DOSPUNTOS = r':'
t_PUNTOCOMA = r';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_IGUALES = r'=='
t_DISTINTOS = r'!='


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = rw.get(t.value.upper(), 'ID')
    return t


def t_FLOATID(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("ERROR IN PARSE TO FLOAT")
        t.value = 0
    return t


def t_INTID(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("ERROR IN PARSE TO INT")
        t.value = 0
    return t


def t_STRINGID(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t


t_ignore = " \t"


def t_COMENTARIO(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count("\n")


def t_COMLINEA(t):
    r'\#.*\n'
    t.lexer.lineno += 1


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex
lexer = lex.lex()


precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUALES', 'DISTINTOS'),
    ('left', 'MAYORIGUAL', 'MENORIGUAL', 'MAYOR', 'MENOR'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTI', 'DIV'),
    ('right', 'NOT'),
    ('right', 'UMINUS'),
)


# SYNTACTIC ANALYSIS

def p_start(t):
    'start : instructions'
    t[0] = t[1]
    return t[0]


def p_instrucciones(t):
    '''instrucciones : instrucciones instruccion
                    | instruccion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]


def p_instruccion(t):
    '''instruccion  : printINS PUNTOCOMA
                    | ifINS PUNTOCOMA'''
    t[0] = t[1]


# STATEMENT
def p_sentencia(t):
    '''sentencia : instrucciones'''
    t[0] = Sentencia(t[1], t.lineno(1), t.lexpos(0))


# PRINT ST
def p_printlnINS(t):
    'printINS  : PRINTLN PARIZQ expresion PARDER'
    t[0] = Print(t[3], t.lineno(1), t.lexpos(0), True)


def p_printINS(t):
    'printINS  : PRINT PARIZQ expresion PARDER'
    t[0] = Print(t[3], t.lineno(1), t.lexpos(0))


# IFST
def p_ifINS(t):
    '''ifINS : IF expresion sentencia END
             | IF expresion sentencia ELSE sentencia END
             | IF expresion sentencia elseIfLista END'''
    if len(t) == 5:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0))
    elif len(t) == 7:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])


def p_elseIfLista(t):
    '''elseIfLista   : ELSEIF expresion sentencia
                     | ELSEIF expresion sentencia ELSE sentencia
                     | ELSEIF expresion sentencia elseIfList'''
    if len(t) == 4:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0))
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])
    elif len(t) == 5:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])


def p_expresion(t):
    '''expresion    : MENOS expresion %prec UMINUS
                    | NOT expresion %prec UMINUS

                    | expresion MAS expresion
                    | expresion MENOS expresion
                    | expresion MULTI expresion
                    | expresion DIV expresion
                    | expresion MAYOR expresion
                    | expresion MENOR expresion
                    | expresion MAYORIGUAL expresion
                    | expresion MENORIGUAL expresion
                    | expresion IGUALES expresion
                    | expresion DISTINTOS expresion

                    | expresion OR expresion
                    | expresion AND expresion
                    | expValor'''
    if len(t) == 2:
        t[0] = t[1]
    elif len(t) == 3:
        # UMINUS
        t[0] = Aritmetico(Literal(0, Tipo.INT, t.lineno(1), t.lexpos(0)), t[2], OperacionAritmetica.MINUS, t.lineno(1),
                          t.lexpos(0))
    else:
        if t[2] == "+":
            t[0] = Aritmetico(t[1], t[3], OperacionAritmetica.PLUS, t.lineno(2), t.lexpos(0))
        elif t[2] == "-":
            t[0] = Aritmetico(t[1], t[3], OperacionAritmetica.MINUS, t.lineno(2), t.lexpos(0))
        elif t[2] == "*":
            t[0] = Aritmetico(t[1], t[3], OperacionAritmetica.TIMES, t.lineno(2), t.lexpos(0))
        elif t[2] == "/":
            t[0] = Aritmetico(t[1], t[3], OperacionAritmetica.DIV, t.lineno(2), t.lexpos(0))
        elif t[2] == ">":
            t[0] = Relacional(t[1], t[3], OperacionRelacional.GREATER, t.lineno(2), t.lexpos(2))
        elif t[2] == "<":
            t[0] = Relacional(t[1], t[3], OperacionRelacional.LESS, t.lineno(2), t.lexpos(2))
        elif t[2] == ">=":
            t[0] = Relacional(t[1], t[3], OperacionRelacional.GREATEREQUAL, t.lineno(2), t.lexpos(2))
        elif t[2] == "<=":
            t[0] = Relacional(t[1], t[3], OperacionRelacional.LESSEQUAL, t.lineno(2), t.lexpos(2))
        elif t[2] == "==":
            t[0] = Relacional(t[1], t[3], OperacionRelacional.EQUALSEQUALS, t.lineno(2), t.lexpos(2))
        elif t[2] == "!=":
            t[0] = Relacional(t[1], t[3], OperacionRelacional.DISTINT, t.lineno(2), t.lexpos(2))
        elif t[2] == "||":
            # OR
            t[0] = 0
        elif t[2] == "&&":
            # AND
            t[0] = 0


def p_finalExp(t):
    '''expValor : PARIZQ expression PARDER
                | INTID
                | FLOATID
                | STRINGID
                | TRUE
                | FALSE'''
    if len(t) == 2:
        if isinstance(t[1], int):
            t[0] = Literal(int(t[1]), Tipo.INT, t.lineno(1), t.lexpos(0))
        elif isinstance(t[1], float):
            t[0] = Literal(float(t[1]), Tipo.FLOAT, t.lineno(1), t.lexpos(0))
        elif isinstance(t[1], str):
            value = str(t[1])
            if "true" in value:
                t[0] = Literal(True, Tipo.BOOLEAN, t.lineno(1), t.lexpos(0))
            elif "false" in value:
                t[0] = Literal(False, Tipo.BOOLEAN, t.lineno(1), t.lexpos(0))
            else:
                t[0] = Literal(str(t[1]), Tipo.STRING, t.lineno(1), t.lexpos(0))
    else:
        t[0] = t[2]


def p_error(t):
    print(t)
    print("Syntactic error in '%s'" % t.value)


import ply.yacc as yacc

parser = yacc.yacc()


def parse():
    f = open("./input.jl", "r")
    input = f.read()
    return parser.parse(input)