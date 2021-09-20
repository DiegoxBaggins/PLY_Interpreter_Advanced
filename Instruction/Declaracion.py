from Abstract.Expresion import *
from Abstract.Return import *
from enum import Enum
from Symbol.Simbolo import Simbolo


class TipoAcceso(Enum):
    GLOBAL = 0
    LOCAL = 1
    VACIO = 2


class Declaracion(Expresion):
    def __init__(self, acceso, id, valor, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.acceso = acceso
        self.id = id
        self.valor = valor
        self.tipo = tipo

    def chequearTipo(self, valor):
        if self.tipo == Tipo.UNDEFINED:
            return True
        else:
            if valor.tipo != self.tipo:
                print(valor.tipo, self.tipo)
                return False
            else:
                return True

    def execute(self, entorno):
        if self.valor is not None:
            valor = self.valor.execute(entorno)
            if isinstance(valor, Simbolo) and valor.tipo == Tipo.ARRAY:
                valor = Return(valor.valor, valor.tipo)
        else:
            valor = Simbolo(None, self.id, Tipo.UNDEFINED)
        if self.chequearTipo(valor):
            if self.acceso == TipoAcceso.LOCAL:
                if valor.tipo == Tipo.STRUCT:
                    entorno.newVarStructLocal(self.id, valor)
                else:
                    entorno.newVariableLocal(self.id, valor.valor, valor.tipo)
            elif self.acceso == TipoAcceso.GLOBAL:
                if valor.tipo == Tipo.STRUCT:
                    entorno.newVarStructGlobal(self.id, valor)
                else:
                    entorno.newVariableGlobal(self.id, valor.valor, valor.tipo)
            else:
                if valor.tipo == Tipo.STRUCT:
                    entorno.newVarStruct(self.id, valor)
                else:
                    entorno.newVariable(self.id, valor.valor, valor.tipo)
            entorno.guardarTS(self.id, self.linea, self.columna, valor.tipo)
        else:
            print("Error, tipos no coinciden")
            entorno.guardarError("Error, los tipos no coinciden", self.linea, self.columna)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), "DECLARACION")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        grafo.node(str(graph.indice), "Acceso: " + self.acceso.name)
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.indice += 1
        grafo.node(str(graph.indice), "Id: " + self.id)
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.indice += 1
        grafo.node(str(graph.indice), "Exp")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        aux = graph.pivote1
        graph.pivote1 = graph.indice
        graph.indice += 1
        self.valor.graph(grafo, graph)
        graph.indice += 1
        graph.pivote1 = aux
        grafo.node(str(graph.indice), "Tipo: " + self.tipo.name)
        grafo.edge(str(graph.pivote1), str(graph.indice))

