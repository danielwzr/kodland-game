import pygame 
from pygame.locals import *
from sys import exit
import logging
from random import randint

pygame.display.set_caption("Kodland Jogo")
relogio = pygame.time.Clock()

altura = 480
largura = 640
tela = pygame.display.set_mode((largura,altura))

x=largura/2
y=altura/2

movespeed = 4

spritebook = pygame.image.load('book.webp')
spritebook = pygame.transform.scale(spritebook, (40, 40))

spriteplayer = pygame.image.load('estudante.png')
spriteplayer = pygame.transform.scale(spriteplayer, (40,40))

spriteinimigo = pygame.image.load('inimigo.png')
spriteinimigo = pygame.transform.scale(spriteinimigo, (40,40))

spritekodland = pygame.image.load('kodland.png')
spritekodland = pygame.transform.scale(spritekodland, (180, 55))


pygame.init()

fonte = pygame.font.SysFont('arial', 20, True, True)

book_x = 200
book_y = 200

inimigo_x = 500
inimigo_y = 400
inimigo_movespeed = 0.8

pontos = 0

while True:
    
    if pontos >= 5: 
        tela.fill((0,0,0))
        relogio.tick(165)
        for event in pygame.event.get():
             if event.type == QUIT:
                pygame.quit()
                exit()
        tela.blit(spritekodland, (240,220))
        tela.blit(parabens_formatado, (130, 180))
        pygame.display.update()
    else:
        relogio.tick(165)
        tela.fill((0,0,0))
        mensagem = f'Pontos: {pontos}'
        parabens = f'Parabéns pelo aprendizado conquistado!'
        texto_formatado = fonte.render(mensagem, True, (255,255,255))
        parabens_formatado = fonte.render(parabens, True, (255,255,255))
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit()
             
        if (pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]) and x>0 : x = x - movespeed
        if (pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT])  and x<=(largura-30): x = x + movespeed
        if (pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP])  and y>0: y = y - movespeed
        if (pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN])  and y<=(altura-30): y = y + movespeed
            
        background = pygame.draw.rect(tela, (0,0,0), (0,0,largura,altura))
        spritebg = pygame.image.load('school.png')
        spritebg = pygame.transform.scale(spritebg, (640,480))
        tela.blit(spritebg, (0,0))
    
        player = pygame.draw.rect(tela, (0,0,0), (x,y,40,40))
        tela.blit(spriteplayer, (x,y))
    
        book = pygame.draw.rect(tela, (0,0,0), (book_x, book_y, 40, 40))
        tela.blit(spritebook, (book_x,book_y))
    
    
        inimigo = pygame.draw.rect(tela, (0,0,0), (inimigo_x, inimigo_y, 40,40))
        tela.blit(spriteinimigo, (inimigo_x, inimigo_y))
    
    
    
        if player.colliderect(book): 
            book_x = randint(0,600)
            book_y = randint(0,440)
            pontos = pontos + 1
        
        if player.colliderect(inimigo):
            pontos = 0
            ##pygame.quit()
                
        if x > inimigo_x:
            inimigo_x = inimigo_x + inimigo_movespeed
        if x < inimigo_x:
            inimigo_x = inimigo_x - inimigo_movespeed
        if y > inimigo_y:
            inimigo_y = inimigo_y + inimigo_movespeed
        if y < inimigo_y:
            inimigo_y = inimigo_y - inimigo_movespeed
    
  
   ## else: x = x + 1
    
        tela.blit(texto_formatado, (500, 20))
        pygame.display.update()

   ## bola = pygame.draw.ellipse(tela, (240,55,20), (90,120,90,90))
   ## linha = pygame.draw.line(tela, (0,90,211),(100,100),(200,100))