import pygame
import re
from colores import *
#from basededatos import *
#from nivel_uno import *

pygame.init()
ancho_ventana = 1200
alto_ventana = 700
imagen_fondo = pygame.image.load("Recuperar/imagenes/username.png")#llamo a la imagen
imagen_fuego = pygame.image.load("Recuperar/imagenes/asd.png")#llamo a la imagen
imagen_fondo = pygame.transform.scale(imagen_fondo,(1008,416)) #cambio el tamaño de la imagen........ si pongo () es para no cambiar el tamaño, [] para cambiar 
imagen_fuego = pygame.transform.scale(imagen_fuego,(228,200)) #cambio el tamaño de la imagen........ si pongo () es para no cambiar el tamaño, [] para cambiar 

font = pygame.font.SysFont("Arial Narrow", 80) #letra y tamaño

screen = pygame.display.set_mode([ancho_ventana, alto_ventana]) #se crea una ventana
pygame.display.set_caption('Mi primer juego')#titulo de la ventana


def validar_string(cadena):
    if type(cadena) == str:
        if re.search('[^a-zA-Z0-9_\-]', cadena):
            resultado = False
        else:
            resultado = True
    else: 
        resultado = False
    return resultado

def muestro_nombre(screen, nombre):
    user = font.render(nombre, 1, BLANCO)
    screen.blit(user, (500,240))
    #return nombre
        

def inicio(screen):

    running = True
    nombre = ""

    while running:

        #fondo de pantalla
        screen.fill(NEGRO)

        #evento para cerrar el juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif event.key == pygame.K_RETURN and len(nombre) > 0:
                    running = False
                    #global nombre_global
                    #nombre_global = nombre
                    return nombre
                elif event.key == pygame.K_SPACE:
                    nombre += '_'
                else:
                    letra = event.unicode
                    if validar_string(letra) and len(nombre) < 6:
                        nombre += letra        

            #elif event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_RETURN:
                    #running = False

        screen.blit(imagen_fondo,(140,100))
        screen.blit(imagen_fuego,(480,490))
        muestro_nombre(screen, nombre)
        #muestro_nombre(screen, nombre)

        
        pygame.display.flip()#muestra los cambios en la pantalla
        #return nombre
#inicio(screen)


