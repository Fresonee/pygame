import pygame
from jugadores import *
from colores import *
from meteoritos import *
from funciones import *
from funciones import lista_jugadores
from contadores import *
from game_over import perder
from esferas import *
from basededatos import pantalla_puntajes
import random


pygame.init()
#nivel = pygame.display.set_mode([1200, 700]) #se crea una ventana
#pygame.display.set_caption('Mi primer juego')#titulo de la ventana

ANCHO = 1200
ALTO = 700
mitad = ANCHO / 2

posicion_puntos = (600,10)
posicion_vidas = (10,10)
pos_esferas = (1000,10)

tamaño = (50,50)
tamaño_grande = (100,100)

#---JUGADOR---

player = Jugador(3,mitad,ANCHO,ALTO)
lista_jugadores.append(player)



def nivel_uno(screen, ANCHO, ALTO, player):

    clock = pygame.time.Clock()  
    pos_estrellas(70, ANCHO, ALTO)
    creo_meteoritos(5,tamaño)
    creo_explosion()
    genero_esferas(imagenes)
    
    
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        
        screen.fill(NEGRO)

        #Muestro las estrellas en pantalla
        muestro_estrellas(estrellas, screen, BLANCO, ALTO)
        
        #Muestro el personaje en pantalla
        muestro_personaje(lista_jugadores,screen,player)
        
        #Muestro las balas en pantalla
        muestro_balas(lista_balas,screen)

        #Muestro los meteoritos en pantalla
        muestro_meteoritos(lista_meteoritos,screen)

        #Colisiones
        bala_colision_meteorito()
        player_colision_meteorito()

        #Muestro explosion en pantalla
        muestro_explosion(screen)

        for esfera in lista_esferas:
            esfera.update()
        
        #Muestro las esferas en pantalla
        muestro_esferas(lista_esferas,screen)

        #Colision
        player_colision_esfera()



        mostrar_puntuacion(screen,'Score: ', puntos.puntaje, posicion_puntos)
        mostrar_puntuacion(screen,'Vidas: ', puntos.vida, posicion_vidas)
        mostrar_puntuacion_esferas(screen,'Esfera: ', puntos.esferas, pos_esferas)


        if puntos.vida == 0:
            perder(screen)
            pantalla_puntajes(screen)
            running = False
        elif puntos.esferas == 7:
            running = False


        pygame.display.flip()#muestra los cambios en la pantalla

        clock.tick(60)
#nivel_uno()
    

