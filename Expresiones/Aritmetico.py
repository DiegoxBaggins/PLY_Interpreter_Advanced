from Abstract.Expresion import *
from Abstract.Return import *
from enum import Enum


class OperacionAritmetica(Enum):
    SUMA = 0
    RESTA = 1
    MULTI = 2
    DIV = 3
    MENOS = 4


class Aritmetico(Expresion):

    def __init__(self, izq, der, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.izq = izq
        self.der = der
        self.tipo = tipo

    def execute(self, entorno):
        valorIzq = self.izq.execute(entorno)
        valorDer = self.der.execute(entorno)
        resultado = Return(0, Tipo.INT)
        if self.tipo == OperacionAritmetica.SUMA:
            resultado.valor = valorIzq.valor + valorDer.valor
        elif self.tipo == OperacionAritmetica.RESTA:
            resultado.valor = valorIzq.valor - valorDer.valor
        elif self.tipo == OperacionAritmetica.MULTI:
            resultado.valor = valorIzq.valor * valorDer.valor
        elif self.tipo == OperacionAritmetica.DIV:
            resultado.valor = valorIzq.valor / valorDer.valor
        elif self.tipo == OperacionAritmetica.MENOS:
            resultado.valor = -valorIzq
        return resultado
