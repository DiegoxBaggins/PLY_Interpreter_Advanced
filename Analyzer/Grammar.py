from Instruction.Print import *
from Instruction.Sentencia import *
from Instruction.If import *

from Expresiones.Literal import *
from Expresiones.Aritmetico import *
from Expresiones.Relacional import *

rw = {
    "NULO": "NULO", "INT64": "INT64", "FLOAT64": "FLOAT64", "BOOL": "BOOL", "CHAR": "CHAR", "STRING": "STRING",
    "TRUE": "TRUE", "FALSE": "FALSE", "IF": "IF", "ELSE": "ELSE", "ELSEIF": "ELSEIF", "PRINT": "PRINT"
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
