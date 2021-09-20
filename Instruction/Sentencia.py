from Abstract.Expresion import *
from Abstract.Return import *
from Symbol.Entorno import *


class Sentencia(Expresion):

    def __init__(self, instrucciones, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.instrucciones = instrucciones

    def execute(self, entorno):
        try:
            for ins in self.instrucciones:
                rtr = ins.execute(entorno)
                if rtr is not None:
                    return rtr
        except:
            print("Error ejecutando instrucciones")
            entorno.guardarError("Error ejecutando instrucciones", self.linea, self.columna)

    def graph(self, grafo, graph):
        aux = graph.pivote1
        for ins in self.instrucciones:
            ins.graph(grafo, graph)
            graph.indice += 1
            graph.pivote1 = aux
