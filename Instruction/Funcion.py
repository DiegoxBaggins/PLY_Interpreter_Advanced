from Abstract.Expresion import *


class Function(Expresion):
    def __init__(self, id, params, instr, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.params = params
        self.instrucciones = instr

    def execute(self, entorno):
        func = entorno.getFunc(self.id)
        if func is None:
            entorno.newFunc(self.id, self)
            entorno.guardarTS(self.id, self.linea, self.columna, "Funcion")
        else:
            print("Funcion " + self.id + "repetida")
            entorno.guardarError("Funcion " + self.id + "repetida", self.linea, self.columna)
