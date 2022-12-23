import pygame
from scipy.constants import g, speed_of_light, gravitational_constant
from Assets.imagePaths import *

pygame.init()

class EnvironmentInterface:
    def __init__(self):
        #Define screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.clock = pygame.time.Clock()

        #CONSTANTS
        self.gravity = g
        self.speedOfLight = speed_of_light
        self.gravitationalConstant = gravitational_constant

    #GETTERS

    def getGravity(self):
        return self.gravity

    def getSpeedOfLight(self):
        return self.speedOfLight

    def getGravitationalConstant(self):
        return self.gravitationalConstant

    def getScreen(self):
        return self.screen