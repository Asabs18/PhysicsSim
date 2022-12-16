import pygame

pygame.init()

class Environment:
    def __init__(self, screen):
        self.screen = screen

        #find equation or package to get more accurate gravity const
        self.gravity = 9.8066

    #GETTERS

    def getGravity(self):
        return self.gravity

    def getScreen(self):
        return self.screen