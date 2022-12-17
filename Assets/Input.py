import pygame, math, sys

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
        self.font = pygame.font.SysFont('consolas', 20, True)

    #Exits the program if q or exit button is clicked
    def handleExit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    #Updates angle and or shoots projectile based on click location
    def handleClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if not self.projectile.isShot() and not self.controller.getRect().collidepoint(pos):
                self.controller.setAngle(math.degrees(self.cannon.findAngle(pos)))
                self.projectile.shoot()
            elif not self.projectile.isShot() and self.controller.isClickedSB(pos):
                self.projectile.shoot()
            else:
                self.controller.isClickedRB(pos)