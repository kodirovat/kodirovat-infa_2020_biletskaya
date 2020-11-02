import pygame as pg
import numpy as np
from random import randint

screen_size = (800, 800)  
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 128)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
target_colors = [magenta, cyan]
FPS = 30
font_size = 50

pg.init()

screen = pg.display.set_mode(screen_size)
screen_size = (screen_size[0], screen_size[1] - 100)
pg.display.set_caption("The gun of Khiryanov")
clock = pg.time.Clock()
screen.fill(black)

font = pg.font.Font(None, font_size)
g = 10  # ускорение свободного падения
(g_min, g_max) = (0, 50)
k = 0.8  # потеря импульса при соударении со стенками
number_of_targets = 5
counter = 0 
score = 0 
scale0 = 10


class Ball:
    def __init__(self, coord, vel, t0):
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.coord = coord
        self.vel = vel
        self.rad = 15
        self.is_alive = True
        self.time = t0  # время когда заспавнили шарик

    def draw(self):
        pg.draw.circle(screen, self.color, self.coord, self.rad)

    def check_walls(self, v):
        if self.coord[0] < self.rad:
            self.coord[0] = self.rad
            self.vel[0] = (-k) * v[0]
        elif self.coord[0] > screen_size[0] - self.rad:
            self.coord[0] = screen_size[0] - self.rad
            self.vel[0] = (-k) * v[0]

    def move(self, t):
        self.vel = list(self.vel)
        self.coord = list(self.coord)
        vel_y = self.vel[1] + g * (t - self.time) / FPS
        self.coord[0] = self.coord[0] + int(self.vel[0])
        self.coord[1] = self.coord[1] + int(vel_y)
        self.check_walls((self.vel[0], vel_y))
        if self.coord[1] > (screen_size[1] + 2 * self.rad):  # улетел вниз
            self.is_alive = False
        if g == 0 and self.coord[1] < (-2) * self.rad:  # улетел вверх и g=0
            self.is_alive = False
        if g == 0 and (t - self.time) / FPS > 5:  # если строго горизонтально
            self.is_alive = False


class Cannon:
    def __init__(self):
        self.coord = (0, screen_size[1] // 2)
        self.angle = 0
        self.min_pow = 0
        self.max_pow = 40
        self.power = randint(self.min_pow + 20, self.max_pow)
        self.active = False

    def draw(self):
        end_pos = (int(self.coord[0] + self.power * 2 * np.cos(self.angle)),
                   int(self.coord[1] + self.power * 2 * np.sin(self.angle)))
        pg.draw.line(screen, white, self.coord, end_pos, 5)
        return end_pos

    def strike(self):
        vel = (int(self.power * np.cos(self.angle)),
               int(self.power * np.sin(self.angle)))
        self.active = False
        return vel

    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1],
                                mouse_pos[0] - self.coord[0])


class Target:
    def __init__(self):
        self.coords = list((randint(50, screen_size[0] - 50),
                            randint(50, screen_size[1] - 50)))
        self.radius = 30
        self.vel = list((randint(0, 7), randint(0, 7)))
        self.color = target_colors[randint(0, 1)]

    def draw(self):
        pg.draw.circle(screen, self.color, self.coords, self.radius)
        pg.draw.circle(screen, white, self.coords, self.radius - 10)
        pg.draw.circle(screen, self.color, self.coords, self.radius - 20)

    def hit_check(self, xy, ball_radius):
        (ball_x, ball_y) = xy
        (x, y) = self.coords
        distance = ((ball_x - x) ** 2 + (ball_y - y) ** 2) ** 0.5
        if distance <= (self.radius + ball_radius):
            self.coords = list((randint(50, screen_size[0] - 50),
                                randint(50, screen_size[1] - 50)))
            self.vel = list((randint(0, 5), randint(0, 5)))
            self.color = target_colors[randint(0, 1)]
            return 1
        else:
            return 0

    def check_walls(self):
        for i in (0, 1):
            if self.coords[i] < self.radius:
                self.coords[i] = self.radius
                self.vel[i] = (-1) * self.vel[i]
            elif self.coords[i] > screen_size[i] - self.radius:
                self.coords[i] = screen_size[i] - self.radius
                self.vel[i] = (-1) * self.vel[i]

    def move(self):
        for i in (0, 1):
            self.coords[i] = self.coords[i] + self.vel[i]
        self.check_walls()


def clock_and_score_renewal(time0, score0):
    time_passed = int(time0 / FPS)
    if time_passed < 60:
        str_format_time = "time: " + str(time_passed) + "s"
    else:
        str_format_time = "time: " + str(time_passed // 60) + "m " + \
                          str(time_passed % 60) + "s"
    text2 = font.render(str_format_time, True, blue)
    str_format_score = "score: " + str(score0)
    text3 = font.render(str_format_score, True, blue)
    pg.draw.rect(screen, white, (0, screen_size[1], screen_size[0], 100))
    screen.blit(text2, (screen_size[0] * 6 // 23, screen_size[1] + 35))
    screen.blit(text3, (10, screen_size[1] + 35))


target_list = list(Target() for q in range(number_of_targets))
gun = Cannon()
pg.display.update()
finished = False
ball_list = []
ball_new_list = []


def g_and_cannon_power_renewal():
    font1 = pg.font.Font(None, font_size * 4 // 5)
    str_format_g = "g: " + str(g) + " (left/right)"
    str_format_power = "power: " + str(gun.power) + " (up/down)"
    text4 = font1.render(str_format_g, True, blue)
    text5 = font1.render(str_format_power, True, blue)
    screen.blit(text4, (screen_size[0] * 12 // 20, screen_size[1] + 20))
    screen.blit(text5, (screen_size[0] * 12 // 20, screen_size[1] + 55))


while not finished:
    clock.tick(FPS)
    counter += 1
    screen.fill(black)
    for target in target_list:
        target.move()
        target.draw()
    gun_end = gun.draw()
    ball_new_list = []
    for ball in ball_list:
        ball.move(counter)
        for target in target_list:
            score += target.hit_check(ball.coord, ball.rad)
        if ball.is_alive:
            ball.draw()
            ball_new_list.append(ball)  # минус шары
    ball_list = ball_new_list
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            gun.set_angle(event.pos)
            ball_list.append(Ball(gun_end, gun.strike(), counter))
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT and g != g_max:
                g += 1
            if event.key == pg.K_LEFT and g != g_min:
                g -= 1
            if event.key == pg.K_UP and gun.power != gun.max_pow:
                gun.power += 1
            if event.key == pg.K_DOWN and gun.power != gun.min_pow:
                gun.power -= 1
    clock_and_score_renewal(counter, score)
    g_and_cannon_power_renewal()
    pg.display.update()

pg.quit()