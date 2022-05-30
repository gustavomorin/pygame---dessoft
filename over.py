import pygame
from config import *
def tela_final(window):

    over = pygame.image.load('assets/game_over.png').convert() #imagem inicial
    over = pygame.transform.scale(over, (largura,altura)) #definir tamanho da imagem
    clock = pygame.time.Clock()
    status = OVER
    while status == OVER:
        clock.tick(FPS)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                status = QUIT

        window.blit(over, (0, 0))
        pygame.display.update()
    return status
