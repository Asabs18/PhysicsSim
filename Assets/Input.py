import pygame, math, sys
from Assets.constants import *

pygame.init()

#Handles any user input to the program
class Input:
    def __init__(self, environment, floor, cannon, projectile, controller):
        #Relevant classes
        self.environment = environment
        self.floor = floor
        self.cannon = cannon
        self.projectile = projectile
        self.controller = controller

        #Define screen 
        self.screen = self.environment.screen

        #Define font
        self.font = DEFAULT_F

    #Exits the program if q or exit button is clicked
    def handleExit(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.controller.isClickedQB(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()


    #Updates angle and or shoots projectile based on click location
    def handleClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if not self.projectile.isShot() and not self.controller.getRect().collidepoint(pos):
                self.controller.setAngle(self.cannon.findAngle(pos))
                self.projectile.shoot()
            elif not self.projectile.isShot() and self.controller.isClickedSB(pos):
                self.projectile.shoot()
            else:
                self.controller.isClickedRB(pos)

    def handleKeypress(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.controller.getVelocityInput().deactivate()
                self.controller.getAngleInput().deactivate()
                self.controller.getDistanceInput().deactivate()
