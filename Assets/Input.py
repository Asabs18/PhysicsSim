import pygame, math, sys
from Assets.constants import *

pygame.init()

# Handles any user input to the program
class Input:
    def __init__(self, environment, cannon, controller):
        # Store references to relevant classes
        self.environment = environment
        self.floor = cannon.floor
        self.cannon = cannon
        self.projectile = cannon.projectile
        self.controller = controller

        # Define screen and font
        self.screen = self.environment.screen
        self.font = DEFAULT_F

    def handleExit(self, event):
        """
        Exits the program if quit button is clicked.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.controller.isClickedQB(pygame.mouse.get_pos()):
                self.controller.executeQuitButton()

    def handleClick(self, event):
        """
        Updates angle or shoots projectile based on click location.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if not self.projectile.isShot() and not self.controller.getRect().collidepoint(pos):
                self.controller.setAngle(self.cannon.findAngle(pos))
                self.controller.executeStartButton()
            elif not self.projectile.isShot() and self.controller.isClickedSB(pos):
                self.controller.executeStartButton()
            else:
                if self.controller.isClickedRB(pos):
                    self.controller.executeResetButton()

    def handleKeypress(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.controller.getVelocityInput().deactivate()
                self.controller.getAngleInput().deactivate()
                self.controller.getDistanceInput().deactivate()
