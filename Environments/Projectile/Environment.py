import pygame

from scipy.constants import g, speed_of_light, gravitational_constant

from Assets.imagePaths import *

from Interfaces.EnvironmentInterface import EnvironmentInterface

pygame.init()

#Maintains any variables that apply to the overall environment or any universal constants
class Environment(EnvironmentInterface):
    def __init__(self, screen):
        #define screen
        self.screen = screen 

        #constants
        self.gravity = g