import pygame
from config import *
def tela_final(window):
    over = pygame.image.load('assets/game_over.png').convert() #imagem inicial
    over = pygame.transform.scale(over, (largura,altura)) #definir tamanho da imagem