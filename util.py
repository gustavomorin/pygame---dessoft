#funcao do texto
import pygame

def texto (window, font, msg, cor, largura, altura):
    texto1 = font.render(msg, True, cor)
    x = texto1.get_width() / 2
    y = texto1.get_height() / 2    
    window.blit(texto1, (largura - x, altura - y))
    pygame.display.flip()
