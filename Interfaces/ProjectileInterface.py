import pygame, math
from Assets.constants import *
from Assets.imagePaths import *

pygame.init()

#Maintains the projectile and all relevant info
class ProjectileInterface:
    def __init__(self, environment, floor, velocity, angle, x, y):
        self.screen = environment.getScreen()

        #Relevant classes
        self.environment = environment
        self.floor = floor

        #Define dimensions and location of projectile
        self.width = BALL_W
        self.height = BALL_H

        self.x = x
        self.y = y

        #Define values which describe the projectiles movement
        self.velocity = velocity
        self.angle = angle
        self.acceleration = self.environment.getGravity() // 2
        self.time = 0

        self.velocityX, self.velocityY = 0, 0

        #Define projectile assets
        self.projectileImage = pygame.image.load(PROJECTILE_IMAGE_P).convert_alpha()
        self.projectileImage = pygame.transform.scale(self.projectileImage, (self.width, self.height))

        #Keeps track of path the projectile traveled
        self.path = []

        self.shot = False


    #Current distance from starting point based on time into simulation
    def findCurrDistance(self, time):
        x = (self.velocityX * time)
        y = ((self.velocityY * time) + ((self.acceleration * (time ** 2)) / 2))
        return x, y

    #Velocity in the x and y directions based on an overall velocity in a certain angle
    def splitVelocityComponents(self):
        #math.cos/math.sin take radians so degrees must be converted before using
        velX = (self.velocity*math.cos(self.angle))
        velY = (self.velocity*math.sin(self.angle))

        return velX, velY

    #Updates the current distance to the new distance
    def update(self):
        if not pygame.Rect.colliderect(self.getRect(), self.floor.getRect()) and self.shot:
            self.x, self.y = self.findCurrDistance(self.time)
            self.time += TIME_INC
            self.path.append((self.x + (self.width // 2), self.y + (self.height // 2)))

    #Prints the projectile to the screen
    def draw(self, showPath=True):
        if showPath:
            for point in self.path:
                pygame.draw.rect(self.screen, WHITE, (point[0], point[1], PATH_WIDTH, PATH_WIDTH))
        pygame.draw.rect(self.screen, RED, (self.x, self.y, self.width, self.height))

    #Start the projectiles shot (Update modifies all values after initial call to shoot)
    def shoot(self):
        self.shot = True

        self.velocityX, self.velocityY = self.splitVelocityComponents()
        self.x, self.y = self.findCurrDistance(0)

    #GETTERS 

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def getVelocity(self):
        return self.velocity

    def getDistance(self):
        return self.x

    def getTime(self):
        return self.time

    def isShot(self):
        return self.shot

    #SETTERS

    def setVelocity(self, newVelocity):
        self.velocity = newVelocity
        self.cannon.setVelocity(self.velocity)

    def setAngle(self, newAngle):
        self.angle = newAngle
        self.cannon.setAngle(self.angle)