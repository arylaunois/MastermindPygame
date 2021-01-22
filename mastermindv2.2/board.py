""" Board class for drawing of the board and hiding of answer 0811 """

#Imports
import pygame
from pygame.locals import *
from mmglobals import *

class board:
    #Init
    def __init__(self):
        self.hideAns = True
        self.rows = 14
        self.cols = 5
        self.sqW = gameW // self.cols
        self.sqH = gameH//self.rows
        self.lw = 3

    #Draw function
    def draw(self, surface):
        for i in range(self.rows):
            for j in range(self.cols):
                pygame.draw.rect(surface,cols["BLACK"],(self.sqW*j,self.sqH*i,self.sqW,self.sqH),self.lw)
        pygame.draw.rect(surface,cols["WHITE"],(0,self.sqH*(self.rows-1),gameW,gameH))

    #Rectangle that covers the answer
    def hideAnswer(self, surface):
        if self.hideAns:
            pygame.draw.rect(surface,cols["BLACK"],(0,0,gameW,self.sqH))
