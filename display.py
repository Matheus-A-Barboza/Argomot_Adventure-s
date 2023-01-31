from pygame import mixer
from pygame import font
import pygame


pygame.init()


#Imagens_utilizadas
fundo = pygame.image.load("cenario2.jpg")
silhueta = pygame.image.load("silhuetafundo.png")
fundoText = pygame.image.load("caixatextoFundo (2).png")



#Cod
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Argomot Adventure's")
font = pygame.font.Font('Ancient Modern Tales.otf', 32)
text = font.render("AAAAAAAAAHHH...", True, (0,0,0))
textName = font.render("?????", True, (255,255,255))


janela_aberta1 = True

#Display1
while janela_aberta1:
    pygame.time.delay(50)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta1 = False


#Inserção_De_Objetos
    janela.blit(fundo,(0,0))
    janela.blit(silhueta, (100,0))
    janela.blit(fundoText, (58, 360))
    janela.blit(text, (90, 430))
    janela.blit(textName,(235,377))
    pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.mouse.get_pos()
        break
        next(object(janela_aberta2))

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#Display2

fundo = pygame.image.load("cenario2.jpg")
usersilhueta = pygame.image.load("userfundo.png")
fundoText = pygame.image.load("caixatextoFundo (2).png")

#Cod
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Argomot Adventure's")
font = pygame.font.Font('Ancient Modern Tales.otf', 32)
textWel = font.render("Olá, Guerreiro! Antes de me apresentar, me diga seu nome:", True, (0,0,0))
textName = font.render("?????", True, (255,255,255))


janela_aberta2 = True

while janela_aberta2:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta2 = False

    janela.blit(fundo,(0,0))
    janela.blit(usersilhueta, (0,0))
    janela.blit(fundoText, (58, 360))
    janela.blit(textWel, (90, 430))
    janela.blit(textName,(235,377))
    pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.mouse.get_pos()
        break
        next(object(janela_aberta3))

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

#Display3

