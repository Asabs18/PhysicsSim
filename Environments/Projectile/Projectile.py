import pygame, math
from Assets.constants import *
from Assets.imagePaths import *

pygame.init()

class Projectile:
    def __init__(self, floor, cannon):
        self.floor = floor
        self.screen = self.floor.environment.getScreen()

        self.width = BALL_W
        self.height = BALL_H

        self.cannon = cannon

        self.velocity = self.cannon.getVelocity()

        self.velocityX, self.velocityY = 0, 0

        self.distX, self.distY = 0, 0

        self.time = 0

        self.shot = False

        self.projectileImage = pygame.image.load(PROJECTILE_IMAGE_P).convert_alpha()
        self.projectileImage = pygame.transform.scale(self.projectileImage, (self.width, self.height))

        self.path = []


    #Current distance from starting point based on time into simulation
    def findCurrDistance(self, time):
        distX = (self.velocityX * time) + self.cannon.getRect()[0] + (self.cannon.getWidth() // 2)
        distY = ((self.velocityY * time) + ((4.9 * (time ** 2)) / 2)) + (self.cannon.getRect()[1] + 45)
        return distX, distY

    #Velocity in the x and y directions based on an overall velocity in a certain angle
    def splitVelocityComponents(self):
        velX = (self.velocity*math.cos(math.radians(self.cannon.getAngle())))
        velY = (self.velocity*math.sin(math.radians(self.cannon.getAngle())))

        return velX, velY

    #Updates the current distance to the new distance
    def update(self):
        if not pygame.Rect.colliderect(self.getRect(), self.floor.getRect()) and self.shot:
            self.distX, self.distY = self.findCurrDistance(self.time)
            self.time += TIME_INC
            self.path.append((self.distX + (self.width // 2), self.distY + (self.height // 2)))

    #Prints the projectile to the screen
    def draw(self, showPath=True):
        if showPath:
            for point in self.path:
                pygame.draw.rect(self.screen, WHITE, (point[0], point[1], PATH_WIDTH, PATH_WIDTH))
        self.screen.blit(self.projectileImage, (self.distX, self.distY))

    def shoot(self):
        self.shot = True

        self.velocityX, self.velocityY = self.splitVelocityComponents()
        self.distX, self.distY = self.findCurrDistance(0)

    #GETTERS 

    def getRect(self):
        return pygame.Rect(self.distX, self.distY, self.width, self.height)
    
    def getVelocity(self):
        return self.velocity

    def isShot(self):
        return self.shot