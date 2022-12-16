import pygame

from Assets.constants import *

pygame.init()

class Floor:
    def __init__(self, screen, height):
        self.screen = screen

        self.screenWidth = screen.get_width()
        self.screenHeight = screen.get_height()

        self.width = self.screenWidth
        self.height = height

        self.x = (.5)*(self.screenWidth - self.width)
        self.y = (self.screenHeight - self.height)

    #Displays the floor on the screen
    def draw(self):
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(self.x, self.y, self.width, self.height))

    #Returns a Rect Object that contains the x and y coords as well as the width and height of the floor
    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)