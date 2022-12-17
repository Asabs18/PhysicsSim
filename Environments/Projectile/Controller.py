import pygame

from Assets.constants import *
from Assets.Button import Button
from Assets.InputBox import InputBox

from Environments.Projectile.Environment import Environment
from Environments.Projectile.Floor import Floor
from Environments.Projectile.Cannon import Cannon
from Environments.Projectile.Projectile import Projectile

pygame.init()

#Maintains the dialog box and all relevant info
class Controller:
    def __init__(self, environment, projectile):
        self.screen = environment.getScreen()

        #Relevant classes
        self.environment = environment
        self.projectile = projectile

        #Define angle and velocity to same as cannon angle and velocity (They are always linked)
        self.angle = self.setAngle(self.projectile.cannon.getAngle())
        self.velocity = self.projectile.getVelocity()

        self.floorHeight = self.projectile.floor.getHeight()

        #Define dimensions and location of dialog box dynamically to fit to any screen size
        self.width = self.environment.screen.get_width() // 4
        self.height = self.width
        self.x = self.environment.screen.get_width() - (self.width + CONTROLLER_OFFSET_X)
        self.y = self.environment.screen.get_width() - (self.x * CONTROLLER_OFFSET_MULTIPLIER_Y)

        self.createButtons()

        #Make update calls for each input box
        velocityInput = InputBox((100, 100), "", False)
        accelerationInput = InputBox((100, 200), "", False)
        distanceInput = InputBox((100, 300), "", False)



    #Check if shoot button clicked
    def isClickedSB(self, cursorPos):
        isClicked = False

        if self.shootButton.isClicked(cursorPos):
            self.executeShootButton()
            isClicked = True

        return isClicked


    #Check if reset button clicked
    def isClickedRB(self, cursorPos):
        isClicked = False

        if self.resetButton.isClicked(cursorPos):
            self.executeResetButton()
            isClicked = True

        return isClicked
                
    #Shoot projectile
    def executeShootButton(self):
        self.projectile.shoot()

    #Reset entire program to init values
    def executeResetButton(self):
        pass

    #Create buttons dynamically based on size and location of dialog box
    def createButtons(self):
        shootButtonRect = pygame.Rect((self.x + (self.width // 2)) - CONTROLLER_BUTTON_OFFSET_X, self.height + 30, BUTTON_WIDTH, BUTTON_HEIGHT)
        resetButtonRect = pygame.Rect((self.x + (self.width // 2)) + CONTROLLER_BUTTON_OFFSET_X, self.height + 30, BUTTON_WIDTH, BUTTON_HEIGHT)

        self.shootButton = Button(self.screen, "Shoot", shootButtonRect, D_GREY)
        self.resetButton = Button(self.screen, "Reset", resetButtonRect, D_GREY)

    #Draw all controller assets to screen
    def draw(self):
        pygame.draw.rect(self.screen, GREY, pygame.Rect(self.x, self.y, self.width, self.height))
        self.shootButton.draw()
        self.resetButton.draw()
        self.screen.blit(self.textinput.surface, (10, 10))

    #GETTERS

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    #SETTERS

    def setAngle(self, newAngle):
        self.angle = newAngle
        self.projectile.cannon.setAngle(self.angle)

