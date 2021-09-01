from Grammar import parse
from Symbol.Entorno import *

newEnv = Entorno(None)


f = open("../output.txt", "w")
f.write("")
f.close()
print("ingrese direccion de archivo")
texto = input()

f = open(texto, "r")
lectura = f.read()
f.close()
ast = parse(lectura)
for instr in ast:
    instr.execute(newEnv)