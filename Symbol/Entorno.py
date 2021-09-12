from Symbol.Simbolo import *


class Entorno:

    def __init__(self, prev, nombre):
        self.nombre = nombre
        self.prev = prev
        self.variables = {}
        self.funciones = {}
        self.structs = {}

    def newVariableGlobal(self, idVar, valor, tipo):
        nuevoSimbolo = Simbolo(valor, idVar, tipo)
        glb = self.getGlobal()
        glb.variables[idVar] = nuevoSimbolo

    def newVariableLocal(self, idVar, valor, tipo):
        nuevoSimbolo = Simbolo(valor, idVar, tipo)
        self.variables[idVar] = nuevoSimbolo

    def newVariable(self, idVar, valor, tipo):
        env = self
        nuevoSimbolo = Simbolo(valor, idVar, tipo)
        while env.prev is not None:
            if idVar in env.variables.keys():
                env.variables[idVar] = nuevoSimbolo
                return
            env = env.prev
        self.variables[idVar] = nuevoSimbolo

    def newVarStructGlobal(self, idVar, attrs, tipo):
        nuevoSimbolo = Simbolo(None, idVar, Tipo.STRUCT, tipo)
        nuevoSimbolo.atributos = attrs
        glb = self.getGlobal()
        glb.variables[idVar] = nuevoSimbolo

    def newVarStructLocal(self, idVar, attrs, tipo):
        nuevoSimbolo = Simbolo(None, idVar, Tipo.STRUCT, tipo)
        nuevoSimbolo.atributos = attrs
        self.variables[idVar] = nuevoSimbolo

    def newVarStruct(self, idVar, attrs, tipo):
        env = self
        nuevoSimbolo = Simbolo(None, idVar, Tipo.STRUCT, tipo)
        nuevoSimbolo.atributos = attrs
        while env.prev is not None:
            if idVar in env.variables.keys():
                env.variables[idVar] = nuevoSimbolo
                return
            env = env.prev
        self.variables[idVar] = nuevoSimbolo

    def newFunc(self, idFunc, function):
        if idFunc in self.funciones.keys():
            print("Función repetida")
        else:
            self.funciones[idFunc] = function

    def newStruct(self, idStruct, struct):
        if idStruct in self.structs.keys():
            print("Struct repetido")
        else:
            self.structs[idStruct] = struct

    def getVar(self, idVar):
        env = self
        while env is not None:
            if idVar in env.variables.keys():
                return env.variables[idVar]
            env = env.prev
        return None

    def getFunc(self, idFunc):
        env = self
        while env is not None:
            if idFunc in env.funciones.keys():
                return env.funciones[idFunc]
            env = env.prev
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
