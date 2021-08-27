from Abstract.Expresion import *
from Abstract.Return import *


class Literal(Expresion):

    def __init__(self, valor, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.valor = valor
        self.tipo = tipo

    def execute(self, entorno):
        return Return(self.valor, self.tipo)
