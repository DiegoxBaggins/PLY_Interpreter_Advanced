from Abstract.Expresion import *
from Structs.Nuevo import *


class AsignacionStruct(Expresion):
    def __init__(self, id, atributo, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.atributo = atributo
        self.exp = exp

    def execute(self, entorno):
        valor = self.exp.execute(entorno)
        variable = entorno.getVar(self.id)
        if variable is not None:
            struct = entorno.getStruct(variable.objeto)
            if struct.tipo == TipoStruct.MUTABLE:
                atributo = variable.atributos.get(self.atributo)
                if atributo is not None:
                    variable.atributos[self.atributo] = valor
                else:
                    print("Struct no cuenta con este atributo")
            else:
                print("El struct no es mutable")
        else:
            print("var no existe")
