import pygame

class Contador:
    def __init__(self, puntaje, vida, esferas):
        self.puntaje = puntaje
        self.vida = vida
        self.esferas = esferas

    def __iadd__(self, other):
        if isinstance(other, int):
            self.puntaje += other
            self.vida += other
            self.esferas += other
            return self
        else:
            raise TypeError("Operación no válida")