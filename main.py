import pygame
from pantalla_i import *
from nombre_user import *
from regresion import cuenta_regresiva
from nivel_uno import *
from colores import *
from siguiente_nivel import *
from nivel_dos import *
from basededatos import *

ANCHO = 1200
ALTO = 700


pygame.init()

screen = pygame.display.set_mode([ANCHO, ALTO]) #se crea una ventana
pygame.display.set_caption('Dragons Sphere Chase: Meteorite Edition ')#titulo de la ventana

timer_event = pygame.USEREVENT + 0
pygame.time.set_timer(timer_event, 1000)  # Temporizador de 1 segundo


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pantalla_inicial(screen)
    cuenta_regresiva(screen) 
    nivel_uno(screen, ANCHO, ALTO, player)
    siguiente(screen)
    nivel_dos(screen)

    
    pygame.display.flip()

pygame.quit() #fin





