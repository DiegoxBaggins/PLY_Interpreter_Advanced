import math
from Abstract.Expresion import *
from Abstract.Return import *
from enum import Enum


class FuncionNativa(Enum):
    LOG10 = 0
    LOGBAS = 1
    SEN = 2
    COS = 3
    TAN = 4
    RAIZ = 5
    UPPER = 6
    LOWER = 7


class Nativo(Expresion):

    def __init__(self, arg1, arg2, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.arg1 = arg1
        self.arg2 = arg2
        self.tipo = tipo

    def execute(self, entorno):
        valorArg1 = self.arg1.execute(entorno)
        resultado = Return(0.0, Tipo.FLOAT)
        if self.tipo == FuncionNativa.LOG10:
            resultado.valor = math.log(valorArg1.valor, 10)
        elif self.tipo == FuncionNativa.LOGBAS:
            valorArg2 = self.arg2.execute(entorno)
            resultado.valor = math.log(valorArg2.valor, valorArg1.valor)
        elif self.tipo == FuncionNativa.SEN:
            resultado.valor = math.sin(valorArg1.valor)
        elif self.tipo == FuncionNativa.COS:
            resultado.valor = math.cos(valorArg1.valor)
        elif self.tipo == FuncionNativa.TAN:
            resultado.valor = math.tan(valorArg1.valor)
        elif self.tipo == FuncionNativa.RAIZ:
            resultado.valor = math.sqrt(valorArg1.valor)
        elif self.tipo == FuncionNativa.UPPER:
            resultado = Return("", Tipo.STRING)
            resultado.valor = valorArg1.valor.upper()
        elif self.tipo == FuncionNativa.LOWER:
            resultado = Return("", Tipo.STRING)
            resultado.valor = valorArg1.valor.lower()
        return resultado


