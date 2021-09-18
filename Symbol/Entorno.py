from enum import Enum
from Abstract.Expresion import *
from Symbol.Simbolo import *
from Instruction.Declaracion import *
from datetime import datetime


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
        self.simbols = []
        self.errors = []

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

    def guardarTS(self, id, linea, columna, clas):
        env = self.getGlobal()
        simbol = TablaS(id, clas, self.nombre, linea, columna)
        var = None
        if isinstance(clas, Enum):
            tp = clas.name
        else:
            tp = clas
        for elemento in env.simbols:
            if elemento[0] == id and elemento[1] == tp and elemento[2] == self.nombre and elemento[3] == linea:
                var = elemento
        if var is None:
            env.simbols.append(simbol)

    def guardarError(self, descripcion, linea, columna):
        now = datetime.now()
        env = self.getGlobal()
        num = len(env.errors) + 1
        fecha = now.strftime("%d/%m/%Y %H:%M:%S")
        error = Error(num, descripcion, linea, columna, fecha)
        env.errors.append(error)


def TablaS(id, tipo, ambito, linea, columna):
    if isinstance(tipo, Enum):
        tp = tipo.name
    else:
        tp = tipo
    return [id, tp, ambito, linea, columna]


def Error(num, descripcion, linea, columna, fecha):
    return [num, descripcion, linea, columna, fecha]
