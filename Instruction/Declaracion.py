from Abstract.Expresion import *
from Abstract.Return import *
from enum import Enum


class TipoAcceso(Enum):
    GLOBAL = 0
    LOCAL = 1
    VACIO = 2


class Declaracion(Expresion):
    def __init__(self, acceso, id, valor, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.acceso = acceso
        self.id = id
        self.valor = valor
        self.tipo = tipo

    def chequearTipo(self, valor):
        if self.tipo == Tipo.UNDEFINED:
            self.tipo = valor.tipo
            return True
        else:
            if valor.tipo != self.tipo:
                return False
            else:
                return True

    def execute(self, entorno):
        valor = self.valor.execute(entorno)
        if self.chequearTipo(valor):
            if self.acceso == TipoAcceso.LOCAL:
                if valor.tipo == Tipo.STRUCT:
                    entorno.newVarStructLocal(self.id, valor.valor, valor.auxTipo)
                else:
                    entorno.newVariableLocal(self.id, valor.valor, valor.tipo)
            elif self.acceso == TipoAcceso.GLOBAL:
                if valor.tipo == Tipo.STRUCT:
                    entorno.newVarStructGlobal(self.id, valor.valor, valor.auxTipo)
                else:
                    entorno.newVariableGlobal(self.id, valor.valor, valor.tipo)
            else:
                if valor.tipo == Tipo.STRUCT:
                    entorno.newVarStruct(self.id, valor.valor, valor.auxTipo)
                else:
                    entorno.newVariable(self.id, valor.valor, valor.tipo)
        else:
            print("Error, tipos no coinciden")
