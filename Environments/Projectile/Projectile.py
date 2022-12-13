import pygame
from Components.assets import *

pygame.init()

class Projectile:
    def __init__(self, screen, cannon):
        self.screen = screen

        self.width = BALL_W
        self.height = BALL_H

        self.x = cannon.getRect()[0]
        self.y = cannon.getRect()[1]

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.width, self.height))