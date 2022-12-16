import pygame

from Assets.constants import *
from Assets.imagePaths import *

pygame.init()

class Floor:
    def __init__(self, environment, height):
        self.environment = environment
        self.screen = self.environment.getScreen()

        self.screenWidth = self.screen.get_width()
        self.screenHeight = self.screen.get_height()

        self.width = self.screenWidth
        self.height = height

        self.x = (.5)*(self.screenWidth - self.width)
        self.y = (self.screenHeight - self.height)

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