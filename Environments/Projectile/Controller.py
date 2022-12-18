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
class Controller:
    def __init__(self, environment, projectile):
        self.screen = environment.getScreen()

        #Relevant classes
        self.environment = environment
        self.projectile = projectile

        #Define angle and velocity to same as cannon angle and velocity (They are always linked)
        self.setAngle(self.projectile.cannon.getAngle())
        self.velocity = self.projectile.getVelocity()

        self.floorHeight = self.projectile.floor.getHeight()

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

    def update(self, events): 
        self.velocityInput.update(events)
        if self.projectile.isShot():
            self.angleInput.update(events, str(-round(self.projectile.cannon.getAngle(), 2)))
            self.distanceInput.update(events, str(round(self.projectile.getDistance(), 2)))
        else:
            if not self.velocityInput.isActive():
                self.projectile.setVelocity(int(self.velocityInput.getText()))
            if not self.angleInput.isActive():
                self.projectile.setAngle(-int(self.angleInput.getText()))
            self.angleInput.update(events)
            self.distanceInput.update(events)

    #Check if shoot button clicked
    def isClickedSB(self, cursorPos):
        isClicked = False

        if self.shootButton.isClicked(cursorPos):
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
                
    #Shoot projectile
    def executeShootButton(self):
        self.projectile.shoot()

    #Reset entire program to init values
    def executeResetButton(self):
        self.restart = True

    #Quit Program
    def executeQuitButton(self):
        pygame.quit()
        sys.exit()

    #Create buttons dynamically based on size and location of dialog box
    def createButtons(self):
        shootButtonRect = pygame.Rect((self.x + (self.width // 2)) - CONTROLLER_BUTTON_OFFSET_X, self.height + 30, BUTTON_WIDTH, BUTTON_HEIGHT)
        resetButtonRect = pygame.Rect((self.x + (self.width // 2)) + CONTROLLER_BUTTON_OFFSET_X, self.height + 30, BUTTON_WIDTH, BUTTON_HEIGHT)
        quitButtonRect = pygame.Rect((self.x + (self.width // 2)), self.height - 30, L_BUTTON_WIDTH, BUTTON_HEIGHT)

        self.shootButton = Button(self.screen, "Shoot", shootButtonRect, D_GREY)
        self.resetButton = Button(self.screen, "Reset", resetButtonRect, D_GREY)
        self.quitButton = Button(self.screen, "Quit", quitButtonRect, D_GREY)

    #Create text inputs dynamically based on size and location of dialog box
    def createTextInputs(self):
        velocityInputRect = pygame.Rect(self.x + self.width - TEXTBOX_OFFSET_X, 100, TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT)
        angleInputRect = pygame.Rect(self.x + self.width - TEXTBOX_OFFSET_X, 200, TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT)
        distanceInputRect = pygame.Rect(self.x + self.width - TEXTBOX_OFFSET_X, 300, TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT)
        
        self.velocityInput = InputBox(self.environment, velocityInputRect, str(self.velocity), "m/s", False, False)
        self.angleInput = InputBox(self.environment, angleInputRect, str(-self.angle), "°", False, False)
        self.distanceInput = InputBox(self.environment, distanceInputRect, "0", "m", False, True)

    def drawInputLabels(self):
        #Print "Velocity" to screen next to input box
        textSurf = self.font.render("Velocity:", 0, BLACK)
        inputRect = self.velocityInput.getRect()
        self.screen.blit(textSurf, (inputRect[0] - LABEL_OFFSET_X, inputRect[1] + LABEL_OFFSET_Y))

        #Print "Acceleration" to screen next to input box
        textSurf = self.font.render("Angle:", 0, BLACK)
        inputRect = self.angleInput.getRect()
        self.screen.blit(textSurf, (inputRect[0] - LABEL_OFFSET_X, inputRect[1] + LABEL_OFFSET_Y))

        #Print "Distance" to screen next to input box
        textSurf = self.font.render("Distance:", 0, BLACK)
        inputRect = self.distanceInput.getRect()
        self.screen.blit(textSurf, (inputRect[0] - LABEL_OFFSET_X, inputRect[1] + LABEL_OFFSET_Y))

    #Display time on screen
    def drawTime(self):
        textSurf = self.font.render("Time: " + str(round(self.projectile.getTime())) + " s", 0, BLACK)
        self.screen.blit(textSurf, (self.x + self.width - TEXTBOX_OFFSET_X, 375))

    #Draw all controller assets to screen
    def draw(self):
        pygame.draw.rect(self.screen, GREY, pygame.Rect(self.x, self.y, self.width, self.height))
        self.shootButton.draw()
        self.resetButton.draw()
        self.quitButton.draw()
        self.drawInputLabels()
        self.drawTime()

    #GETTERS

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def getVelocityInput(self):
        return self.velocityInput

    def getAngleInput(self):
        return self.angleInput

    def getDistanceInput(self):
        return self.distanceInput

    def isRestart(self):
        return self.restart

    #SETTERS

    def setAngle(self, newAngle):
        self.angle = newAngle
        self.projectile.cannon.setAngle(self.angle)

