import pygame

from scipy.constants import g, speed_of_light, gravitational_constant

from Assets.imagePaths import *

from Interfaces.EnvironmentInterface import EnvironmentInterface

pygame.init()

#Maintains any variables that apply to the overall environment or any universal constants
class Environment(EnvironmentInterface):
    def __init__(self):
        #Define screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Physics Simulation")

        #constants
        self.gravity = g