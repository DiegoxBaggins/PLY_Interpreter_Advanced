from Grammar import parse
from Symbol.Entorno import *

newEnv = Entorno(None)

try:
    print("ingrese direccion de archivo")
    texto = input()
    f = open(texto, "r")
    lectura = f.read()
    ast = parse(lectura)
    for instr in ast:
        instr.execute(newEnv)
except:
    print("Error al ejecutar instrucciones")
