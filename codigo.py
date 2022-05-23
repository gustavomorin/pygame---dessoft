#importar bibliotecas
from cgitb import text
from tkinter import font
import pygame 

pygame.init() #iniciando o pygame

altura = 700
largura = 1500
window = pygame.display.set_mode((largura, altura)) #tamanho da janela
font = pygame.font.SysFont(None, 100)

pygame.display.set_caption('SAVE IF YOU CAN') #definido o titulo da janela

game = True 
imagem_inicial = pygame.image.load('assets/allianz-parque.jpg').convert() #imagem inicial
imagem_inicial = pygame.transform.scale(imagem_inicial, (largura,altura)) #definir tamanho da imagem
brasil = pygame.image.load('assets/brasil.png').convert()
brasil = pygame.transform.scale(brasil, (300,150))
argentina = pygame.image.load('assets/argentina.png').convert()
argentina = pygame.transform.scale(argentina, (300,150))
alemanha = pygame.image.load('assets/alemanha.png').convert()
alemanha = pygame.transform.scale(alemanha, (300,150))
franca = pygame.image.load('assets/franca.png').convert()
franca = pygame.transform.scale(franca, (300,150))
gramado = pygame.image.load('assets/gramado.png').convert()
gramado = pygame.transform.scale(gramado, (largura, altura))
branco = (255,255,255)
preto = (0,0,0)
vermelho=(255,0,0)
verde = (0,255,0)
azul = (0,0,255)


def texto (msg, cor):
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, [650, 280])

window.blit(imagem_inicial, (0, 0))
pygame.draw.rect(window, verde, [500, 250, 500, 150])
texto('Jogar', branco)

while game: #looping enquanto game = True
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            game = False

    '''window.blit(imagem_inicial, (0, 0))
    pygame.draw.rect(window, verde, [500, 250, 500, 150])
    texto('Jogar', branco)'''
    if event.type == pygame.MOUSEBUTTONDOWN:
        x = pygame.mouse.get_pos()[0]
        y =  pygame.mouse.get_pos()[1]
        if x > 500 and y > 250 and x < 1000 and y < 400:
            window.blit(gramado, (0, 0))
            window.blit(brasil, ((largura/2+50), (altura/2-200)))
            window.blit(argentina, ((largura/2+50), (altura/2+50)))
            window.blit(alemanha, ((largura/2-350), (altura/2-200)))
            window.blit(franca, ((largura/2-350), (altura/2+50)))
            
    pygame.display.update()

    


pygame.quit()