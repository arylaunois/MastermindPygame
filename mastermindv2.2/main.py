""" Main 2512"""

#Imports
import pygame
import time
import sys
from pygame.locals import *
from mmglobals import *
from board import *
from pegs import *
from button import *
from clickerPeg import *

#Drawing of notice
def drawNote(surface):
    font = pygame.font.SysFont("Comic Sans MS", 20)
    font2 = pygame.font.SysFont('Comic Sans MS', 13)
    titleSurf = font.render("Note: ",True,cols["BLACK"])
    surface.blit(titleSurf, (menuW//2,20))

    noteSurf = font2.render("Green pegs - Correct colour, Wrong position",True,cols["BLACK"])
    noteSurf2 = font2.render("Red pegs - Correct colour, Correct position",True,cols["BLACK"])
    surface.blit(noteSurf,(menuW//2,45))
    surface.blit(noteSurf2,(menuW//2,60))
    

#Drawing of leaderboard
def drawLeaderboard(surface,leaderboard):
    font = pygame.font.SysFont('Comic Sans MS', 20)
    font2 = pygame.font.SysFont('Comic Sans MS', 16)
    titleSurf = font.render("Leaderboard:",True,cols["BLACK"])
    surface.blit(titleSurf, (10,10))

    for i in range(len(leaderboard)):
        text = str(i+1)+". "+leaderboard[i][0]+" : "+str(leaderboard[i][1])
        textSurf = font2.render(text,True,cols["BLACK"])
        surface.blit(textSurf, (10,(i*30)+40))

#Saving leaderboard
def saveLeaderboard(leaderboard):
    file = open("Res/leaderboard.txt","w")
    for p in leaderboard:
        file.write(p[0]+","+str(p[1]))
        file.write("\n")
    file.close()

#Loading leaderboard
def loadLeaderboard():
    leaderboard = []
    file = open("Res/leaderboard.txt","r")
    for line in file.read().split("\n"):
        temp = []
        for item in line.split(","):
            temp.append(item)
        leaderboard.append(temp)
    leaderboard.pop()
    file.close()
    return leaderboard

#Saves the current board to a file
def saveGame(board,turn,nickname, hideAns):
    file = open("Res/save.txt","w")
    for row in board:
        count = 0
        for item in row:
            if count < 4:
                file.write(item)
                file.write("\n")
            else:
                if item == []:
                    file.write(str(turn)+","+str(nickname)+","+str(hideAns))
                    file.write("\n")
                    file.write("\n")
                else:
                    for i in range(len(item)):
                        if i < len(item)-1:
                            file.write(item[i])
                            file.write(",")
                        else:
                            file.write(item[i])
                            file.write("\n")
                            file.write("\n")
            count += 1
                
    file.close()

#Loads the board from a file and returns it
def loadGame():
    file = open("Res/save.txt","r")
    newBoard = []
    finalBoard = []
    for line in file.read().split("\n\n"):
        newBoard.append(line.split("\n"))
    newBoard.pop()
    for line in newBoard:
        temp = []
        for i in range(len(line)):
            if i < 4:
                temp.append(line[i])
            else:
                temp.append(line[i].split(","))
        finalBoard.append(temp)

    turn = int(finalBoard[0][4][0])
    nickname = str(finalBoard[0][4][1])
    if str(finalBoard[0][4][2]) == "True":
        hideAns = True
    if str(finalBoard[0][4][2]) == "False":
        hideAns = False
    finalBoard[0][4] = []
    file.close()

    return finalBoard, turn,nickname, hideAns

def main():

    #Init
    pygame.init()
    pygame.font.init()
    pygame.mouse.set_visible(True)

    #Surfaces
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    gameSurface = pygame.Surface((gameW,gameH))
    menuSurface = pygame.Surface((menuW,menuH))
    lbSurface = pygame.Surface((lbW,lbH))

    #Objects and variables
    playerPeg = clickerPeg(-100,-100,"WHITE", 0)
    p = pegs()
    brd = board()
    clickPos = [-1,-1]
    turn = 1
    nickname = "TypeName"
    clock = pygame.time.Clock()

    running = True
    typing = False

    #Images
    win = pygame.image.load("Res/smiley.png").convert()
    lose = pygame.image.load("Res/frowny.png").convert()
    
    #Defining leaderboard
    leaderboard = loadLeaderboard()
    
    #Creates the buttons
    saveButton = button("MAGENTA","Save Game",menuSurface,y=1.55)
    loadButton = button("RED", "Load Game",menuSurface,y=2.6,fontsize = 28)
    newButton = button("YELLOW", "New Game",menuSurface, y=8.3)
    nameButton = button("BLACK", nickname,menuSurface,x=2,y=2,border=6,width=3.5)

    #Cursor
    rect = nameButton.txtsurface.get_rect()
    rect.topleft = (int(menuW//1.95),int(menuH//1.86))
    cursor = Rect(rect.topright, (3, rect.height))

    #Creation of main pegs that you use to place other pegs
    clickerPegs = []
    for i in range(len(clickerPegCols)):
        xcoord = int(i*gameW//len(clickerPegCols)+gameW//len(clickerPegCols)//2)
        ycoord = int((brd.rows-1)*brd.sqH+brd.sqH/2)
        clickerPegs.append(clickerPeg(xcoord,ycoord,clickerPegCols[i]))

    #Main loop
    while running:
        #Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                #Query click position
                clickPos = pygame.mouse.get_pos()

                #If button is pressed performs appropriate function
                    #Save
                if saveButton.button.collidepoint((clickPos[0],clickPos[1]-gameH)):
                    print("Save")
                    saveGame(p.bord,turn,nickname,brd.hideAns)
                    #Load
                if loadButton.button.collidepoint((clickPos[0],clickPos[1]-gameH)):
                    print("Load")
                    p.bord, turn, nickname, brd.hideAns = loadGame()
                    #New game
                if newButton.button.collidepoint((clickPos[0],clickPos[1]-gameH)):
                    print("New Game")
                    nickname, turn = p.resetPegs()
                    brd.hideAns = True
                    #Name
                if nameButton.button.collidepoint((clickPos[0],clickPos[1]-gameH)):
                    typing = True
                    pygame.mouse.set_visible(False)
                    if nickname == "TypeName":
                        nickname = ''
                    #Select colour
                for peg in clickerPegs:
                    if peg.isClicked(clickPos):
                        col = peg.col
                        playerPeg.r = int(gameW//33.3333)
                        playerPeg.col = col
                    #Place colour
                x, y = clickPos[0]//brd.sqW, clickPos[1]//brd.sqH
                row = brd.rows - turn
                if x != 4 and y == row-1 and col != "NONE":
                    p.bord[y][x] = col
                    col = "NONE"
                    playerPeg.col = "WHITE"
                    playerPeg.r = 0
                    
            #Allows user type name
            if typing:
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        typing = False
                        pygame.mouse.set_visible(True)
                    elif event.key == K_BACKSPACE:
                        nickname = nickname[:-1]
                    else:
                        nickname += event.unicode

        #Queries whether the 4th peg has been placed
        #runs the logic of the small pegs and winning/losing
        if "WHITE" not in p.bord[brd.rows-turn-1]:
            red, blue = p.logic(turn)
            if red == 4:
                brd.hideAns = False
                #Displays smiley face when won
                print("WIN")
                screen.blit(win,(0,0))
                pygame.display.update()
                clock.tick(1)
                pygame.time.delay(1500)

                #updating of leaderboard
                pos = -1
                for i in range(len(leaderboard)-1,-1,-1):
                    if turn < int(leaderboard[i][1]):
                        pos = i
                if pos > -1:
                    leaderboard.insert(pos,[nickname, turn])
                    leaderboard.pop()
                    saveLeaderboard(leaderboard)

            turn += 1
        if turn == 13:
            brd.hideAns = False
            #Displays frowny face when lost
            print('LOSE')
            screen.blit(lose,(0,0))
            pygame.display.update()
            clock.tick(1)
            pygame.time.delay(1500)
            turn = p.resetPegs()[1]
            brd.hideAns = True
        playerPeg.x, playerPeg.y = pygame.mouse.get_pos()

        #Rendering
        screen.fill(cols["WHITE"])
        gameSurface.fill(cols["WHITE"])
        menuSurface.fill(cols["WHITE"])
        lbSurface.fill(cols["WHITE"])

        #Game
        brd.draw(gameSurface)
        p.drawPegs(brd, gameSurface)
        for peg in clickerPegs:
            peg.draw(gameSurface)
        playerPeg.draw(gameSurface)

        #Leaderboard
        drawLeaderboard(lbSurface,leaderboard)

        #Note
        drawNote(menuSurface)

        #Menu buttons
        saveButton.draw(menuSurface, "Save Game")
        loadButton.draw(menuSurface,"Load Game")
        newButton.draw(menuSurface,"New Game")
        nameButton.draw(menuSurface, nickname)

        #Cursor
        rect.size = nameButton.txtsurface.get_size()
        cursor.topleft = rect.topright
        if time.time() % 1 > 0.5 and typing:
            pygame.draw.rect(menuSurface, cols["BLACK"], cursor)
        
        #Hides or displays answer
        brd.hideAnswer(gameSurface)

        screen.blit(gameSurface, (0,0))
        screen.blit(menuSurface, (0,gameH))
        screen.blit(lbSurface,(gameW,0))
        pygame.display.update()


#Run
if __name__ == "__main__":
    main()
