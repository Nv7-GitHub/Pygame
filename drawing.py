# Import Other Things Here
""""This section is not required"""

# Get Pygame
import pygame
pygame.init()


# Initialize Window
WIDTH = 1400
HEIGHT = 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing")
FPS = pygame.time.Clock()


# Variables
radius = 5


def render():
    # Draw
    if pygame.mouse.get_pressed()[0]:
        pygame.draw.circle(win, (255, 255, 255), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), radius)

    # Update Display
    pygame.display.update()


# Loop
run = True
while run:
    FPS.tick(120)

    # window closed?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_c]:
        win.fill((0, 0, 0))

    if keys[pygame.K_UP]:
        radius += 1

    elif keys[pygame.K_DOWN] and not radius <= 1:
        radius -= 1

    render()

pygame.quit()
