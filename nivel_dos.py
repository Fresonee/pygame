import pygame
from nivel_uno import *
from funciones import creo_meteoritos_diagonal
from ganar import ganaste

pygame.init()

tamaño = (50,50)
tamaño_grande = (100,100)
def nivel_dos(screen):

    puntos.vida = 3
    puntos.esferas = 0
    

    pos_estrellas(70, ANCHO, ALTO)
    creo_meteoritos(1,tamaño)
    creo_meteoritos(1, tamaño_grande)
    creo_meteoritos_diagonal(3, tamaño)
    creo_explosion()
    genero_esferas(imagenes)
    
    meteorito = Meteorito(tamaño)

    clock = pygame.time.Clock()  


    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        
        screen.fill(NEGRO)

        #Muestro Estrellas
        muestro_estrellas(estrellas, screen, VIOLETA, ALTO)

        #Muestro Personaje
        muestro_personaje(lista_jugadores,screen,player)

        #Muestro Balas
        muestro_balas(lista_balas,screen)

        #Muestro Meteoritos
        muestro_meteoritos(lista_meteoritos,screen)
        muestro_meteoritos_diagonal(lista_meteoritos_diagonal,screen)
        update_diagonal(lista_meteoritos_diagonal)

        #Colisiones
        bala_colision_meteorito()
        player_colision_meteorito()
        bala_colision_meteorito_diagonal()
        player_colision_esfera()
        player_colision_meteorito_diagonal()

        #Muestro Explosion
        muestro_explosion(screen)
        
        #Muesto Esferas
        muestro_esferas(lista_esferas,screen)

        for esfera in lista_esferas:
            esfera.update()

        mostrar_puntuacion(screen,'Score: ', puntos.puntaje, posicion_puntos)
        mostrar_puntuacion(screen,'Vidas: ', puntos.vida, posicion_vidas)
        mostrar_puntuacion_esferas(screen,'Esfera: ', puntos.esferas, pos_esferas)


        if puntos.vida == 0:
            perder(screen)
            pantalla_puntajes(screen)
            running = False

        elif puntos.esferas == 7:
            ganaste(screen)
            running = False
        
        
        pygame.display.flip()#muestra los cambios en la pantalla
        clock.tick(60)




