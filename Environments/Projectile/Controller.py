import pygame
from Assets.constants import *

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


    def update(self):
        if not self.projectile.isShot():
            self.angle = self.projectile.cannon.getAngle()
            self.velocity = self.projectile.getVelocity()

    def draw(self):
        pygame.draw.rect(self.environment.screen, GREY, pygame.Rect(self.x, self.y, self.width, self.height))

