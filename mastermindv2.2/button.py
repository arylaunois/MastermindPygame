''' Allows the creation of any clickable button for the menu 1402'''

import pygame
from mmglobals import *

class button:
    #Init
    def __init__(self, col, text, surface, x = 8, y = 8,width = 4, height = 4, fontsize = 25,border=0):
        self.height, self.width = height,width
        self.font = pygame.font.SysFont('Comic Sans MS', fontsize)
        self.x,self.y = x,y
        self.col = col
        self.text = text
        self.border = border
        self.button = pygame.draw.rect(surface,cols[self.col],((menuW//self.x),(menuH//self.y),(menuW//self.width),(menuH//self.height)),self.border)
        self.txtsurface = self.font.render(text, True, cols["BLACK"])

    #Render the button
    def draw(self,surface, text):
        self.txtsurface = self.font.render(text, True, cols["BLACK"])
        self.button = pygame.draw.rect(surface,cols[self.col],((menuW//self.x),(menuH//self.y),(menuW//self.width),(menuH/self.height)),self.border)
        surface.blit(self.txtsurface,((menuW//self.x)+5,(menuH//self.y)+7))



            
        
