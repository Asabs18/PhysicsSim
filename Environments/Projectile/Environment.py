import pygame

pygame.init()

class Environment:
    def __init__(self, screen):
        self.screen = screen

        self.gravity = 9.8

    #GETTERS

    def getGravity(self):
        return self.gravity

    def getScreen(self):
        return self.screen