from Abstract.Expresion import *
from Abstract.Return import *


class Acceso(Expresion):
    def __init__(self, id, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id

    def execute(self, entorno):
        valor = entorno.getVar(self.id)
        if valor is None:
            entorno.guardarError("Variable " + self.id + "no existe", self.linea, self.columna)
            print("Error, no existe la variable: ", self.id, self.linea, "columna ", self.columna)
            return Return(None, Tipo.UNDEFINED)
        if valor.tipo == Tipo.STRUCT or valor.tipo == Tipo.ARRAY:
            return valor
        return Return(valor.valor, valor.tipo)
