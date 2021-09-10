from Abstract.Expresion import *
from Abstract.Return import *
from Symbol.Entorno import *


class Sentencia(Expresion):

    def __init__(self, instrucciones, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.instrucciones = instrucciones

    def execute(self, entorno):
        for ins in self.instrucciones:
            rtr = ins.execute(entorno)
            if rtr is not None:
                return rtr
            