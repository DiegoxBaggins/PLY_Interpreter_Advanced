from Abstract.Expresion import *


class AccesoStruct(Expresion):
    def __init__(self, id, atributo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.atributo = atributo

    def execute(self, entorno):
        var = None
        if isinstance(self.id, AccesoStruct):
            var = self.id.execute(entorno)
        else:
            var = entorno.getVar(self.id)
        if var is not None:
            atributo = var.atributos.get(self.atributo)
            if atributo is not None:
                return atributo
            else:
                print("No existe ese atributo")
                entorno.guardarError("No existe el atributo" + self.atributo, self.linea, self.columna)
        else:
            print("No existe la variable")
            entorno.guardarError("Variable " + self.id + " no exoste", self.linea, self.columna)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), "ACCESO STRUCT")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        if isinstance(self.id, AccesoStruct):
            self.id.graph(grafo, graph)
        else:
            grafo.node(str(graph.indice), "Id: " + self.id)
            grafo.edge(str(graph.pivote1), str(graph.indice))
            graph.indice += 1
        grafo.node(str(graph.indice), "Atributo: " + self.atributo)
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.indice += 1


