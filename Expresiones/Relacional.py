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

    def execute(self, entorno):
        valorIzq = self.izq.execute(entorno)
        resultado = Return(False, Tipo.BOOLEAN)
        if self.tipo == OperacionRelacional.MAYOR:
            valorDer = self.der.execute(entorno)
            resultado.valor = valorIzq.valor > valorDer.valor
        elif self.tipo == OperacionRelacional.MENOR:
            valorDer = self.der.execute(entorno)
            resultado.valor = valorIzq.valor < valorDer.valor
        elif self.tipo == OperacionRelacional.MAYORIGUAL:
            valorDer = self.der.execute(entorno)
            resultado.valor = valorIzq.valor >= valorDer.valor
        elif self.tipo == OperacionRelacional.MENORIGUAL:
            valorDer = self.der.execute(entorno)
            resultado.valor = valorIzq.valor <= valorDer.valor
        elif self.tipo == OperacionRelacional.IGUALES:
            valorDer = self.der.execute(entorno)
            resultado.valor = valorIzq.valor == valorDer.valor
        elif self.tipo == OperacionRelacional.DISTINTOS:
            valorDer = self.der.execute(entorno)
            resultado.valor = valorIzq.valor != valorDer.valor
        elif self.tipo == OperacionRelacional.AND:
            if valorIzq.tipo != Tipo.BOOLEAN:
                print("Los tipos no son bool")
                entorno.guardarError("Los tipos no son bool", self.linea, self.columna)
            else:
                if valorIzq.valor is True:
                    valorDer = self.der.execute(entorno)
                    if valorDer.tipo != Tipo.BOOLEAN:
                        print("los tipos no son bool")
                        entorno.guardarError("Los tipos no son bool", self.linea, self.columna)
                    else:
                        resultado.valor = valorDer.valor
        elif self.tipo == OperacionRelacional.OR:
            if valorIzq.tipo != Tipo.BOOLEAN:
                print("Los tipos no son bool")
                entorno.guardarError("Los tipos no son bool", self.linea, self.columna)
            else:
                if valorIzq.valor is True:
                    resultado.valor = True
                else:
                    valorDer = self.der.execute(entorno)
                    if valorDer.tipo != Tipo.BOOLEAN:
                        print("los tipos no son bool")
                        entorno.guardarError("Los tipos no son bool", self.linea, self.columna)
                    else:
                        resultado.valor = valorDer.valor
        elif self.tipo == OperacionRelacional.NOT:
            if valorIzq.tipo != Tipo.BOOLEAN:
                print("Los tipos no son bool")
                entorno.guardarError("Los tipos no son bool", self.linea, self.columna)
            else:
                resultado.valor = not valorIzq.valor
        return resultado

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), self.tipo.name)
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        aux = graph.indice
        graph.indice += 1
        self.izq.graph(grafo, graph)
        graph.indice += 1
        graph.pivote1 = aux
        if self.tipo != OperacionRelacional.NOT:
            self.der.graph(grafo, graph)
            graph.indice += 1