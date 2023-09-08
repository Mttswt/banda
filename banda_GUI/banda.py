from instrumentos1 import *
from musico import *
from random import choice, randint
class Banda:
    def __init__(self):
        self.instrumentos = [Guitarra(),Bajo(),Piano(),Bateria(),Trompeta(),Tuba(),Acordeon()]
        self.musicos = []

    def asignar_instrumento(self,):
        return choice (self.instrumentos)
    def crear_banda(self):
        cant = randint(0,5)
        for i in range(cant):
            self.musicos.append(Musico(self.asignar_instrumento()))

    def afinar_banda(self):
        for m in self.musicos:
            m.afinar_instrumento()
    def tocar_banda(self):
        for e in self.musicos:
            e.tocar_instrumento()
