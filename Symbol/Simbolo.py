from Abstract.Return import *


class Simbolo:

    def __init__(self, valor, iden, tipo, objeto=""):
        self.valor = valor
        self.id = iden
        self.tipo = tipo
        self.objeto = objeto
        self.atributos = {}
