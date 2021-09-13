from Abstract.Expresion import *


def imprimirlistas(lista, f):
    print("[", end="")
    f.write("[")
    i = 1
    for elemento in lista:
        if elemento.tipo == Tipo.ARRAY:
            imprimirlistas(elemento.valor, f)
        else:
            print(elemento.valor, end="")
            f.write(str(elemento.valor))
        if i != len(lista):
            print(",", end="")
            f.write(",")
        i += 1
    print("]", end="")
    f.write("]")


class Print(Expresion):

    def __init__(self, valor, linea, columna, salto=False):
        Expresion.__init__(self, linea, columna)
        self.valor = valor
        self.salto = salto

    def execute(self, entorno):
        f = open("./output.txt", "a")
        for exp in self.valor:
            valor = exp.execute(entorno)
            if valor.tipo == Tipo.ARRAY:
                print("[", end="")
                f.write("[")
                i = 1
                for valores in valor.valor:
                    if valores.tipo == Tipo.ARRAY:
                        imprimirlistas(valores.valor, f)
                    else:
                        print(valores.valor, end="")
                        f.write(str(valores.valor))
                    if i != len(valor.valor):
                        print(",", end="")
                        f.write(",")
                    i += 1
                print("]", end="")
                f.write("]")
            else:
                print(valor.valor, end="")
                f.write(str(valor.valor))
        if self.salto:
            print("\n")
            f.write("\n")
        f.close()
