import pygame
from colores import *


pygame.init()

ancho_ventana = 1200
alto_ventana = 700
imagen_fondo = pygame.image.load("Recuperar/imagenes/inicio.png")#llamo a la imagen
imagen_fondo = pygame.transform.scale(imagen_fondo,(1200,700)) #cambio el tamaño de la imagen........ si pongo () es para no cambiar el tamaño, [] para cambiar 
screen = pygame.display.set_mode([ancho_ventana, alto_ventana]) #se crea una ventana
pygame.display.set_caption('Mi primer juego')#titulo de la ventana

sonido_inicio = pygame.mixer.Sound('Recuperar/sonidos/sonido_inicial.mp3')

def pantalla_inicial(screen):

    running = True
    #cuenta_regresiva_mostrar = False

    while running:
        
        sonido_inicio.play()
        #fondo de pantalla
        screen.fill(NEGRO)

        #evento para cerrar el juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                    #cuenta_regresiva_mostrar = True
                    #cuenta_regresiva(screen)
        screen.blit(imagen_fondo,(80,50))
        
        pygame.display.flip()#muestra los cambios en la pantalla
