from enum import Enum


class Tipo(Enum):
    NULL = 0
    INT = 1
    FLOAT = 2
    BOOLEAN = 3
    CHAR = 4
    STRING = 5
    ARRAY = 6
    STRUCT = 7
    UNDEFINED = 8
    RETURNINS = 9
    BREAKINS = 10
    CONTINUEINS = 11


class Return:
    def __init__(self, valor, returnTipo, auxTipo=""):
        self.valor = valor
        self.tipo = returnTipo
        self.auxTipo = auxTipo

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), str(self.valor))
        grafo.edge(str(graph.pivote1), str(graph.indice))
