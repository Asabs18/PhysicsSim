import pygame, sys

from Assets.constants import *
from Assets.Button import Button
from Assets.InputBox import InputBox

from Environments.Projectile.Environment import Environment
from Environments.Projectile.Floor import Floor
from Environments.Projectile.Cannon import Cannon
from Environments.Projectile.Projectile import Projectile

pygame.init()

#Maintains the dialog box and all relevant info
class ControllerInterface:
    def __init__(self, environment):
        self.screen = environment.getScreen()

        #Relevant classes
        self.environment = environment

        #Define dimensions and location of dialog box dynamically to fit to any screen size
        self.width = self.environment.screen.get_width() // 4
        self.height = self.width
        self.x = self.environment.screen.get_width() - (self.width + CONTROLLER_OFFSET_X)
        self.y = self.environment.screen.get_width() - (self.x * CONTROLLER_OFFSET_MULTIPLIER_Y)

        #define font
        self.font = DEFAULT_F

        #Create interactive elements
        self.createButtons()
        self.createTextInputs()

        #Define restart variable
        self.restart = False

    #Check if shoot button clicked
    def isClickedSB(self, cursorPos):
        isClicked = False

        if self.startButton.isClicked(cursorPos):
            isClicked = True

        return isClicked


    #Check if reset button clicked
    def isClickedRB(self, cursorPos):
        isClicked = False

        if self.resetButton.isClicked(cursorPos):
            isClicked = True

        return isClicked

    #Check if quit button clicked
    def isClickedQB(self, cursorPos):
        isClicked = False

        if self.quitButton.isClicked(cursorPos):
            isClicked = True

        return isClicked
                
    #Start the time
    def executeStartButton(self):
        pass

    #Reset entire program to init values
    def executeResetButton(self):
        self.restart = True

    #Quit Program
    def executeQuitButton(self):
        pygame.quit()
        sys.exit()

    #Create buttons dynamically based on size and location of dialog box
    def createButtons(self):
        startButtonRect = pygame.Rect((self.x + (self.width // 2)) - CONTROLLER_BUTTON_OFFSET_X, self.height + 30, BUTTON_WIDTH, BUTTON_HEIGHT)
        resetButtonRect = pygame.Rect((self.x + (self.width // 2)) + CONTROLLER_BUTTON_OFFSET_X, self.height + 30, BUTTON_WIDTH, BUTTON_HEIGHT)
        quitButtonRect = pygame.Rect((self.x + (self.width // 2)), self.height - 30, L_BUTTON_WIDTH, BUTTON_HEIGHT)

        self.startButton = Button(self.screen, "Start", startButtonRect, D_GREY)
        self.resetButton = Button(self.screen, "Reset", resetButtonRect, D_GREY)
        self.quitButton = Button(self.screen, "Quit", quitButtonRect, D_GREY)

    #Display time on screen
    def drawTime(self):
        textSurf = self.font.render("Time: " + str(round(self.projectile.getTime())) + " s", 0, BLACK)
        self.screen.blit(textSurf, (self.x + self.width - TEXTBOX_OFFSET_X, self.y+self.height//1.75))

    #Draw all controller assets to screen
    def draw(self):
        pygame.draw.rect(self.screen, GREY, pygame.Rect(self.x, self.y, self.width, self.height))
        self.startButton.draw()
        self.resetButton.draw()
        self.quitButton.draw()
        self.drawTime()

    #GETTERS

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def isRestart(self):
        return self.restart

