import pygame
from scipy.constants import g, speed_of_light, gravitational_constant
from Assets.imagePaths import *

pygame.init()

#Maintains any variables that apply to the overall environment or any universal constants
class Environment:
    def __init__(self, screen):
        #Define screen
        self.screen = screen

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