import pygame
from scipy.constants import g
from Assets.imagePaths import *

pygame.init()

class Environment:
    def __init__(self, screen):
        self.screen = screen

        self.gravity = g

    #GETTERS

    def getGravity(self):
        return self.gravity

    def getScreen(self):
        return self.screen