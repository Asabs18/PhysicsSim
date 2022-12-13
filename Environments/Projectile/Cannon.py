import pygame
from Assets.constants import *

pygame.init()

class Cannon:
    def __init__(self, environment, floor, angle, velocity):
        self.environment = environment
        self.screen = self.environment.getScreen()

        self.width = 100
        self.height = 50

        self.x = CANNON_OFFSET_X
        self.y = (floor.getRect()[1] - self.height)

        self.floor = floor

        self.angle = angle
        self.velocity = velocity

    #Displays the cannon on the screen
    def draw(self):
        pygame.draw.rect(self.screen, RED, pygame.Rect(self.x, self.y, self.width, self.height))

    #Returns a Rect Object that contains the x and y coords as well as the width and height of the floor
    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def getVelocity(self):
        return self.velocity

    def getAngle(self):
        return self.angle

    def getWidth(self):
        return self.width