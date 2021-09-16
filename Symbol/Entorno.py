from Symbol.Simbolo import *


def copiarArreglo(arreglo):
    arregloNuevo = []
    for elemento in arreglo:
        valor = elemento.valor
        if isinstance(valor, list):
            valor = copiarArreglo(valor)
        else:
            valor = elemento
        arregloNuevo.append(valor)
    return Return(arregloNuevo, Tipo.ARRAY)


class Entorno:

    def __init__(self, prev, nombre):
        self.nombre = nombre
        self.prev = prev
        self.variables = {}
        self.funciones = {}
        self.structs = {}

    def newVariableGlobal(self, idVar, valor, tipo):
        if isinstance(valor, list):
            nuevo = copiarArreglo(valor)
            valor = nuevo.valor
        nuevoSimbolo = Simbolo(valor, idVar, tipo)
        glb = self.getGlobal()
        glb.variables[idVar] = nuevoSimbolo

    def newVariableLocal(self, idVar, valor, tipo):
        if isinstance(valor, list):
            nuevo = copiarArreglo(valor)
            valor = nuevo.valor
        nuevoSimbolo = Simbolo(valor, idVar, tipo)
        self.variables[idVar] = nuevoSimbolo

    def newVariable(self, idVar, valor, tipo):
        if isinstance(valor, list):
            nuevo = copiarArreglo(valor)
            valor = nuevo.valor
        env = self
        nuevoSimbolo = Simbolo(valor, idVar, tipo)
        while env.prev is not None:
            if idVar in env.variables.keys():
                env.variables[idVar] = nuevoSimbolo
                return
            env = env.prev
        self.variables[idVar] = nuevoSimbolo

    def newVarStructGlobal(self, idVar, obj):
        glb = self.getGlobal()
        glb.variables[idVar] = obj

    def newVarStructLocal(self, idVar, obj):
        self.variables[idVar] = obj

    def newVarStruct(self, idVar, obj):
        env = self
        while env.prev is not None:
            if idVar in env.variables.keys():
                env.variables[idVar] = obj
                return
            env = env.prev
        self.variables[idVar] = obj

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
