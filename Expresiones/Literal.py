from Abstract.Expresion import *
from Abstract.Return import *


class Literal(Expresion):

    def __init__(self, valor, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.valor = valor
        self.tipo = tipo

    def execute(self, entorno):
        return Return(self.valor, self.tipo)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), str(self.valor))
        grafo.edge(str(graph.pivote1), str(graph.indice))
