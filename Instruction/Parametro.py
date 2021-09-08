from Abstract.Expresion import *


class Parametro(Expresion):
    def __init__(self, id, line, column):
        Expresion.__init__(self, line, column)
        self.id = id

    def execute(self):
        return self
