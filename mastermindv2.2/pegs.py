""" Pegs class used to hold all peg information on the board 0610 """

#Imports
import pygame, random
from pygame.locals import *
from mmglobals import *

class pegs:

    #Init
    def __init__(self):

        #Random answer generation
        self.answer = []
        for i in range(4):
            self.answer.append(clickerPegCols[random.randint(0,len(clickerPegCols)-1)])

        #Data of peg positions on the board (named bord as to not conflict with other variables
        self.bord = [[self.answer[0],self.answer[1],self.answer[2],self.answer[3],[]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                     ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]]
            ]

    #Draw function of the board
    def drawPegs(self, brd, surface):
        for i in range(len(self.bord)):
            for j in range(len(self.bord[i])):
                if j != 4:
                    pygame.draw.circle(surface, cols[self.bord[i][j]], ((j*brd.sqW)+(brd.sqW//2),(i*brd.sqH)+(brd.sqH//2)),int(gameW//33.333))
                else:
                    l, h = 1,1
                    for k in range(len(self.bord[i][j])):
                        x, y = (brd.cols - 1) * brd.sqW, i * brd.sqH
                        pygame.draw.circle(surface, cols[self.bord[i][j][k]], ((x+l*int(gameW//35)+(int(brd.sqW//3.5))),(y+h*int(gameW//35))),int(gameW//100))
                        if h == 2:
                            h -= 1
                            l += 1
                        else:
                            h += 1

    #Logic function for all smaller pegs
    def logic(self, turn):
        red = 0
        blue = 0
        pegged = []
        peggedAns = []

        rw = len(self.bord) - turn

        #Checks if won
        if self.bord[0][0:4] == self.bord[rw][0:4]:
            red = 4
            return red,blue

        #Checks for reds
        for i in range(4):
            if self.bord[0][i] == self.bord[rw][i] and i not in pegged:
                red += 1
                pegged.append(i)
                peggedAns.append(i)

        #Checks for blues
        for i in range(4):
            for j in range(4):
                if self.bord[rw][i] == self.bord[0][j] and j not in peggedAns and i not in pegged:
                    blue += 1
                    pegged.append(i)
                    peggedAns.append(j)
            pegged.append(i)

        #Changes appropriate amount of pegs
        for i in range(red):
            self.bord[rw][4][i] = "RED"
        for i in range(red,blue+red):
            self.bord[rw][4][i] = "GREEN"
        return red,blue

    #Resets the peg board
    def resetPegs(self):
        self.answer = []
        for i in range(4):
                self.answer.append(clickerPegCols[random.randint(0,len(clickerPegCols)-1)])
        self.bord = [[self.answer[0],self.answer[1],self.answer[2],self.answer[3],[]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]],
                         ["WHITE","WHITE","WHITE","WHITE",["BLACK","BLACK","BLACK","BLACK"]]
                ]

        #Returns reseted turn and nickname to reset the whole game
        turn = 1
        nickname = "TypeName"
        return nickname, turn
        
