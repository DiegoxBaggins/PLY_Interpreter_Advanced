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


def imprimirObjeto(objeto, f):
    atributos = objeto.atributos
    tipo = objeto.objeto
    print("Struct:    {")
    print("Tipo: ", tipo, ",")
    f.write("Struct     {\nTipo: " + tipo + "\n")
    llaves = atributos.keys()
    for elemento in llaves:
        valor = atributos.get(elemento)
        print(elemento, ": ", end="")
        f.write(elemento + ": ")
        if valor.tipo == Tipo.ARRAY:
            imprimirlistas(valor.valor, f)
            print()
            f.write("\n")
        elif valor.tipo == Tipo.STRUCT:
            print("struct: ", valor.objeto)
            f.write("struct: " + valor.objeto + "\n")
        else:
            print(valor.valor)
            f.write(str(valor.valor) + "\n")
    print("}", end="")
    f.write("}")


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
            elif valor.tipo == Tipo.STRUCT:
                imprimirObjeto(valor, f)
            else:
                print(valor.valor, end="")
                f.write(str(valor.valor))
        if self.salto:
            print("\n")
            f.write("\n")
        f.close()
