from Abstract.Expresion import *
from Abstract.Return import *
from enum import Enum
from Arreglos.Asignacion import *


class FuncionArreglo(Enum):
    LENGTH = 0
    PUSH = 1
    POP = 2


class FuncArreglo(Expresion):
    def __init__(self, id, exp, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.exp = exp
        self.tipo = tipo

    def execute(self, entorno):
        if self.tipo == FuncionArreglo.LENGTH:
            if isinstance(self.id, str):
                var = entorno.getVar(self.id)
            else:
                var = self.id.execute(entorno)
            if var.tipo == Tipo.ARRAY:
                return Return(len(var.valor), Tipo.INT)
            else:
                entorno.guardarError("No se puede obtener length si no es arrelo", self.linea, self.columna)
        elif self.tipo == FuncionArreglo.PUSH:
            exp = self.exp.execute(entorno)
            var = None
            if isinstance(self.id, str):
                var = entorno.getVar(self.id)
            else:
                var = self.id.execute(entorno)
            if var.tipo == Tipo.ARRAY:
                var.valor.append(exp)
            else:
                print("Var no es un arreglo")
                entorno.guardarError("Var no es un arreglo", self.linea, self.columna)
        elif self.tipo == FuncionArreglo.POP:
            var = None
            if isinstance(self.id, str):
                var = entorno.getVar(self.id)
            else:
                var = self.id.execute(entorno)
            if var.tipo == Tipo.ARRAY:
                exp = var.valor.pop()
                return exp
            else:
                print("Var no es arreglo")
                entorno.guardarError("Var no es arreglo", self.linea, self.columna)
                return Return(None, Tipo.UNDEFINED)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), self.tipo.name)
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        aux = graph.pivote1
        if isinstance(self.id, str):
            grafo.node(str(graph.indice), "Id: " + self.id)
            grafo.edge(str(graph.pivote1), str(graph.indice))
            graph.indice += 1
        else:
            self.id.graph(grafo, graph)
        graph.pivote1 = aux
        if self.tipo == FuncionArreglo.PUSH:
            grafo.node(str(graph.indice), "EXP")
            grafo.edge(str(graph.pivote1), str(graph.indice))
            graph.pivote1 = graph.indice
            graph.indice += 1
            self.exp.graph(grafo, graph)

