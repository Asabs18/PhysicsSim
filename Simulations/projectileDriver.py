import pygame, math

from Assets.constants import *
from Assets.Input import Input

from Environments.Projectile.Environment import Environment
from Environments.Projectile.Projectile import Projectile
from Environments.Projectile.Cannon import Cannon
from Environments.Projectile.Controller import Controller

pygame.init()

def drawScreen(controller):
    controller.screen.fill(L_GREY)
    controller.projectile.floor.draw()
    controller.projectile.draw()
    controller.projectile.cannon.draw()
    controller.draw()

def update(events, controller):
    controller.projectile.update()
    drawScreen(controller)
    controller.update(events)
    pygame.display.update()

#Runs simulation for projectile motion
def projectileDriver():
    #Restart Program Level Loop
    while True:
        #Setup Environment
        environment = Environment()

        cannon = Cannon(environment, 90, INIT_ANGLE)

        controller = Controller(environment, cannon.projectile)

        input = Input(environment, cannon, controller)
        

        #Main loop 
        runGL = True

        while runGL:
            environment.clock.tick(FPS)

            events = pygame.event.get()

            for event in events:
                input.handleExit(event)
                input.handleClick(event)
                input.handleKeypress(event)

            update(events, controller)
            if controller.isRestart():
                break