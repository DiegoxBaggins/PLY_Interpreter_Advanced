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


def casteos(izq, der):
    if izq.tipo == Tipo.FLOAT or der.tipo == Tipo.FLOAT:
        return Return(0.0, Tipo.FLOAT)
    elif izq.tipo == Tipo.STRING or der.tipo == Tipo.STRING:
        return Return("", Tipo.STRING)
    else:
        return Return(0, Tipo.INT)


def comprobar(izq, der):
    if izq.tipo == Tipo.FLOAT or izq.tipo == Tipo.INT:
        if der.tipo == Tipo.FLOAT or der.tipo == Tipo.INT:
            return True
        else:
            return False
    else:
        return False


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
            if comprobar(valorIzq, valorDer):
                resultado.valor = valorIzq.valor + valorDer.valor
            else:
                print("No se puede sumar tipo: " + valorIzq.tipo.name + " y tipo: " + valorDer.tipo.name)
                entorno.guardarError("No se puede sumar tipo: " + valorIzq.tipo.name + " y tipo: " + valorDer.tipo.name
                                     , self.linea, self.columna)
        elif self.tipo == OperacionAritmetica.RESTA:
            if comprobar(valorIzq, valorDer):
                resultado.valor = valorIzq.valor - valorDer.valor
            else:
                print("No se puede restar tipo: " + valorIzq.tipo.name + " y tipo: " + valorDer.tipo.name)
                entorno.guardarError("No se puede restar tipo: " + valorIzq.tipo.name + " y tipo: " + valorDer.tipo.name
                                     , self.linea, self.columna)
        elif self.tipo == OperacionAritmetica.MULTI:
            if valorIzq.tipo == Tipo.STRING and valorDer.tipo == Tipo.STRING:
                resultado.valor = valorIzq.valor + valorDer.valor
            elif comprobar(valorIzq, valorDer):
                resultado.valor = valorIzq.valor * valorDer.valor
            else:
                print("No se puede multplicar o concatenar tipo: " + valorIzq.tipo.name + " y tipo: " + valorDer.tipo.name)
                entorno.guardarError("No se puede multiplicar o concatenar tipo: " + valorIzq.tipo.name + " y tipo: " +
                                     valorDer.tipo.name, self.linea, self.columna)
        elif self.tipo == OperacionAritmetica.DIV:
            if comprobar(valorIzq, valorDer):
                resultado = Return(0.0, Tipo.FLOAT)
                resultado.valor = valorIzq.valor / valorDer.valor
            else:
                print("No se puede dividir tipo: " + valorIzq.tipo.name + " y tipo: " + valorDer.tipo.name)
                entorno.guardarError("No se puede dividr tipo: " + valorIzq.tipo.name + " y tipo: " + valorDer.tipo.name
                                     , self.linea, self.columna)
        elif self.tipo == OperacionAritmetica.MENOS:
            if comprobar(valorIzq, valorDer):
                resultado.valor = -valorIzq.valor
            else:
                print("No se puede hacer negativo tipo: " + valorIzq.tipo.name)
                entorno.guardarError("No se puede hacer negativo de tipo: " + valorIzq.tipo.name, self.linea, self.columna)
        elif self.tipo == OperacionAritmetica.POTENCIA:
            if valorIzq.tipo == Tipo.STRING and valorDer.tipo == Tipo.INT:
                resultado.valor = valorIzq.valor * valorDer.valor
            elif comprobar(valorIzq, valorDer):
                resultado.valor = math.pow(valorIzq.valor, valorDer.valor)
            else:
                print("No se puede potenciar o multplicar string de tipo: " + valorIzq.tipo.name + " y tipo: " +
                      valorDer.tipo.name)
                entorno.guardarError("No se puede potenciar o multplicar string de tipo: " + valorIzq.tipo.name + " y tipo: "
                                     + valorDer.tipo.name, self.linea, self.columna)
        elif self.tipo == OperacionAritmetica.MODULO:
            if comprobar(valorIzq, valorDer):
                resultado.valor = valorIzq.valor % valorDer.valor
            else:
                print("No se puede modulo de tipo: " + valorIzq.tipo.name + " y tipo: " + valorDer.tipo.name)
                entorno.guardarError("No se puede modulo de tipo: " + valorIzq.tipo.name + " y tipo: " + valorDer.tipo.name
                                     , self.linea, self.columna)
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
        if self.tipo != OperacionAritmetica.MENOS:
            self.der.graph(grafo, graph)
            graph.indice += 1
