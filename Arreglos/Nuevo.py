from Abstract.Expresion import *


class NuevoArray(Expresion):
    def __init__(self, expresiones, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expresiones = expresiones

    def execute(self, entorno):
        i = 0
        for exp in self.expresiones:
            newExp = exp.execute(entorno)
            self.expresiones[i] = newExp
            i += 1
        return Return(self.expresiones, Tipo.ARRAY)
