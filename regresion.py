import pygame
from colores import *

ANCHO = 1200
ALTO = 700

pygame.init()

#screen = pygame.display.set_mode([ANCHO, ALTO]) #se crea una ventana
#pygame.display.set_caption('Mi primer juego')#titulo de la ventana

font = pygame.font.SysFont("Arial Narrow", 80) #letra y tamaño
timer_event = pygame.USEREVENT + 0
pygame.time.set_timer(timer_event, 1000)  # Temporizador de 1 segundo

def cuenta_regresiva(screen):
    #pygame.init()

    tiempo_inicial = 3
    running = True
    while running:
        screen.fill(NEGRO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == timer_event:
                tiempo_inicial -= 1
            if tiempo_inicial == 0:
                running = False


        texto = font.render(str(tiempo_inicial), True, BLANCO)
        screen.blit(texto, (580,300))
        pygame.display.flip()
    
    #pygame.quit()
#cuenta_regresiva(screen)
                    
