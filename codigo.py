#importar bibliotecas
from cgitb import text
from multiprocessing.pool import INIT
from tkinter import font
import pygame 

pygame.init() #iniciando o pygame

altura = 700
largura = 1500
window = pygame.display.set_mode((largura, altura)) #tamanho da janela
font = pygame.font.SysFont(None, 100) #fonte

pygame.display.set_caption('SAVE IF YOU CAN') #definido o titulo da janela

game = True 
imagem_inicial = pygame.image.load('assets/allianz-parque.jpg').convert() #imagem inicial
imagem_inicial = pygame.transform.scale(imagem_inicial, (largura,altura)) #definir tamanho da imagem
brasil = pygame.image.load('assets/brasil.png').convert() #bandeira brasil
brasil = pygame.transform.scale(brasil, (300,150)) #posicao bandeira brasil
argentina = pygame.image.load('assets/argentina.png').convert() #bandeira argentina
argentina = pygame.transform.scale(argentina, (300,150)) # posicao bandeira argentina
alemanha = pygame.image.load('assets/alemanha.png').convert() #bandeira alemanha
alemanha = pygame.transform.scale(alemanha, (300,150)) #posicao bandeira alemanha
franca = pygame.image.load('assets/franca.png').convert() #bandeira franca
franca = pygame.transform.scale(franca, (300,150)) #posicao bandeira franca
gramado = pygame.image.load('assets/gramado.png').convert() #imagem gramado
gramado = pygame.transform.scale(gramado, (largura, altura)) #posicao imagem gramado
logo= pygame.image.load("assets/logo.png").convert_alpha()#imagem logo do jogo
logo=pygame.transform.scale(logo, (700,350))#posicão do logo
goleiro=pygame.image.load("assets/Goleiro.jpeg").convert()
goleiro=pygame.transform.scale(goleiro,(largura,altura))

#cores
branco = (255,255,255)
preto = (0,0,0)
vermelho=(255,0,0)
verde = (0,255,0)
azul = (0,0,255)
clock = pygame.time.Clock()

#funcao do texto
def texto (msg, cor, largura, altura):
    texto1 = font.render(msg, True, cor)
    x = texto1.get_width() / 2
    y = texto1.get_height() / 2    
    window.blit(texto1, (largura - x, altura - y))
    pygame.display.flip()

FPS = 30
INICIAL = 0
QUIT = -1
SELECT_COUNTRY = 1
GAME = 2
status = INICIAL
while status != QUIT:
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
        texto('Jogar', branco, largura/2, altura/2+150)
        pygame.display.update()

    while status == SELECT_COUNTRY:
        clock.tick(FPS)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                status = QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0] #pega a posicao do x (mouse)
                y =  pygame.mouse.get_pos()[1] #pega a posicao do y (mouse)
                if x > (0) and y > (0) and x < 1500 and y < 700:
                    status = GAME

        window.blit(gramado, (0, 0))
        window.blit(brasil, ((largura/2+50), (altura/2-200)))
        window.blit(argentina, ((largura/2+50), (altura/2+50)))
        window.blit(alemanha, ((largura/2-350), (altura/2-200)))
        window.blit(franca, ((largura/2-350), (altura/2+50)))
        texto('Escolha um país para representar:', branco, largura/2, 75)
        pygame.display.update()

    while status == GAME: #looping enquanto game = True
        clock.tick(FPS)
        window.blit(goleiro, (0, 0))
        pygame.display.update()

pygame.quit()