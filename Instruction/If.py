from Abstract.Expresion import *
from Abstract.Return import *


class If(Expresion):

    def __init__(self, condicion, instrucciones, linea, columna, elseIns=None):
        Expresion.__init__(self, linea, columna)
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.elseIns = elseIns

    def execute(self, entorno):
        cond = self.condicion.execute(entorno)
        if cond.type != Tipo.BOOLEAN:
            print("Condición de tipo no boolean")
            return
        if cond.value:
            return self.instrucciones.execute(entorno)
        elif self.elseIns is not None:
            return self.elseIns.execute(entorno)
