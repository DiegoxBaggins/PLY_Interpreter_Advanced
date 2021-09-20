from Abstract.Expresion import *
from Abstract.Return import *
from Symbol.Entorno import *


class For(Expresion):
    def __init__(self, variable, exp1, exp2, instrucciones, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.variable = variable
        self.exp1 = exp1
        self.exp2 = exp2
        self.instrucciones = instrucciones

    def execute(self, entorno):
        expresion1 = self.exp1.execute(entorno)
        idVar = self.variable
        nuevoEntorno = Entorno(entorno, "FOR")
        if self.exp2 is not None:
            expresion2 = self.exp2.execute(entorno)
            nuevoEntorno.newVariable(idVar, expresion1.valor, expresion1.tipo)
            while nuevoEntorno.getVar(idVar).valor <= expresion2.valor:
                rtr = self.instrucciones.execute(nuevoEntorno)
                if rtr is not None:
                    if rtr.tipo == Tipo.BREAKINS:
                        break
                    elif rtr.tipo == Tipo.CONTINUEINS:
                        continue
                    else:
                        return rtr
                var = nuevoEntorno.getVar(idVar)
                nuevoEntorno.newVariable(idVar, var.valor + 1, var.tipo)
        else:
            if expresion1.tipo == Tipo.STRING:
                nuevoEntorno.newVariable(idVar, "", expresion1.tipo)
                for caracter in expresion1.valor:
                    var = nuevoEntorno.getVar(idVar)
                    nuevoEntorno.newVariable(idVar, caracter, var.tipo)
                    rtr = self.instrucciones.execute(nuevoEntorno)
                    if rtr is not None:
                        if rtr.tipo == Tipo.BREAKINS:
                            break
                        elif rtr.tipo == Tipo.CONTINUEINS:
                            continue
                        else:
                            return rtr
            elif expresion1.tipo == Tipo.ARRAY:
                nuevoEntorno.newVariable(idVar, "", Tipo.UNDEFINED)
                for exp in expresion1.valor:
                    var = nuevoEntorno.getVar(idVar)
                    nuevoEntorno.newVariable(idVar, exp.valor, exp.tipo)
                    rtr = self.instrucciones.execute(nuevoEntorno)
                    if rtr is not None:
                        if rtr.tipo == Tipo.BREAKINS:
                            break
                        elif rtr.tipo == Tipo.CONTINUEINS:
                            continue
                        else:
                            return rtr
            else:
                print("No se puede hacer For de tipo: " + expresion1.tipo.name)
                entorno.guardarError("No se puede hacer For de tipo: " + expresion1.tipo.name, self.linea, self.columna)

    def graph(self, grafo, graph):
        grafo.node(str(graph.indice), "FOR")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        aux = graph.indice
        graph.indice += 1
        grafo.node(str(graph.indice), "Id: " + self.variable)
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.indice += 1
        if self.exp2 is not None:
            grafo.node(str(graph.indice), "Rango")
            grafo.edge(str(graph.pivote1), str(graph.indice))
            graph.pivote1 = graph.indice
            aux2 = graph.indice
            graph.indice += 1
            self.exp1.graph(grafo, graph)
            graph.indice += 1
            graph.pivote1 = aux2
            self.exp2.graph(grafo, graph)
            graph.indice += 1
        else:
            self.exp1.graph(grafo, graph)
            graph.indice += 1
        graph.pivote1 = aux
        grafo.node(str(graph.indice), "INSTRUCCIONES")
        grafo.edge(str(graph.pivote1), str(graph.indice))
        graph.pivote1 = graph.indice
        graph.indice += 1
        self.instrucciones.graph(grafo, graph)
