# Import Other Things Here
""""This section is not required"""

# Get Pygame
import pygame
pygame.init()


# Initialize Window
WIDTH = 500
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Window Title Here")
FPS = pygame.time.Clock()


# Variables
variable = "Define variables here"


def render():
    # Clear Screen
    win.fill((0, 0, 0))

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
