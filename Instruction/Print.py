from Abstract.Expresion import *


class Print(Expresion):

    def __init__(self, valor, linea, columna, salto=False):
        Expresion.__init__(self, linea, columna)
        self.valor = valor
        self.salto = salto

    def execute(self, entorno):
        valor = self.valor.execute(entorno)
        f = open("./output.txt", "a")
        if self.salto:
            print(valor.valor)
            f.write(str(valor.valor) + "\n")
        else:
            print(valor.valor, end="")
            f.write(str(valor.valor))
        f.close()
