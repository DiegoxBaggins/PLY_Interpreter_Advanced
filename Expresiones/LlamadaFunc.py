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
                i = 0
                for param in self.params:
                    valor = param.execute(entorno)
                    nuevoEntorno.newVariable(func.params[i].id, valor.valor, valor.tipo)
                    i += 1
                ret = func.instrucciones.execute(nuevoEntorno)
                if ret is not None:
                    return ret
        except:
            print("Error en llamada a funcion")