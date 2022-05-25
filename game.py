from sprites import *
from config import *
import random
import pygame


def tela_game(window):

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
    bola = pygame.image.load('assets/bola.png').convert_alpha()#imagem da bola
    bola = pygame.transform.scale(bola, (200, 200))#tamanho da bola

    luva_img = luva_brasil
    luva = Luva(luva_img, 0, 0)
    status = GAME
    clock = pygame.time.Clock()
    troca_vel = True


    all_sprites = pygame.sprite.Group()
    all_sprites.add(luva)

    while status == GAME: #looping enquanto game = True
        clock.tick(FPS)
        window.blit(goleiro, (0, 0))
        if troca_vel:
            traj_y=random.randint(-5,5)
            traj_x=(-traj_y**2+225)**(1/2)
            sinal = random.randint(0,1)
            if sinal == 1:
                traj_x = -traj_x
            troca_vel = False
        luva_img = luva_brasil if luva == 'brasil' else luva_alemanha if luva == 'alemanha' else luva_franca if luva == 'franca' else luva_argentina
        
        mx,my= pygame.mouse.get_pos()
        luva.rect.centerx = mx
        luva.rect.centery = my
        if luva == 'brasil':
                window.blit(bola, ((pos_bolax),(pos_bolay)))
                pos_bolax +=traj_x
                pos_bolay+=traj_y
                if pos_bolax>=largura or pos_bolax < 0 or pos_bolay >= altura or pos_bolay < 0:
                    pos_bolax = largura/2-50
                    pos_bolay = altura/2-150
                    troca_vel=True
                window.blit(luva_brasil, ((mx),(my)))
                '''pygame.sprite.groupcollide(bola, luva_brasil, True, True, pygame.sprite.collide_mask)
                for chute in defesas:
                    defesas+=1
                    window.blit(errou, ((largura/2),(altura/2)))'''
                pygame.display.flip()
                pygame.display.update()
        elif luva == 'argentina':
                window.blit(bola, ((pos_bolax),(pos_bolay)))
                pos_bolax +=5
                pos_bolay+=5
                if pos_bolax>=largura or pos_bolay >= altura:
                    pos_bolax = largura/2-50
                    pos_bolay = altura/2-150
                window.blit(luva_argentina, ((mx),(my)))
                pygame.display.flip()
        elif luva == 'alemanha':
                window.blit(bola, ((pos_bolax),(pos_bolay)))
                pos_bolax +=5
                pos_bolay+=5
                if pos_bolax>=largura or pos_bolay >= altura:
                    pos_bolax = largura/2-50
                    pos_bolay = altura/2-150
                window.blit(luva_alemanha, ((mx),(my)))
                pygame.display.flip()
        elif luva == 'franca':
                window.blit(bola, ((pos_bolax),(pos_bolay)))
                pos_bolax +=5
                pos_bolay+=5
                if pos_bolax>=largura or pos_bolay >= altura:
                    pos_bolax = largura/2-50
                    pos_bolay = altura/2-150
                window.blit(luva_franca, ((mx),(my)))
                pygame.display.flip()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                status = QUIT

        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(goleiro, (0, 0))

        all_sprites.draw(window)

        pygame.display.update()
    return status
