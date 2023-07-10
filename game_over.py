import pygame
import re
from colores import *
from basededatos import *
from nivel_uno import *

pygame.init()

ANCHO = 1200
ALTO = 700

screen = pygame.display.set_mode([ANCHO, ALTO]) #se crea una ventana
pygame.display.set_caption('Mi primer juego')#titulo de la ventana

fondo = pygame.image.load("Recuperar/imagenes/perdiste.png")#llamo a la imagen
fondo = pygame.transform.scale(fondo,(1008,416))


font = pygame.font.SysFont("Arial Narrow", 80)
letra_score = pygame.font.SysFont("Arial Narrow", 30)
pos_puntos = (550,400)

sonido_perder = pygame.mixer.Sound('Recuperar/sonidos/game_over.mp3')



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

def perder(screen):
    sonido_perder.play()
    nombre = ""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif event.key == pygame.K_RETURN and len(nombre) > 0:
                    running = False
                    #pygame.quit()
                    #return nombre
                elif event.key == pygame.K_SPACE:
                    nombre += '_'
                else:
                    letra = event.unicode
                    if validar_string(letra) and len(nombre) < 6:
                        nombre += letra
            #if not running:
        screen.fill(NEGRO)
        screen.blit(fondo,(140,100))
        muestro_nombre(screen, nombre)
        pygame.display.flip()
        
    crear_base_de_datos()
    insertar_nombre_score(nombre,puntos.puntaje)
    ranking()
    pygame.quit()

    #return nombre
#perder(screen)
    
        