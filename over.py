import pygame
from config import *
from util import *
from game import *

def tela_final(window):
    over = pygame.image.load('assets/game_over.png').convert() #imagem inicial
    over = pygame.transform.scale(over, (largura,altura)) #definir tamanho da imagem
    clock = pygame.time.Clock()
    status = OVER
    font = pygame.font.SysFont(None, 70) #fonte
    som_final = pygame.mixer.music.load('assets/final.mp3')
    pygame.mixer.music.set_volume(2)
    pygame.mixer.music.play(1)
    recorde = 1
    a = str(recorde)
    texto(window, font, a , branco, largura/2, altura/2)
    while status == OVER:
        clock.tick(FPS)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                status = QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0] #pega a posicao do x (mouse)
                y =  pygame.mouse.get_pos()[1] #pega a posicao do y (mouse)
                if x > 500 and y > 450 and x < 1000 and y < 550:
                    status = SELECT_COUNTRY
                    som_inicial = pygame.mixer.music.load('assets\E-A-Gambazada-Viverá-a-Chorar-●-Letras-●-Mancha-alvi-Verde.mp3')
                    pygame.mixer.music.set_volume(0.8)
                    pygame.mixer.music.play(-1)
        window.blit(over, (0, 0))
        #botao
        pygame.draw.rect(window,verde , [500, 450, 500, 100])
        #texto no botao
        texto(window, font, 'Jogar novamente', branco, largura/2, altura/2+150)
        pygame.display.update()
    return status
