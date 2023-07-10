import pygame

class Nave:
    def __init__(self, vida, pos_nave, x, puntos = 0):
        self.imagen_original = pygame.image.load("naveeee.png").convert_alpha()
        self.pos_nave = pos_nave
        self.imagen = pygame.transform.scale(self.imagen_original, self.pos_nave)
        self.rect = self.imagen.get_rect()
        self.rect.centerx = 1200 / 2
        self.rect.bottom = 700 - 10
        self.x = x
        self.vida = vida
        self.puntos = puntos
        self.disparando = False

        
