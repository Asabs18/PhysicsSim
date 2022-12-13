import pygame, sys
from Components.assets import *
from Environments.Projectile.Floor import Floor
from Environments.Projectile.Projectile import Projectile
from Environments.Projectile.Cannon import Cannon

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


floor = Floor(screen, 100)
cannon = Cannon(screen, floor, 50, 30)
projectile = Projectile(screen, cannon)

clock = pygame.time.Clock()
pygame.display.set_caption("Physics Simulation")

runMain = True
while runMain:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    
    screen.fill(GREY)
    floor.draw()
    projectile.draw()
    cannon.draw()
    pygame.display.update()