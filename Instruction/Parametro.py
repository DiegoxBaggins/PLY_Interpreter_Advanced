from Abstract.Expresion import *


class Parametro(Expresion):
    def __init__(self, id, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id

    def execute(self):
        return self

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), self.id)
        grafo.edge(str(graph.pivote1), str(graph.indice))
