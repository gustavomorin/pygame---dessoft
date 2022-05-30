#importar bibliotecas
from cgitb import text
from multiprocessing.pool import INIT
from tkinter import font
import pygame 
import random
from config import *
from game import tela_game
from over import tela_final
from util import *
from inicial import tela_inicial

pygame.init() #iniciando o pygame

window = pygame.display.set_mode((largura, altura)) #tamanho da janela

pygame.display.set_caption('SAVE IF YOU CAN') #definido o titulo da janela

game = True 
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
pos_bolax=largura/2-50
pos_bolay=altura/2-150
troca_vel = True
defesas=0

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100) #fonte


status = INICIAL
luva = None
while status != QUIT:

    if status == INICIAL:
        status = tela_inicial(window)

    while status == SELECT_COUNTRY:
        clock.tick(FPS)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                status = QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0] #pega a posicao do x (mouse)
                y =  pygame.mouse.get_pos()[1] #pega a posicao do y (mouse)
                if x > (largura/2+50) and y > (altura/2-200) and x < largura/2+350 and y < altura/2-50:
                    luva = 'brasil'
                    status = GAME
                if x > (largura/2+50) and y > (altura/2+50) and x < largura/2+350 and y < altura/2+200:
                    luva = 'argentina'
                    status = GAME
                if x > (largura/2-350) and y > (altura/2-200) and x < largura/2-50 and y < altura/2-50:
                    luva = 'alemanha'
                    status = GAME
                if x > (largura/2-350) and y > (altura/2+50) and x < largura/2-50 and y < altura/2+200:
                    luva = 'franca'
                    status = GAME


        window.blit(gramado, (0, 0))
        window.blit(brasil, ((largura/2+50), (altura/2-200)))
        window.blit(argentina, ((largura/2+50), (altura/2+50)))
        window.blit(alemanha, ((largura/2-350), (altura/2-200)))
        window.blit(franca, ((largura/2-350), (altura/2+50)))
        texto(window, font, 'Escolha um país para representar:', branco, largura/2, 75)
        pygame.display.update()

    if status == GAME:
        status = tela_game(window, luva)   

    if status == OVER:
        status =  tela_final(window)
    

pygame.quit()