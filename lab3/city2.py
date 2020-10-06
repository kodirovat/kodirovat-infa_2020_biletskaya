import pygame
import pygame.draw as d

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 600))

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


def car(color, x, y, car_width, car_length):
    d.rect(screen, black, (x - 35, y + 30, car_width, car_length))
    d.rect(screen, color, (x, y, 8 * car_width, 6 * car_length))
    d.rect(screen, color, (x - 30, y + 20, 15 * car_width, 4 * car_length))
    d.rect(screen, white, (x + 5, y + 5, 2 * car_width, 2 * car_length))
    d.rect(screen, white, (x + 50, y + 5, 2 * car_width, 2 * car_length))
    d.ellipse(screen, black, (x - 15, y + 30, 3 * car_width, 5 * car_length))
    d.ellipse(screen, black, (x + 80, y + 30, 3 * car_width, 5 * car_length))


car(gray5, x_car - 150, y_car - 30, 10, 5)
car(gray1, x_car + 100, y_car - 30, 10, 5)
car(gray2, x_car, y_car, 10, 5)

car(blue, x_car - 150, y_car + 80, 10, 5)
car(blue, x_car + 110, y_car + 100, 10, 5)
car(blue, x_car - 32, y_car + 120, 10, 5)


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
