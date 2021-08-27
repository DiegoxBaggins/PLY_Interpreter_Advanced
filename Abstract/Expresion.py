from abc import ABC, abstractmethod
from Symbol.Entorno import *


class Expresion(ABC):

    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna

        @abstractmethod
        def execute(self, entorno):
            pass
