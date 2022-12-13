import pygame

from Assets.constants import *

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

    #Displays the floor on the screen
    def draw(self):
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(self.x, self.y, self.width, self.height))

    #GETTERS

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)