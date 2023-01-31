from pygame import mixer
from pygame import font
import pygame

pygame.init()


#Imagens utilizadas
fundo = pygame.image.load("cenario2.jpg")
silhueta = pygame.image.load("silhuetafundo.png")
mob = pygame.image.load("orkfundo[.png")
mago = pygame.image.load("magofundo.png")


#Cod
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Argomot Adventure's")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    clique = pygame.key.get_pressed()


    janela.blit(fundo,(0,0))
    janela.blit(silhueta, (100,0))
    pygame.display.update()