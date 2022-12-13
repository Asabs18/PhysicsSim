import pygame, math
from Components.assets import *

pygame.init()

class Projectile:
    def __init__(self, screen, cannon):
        self.screen = screen

        self.width = BALL_W
        self.height = BALL_H

        self.cannon = cannon

        self.x = self.cannon.getRect()[0] + self.cannon.getWidth()
        self.y = self.cannon.getRect()[1]

        self.velocityInit = self.cannon.getVelocity()
        self.velocityCurr = self.velocityInit

        self.velocityX, self.velocityY = self.splitVelocityComponents()


    def splitVelocityComponents(self):
        velX = (self.velocityCurr*math.cos(math.radians(self.cannon.getAngle())))
        velY = (self.velocityCurr*math.sin(math.radians(self.cannon.getAngle())))

        return velX, velY

    def updatePosition(self):
        pass #Update position w magnitude in correct direction

    def updateVelocity(self):
        pass #UPDATE VELOCITY

    def update(self):
        self.updatePosition()
        self.updateVelocity()

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.width, self.height))