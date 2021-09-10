from Abstract.Expresion import *
from Abstract.Return import *


class Acceso(Expresion):
    def __init__(self, id, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id

    def execute(self, entorno):
        valor = entorno.getVar(self.id)
        if valor is None:
            print("Error, no existe la variable: ", self.id, self.linea, self.columna)
            return
        return Return(valor.valor, valor.tipo)
