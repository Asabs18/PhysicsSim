import pygame

from Assets.constants import *
from Assets.imagePaths import *

pygame.init()

#Maintains the floor and all relevant info
class Floor:
    def __init__(self, environment, height):
        self.screen = environment.getScreen()

        #Relevant classes
        self.environment = environment

        #Define dimensions and location of floor
        self.width = self.screen.get_width()
        self.height = height

        self.x = (.5)*(self.screen.get_width() - self.width)
        self.y = (self.screen.get_height() - self.height)

        #Define assets for the floor
        self.floorImage = pygame.image.load(FLOOR_IMAGE_P).convert()
        self.floorImage = pygame.transform.scale(self.floorImage, (self.width, self.floorImage.get_height()))

    #Displays the floor on the screen
    def draw(self):
        pygame.draw.rect(self.screen, D_GREY, pygame.Rect(self.x, self.y, self.width, self.height))
        self.screen.blit(self.floorImage, (self.x, self.y))

    #GETTERS

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def getHeight(self):
        return self.height