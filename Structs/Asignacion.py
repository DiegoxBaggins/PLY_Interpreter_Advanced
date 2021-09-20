from Abstract.Expresion import *
from Structs.Nuevo import *
from Structs.Acceso import *


class AsignacionStruct(Expresion):
    def __init__(self, id, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.exp = exp

    def execute(self, entorno):
        valor = self.exp.execute(entorno)
        id = self.id.id
        atributo = self.id.atributo
        if isinstance(id, AccesoStruct):
            variable = id.execute(entorno)
        else:
            variable = entorno.getVar(id)
        if variable is not None:
            struct = entorno.getStruct(variable.objeto)
            if struct.tipo == TipoStruct.MUTABLE:
                atr = variable.atributos.get(atributo)
                if atr is not None:
                    variable.atributos[atributo] = valor
                else:
                    print("Struct no cuenta con este atributo")
                    entorno.guardarError("Struct no cuenta con este atributo " + atributo, self.linea, self.columna)
            else:
                print("El struct no es mutable")
                entorno.guardarError("El struct no es mutable", self.linea, self.columna)
        else:
            print("var no existe")
            entorno.guardarError("La variable no existe", self.linea, self.columna)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), "ASIGNACION STRUCT")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        aux = graph.pivote1
        id = self.id.id
        atributo = self.id.atributo
        if isinstance(id, AccesoStruct):
            id.graph(grafo, graph)
        else:
            grafo.node(str(graph.indice), "Id: " + id)
            grafo.edge(str(graph.pivote1), str(graph.indice))
            graph.indice += 1
        graph.pivote1 = aux
        grafo.node(str(graph.indice), "Atributo: " + atributo)
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.indice += 1
        grafo.node(str(graph.indice), "EXP")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        self.exp.graph(grafo, graph)
