import pygame, math
from Assets.constants import *
from Assets.imagePaths import *

pygame.init()

#Maintains the projectile and all relevant info
class Projectile:
    def __init__(self, environment, floor, cannon):
        self.screen = environment.getScreen()

        #Relevant classes
        self.environment = environment
        self.floor = floor
        self.cannon = cannon

        #Define dimensions and location of projectile
        self.width = BALL_W
        self.height = BALL_H

        self.x = (self.cannon.getRect()[0] + (self.cannon.getWidth() // 2))
        self.y = (self.cannon.getRect()[1] + PROJECTILE_INIT_CANNON_OFFSET_Y)

        #Define values which describe the projectiles movement
        self.velocity = self.cannon.getVelocity()
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
        x = (self.velocityX * time) + (self.cannon.getRect()[0] + (self.cannon.getWidth() // 2))
        y = ((self.velocityY * time) + ((self.acceleration * (time ** 2)) / 2)) + (self.cannon.getRect()[1] + PROJECTILE_INIT_CANNON_OFFSET_Y)
        return x, y

    #Velocity in the x and y directions based on an overall velocity in a certain angle
    def splitVelocityComponents(self):
        #math.cos/math.sin take radians so degrees must be converted before using
        velX = (self.velocity*math.cos(math.radians(self.cannon.getAngle())))
        velY = (self.velocity*math.sin(math.radians(self.cannon.getAngle())))

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
        self.screen.blit(self.projectileImage, (self.x, self.y))

    #Start the projectiles shot (Update modifies all values after initial call to shoot)
    def shoot(self):
        self.shot = True

        self.cannon.update()

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