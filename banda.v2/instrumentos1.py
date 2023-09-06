class Instrumento:
    def afinar(self):
        pass
    def tocar(self):
        pass

class Guitarra(Instrumento):
    def afinar(self):
        print("esta afinando su Guitarra...")
    def tocar(self):
        print("esta tocando su Guitarra!")



class Bajo(Instrumento):
    def afinar(self):
        print("esta afinando su Bajo...")
    def tocar(self):
        print("esta tocando su bajo!")



class Piano (Instrumento):
    def afinar(self):
        print("no se necesita afinar su Piano...")
    def tocar(self):
        print("esta tocando su Piano!")

class Bateria (Instrumento):
    def afinar(self):
        print("armando y afinando su bateria...")
    def tocar(self):
        print("esta tocando su bateria!")


class Trompeta(Instrumento):
    def afinar(self):
        print("esta afinando su trompeta...")
    def tocar(self):
        print("esta tocando su Trompeta!")



class Tuba(Instrumento):
    def afinar(self):
        print("esta afinando su Tuba...")
    def tocar(self):
        print("esta tocando su Tuba!")



class Acordeon(Instrumento):
    def afinar(self):
        print("esta afinando su Acordeon...")
    def tocar(self):
        print("esta tocando su Acordeon!")