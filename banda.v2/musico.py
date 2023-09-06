from instrumentos1 import *
class Musico:
    def __init__(self,instrumento):
        self.instrumento = instrumento
    def tocar_instrumento(self):
        self.instrumento.tocar()
    def afinar_instrumento(self):
        self.instrumento.afinar()
        