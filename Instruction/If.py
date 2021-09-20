from Abstract.Expresion import *
from Abstract.Return import *


class If(Expresion):

    def __init__(self, condicion, instrucciones, linea, columna, elseIns=None):
        Expresion.__init__(self, linea, columna)
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.elseIns = elseIns

    def execute(self, entorno):
        cond = self.condicion.execute(entorno)
        if cond.tipo != Tipo.BOOLEAN:
            print("Condición de tipo no boolean")
            entorno.guardarError("Condicion no es de tipo boolean", self.linea, self.columna)
            return
        if cond.valor:
            return self.instrucciones.execute(entorno)
        elif self.elseIns is not None:
            return self.elseIns.execute(entorno)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), "IF")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        grafo.node(str(graph.indice), "Condición")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        aux = graph.pivote1
        graph.pivote1 = graph.indice
        graph.indice += 1
        self.condicion.graph(grafo, graph)
        graph.indice += 1
        graph.pivote1 = aux
        grafo.node(str(graph.indice), "TRUE INSTRUCCIONES")
        grafo.edge(str(aux), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        self.instrucciones.graph(grafo, graph)
        graph.pivote1 = aux
        graph.indice += 1
        if self.elseIns is not None:
            grafo.node(str(graph.indice), "ELSE-ELSEIF INSTRUCCIONES")
            grafo.edge(str(aux), str(graph.indice))
            graph.pivote1 = graph.indice
            graph.indice += 1
            self.elseIns.graph(grafo, graph)
            graph.pivote1 = aux

