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

while game: #looping enquanto game = True
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            game = False

    window.blit(imagem_inicial, (0, 0))

    if event.type == pygame.KEYUP:
        window.blit(gramado, (0, 0))
        window.blit(brasil, ((largura/2+50), (altura/2-200)))
        window.blit(argentina, ((largura/2+50), (altura/2+50)))
        window.blit(alemanha, ((largura/2-350), (altura/2-200)))
        window.blit(franca, ((largura/2-350), (altura/2+50)))
    
    pygame.display.update()

    


pygame.quit()