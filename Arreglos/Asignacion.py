from Abstract.Expresion import *
from Arreglos.Acceso import *


def asignarAtras(acceso, exp, entorno):
    id = acceso.id
    if isinstance(id, AccesoArreglo):
        variable = id.execute(entorno)
        indice = acceso.exp.execute(entorno).valor - 1
        variable.valor[indice] = exp
        exp = variable
        asignarAtras(id, exp, entorno)
    else:
        var = entorno.getVar(id)
        indice = acceso.exp.execute(entorno).valor - 1
        var.valor[indice] = exp
        entorno.newVariable(var.id, var.valor, var.tipo)


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
        asignarAtras(self.id, valor, entorno)

