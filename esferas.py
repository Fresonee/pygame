import random
import pygame

#imagenes = ["esfera1.png", "esfera2.png", "esfera3.png", "esfera4.png", "esfera5.png", "esfera6.png", "esfera7.png"]
imagenes = ["Recuperar/imagenes/esfera1.png", "Recuperar/imagenes/esfera2.png", "Recuperar/imagenes/esfera3.png", "Recuperar/imagenes/esfera4.png", "Recuperar/imagenes/esfera5.png", "Recuperar/imagenes/esfera6.png", "Recuperar/imagenes/esfera7.png"]
ANCHO = 1200
ALTO = 700

lista_esferas = []



def genero_esferas(imagenes):
    for _ in range(1):
        nombre_imagen = random.choice(imagenes)
        esfera = Esfera(nombre_imagen)
        lista_esferas.append(esfera)

def muestro_esferas(lista_esferas, screen):
    for esfera in lista_esferas:
        screen.blit(esfera.imagen, esfera.rect)

class Esfera:
    def __init__(self, nombre_imagen):
        self.imagen_original = pygame.image.load(nombre_imagen).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen_original, (70, 70))
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.velocidad = random.randrange(3, 5)

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            self.regenerar()

    def regenerar(self):
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.velocidad = random.randrange(3, 10)
        nueva_imagen = random.choice(imagenes)
        self.imagen_original = pygame.image.load(nueva_imagen).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen_original, (70, 70))


