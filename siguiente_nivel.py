import pygame
from colores import *


pygame.init()

imagen_nivel = pygame.image.load("Recuperar/imagenes/nivel.png")
imagen_nivel = pygame.transform.scale(imagen_nivel,(1008,416))

aplausos = pygame.mixer.Sound('Recuperar/sonidos/aplausos.mp3')

timer_event = pygame.USEREVENT + 0
pygame.time.set_timer(timer_event, 1000)  # Temporizador de 1 segundo

def siguiente(screen):

    aplausos.play()

    running = True

    while running:

        screen.fill(NEGRO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                    
        screen.blit(imagen_nivel,(150,150))
        pygame.display.flip()#muestra los cambios en la pantalla