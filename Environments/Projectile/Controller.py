import pygame
from Assets.constants import *
from Assets.Button import Button
from Environments.Projectile.Environment import Environment
from Environments.Projectile.Floor import Floor
from Environments.Projectile.Cannon import Cannon
from Environments.Projectile.Projectile import Projectile

pygame.init()

class Controller:
    def __init__(self, environment, projectile):
        self.environment = environment

        self.projectile = projectile

        self.angle = self.projectile.cannon.getAngle()
        self.velocity = self.projectile.getVelocity()
        self.floorHeight = self.projectile.floor.getHeight()

        self.width = self.environment.screen.get_width() // 4
        self.height = self.width

        self.x = self.environment.screen.get_width() - (self.width + CONTROLLER_OFFSET_X)
        #Uses constant to dynamically keep the controller in the upper right corner no matter of screen size
        self.y = self.environment.screen.get_width() - (self.x * 1.375)

        self.buttons = self.createButtons()

    def checkButtonClick(self, cursorPos):
        if self.buttons[0].isClicked(cursorPos):
            self.executeShootButton()
        elif self.buttons[1].isClicked(cursorPos):
            self.executeResetButton()
        
    def executeShootButton(self):
        print("Shoot Button Clicked")

    def executeResetButton(self):
        environment = Environment(self.environment.screen)
        floor = Floor(environment, 100)
        cannon = Cannon(environment, floor, 90)
        projectile = Projectile(floor, cannon)
        controller = Controller(environment, projectile)

    def createButtons(self):
        buttons = []

        shootButtonRect = pygame.Rect((self.x + (self.width // 2)) - CONTROLLER_BUTTON_OFFSET_X, self.height + 30, BUTTON_WIDTH, BUTTON_HEIGHT)
        resetButtonRect = pygame.Rect((self.x + (self.width // 2)) + CONTROLLER_BUTTON_OFFSET_X, self.height + 30, BUTTON_WIDTH, BUTTON_HEIGHT)

        buttons.append(Button(self.environment.screen, "Shoot", shootButtonRect, D_GREY))
        buttons.append(Button(self.environment.screen, "Reset", resetButtonRect, D_GREY))

        return buttons


    def update(self):
        if not self.projectile.isShot():
            self.angle = self.projectile.cannon.getAngle()
            self.velocity = self.projectile.getVelocity()

    def draw(self):
        pygame.draw.rect(self.environment.screen, GREY, pygame.Rect(self.x, self.y, self.width, self.height))
        for button in self.buttons:
            button.draw()

    #GETTERS

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

