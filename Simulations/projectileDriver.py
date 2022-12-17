import pygame, sys, math
from Assets.constants import *
from Environments.Projectile.Environment import Environment
from Environments.Projectile.Floor import Floor
from Environments.Projectile.Projectile import Projectile
from Environments.Projectile.Cannon import Cannon
from Environments.Projectile.Controller import Controller

#Make angle and velocity able to be set by cursor position on screen or by text dialog on side of screen then hitting shoot button

pygame.init()

#Setup Environment
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

environment = Environment(screen)
floor = Floor(environment, 100)
cannon = Cannon(environment, floor, 90)
projectile = Projectile(floor, cannon)
controller = Controller(environment, projectile)

clock = pygame.time.Clock()
pygame.display.set_caption("Physics Simulation")

def drawScreen():
    screen.fill(L_GREY)
    floor.draw()
    projectile.draw()
    cannon.draw()
    controller.draw()
    pygame.display.update()

#Runs simulation for projectile motion
def projectileDriver():

    runGL = True
    while runGL:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not projectile.isShot() and not controller.getRect().collidepoint(pygame.mouse.get_pos()):
                    cannon.setAngle(math.degrees(cannon.findAngle(pygame.mouse.get_pos())))
                    controller.update()
                    projectile.shoot()
                controller.checkButtonClick(pygame.mouse.get_pos())
        
        projectile.update()
        drawScreen()