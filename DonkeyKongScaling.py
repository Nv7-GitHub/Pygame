# Get Pygame
import pygame

pygame.init()

# Initialize Window
WIDTH = 500
HEIGHT = 586
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donkey Kong Scaling")

DonkeyKong = pygame.transform.scale(pygame.image.load("Donkey Kong.png"), (WIDTH, HEIGHT))
win.fill((255, 255, 255))
win.blit(DonkeyKong, (0, 0))

# Loop
run = True
while run:
    # window closed?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
