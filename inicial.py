import pygame
from config import *
from util import *

def tela_inicial(window):

    imagem_inicial = pygame.image.load('assets/allianz-parque.jpg').convert() #imagem inicial
    imagem_inicial = pygame.transform.scale(imagem_inicial, (largura,altura)) #definir tamanho da imagem
    logo= pygame.image.load("assets/logo.png").convert_alpha()#imagem logo do jogo
    logo=pygame.transform.scale(logo, (700,350))#posicão do logo
    som_inicial = pygame.mixer.music.load('assets\E-A-Gambazada-Viverá-a-Chorar-●-Letras-●-Mancha-alvi-Verde.mp3')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)
   
    font = pygame.font.SysFont(None, 100) #fonte

    status = INICIAL
    clock = pygame.time.Clock()
    while status == INICIAL:
        clock.tick(FPS)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                status = QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0] #pega a posicao do x (mouse)
                y =  pygame.mouse.get_pos()[1] #pega a posicao do y (mouse)
                if x > 500 and y > 450 and x < 1000 and y < 550:
                    status = SELECT_COUNTRY

        #abertura tela inicial
        window.blit(imagem_inicial, (0, 0))
        window.blit(logo, (420,50))
        #botao
        pygame.draw.rect(window, verde, [500, 450, 500, 100])
        #texto no botao
        texto(window, font, 'Jogar', branco, largura/2, altura/2+150)
        pygame.display.update()
    return status