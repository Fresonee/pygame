import pygame
from colores import *




pygame.init()

imagen_ganar = pygame.image.load("Recuperar/imagenes/ganaste.png")
imagen_ganar = pygame.transform.scale(imagen_ganar,(1008,416)) 

aplausos = pygame.mixer.Sound('Recuperar/sonidos/aplausos.mp3')

def ganaste(screen):
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
                    pygame.quit()
                    
        screen.blit(imagen_ganar,(150,150))
        pygame.display.flip()#muestra los cambios en la pantalla