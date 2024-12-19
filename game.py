import pygame 
from pygame.locals import *
from sys import exit
import logging


pygame.display.set_caption("adsadas")
tela = pygame.display.set_mode((640,480))

pygame.init()

while True:
    for event in pygame.event.get():
        logging.warning(event.dict)
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    bolinha = pygame.draw.rect(tela, (255,0,0), (50,50,30,30), 90,25)