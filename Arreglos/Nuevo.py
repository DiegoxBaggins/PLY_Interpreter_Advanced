from Abstract.Expresion import *
from Abstract.Return import *


class NuevoArray(Expresion):
    def __init__(self, expresiones, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expresiones = expresiones

    def execute(self, entorno):
        nuevoArreglo = []
        for exp in self.expresiones:
            newExp = exp.execute(entorno)
            nuevoArreglo.append(newExp)
        return Return(nuevoArreglo, Tipo.ARRAY)
