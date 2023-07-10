import pygame

class Balaa:
    def __init__(self,x,y):
        self.imagen_original = pygame.image.load("Recuperar/imagenes/bala.png")
        self.imagen = pygame.transform.scale(self.imagen_original, (20,40))
        self.rect = self.imagen.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.velocidad = -7
    def update(self):
        self.rect.y += self.velocidad