from Abstract.Expresion import *
from Abstract.Return import *
from enum import Enum
from Arreglos.Asignacion import *


class FuncionArreglo(Enum):
    LENGTH = 0
    PUSH = 1
    POP = 2


class FuncArreglo(Expresion):
    def __init__(self, id, exp, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.exp = exp
        self.tipo = tipo

    def execute(self, entorno):
        if self.tipo == FuncionArreglo.LENGTH:
            if isinstance(self.id, str):
                var = entorno.getVar(self.id)
            else:
                var = self.id.execute(entorno)
            if var.tipo == Tipo.ARRAY:
                return Return(len(var.valor), Tipo.INT)
        elif self.tipo == FuncionArreglo.PUSH:
            exp = self.exp.execute(entorno)
            if isinstance(self.id, str):
                var = entorno.getVar(self.id)
                var.valor.append(exp)
            else:
                var = self.id.execute(entorno)
                var.valor.append(exp)
        elif self.tipo == FuncionArreglo.POP:
            if isinstance(self.id, str):
                var = entorno.getVar(self.id)
                exp = var.valor.pop()
            else:
                var = self.id.execute(entorno)
                exp = var.valor.pop()
            return exp
