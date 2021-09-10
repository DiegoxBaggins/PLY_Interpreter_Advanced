from Abstract.Expresion import *
from Abstract.Return import *


class While(Expresion):
    def __init__(self, condicion, instrucciones, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.condicion = condicion
        self.instrucciones = instrucciones

    def execute(self, entorno):
        condicion = self.condicion.execute(entorno)
        if condicion.tipo != Tipo.BOOLEAN:
            print("La condicion no es bool")
            return
        control = 0
        nuevoEntorno = Entorno(entorno, "WHILE")
        while condicion.valor is True and control < 250:
            rtr = self.instrucciones.execute(nuevoEntorno)
            if rtr is not None:
                return rtr
            condicion = self.condicion.execute(entorno)
            control += 1
