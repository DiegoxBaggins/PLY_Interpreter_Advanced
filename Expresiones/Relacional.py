from Abstract.Expresion import *
from Abstract.Return import *
from enum import Enum


class OperacionRelacional(Enum):
    MAYOR = 0
    MENOR = 1
    MAYORIGUAL = 2
    MENORIGUAL = 3
    IGUALES = 4
    DISTINTOS = 5
    OR = 6
    AND = 7
    NOT = 8


class Relacional(Expresion):

    def __init__(self, izq, der, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.izq = izq
        self.der = der
        self.tipo = tipo

    def execute(self, environment):
        valorIzq = self.izq.execute(environment)
        valorDer = self.der.execute(environment)
        resultado = Return(False, Tipo.BOOLEAN)
        if self.tipo == OperacionRelacional.MAYOR:
            resultado.valor = valorIzq.valor > valorDer.valor
        elif self.tipo == OperacionRelacional.MENOR:
            resultado.valor = valorIzq.valor < valorDer.valor
        elif self.tipo == OperacionRelacional.MAYORIGUAL:
            resultado.valor = valorIzq.valor >= valorDer.valor
        elif self.tipo == OperacionRelacional.MENORIGUAL:
            resultado.valor = valorIzq.valor <= valorDer.valor
        elif self.tipo == OperacionRelacional.IGUALES:
            resultado.valor = valorIzq.valor == valorDer.valor
        elif self.tipo == OperacionRelacional.DISTINTOS:
            resultado.valor = valorIzq.valor != valorDer.valor
        elif self.tipo == OperacionRelacional.AND:
            resultado.valor = valorIzq.valor and valorDer.valor
        elif self.tipo == OperacionRelacional.OR:
            resultado.valor = valorIzq.valor or valorDer.valor
        elif self.tipo == OperacionRelacional.NOT:
            resultado.valor = not valorIzq.valor
        return resultado
