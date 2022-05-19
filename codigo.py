#importar bibliotecas
import pygame 

pygame.init() #iniciando o pygame

altura = 700
largura = 1500
window = pygame.display.set_mode((largura, altura)) #tamanho da janela

pygame.display.set_caption('SAVE IF YOU CAN') #definido o titulo da janela

game = True 
imagem_inicial = pygame.image.load('assets/allianz-parque.jpg').convert() #imagem inicial
imagem_inicial = pygame.transform.scale(imagem_inicial, (largura,altura)) #definir tamanho da imagem

while game: #looping enquanto game = True
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            game = False

    window.blit(imagem_inicial, (0, 0))
    pygame.display.update()

pygame.quit()