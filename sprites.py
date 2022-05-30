import pygame
import random
from config import *
class Luva(pygame.sprite.Sprite):

    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = x
        self.rect.centery = y


    def update(self):
        pass

class Bola(pygame.sprite.Sprite):
    def __init__(self, img, x, y, tx, ty, sinal):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = img
        self.image = img
        self.rect = self.image.get_rect()

        self.rect.x=x
        self.rect.y=y

        self.troca_vel = True
        self.sinal = sinal
        self.d_x = random.randint(-15, 15)
        self.d_y = random.randint(-15,15)
        self.profundidade = 50
        
#(self.sinal*(self.d_x**2+100)**(1/2))
    def update(self):
        self.profundidade += 1
        c = self.rect
        self.image = pygame.transform.scale(self.image_original, (2*self.profundidade, 2*self.profundidade))
        self.rect = self.image.get_rect()
        self.rect = c
        self.rect.x += self.d_x
        self.rect.y += self.d_y
        self.troca_vel = False

        if self.rect.x>=largura or self.rect.x < 0 or self.rect.y >= altura or self.rect.y < 0:
            self.kill()
