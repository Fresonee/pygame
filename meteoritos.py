import pygame
import random
from colores import *

#tamaño = (50,50)
ANCHO = 1200
ALTO = 700

class Meteorito:
    def __init__(self,tamaño):
        self.imagen_original = pygame.image.load("Recuperar/imagenes/meteorito.png").convert()
        self.tamaño = tamaño
        self.imagen = pygame.transform.scale(self.imagen_original, tamaño)
        self.rect = self.imagen.get_rect()
        self.imagen.set_colorkey(NEGRO)
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(-350, -40)
        self.velocidad = random.randrange(1,5)
        self.velocidad_x = random.choice([-1, 1]) * random.uniform(1, 5)
        self.velocidad_y = self.velocidad

    def update(self):
        self.rect.y += self.velocidad
        #self.rect.x += self.velocidad_x
        if self.rect.top > ALTO:
        #if self.rect.top > ALTO + 10 or self.rect.left < -25 or self.rect.right > ANCHO + 25:
            self.regenerar()
    
    def regenerar(self):
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(-300, -100)
        self.velocidad = random.randrange(3,10)