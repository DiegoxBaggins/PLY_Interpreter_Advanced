from Abstract.Expresion import *
from Abstract.Return import *


def comprobarEntorno(entorno):
    env = entorno
    while env is not None:
        if env.nombre == "FOR" or env.nombre == "WHILE":
            return True
        else:
            env = env.prev
    return False


class ControlIns(Expresion):
    def __init__(self, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.tipo = tipo

    def execute(self, entorno):
        if comprobarEntorno(entorno):
            return Return(None, self.tipo, "")
        else:
            print("Error en sentencia de control")
            return None
