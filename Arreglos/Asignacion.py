from Abstract.Expresion import *
from Arreglos.Acceso import *
from Abstract.Return import *


class AsignacionArreglo(Expresion):
    def __init__(self, id, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.exp = exp

    def execute(self, entorno):
        if isinstance(self.exp, Return):
            valor = self.exp
        else:
            valor = self.exp.execute(entorno)
        id = self.id.id
        indice = self.id.exp
        if isinstance(id, AccesoArreglo):
            variable = id.execute(entorno)
        else:
            variable = entorno.getVar(id)
        if variable is not None:
            indice = indice.execute(entorno).valor - 1
            if variable.tipo == Tipo.ARRAY:
                tamano = len(variable.valor)
                if tamano > indice >= 0:
                    variable.valor[indice] = valor
                else:
                    print("Indice fuera de rango")
                    entorno.guardarError("Indice fuera de rango", self.linea, self.columna)
            else:
                print("No es un arreglo")
                entorno.guardarError("No es un arreglo", self.linea, self.columna)
        else:
            print("var no existe")
            entorno.guardarError("Variable no existe", self.linea, self.columna)
