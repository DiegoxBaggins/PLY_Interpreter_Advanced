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
        if cond.tipo != Tipo.BOOLEAN:
            print("Condición de tipo no boolean")
            return
        if cond.valor:
            nuevoEntorno = Entorno(entorno, "IF")
            return self.instrucciones.execute(nuevoEntorno)
        elif self.elseIns is not None:
            nuevoEntorno = Entorno(entorno, "ELSE-ELIF")
            return self.elseIns.execute(nuevoEntorno)
