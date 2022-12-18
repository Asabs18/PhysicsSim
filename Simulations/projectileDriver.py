import pygame, math

from Assets.constants import *
from Assets.Input import Input

from Environments.Projectile.Environment import Environment
from Environments.Projectile.Floor import Floor
from Environments.Projectile.Projectile import Projectile
from Environments.Projectile.Cannon import Cannon
from Environments.Projectile.Controller import Controller

pygame.init()

def drawScreen():
    screen.fill(L_GREY)
    floor.draw()
    projectile.draw()
    cannon.draw()
    controller.draw()

def update(events):
    clock.tick(FPS)
    projectile.update()
    drawScreen()
    controller.update(events)
    pygame.display.update()

#Setup Environment
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()

pygame.display.set_caption("Physics Simulation")

environment = Environment(screen)
floor = Floor(environment, 100)
cannon = Cannon(environment, floor, 90)
projectile = Projectile(environment, floor, cannon)
controller = Controller(environment, projectile)
input = Input(environment, floor, cannon, projectile, controller)

#Runs simulation for projectile motion
def projectileDriver():
    runGL = True

    while runGL:
        events = pygame.event.get()

        for event in events:
            input.handleExit(event)
            input.handleClick(event)
            input.handleKeypress(event)

        update(events)