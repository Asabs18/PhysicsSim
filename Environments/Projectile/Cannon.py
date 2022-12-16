import pygame
from Assets.constants import *
from Assets.imagePaths import *

pygame.init()

class Cannon:
    def __init__(self, environment, floor, angle, velocity):
        self.environment = environment
        self.screen = self.environment.getScreen()

        self.width = 100
        self.height = 125

        self.x = CANNON_OFFSET_X
        self.y = (floor.getRect()[1] - (self.height - 20))

        self.floor = floor

        #Negates the passed in angle because the origin in (0, 0) and the cannon is below that
        self.angle = -angle
        
        self.velocity = velocity

        self.cannonImage = pygame.image.load(CANNON_IMAGE_P).convert_alpha()
        self.cannonImage = pygame.transform.scale(self.cannonImage, (self.width, self.height))
        self.cannonImage = pygame.transform.rotate(self.cannonImage, -55 - self.angle)

    #Prints the cannon to the screen
    def draw(self):
        self.screen.blit(self.cannonImage, (self.x, self.y - 20))

    #Returns a Rect Object that contains the x and y coords as well as the width and height of the floor
    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    #GETTERS

    def getVelocity(self):
        return self.velocity

    def getAngle(self):
        return self.angle

    def getWidth(self):
        return self.width

    def getX(self):
        return self.x

    def getY(self):
        return self.y