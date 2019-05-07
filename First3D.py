# Setup
import pygame, math, sys
pygame.init()

# Make Window
WIDTH = 400
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D")
win.fill((255, 255, 255))
FPS = pygame.time.Clock()

# Variables
cx = int(WIDTH / 2)
cy = int(HEIGHT / 2)
verts = (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
edges = (0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (7, 0)


# Render Function
def render():
    # get variables
    global verts
    global edges
    global cx
    global cy

    # Clear screen
    win.fill((255, 255, 255))

    for x, y, z in verts:
        z += 5

        f = 200/z
        x = x * f
        y = y * f

        pygame.draw.circle(win, (0, 0, 0), (cx + int(x), cy + int(y)), 6)

    points = []
    for edge in edges:
        for x, y, z in [verts[edges[0]], verts[edges[1]]]:
            z += 5

            f = 200 / z
            x = x * f
            y = y * f
            points.append([cx + int(x), cx + int(y)])

        pygame.draw.line(win, (0, 0, 0), points[0], points[1], 1)


    pygame.display.flip()


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
