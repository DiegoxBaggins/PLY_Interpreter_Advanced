from Abstract.Expresion import *


class Function(Expresion):
    def __init__(self, id, params, instr, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.params = params
        self.instrucciones = instr

    def execute(self, entorno):
        func = entorno.getFunc(self.id)
        if func is None:
            entorno.newFunc(self.id, self)
            entorno.guardarTS(self.id, self.linea, self.columna, "Funcion")
        else:
            print("Funcion " + self.id + "repetida")
            entorno.guardarError("Funcion " + self.id + "repetida", self.linea, self.columna)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), "FUNCION")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        grafo.node(str(graph.indice), "Id: " + self.id)
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.indice += 1
        grafo.node(str(graph.indice), "Parametros")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        aux = graph.pivote1
        graph.pivote1 = graph.indice
        aux2 = graph.pivote1
        graph.indice += 1
        for par in self.params:
            par.graph(grafo, graph)
            graph.pivote1 = aux2
            graph.indice += 1
        graph.pivote1 = aux
        grafo.node(str(graph.indice), "INSTRUCCIONES")
        grafo.edge(str(aux), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        self.instrucciones.graph(grafo, graph)
