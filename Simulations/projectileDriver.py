import pygame, sys
from Assets.constants import *
from Environments.Projectile.Environment import Environment
from Environments.Projectile.Floor import Floor
from Environments.Projectile.Projectile import Projectile
from Environments.Projectile.Cannon import Cannon

pygame.init()

#Setup Environment
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

environment = Environment(screen)
floor = Floor(environment, 100)
cannon = Cannon(environment, floor, 10, 10)
projectile = Projectile(environment, cannon)

clock = pygame.time.Clock()
pygame.display.set_caption("Physics Simulation")

def drawScreen():
    screen.fill(GREY)
    floor.draw()
    projectile.draw()
    cannon.draw()
    pygame.display.update()

#Runs simulation for projectile motion
def projectileDriver():

    time = 0
    runGL = True
    
    while runGL:
        clock.tick(FPS)
        time += TIME_INC
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
        projectile.update(time)
        drawScreen()
        