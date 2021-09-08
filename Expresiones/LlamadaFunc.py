from Abstract.Expresion import *
from Abstract.Return import *
from Symbol.Entorno import *


class LlamadaFunc(Expresion):

    def __init__(self, id, params, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.params = params

    def execute(self, entorno):
        try:
            func = entorno.getFunc(self.id)
            if func is not None:
                nuevoEntorno = Entorno(entorno.getGlobal(), self.id)
                for param in self.params:
                    valor = param.execute(entorno)
                    nuevoEntorno.newVariable(param.id, valor.valor, valor.tipo)
                func.instrucciones.execute(nuevoEntorno)
        except:
            print("Error en llamada a funcion")