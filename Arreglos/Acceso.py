from Abstract.Expresion import *


class AccesoArreglo(Expresion):
    def __init__(self, id, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.exp = exp

    def execute(self, entorno):
        var = None
        if isinstance(self.id, AccesoArreglo):
            var = self.id.execute(entorno)
        else:
            var = entorno.getVar(self.id)
        if var is not None:
            indice = self.exp.execute(entorno).valor - 1
            tamano = len(var.valor)
            if tamano > indice >= 0:
                rtr = var.valor[indice]
                return rtr
            else:
                print("Indice fuera de rango")
        else:
            print("No existe la variable")
