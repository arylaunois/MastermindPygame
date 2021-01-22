""" Clickable pegs used to select colour 1209 """

#Imports
import pygame
from math import sqrt
from pygame.locals import *
from mmglobals import *

class clickerPeg:

    #Init
    def __init__(self, x, y, col, r = int(gameW//33.3333)):
        self.r = r
        self.x = x
        self.y = y
        self.col = col

    #Draw func
    def draw(self, surface):
        pygame.draw.circle(surface, cols[self.col], (self.x, self.y), self.r)

    #Distance formula for circle used to query if clicks are on the circle
    def isClicked(self, mousePos):
        sqx = (mousePos[0] - self.x)**2
        sqy = (mousePos[1] - self.y)**2

        if sqrt(sqx+sqy) < self.r:
            return True
