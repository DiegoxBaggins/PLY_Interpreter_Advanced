from Abstract.Expresion import *
from enum import Enum


class TipoStruct(Enum):
    NOMUTABLE = 0
    MUTABLE = 1


class NuevoStruct(Expresion):
    def __init__(self, tipo, id, atributos, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.tipo = tipo
        self.id = id
        self.atributos = atributos

    def execute(self, entorno):
        if entorno.getStruct(self.id) is None:
            entorno.newStruct(self.id, self)
            entorno.guardarTS(self.id, self.linea, self.columna, "Struct " + self.tipo.name)
        else:
            print("Struct " + self.id + "repetida")
            entorno.guardarError("Struct " + self.id + "repetida", self.linea, self.columna)
