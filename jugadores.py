import pygame
from balas import Balaa

lista_balas = []
sonido_disparo = pygame.mixer.Sound('Recuperar/sonidos/disparo.wav')


class Jugador:
    def __init__(self, vida,x, ANCHO, ALTO) -> None:
        self.imagen_original = pygame.image.load("Recuperar/imagenes/naveeee.png")
        self.pos_nave = (180,132)
        self.imagen = pygame.transform.scale(self.imagen_original, self.pos_nave)
        self.rect = self.imagen.get_rect()
        #self.rect.center = [x,y]
        self.rect.centerx = ANCHO / 2
        self.rect.bottom = ALTO - 10
        self.x = x
        self.vida = vida
        self.disparando = False

    def update(self):

        lista_teclas = pygame.key.get_pressed()

        if lista_teclas[pygame.K_RIGHT]:
            self.x += 5
            
        if lista_teclas[pygame.K_LEFT]:
            self.x -= 5
            
        self.rect.centerx = self.x

        if lista_teclas[pygame.K_SPACE] and not self.disparando:
            self.disparando = True
            self.disparar()
            sonido_disparo.play()
        elif not lista_teclas[pygame.K_SPACE]:
            self.disparando = False

        if self.rect.right > 1200:
            self.rect.right = 1200
        if self.rect.left < 0:
            self.rect.left = 0

    def draw(self, screen):
        screen.blit(self.imagen, self.rect)
    
    def disparar(self):
        bala = Balaa(self.rect.centerx, self.rect.top)
        lista_balas.append(bala)
