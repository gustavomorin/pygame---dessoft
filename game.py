from sprites import *
from config import *
import random
import pygame


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
    errou=pygame.image.load("assets\errou.jpg").convert_alpha()
    errou=pygame.transform.scale(errou,(200,200))
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

    all_sprites.add(bola)
    all_bola.add(bola)

    while status == GAME: #looping enquanto game = True
        clock.tick(FPS)

        window.blit(goleiro, (0, 0))
        '''if troca_vel:
            traj_y=random.randint(-5,5)
            traj_x=(-traj_y**2+225)**(1/2)
            sinal = random.randint(0,1)
            if sinal == 1:
                traj_x = -traj_x
            troca_vel = False'''
        
        mx,my= pygame.mouse.get_pos()
        luva.rect.centerx = mx
        luva.rect.centery = my
        '''pos_bolax = bola1.rect.x
        pos_bolay = bola1.rect.y
        if pos_bolax>=largura or pos_bolax < 0 or pos_bolay >= altura or pos_bolay < 0:
            pos_bolax = largura/2-50
            pos_bolay = altura/2-150
            bola1.troca_vel=True'''
        bolas = pygame.sprite.spritecollide(luva, all_bola, True, pygame.sprite.collide_mask)
        if len(bolas)>0:
            if bola != None:
                bola.kill()
            bola=Bola(bola_img,pos_bolax,pos_bolay,random.randint(0,700), random.randint(0,1500), random.choice([-1, 1] ))
            all_sprites.empty()
            all_sprites.add(bola)
            all_sprites.add(luva)
            all_bola.add(bola)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                status = QUIT

        all_sprites.update()

        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(goleiro, (0, 0))
        all_sprites.draw(window)
        pygame.display.update()
    return status
