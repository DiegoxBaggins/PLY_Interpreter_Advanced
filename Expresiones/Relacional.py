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
        resultado = Return(False, Tipo.BOOLEAN)
        if self.tipo == OperacionRelacional.MAYOR:
            valorDer = self.der.execute(environment)
            resultado.valor = valorIzq.valor > valorDer.valor
        elif self.tipo == OperacionRelacional.MENOR:
            valorDer = self.der.execute(environment)
            resultado.valor = valorIzq.valor < valorDer.valor
        elif self.tipo == OperacionRelacional.MAYORIGUAL:
            valorDer = self.der.execute(environment)
            resultado.valor = valorIzq.valor >= valorDer.valor
        elif self.tipo == OperacionRelacional.MENORIGUAL:
            valorDer = self.der.execute(environment)
            resultado.valor = valorIzq.valor <= valorDer.valor
        elif self.tipo == OperacionRelacional.IGUALES:
            valorDer = self.der.execute(environment)
            resultado.valor = valorIzq.valor == valorDer.valor
        elif self.tipo == OperacionRelacional.DISTINTOS:
            valorDer = self.der.execute(environment)
            resultado.valor = valorIzq.valor != valorDer.valor
        elif self.tipo == OperacionRelacional.AND:
            if valorIzq.tipo != Tipo.BOOLEAN:
                print("Los tipos no son bool")
            else:
                if valorIzq.valor is True:
                    valorDer = self.der.execute(environment)
                    if valorDer.tipo != Tipo.BOOLEAN:
                        print("los tipos no son bool")
                    else:
                        resultado.valor = valorDer.valor
        elif self.tipo == OperacionRelacional.OR:
            if valorIzq.tipo != Tipo.BOOLEAN:
                print("Los tipos no son bool")
            else:
                if valorIzq.valor is True:
                    resultado.valor = True
                else:
                    valorDer = self.der.execute(environment)
                    if valorDer.tipo != Tipo.BOOLEAN:
                        print("los tipos no son bool")
                    else:
                        resultado.valor = valorDer.valor
        elif self.tipo == OperacionRelacional.NOT:
            if valorIzq.tipo != Tipo.BOOLEAN:
                print("Los tipos no son bool")
            else:
                resultado.valor = not valorIzq.valor
        return resultado
