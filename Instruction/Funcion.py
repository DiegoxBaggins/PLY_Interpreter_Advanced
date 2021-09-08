from Abstract.Expresion import *


class Function(Expresion):
    def __init__(self, id, params, instr, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.params = params
        self.instrucciones = instr

    def execute(self, entorno):
        try:
            entorno.newFunc(self.id, self)
        except:
            print("Error al guardar funcion")
