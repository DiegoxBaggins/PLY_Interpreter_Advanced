from Abstract.Expresion import *


class AccesoStruct(Expresion):
    def __init__(self, id, atributo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.atributo = atributo

    def execute(self, entorno):
        var = None
        if isinstance(self.id, AccesoStruct):
            var = self.id.execute(entorno)
            tp = entorno.getVar(var.auxTipo)
            var = tp
        else:
            var = entorno.getVar(self.id)
        if var is not None:
            if var.atributos.get(self.atributo) is not None:
                rtr = var.atributos.get(self.atributo)
                return rtr
            else:
                print("No existe ese atributo")
        else:
            print("No existe la variable")
