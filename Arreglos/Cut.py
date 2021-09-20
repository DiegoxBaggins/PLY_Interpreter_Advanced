from Abstract.Expresion import *
from Abstract.Return import *
from Arreglos.Asignacion import *


class CutArreglo(Expresion):
    def __init__(self, id, exp1, exp2, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, entorno):
        exp1 = self.exp1.execute(entorno).valor - 1
        exp2 = self.exp2.execute(entorno).valor
        var = None
        if isinstance(self.id, str):
            var = entorno.getVar(self.id)
        else:
            var = self.id.execute(entorno)
        if var is not None:
            if var.tipo == Tipo.ARRAY:
                return Return(var.valor[exp1:exp2], Tipo.ARRAY)
            else:
                print("No es un arreglo")
                entorno.guardarError("No es un arreglo", self.linea, self.columna)
        else:
            entorno.guardarError("El arreglo no existe", self.linea, self.columna)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), "CUT ARREGLO")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        grafo.node(str(graph.indice), "Id: " + self.id)
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.indice += 1
        grafo.node(str(graph.indice), "Exp Inicio")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        aux = graph.pivote1
        graph.pivote1 = graph.indice
        graph.indice += 1
        self.exp1.graph(grafo, graph)
        graph.indice += 1
        grafo.node(str(graph.indice), "Exp Final")
        grafo.edge(str(aux), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        self.exp2.graph(grafo, graph)
