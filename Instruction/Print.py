from Abstract.Expresion import *


class Print(Expresion):

    def __init__(self, valor, linea, columna, salto=False):
        Expresion.__init__(self, linea, columna)
        self.valor = valor
        self.salto = salto

    def execute(self, entorno):
        valor = self.valor.execute(entorno)
        if self.salto:
            print(valor.valor)
        else:
            print(valor.valor, end="")
