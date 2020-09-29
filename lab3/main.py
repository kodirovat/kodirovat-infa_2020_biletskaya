import pygame
import pygame.draw as d

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

white = (255, 255, 255)
black = (0, 0, 0)
gray1 = (183, 200, 196)
gray2 = (200, 200, 200)
gray3 = (83, 108, 103)
gray4 = (183, 196, 200)
blue = (64, 128, 255)


d.rect(screen, gray1, (0, 200, 500, 200))
d.rect(screen, gray2, (100, 50, 40, 200))
d.rect(screen, gray3, ())
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
