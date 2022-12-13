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

        self.velocityX, self.velocityY = self.splitVelocityComponents()

    def splitVelocityComponents(self):
        velX = (self.cannon.getVelocity()*math.cos(math.radians(self.cannon.getAngle())))
        velY = (self.cannon.getVelocity()*math.sin(math.radians(self.cannon.getAngle())))
        return velX, velY

    def updatePosition(self):
        self.x += int(self.velocityX)
        self.y -= int(self.velocityY)

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.width, self.height))