import pygame, math
from Assets.constants import *
from Assets.imagePaths import *

pygame.init()

#Maintains the cannon and all relevant info
class Cannon:
    def __init__(self, environment, floor, velocity):
        self.screen = environment.getScreen()

        #Relevant classes
        self.environment = environment
        self.floor = floor

        #Get location and dimensions of cannon
        self.width = CANNON_WIDTH
        self.height = CANNON_HEIGHT

        self.x = CANNON_OFFSET_X
        self.y = (floor.getRect()[1] - (self.height - 20))

        #Define values which describe the cannon/projectile movement
        self.angle = -INIT_ANGLE #Negates the passed in angle because the origin in (0, 0) and the cannon is below that
        self.velocity = velocity

        #Define cannon assetS
        self.cannonImage = pygame.image.load(CANNON_IMAGE_P).convert_alpha()
        self.cannonImage = pygame.transform.scale(self.cannonImage, (self.width, self.height))
        self.cannonImage = pygame.transform.rotate(self.cannonImage, -55 - self.angle)


    #Prints the cannon to the screen
    def draw(self):
        self.screen.blit(self.cannonImage, (self.x, self.y - 20))

    #find angle between cannon and cursor position
    def findAngle(self, cursorPos):
        dx = cursorPos[0] - self.x
        dy = cursorPos[1] - self.y
        return math.atan2(dy, dx)

    #Update the cannon image rotation to account for current angle
    def update(self):
        self.cannonImage = pygame.transform.rotate(self.cannonImage, -45 - self.angle)

    #GETTERS

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

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

    #SETTERS

    def setAngle(self, newAngle):
        self.angle = newAngle
        self.update() #Updates cannon image angle