from Abstract.Expresion import *
from Abstract.Return import *
from Instruction.Print import *


class NuevoArray(Expresion):
    def __init__(self, expresiones, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expresiones = expresiones

    def execute(self, entorno):
        nuevoArreglo = []
        for exp in self.expresiones:
            newExp = exp.execute(entorno)
            nuevoArreglo.append(newExp)
        return Return(nuevoArreglo, Tipo.ARRAY)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), "ARREGLO")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        aux = graph.indice
        graph.indice += 1
        for exp in self.expresiones:
            exp.graph(grafo, graph)
            graph.indice += 1
            graph.pivote1 = aux
