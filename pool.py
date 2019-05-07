# Import Other Things Here
import random as rand
import math as mt

# Get Pygame
import pygame
pygame.init()

# Initialize Window
WIDTH = 1000
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pool")
FPS = pygame.time.Clock()


# Classes
class Ball(object):
    def __init__(self, x, y, radius, color):
        self.x = round(x)
        self.y = round(y)
        self.color = color
        self.radius = radius

    def render(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


# Variables
radius = 25
startballx = WIDTH / 2 + 3 * radius
startbally = HEIGHT / 2
x = WIDTH / 2
y = HEIGHT / 2
increment = (2 * mt.sqrt(3) - 2) / 2 * radius * 2

# Lists
row = 1
column = 1
balls = []
while column <= 3:
    while row <= column:
        balls.append(Ball(startballx + column * increment, startbally + (row % 2 - 1) * increment, radius, (0, 0, 0)))
        row += 1

    column += 1


def render():
    # Clear Screen
    win.fill((0, 255, 0))

    # Render Balls
    for ball in balls:
        ball.render()

    # Render Cue Ball
    pygame.draw.circle(win, (255, 255, 255), (round(x), round(y)), radius)

    # Update Display
    pygame.display.update()


# Loop
run = True
while run:
    FPS.tick(60)

    # window closed?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    render()

pygame.quit()
