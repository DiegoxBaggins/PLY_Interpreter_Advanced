from Abstract.Expresion import *
from Abstract.Return import *


class AccesoArreglo(Expresion):
    def __init__(self, id, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.exp = exp

    def execute(self, entorno):
        var = None
        if isinstance(self.id, AccesoArreglo):
            var = self.id.execute(entorno)
        else:
            var = entorno.getVar(self.id)
        if var is not None:
            indice = self.exp.execute(entorno).valor - 1
            if var.tipo == Tipo.ARRAY:
                tamano = len(var.valor)
                if tamano > indice >= 0:
                    rtr = var.valor[indice]
                    return rtr
                else:
                    print("Indice fuera de rango")
                    entorno.guardarError("Indice fuera de rango", self.linea, self.columna)
            else:
                print("No es un arreglo")
                entorno.guardarError("No es un arreglo", self.linea, self.columna)
        else:
            print("No existe la variable")
            entorno.guardarError("No existe la variable", self.linea, self.columna)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), "ACCESO ARREGLO")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        if isinstance(self.id, AccesoArreglo):
            self.id.graph(grafo, graph)
        else:
            grafo.node(str(graph.indice), "Id: " + self.id)
            grafo.edge(str(graph.pivote1), str(graph.indice))
            graph.indice += 1
        grafo.node(str(graph.indice), "INDICE")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        self.exp.graph(grafo, graph)
        graph.indice += 1
