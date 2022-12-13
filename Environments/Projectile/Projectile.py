import pygame, math
from Assets.constants import *

pygame.init()

class Projectile:
    def __init__(self, environment, cannon):
        self.environment = environment
        self.screen = self.environment.getScreen()

        self.width = BALL_W
        self.height = BALL_H

        self.cannon = cannon

        self.velocityInit = self.cannon.getVelocity()
        self.velocityCurr = self.velocityInit

        self.velocityX, self.velocityY = self.splitVelocityComponents()

        self.distX, self.distY = self.getCurrDistance(0)


    def getCurrDistance(self, time):
        distX = (self.velocityX * time) + self.cannon.getRect()[0] + self.cannon.getWidth()
        distY = ((self.velocityY * time) + ((((self.environment.getGravity() // 2) * -1) * (time ** 2)) / 2)) + self.cannon.getRect()[1]
        return distX, distY

    def splitVelocityComponents(self):
        velX = (self.velocityCurr*math.cos(math.radians(self.cannon.getAngle())))
        velY = (self.velocityCurr*math.sin(math.radians(self.cannon.getAngle())))

        return velX, velY

    def updatePosition(self):
        self.distX, self.distY = self.getCurrDistance(0)

    def update(self, time):
        self.getCurrDistance(time)
        self.updatePosition()

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.distX, self.distY, self.width, self.height))