import math

from Abstract.Expresion import *
from Abstract.Return import *
from enum import Enum


class OperacionAritmetica(Enum):
    SUMA = 0
    RESTA = 1
    MULTI = 2
    DIV = 3
    MENOS = 4
    MULTSTR = 5
    POTENCIA = 6
    MODULO = 7
    CONCAT = 8


class Aritmetico(Expresion):

    def __init__(self, izq, der, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.izq = izq
        self.der = der
        self.tipo = tipo

    def execute(self, entorno):
        valorIzq = self.izq.execute(entorno)
        valorDer = self.der.execute(entorno)
        resultado = casteos(valorIzq, valorDer)
        if self.tipo == OperacionAritmetica.SUMA:
            resultado.valor = valorIzq.valor + valorDer.valor
        elif self.tipo == OperacionAritmetica.RESTA:
            resultado.valor = valorIzq.valor - valorDer.valor
        elif self.tipo == OperacionAritmetica.MULTI:
            if valorIzq.tipo == Tipo.STRING and valorDer.tipo == Tipo.STRING:
                resultado.valor = valorIzq.valor + valorDer.valor
            else:
                resultado.valor = valorIzq.valor * valorDer.valor
        elif self.tipo == OperacionAritmetica.DIV:
            resultado.valor = valorIzq.valor / valorDer.valor
        elif self.tipo == OperacionAritmetica.MENOS:
            resultado.valor = -valorIzq.valor
        elif self.tipo == OperacionAritmetica.POTENCIA:
            if valorIzq.tipo == Tipo.STRING and valorDer.tipo == Tipo.INT:
                resultado.valor = valorIzq.valor * valorDer.valor
            else:
                resultado.valor = math.pow(valorIzq.valor, valorDer.valor)
        elif self.tipo == OperacionAritmetica.MODULO:
            resultado.valor = valorIzq.valor % valorDer.valor
        return resultado


def casteos(izq, der):
    if izq.tipo == Tipo.FLOAT or der.tipo == Tipo.FLOAT:
        return Return(0.0, Tipo.FLOAT)
    elif izq.tipo == Tipo.STRING or der.tipo == Tipo.STRING:
        return Return("", Tipo.STRING)
    else:
        return Return(0, Tipo.INT)
