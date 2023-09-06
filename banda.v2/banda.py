from musico import *
import random

def crear_banda(num_musicos):
    banda = []
    for i in range(num_musicos):
        nombre_musico = f"Músico-{i + 1}"
        musico = Musico(nombre_musico)
        banda.append(musico)
    return banda