from Abstract.Expresion import *
from Abstract.Return import *
from Symbol.Entorno import *


class LlamadaFunc(Expresion):

    def __init__(self, id, params, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.params = params

    def execute(self, entorno):
        func = entorno.getFunc(self.id)
        struct = entorno.getStruct(self.id)
        if func is not None:
            nuevoEntorno = Entorno(entorno.getGlobal(), self.id)
            i = 0
            for param in self.params:
                valor = param.execute(entorno)
                if isinstance(valor, Simbolo):
                    nuevoEntorno.newVarStruct(func.params[i].id, valor)
                    nuevoEntorno.guardarTS(func.params[i].id, self.linea, self.columna, valor.tipo)
                else:
                    nuevoEntorno.newVariable(func.params[i].id, valor.valor, valor.tipo)
                    nuevoEntorno.guardarTS(func.params[i].id, self.linea, self.columna, valor.tipo)
                i += 1
            rtr = func.instrucciones.execute(nuevoEntorno)
            if rtr is not None:
                if rtr.tipo == Tipo.RETURNINS:
                    return None
                else:
                    return rtr
        elif struct is not None:
            ids = struct.atributos
            attrs = {}
            i = 0
            for id in ids:
                valor = self.params[i].execute(entorno)
                if id.tipo != Tipo.UNDEFINED:
                    if id.tipo == valor.tipo:
                        attrs.update({
                            id.valor: valor
                        })
                    else:
                        print("Error de tipos")
                        entorno.guardarError("Error de tipos", self.linea, self.columna)
                else:
                    attrs.update({
                        id.valor: valor
                    })
                i += 1
            nuevoSimbolo = Simbolo(0, "", Tipo.STRUCT, self.id)
            nuevoSimbolo.atributos = attrs
            return nuevoSimbolo
        else:
            print("No existe la funcion o el struct")
            entorno.guardarError("No existe la funcion o el struct", self.linea, self.columna)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), "LLAMADA FUNC / CREACION STRUCT")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        aux = graph.pivote1
        graph.indice += 1
        grafo.node(str(graph.indice), "Id: " + self.id)
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.indice += 1
        for param in self.params:
            param.graph(grafo, graph)
            graph.pivote1 = aux
            graph.indice += 1
