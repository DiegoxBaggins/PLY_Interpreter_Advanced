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
    PARSE = 8
    TRUNC = 9
    FLOAT = 10
    STRING = 11
    TYPEOF = 12


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
            if valorArg1.tipo == Tipo.FLOAT or valorArg1.tipo == Tipo.INT:
                resultado.valor = math.log(valorArg1.valor, 10)
        elif self.tipo == FuncionNativa.LOGBAS:
            if valorArg1.tipo == Tipo.FLOAT or valorArg1.tipo == Tipo.INT:
                valorArg2 = self.arg2.execute(entorno)
                if valorArg2.tipo == Tipo.FLOAT or valorArg2.tipo == Tipo.INT:
                    resultado.valor = math.log(valorArg2.valor, valorArg1.valor)
        elif self.tipo == FuncionNativa.SEN:
            if valorArg1.tipo == Tipo.FLOAT or valorArg1.tipo == Tipo.INT:
                resultado.valor = math.sin(valorArg1.valor)
        elif self.tipo == FuncionNativa.COS:
            if valorArg1.tipo == Tipo.FLOAT or valorArg1.tipo == Tipo.INT:
                resultado.valor = math.cos(valorArg1.valor)
        elif self.tipo == FuncionNativa.TAN:
            if valorArg1.tipo == Tipo.FLOAT or valorArg1.tipo == Tipo.INT:
                resultado.valor = math.tan(valorArg1.valor)
        elif self.tipo == FuncionNativa.RAIZ:
            if valorArg1.tipo == Tipo.FLOAT or valorArg1.tipo == Tipo.INT:
                resultado.valor = math.sqrt(valorArg1.valor)
        elif self.tipo == FuncionNativa.UPPER:
            if valorArg1.tipo == Tipo.STRING:
                resultado = Return("", Tipo.STRING)
                resultado.valor = valorArg1.valor.upper()
        elif self.tipo == FuncionNativa.LOWER:
            if valorArg1.tipo == Tipo.STRING:
                resultado = Return("", Tipo.STRING)
                resultado.valor = valorArg1.valor.lower()
        elif self.tipo == FuncionNativa.PARSE:
            if self.arg1.tipo == Tipo.STRING:
                if self.arg2 == Tipo.FLOAT:
                    try:
                        resultado.valor = float(valorArg1.valor)
                    except ValueError:
                        print("No es un float")
                elif self.arg2 == Tipo.INT:
                    resultado = Return(0, Tipo.INT)
                    try:
                        resultado.valor = int(valorArg1.valor)
                    except ValueError:
                        print("No es un int")
        elif self.tipo == FuncionNativa.TRUNC:
            if valorArg1.tipo == Tipo.FLOAT:
                resultado = Return(0, Tipo.INT)
                resultado.valor = math.floor(valorArg1.valor)
        elif self.tipo == FuncionNativa.FLOAT:
            if valorArg1.tipo == Tipo.INT:
                resultado.valor = float(valorArg1.valor)
        elif self.tipo == FuncionNativa.STRING:
            if valorArg1.tipo != Tipo.STRING and valorArg1.tipo != Tipo.CHAR:
                resultado = Return("", Tipo.STRING)
                resultado.valor = str(valorArg1.valor)
            else:
                resultado = Return(valorArg1.valor, Tipo.STRING)
        elif self.tipo == FuncionNativa.TYPEOF:
            resultado = Return("", Tipo.STRING)
            resultado.valor = valorArg1.tipo.name
        return resultado
