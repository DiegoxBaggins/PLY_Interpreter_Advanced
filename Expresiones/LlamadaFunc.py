from Abstract.Expresion import *
from Abstract.Return import *
from Symbol.Entorno import *


class LlamadaFunc(Expresion):

    def __init__(self, id, params, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.params = params

    def execute(self, entorno):
        func = entorno.getFunc(self.id)
        if func is not None:
            nuevoEntorno = Entorno(entorno.getGlobal(), self.id)
            i = 0
            for param in self.params:
                valor = param.execute(entorno)
                nuevoEntorno.newVariable(func.params[i].id, valor.valor, valor.tipo)
                i += 1
            rtr = func.instrucciones.execute(nuevoEntorno)
            if rtr is not None:
                if rtr.tipo == Tipo.RETURNINS:
                    return None
                else:
                    return rtr
        struct = entorno.getStruct(self.id)
        if struct is not None:
            ids = struct.atributos
            attrs = {}
            i = 0
            for id in ids:
                valor = self.params[i].execute(entorno)
                if id.tipo != Tipo.UNDEFINED:
                    if id.tipo == valor.tipo:
                        attrs.update({
                            id.valor: valor
                        })
                    else:
                        print("Error de tipos")
                else:
                    attrs.update({
                        id.valor: valor
                    })
                    i += 1
            return Return(attrs, Tipo.STRUCT, self.id)
