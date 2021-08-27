from Symbol.Simbolo import *


class Entorno:

    def __init__(self, prev):
        self.prev = prev
        self.variables = {}
        self.funciones = {}
        self.structs = {}

    def newVariable(self, idVar, valor, tipoVar):
        env = self
        nuevoSimbolo = Simbolo(valor, idVar, tipoVar)
        while env is not None:
            if idVar in env.variables.keys():
                self.variables[idVar] = nuevoSimbolo
                return
            env = env.prev
        self.variables[idVar] = nuevoSimbolo

    def newVarStruct(self, idVar, attrs, tipo):
        env = self
        newSymbol = Simbolo(None, idVar, Tipo.STRUCT, tipo)
        newSymbol.attributes = attrs
        while env is not None:
            if idVar in env.variables.keys():
                env.variables[idVar] = newSymbol
                return
            env = env.prev
        self.variables[idVar] = newSymbol

    def newFunc(self, idFunc, function):
        if idFunc in self.funciones.keys():
            print("Función repetida")
        else:
            self.funciones[idFunc] = function

    def newStruct(self, idStruct, attr):
        if idStruct in self.structs.keys():
            print("Struct repetido")
        else:
            self.structs[idStruct] = attr

    def getVar(self, idVar):
        env = self
        while env is not None:
            if idVar in env.variables.keys():
                return env.variables[idVar]
            env = env.prev
        return None

    def getFunc(self, idFunc):
        if idFunc in self.funciones.keys():
            return self.funciones[idFunc]
        else:
            return None

    def getStruct(self, idStruct):
        env = self
        while env is not None:
            if idStruct in env.structs.keys():
                return env.structs[idStruct]
            env = env.prev
        return None

    def getGlobal(self):
        env = self
        while env.prev is not None:
            env = env.prev
        return env
