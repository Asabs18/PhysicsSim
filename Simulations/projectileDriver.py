import pygame, math

# Import required modules and classes
from Assets.constants import *
from Assets.Input import Input
from Environments.Projectile.Environment import Environment
from Environments.Projectile.Projectile import Projectile
from Environments.Projectile.Cannon import Cannon
from Environments.Projectile.Controller import Controller

pygame.init()

def drawScreen(controller):
    """
    Draws all elements on the screen for the current frame.
    """
    controller.screen.fill(L_GREY)
    controller.projectile.floor.draw()
    controller.projectile.draw()
    controller.projectile.cannon.draw()
    controller.draw()

def update(events, controller):
    """
    Updates simulation state and redraws the screen.
    """
    controller.projectile.update()
    drawScreen(controller)
    controller.update(events)
    pygame.display.update()

def projectileDriver():
    """
    Runs the main loop for the projectile motion simulation.
    """
    while True:  # Restart Program Level Loop
        # Setup Environment and objects
        environment = Environment()
        cannon = Cannon(environment, 90, INIT_ANGLE)
        controller = Controller(environment, cannon.projectile)
        input = Input(environment, cannon, controller)
        # Main loop will follow here
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