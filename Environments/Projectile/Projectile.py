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

        self.velocity = self.cannon.getVelocity()

        self.velocityX, self.velocityY = self.splitVelocityComponents()

        self.distX, self.distY = self.findCurrDistance(0)

    #Current distance from starting point based on time into simulation
    def findCurrDistance(self, time):
        distX = (self.velocityX * time) + self.cannon.getRect()[0] + self.cannon.getWidth()
        distY = ((self.velocityY * time) + ((-4.9 * (time ** 2)) / 2)) + self.cannon.getRect()[1]
        print(distX, distY)
        return distX, distY

    #Velocity in the x and y directions based on an overall velocity in a certain angle
    def splitVelocityComponents(self):
        velX = (self.velocity*math.cos(math.radians(self.cannon.getAngle())))
        velY = (self.velocity*math.sin(math.radians(self.cannon.getAngle())))

        return velX, velY

    #Updates the current distance to the new distance
    def update(self, time):
        self.distX, self.distY = self.findCurrDistance(time)

    #Prints the projectile to the screen
    def draw(self):
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.distX, self.distY, self.width, self.height))