from meteoritos import *
from jugadores import *
from explosion import *
from contadores import *
from esferas import *

lista_contador = []
puntos = Contador(0,3,0)
lista_contador.append(puntos)

sonido_esfera = pygame.mixer.Sound('Recuperar/sonidos/sonido_burbuja.mp3')




#---JUGADOR---
lista_jugadores = []
def muestro_personaje(lista,screen,player):
    for player in lista:
        player.update()
        player.draw(screen)

#---BALAS---
def muestro_balas(lista,screen):
    for bala in lista:
        bala.update()
        screen.blit(bala.imagen, bala.rect)

#---METEORITOS---
lista_meteoritos = []
lista_meteoritos_diagonal = []

def creo_meteoritos(z,tamaño):
    for i in range(z):
        meteorito = Meteorito(tamaño)
        lista_meteoritos.append(meteorito)


def muestro_meteoritos(lista,screen):
    for meteorito in lista:
        screen.blit(meteorito.imagen, meteorito.rect)
        meteorito.update()

def creo_meteoritos_diagonal(z, tamaño):
    for i in range(z):
        meteorito_diagonal = Meteorito(tamaño)
        meteorito_diagonal.velocidad_x = random.choice([1, 1]) * random.uniform(1, 1)
        meteorito_diagonal.velocidad_y = random.uniform(1, 2)
        lista_meteoritos_diagonal.append(meteorito_diagonal)

def update_diagonal(lista_meteoritos_diagonal):
    for meteorito_diagonal in lista_meteoritos_diagonal:
        if meteorito_diagonal.rect.top > ALTO + 10 or meteorito_diagonal.rect.left < -25 or meteorito_diagonal.rect.right > ANCHO + 25:
            meteorito_diagonal.regenerar()

def muestro_meteoritos_diagonal(lista,screen):
    for meteorito_diagonal in lista:
        screen.blit(meteorito_diagonal.imagen, meteorito_diagonal.rect)
        meteorito_diagonal.rect.x += meteorito_diagonal.velocidad_x
        meteorito_diagonal.rect.y += meteorito_diagonal.velocidad
        if meteorito_diagonal.rect.top > ALTO + 10 or meteorito_diagonal.rect.left <-25 or meteorito_diagonal.rect.right > ANCHO + 25:
            #meteorito.rect.x = random.randrange(ANCHO - meteorito.rect.ancho)
            meteorito_diagonal.rect.y = random.randrange(-350, -40)
            meteorito_diagonal.velocidad = random.randrange(1,5)
            meteorito_diagonal.update()



#-------------ESTRELLAS------------------
estrellas = []  # Lista para almacenar las posiciones de las estrellas
velocidad_estrellas = 0.5

def pos_estrellas(n,ANCHO,ALTO):
    for _ in range(n):
        x = random.randint(0, ANCHO)
        y = random.randint(0, ALTO)
        estrellas.append([x, y])

def muestro_estrellas(lista,screen,BLANCO, ALTO):
    for estrella in lista:
        x, y = estrella
        pygame.draw.circle(screen, BLANCO, (x, y), 1)
        estrella[1] += velocidad_estrellas
        if estrella[1] > ALTO:
            estrella[1] = 0

#---COLISIONES---
def bala_colision_meteorito():
    for bala in lista_balas:
        for meteorito in lista_meteoritos:
            if bala.rect.colliderect(meteorito.rect):
                explosion = Explosiones(meteorito.rect.center)
                explosiones.append(explosion)
                lista_balas.remove(bala)
                for puntos in lista_contador:
                    puntos.puntaje += 10
                meteorito.regenerar()
def bala_colision_meteorito_diagonal():
    for bala in lista_balas:
        for meteorito_diagonal in lista_meteoritos_diagonal:
            if bala.rect.colliderect(meteorito_diagonal.rect):
                explosion = Explosiones(meteorito_diagonal.rect.center)
                explosiones.append(explosion)
                lista_balas.remove(bala)
                for puntos in lista_contador:
                    puntos.puntaje += 10
                meteorito_diagonal.regenerar()
                

esfera_colisionada = []

def player_colision_esfera():
    for player in lista_jugadores:
        for esfera in lista_esferas:
            if player.rect.colliderect(esfera.rect):
                sonido_esfera.play()
                if esfera.imagen_original not in esfera_colisionada:
                    for puntos in lista_contador:
                        puntos.puntaje += 25
                        puntos.esferas += 1
                    esfera_colisionada.append(esfera.imagen_original.copy())
                    esfera.regenerar()

def player_colision_meteorito():
    for player in lista_jugadores:
        for meteorito in lista_meteoritos:
            if player.rect.colliderect(meteorito.rect):
                explosion = Explosiones(meteorito.rect.center)
                explosiones.append(explosion)
                puntos.vida += -1
                meteorito.regenerar()

def player_colision_meteorito_diagonal():
    for player in lista_jugadores:
        for meteorito_diagonal in lista_meteoritos_diagonal:
            if player.rect.colliderect(meteorito_diagonal.rect):
                explosion = Explosiones(meteorito_diagonal.rect.center)
                explosiones.append(explosion)
                puntos.vida += -1
                meteorito_diagonal.regenerar()

#---EXPLOSIONES---
def muestro_explosion(screen):
    for explosion in explosiones:
        screen.blit(explosion.image, explosion.rect)
        explosion.update()

#---SCORE---
def mostrar_puntuacion(surface, palabra, clave, posicion):
    font = pygame.font.SysFont('serif', 25)
    text_surface = font.render(palabra + str(clave), True, BLANCO)
    surface.blit(text_surface, posicion)

def mostrar_puntuacion(surface, palabra, clave, posicion):
    font = pygame.font.SysFont('serif', 25)
    text_surface = font.render(palabra + str(clave), True, BLANCO)
    surface.blit(text_surface, posicion)

def mostrar_puntuacion_esferas(surface, palabra, clave, posicion):
    font = pygame.font.SysFont('serif', 25)
    texto = f"{palabra} {clave}/7"
    text_surface = font.render(texto, True, BLANCO)
    surface.blit(text_surface, posicion)

def mover_meteorito_diagonal(meteorito):
    meteorito.rect.x += meteorito.velocidad
    meteorito.rect.y += meteorito.velocidad
    if meteorito.rect.right < 0 or meteorito.rect.left > ANCHO or meteorito.rect.top > ALTO:
        meteorito.regenerar()
