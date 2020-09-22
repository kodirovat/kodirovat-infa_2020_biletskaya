import pygame
import pygame.draw as d

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))
d.circle(screen, (255, 255, 0), (100, 100), 50)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
