from Abstract.Expresion import *
from Abstract.Return import *


def imprimirlistas(lista):
    string = ""
    string += "["
    i = 1
    for elemento in lista:
        if elemento.tipo == Tipo.ARRAY:
            string += imprimirlistas(elemento.valor)
        elif elemento.tipo == Tipo.STRUCT:
            string += imprimirObjeto(elemento)
        else:
            string += str(elemento.valor)
        if i != len(lista):
            string += ","
        i += 1
    string += "]"
    return string


def imprimirObjeto(objeto):
    string = " "
    atributos = objeto.atributos
    tipo = objeto.objeto
    string += "Struct     {\nTipo: " + tipo + "\n"
    llaves = atributos.keys()
    for elemento in llaves:
        valor = atributos.get(elemento)
        string += elemento + ": "
        if valor.tipo == Tipo.ARRAY:
            string += imprimirlistas(valor.valor) + "\n"
        elif valor.tipo == Tipo.STRUCT:
            string += "struct: " + valor.objeto + "\n"
        else:
            string += str(valor.valor) + "\n"
    string += "}"
    return string


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
                recibido = imprimirlistas(valor.valor)
                print(recibido, end="")
                f.write(recibido)
            elif valor.tipo == Tipo.STRUCT:
                recibido = imprimirObjeto(valor)
                print(recibido, end="")
                f.write(recibido)
            else:
                print(valor.valor, end="")
                f.write(str(valor.valor))
        if self.salto:
            print("\n")
            f.write("\n")
        f.close()
            #print("Error en print")
            #entorno.guardarError("Error en print", self.linea, self.columna)
