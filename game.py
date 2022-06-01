from inicial import tela_inicial
from over import *
from sprites import *
from config import *
import random
import pygame
import time

def tela_game(window, luva):

    luva_brasil = pygame.image.load('assets/Luva_Brasil.png').convert_alpha()#imagem da luva com cores do Brasil
    luva_brasil = pygame.transform.scale(luva_brasil, (500, 250))#tamanho da luva do Brasil
    luva_argentina = pygame.image.load('assets/Luva_Argentina.png').convert_alpha()#imagem da luva com cores da Argentina
    luva_argentina = pygame.transform.scale(luva_argentina, (500, 250))#tamanho da luva da Argentina
    luva_alemanha = pygame.image.load('assets/Luva_Alemanha.png').convert_alpha()#imagem da luva com cores da Alemanha
    luva_alemanha = pygame.transform.scale(luva_alemanha, (500, 250))#tamanho da luva da Alemanha
    luva_franca = pygame.image.load('assets/Luva_França.png').convert_alpha()#imagem da luva com cores da França
    luva_franca = pygame.transform.scale(luva_franca, (500, 250))#tamanho da luva da França
    goleiro=pygame.image.load("assets/Goleiro.jpeg").convert()#imagem do gol
    goleiro=pygame.transform.scale(goleiro,(largura,altura))#posicao da imagem do gol
    bola_img = pygame.image.load('assets/bola.png').convert_alpha()#imagem da bola
    bola_img = pygame.transform.scale(bola_img, (200, 200))#tamanho da bola
    defesa=pygame.image.load("assets/defesa.png").convert_alpha()#imagem da defesa
    defesa=pygame.transform.scale(defesa,(200,200))#posicao da imagem da defesa
    pos_bolax=largura/2-50
    pos_bolay=altura/2-150
    bola=None
    mx,my= pygame.mouse.get_pos()

    if luva == 'brasil':
        luva_img = luva_brasil 
    if luva == 'alemanha':
        luva_img = luva_alemanha 
    if luva == 'franca':
        luva_img = luva_franca
    if luva == 'argentina':
        luva_img = luva_argentina
    
    luva = Luva(luva_img, mx, my)
    status = GAME
    clock = pygame.time.Clock()
    troca_vel = True
    defesas=0


    all_sprites = pygame.sprite.Group()
    all_sprites.add(luva)
    all_bola = pygame.sprite.Group()
    bola=Bola(bola_img,pos_bolax,pos_bolay,random.randint(0,700), random.randint(0,1500), random.choice([-1, 1] ))

    all_bola.add(bola)
    
    som_apito = pygame.mixer.music.load('assets/apito.mp3')
    pygame.mixer.music.set_volume(2)
    pygame.mixer.music.play(1)

    jogando = False    
    count = 0
    font1 = pygame.font.SysFont(None, 100)
    recorde = 0
    while status == GAME: #looping enquanto game = True
        
        clock.tick(FPS)
        jogando = count > 15
        
        if not jogando:
            count += 1
            texto(window, font1, 'Prepare-se!!!', branco, largura/2, altura/2)
        else:
            mx,my= pygame.mouse.get_pos()
            luva.rect.centerx = mx
            luva.rect.centery = my
            bolas = pygame.sprite.spritecollide(luva, all_bola, False, pygame.sprite.collide_mask)
            
    
            if len(bolas)>0 and bola.profundidade > 62:
                recorde += 1
                som_defesa = pygame.mixer.music.load('assets\defesa.mp3')
                pygame.mixer.music.set_volume(2)
                pygame.mixer.music.play(1)
                som_chute = pygame.mixer.music.load('assets\chute.mp3')
                pygame.mixer.music.set_volume(2)
                pygame.mixer.music.play(1)
                bola.kill()
                bola=Bola(bola_img,pos_bolax,pos_bolay,random.randint(0,700), random.randint(0,1500), random.choice([-1, 1] ))
                all_sprites.empty()
                all_sprites.add(luva)
                all_bola.add(bola)
        
            if len(all_bola) == 0:
                status = OVER

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    status = QUIT

            all_sprites.update()
            all_bola.update()
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(goleiro, (0, 0))
        if count >= 15:
            all_bola.draw(window)
            all_sprites.draw(window)
        pygame.display.update()
    return status
