import pygame

explosion_anim = []
explosion_anim_diagonal = []
explosiones = []
explosiones_diagonal = []
def creo_explosion():
    for i in range(6):
        file = "explosion{}.png".format(i)
        img = pygame.image.load(file).convert_alpha()
        img_scale = pygame.transform.scale(img, (70,70))
        explosion_anim.append(img_scale)

def creo_explosion_diagonal():
    for i in range(6):
        file = "explosion{}.png".format(i)
        img = pygame.image.load(file).convert_alpha()
        img_scale = pygame.transform.scale(img, (70,70))
        explosion_anim_diagonal.append(img_scale)

class Explosiones:
    def __init__(self, centro):
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = centro
        self.frame = 0
        self.last_update = pygame.time.get_ticks() #tiempo transcurrido para saber cuando ejecuto la animacion
        self.frame_rate = 30 #velocidad de explosion
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                explosiones.remove(self)
            else:
                centro = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = centro