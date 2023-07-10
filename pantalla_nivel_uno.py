import pygame
from colores import *
import random

pygame.init()

estrellas = []  # Lista para almacenar las posiciones de las estrellas
velocidad_estrellas = 0.01

def pos_estrellas(n,ANCHO,ALTO):
    for _ in range(n):
        x = random.randint(0, ANCHO)
        y = random.randint(0, ALTO)
        estrellas.append([x, y])
def dibujar_estrellas(lista,screen,BLANCO, ALTO):
    for estrella in lista:
        x, y = estrella
        pygame.draw.circle(screen, BLANCO, (x, y), 1)
        estrella[1] += velocidad_estrellas
        if estrella[1] > ALTO:
            estrella[1] = 0