import pygame
import pygame.draw as d

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 500))

# цвета

white = (255, 255, 255)
black = (0, 0, 0)
gray1 = (183, 200, 196)
gray2 = (147, 169, 170)
gray3 = (142, 172, 167)
gray4 = (183, 196, 200)
gray5 = (111, 145, 138)
gray6 = (219, 226, 226)
gray7 = (83, 108, 103)
blue = (64, 128, 255)


# фон
def building(surface, color, x, y):
    d.rect(surface, color, (x, y, 80, 320))


d.rect(screen, white, (0, 0, 400, 500))
d.rect(screen, gray4, (0, 340, 400, 500))
d.rect(screen, gray7, (0, 350, 400, 500))
d.ellipse(screen, gray1, (0, 425, 500, 200))

building(screen, gray2, 10, 10)
building(screen, gray3, 100, 25)
building(screen, gray6, 300, 10)
building(screen, gray5, 250, 100)
building(screen, gray1, 50, 75)


# облака
def cloud(x, y):
    d.ellipse(surface_cloud, gray2, (x, y, 400, 90))


surface_cloud = pygame.Surface((400, 500))

surface_cloud.set_alpha(50)
surface_cloud.fill(white)
cloud(-10, 20)
cloud(-50, 220)
cloud(80, 120)

# тачила

x_car = 170
y_car = 410

surface_car = pygame.Surface((400, 500), pygame.SRCALPHA)

def car(x, y):
    d.rect(surface_car, black, (x - 35, y + 30, 10, 5, 255)
    d.rect(surface_car, blue, (x, y, 80, 30, 255))
    d.rect(surface_car, blue, (x - 30, y + 20, 150, 20 ))
    d.rect(surface_car, white, (x + 5, y + 5, 20, 10))
    d.rect(surface_car, white, (x + 50, y + 5, 20, 10))
    d.ellipse(surface_car, black, (x - 15, y + 30, 30, 25))
    d.ellipse(surface_car, black, (x + 80, y + 30, 30, 25))


car(x_car, y_car)

pygame.transform.scale(surface_car, (250, 200))

# дым

def smoke(x, y):
    d.ellipse(surface_smoke, gray2, (x, y, 100, 30))


surface_smoke = pygame.Surface((400, 500))
surface_smoke.set_alpha(50)
surface_smoke.fill(white)
smoke(x_car - 160, y_car + 20)
smoke(x_car - 180, y_car - 20)
smoke(x_car - 220, y_car - 50)

screen.blit(surface_smoke, (0, 0))

screen.blit(surface_cloud, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
