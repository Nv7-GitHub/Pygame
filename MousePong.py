# Pong - Press Space to start. Move mouse up and down to make left paddle go up and down
# Author  - Vikar Industries, Lead Programmer: Nishant Vikramaditya
# Version 1.0

# Get Pygame
import pygame
pygame.init()

# Initialize Window
WIDTH = 1000
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
win.fill((0, 0, 0))
FPS = pygame.time.Clock()

# Initiaize Variables
x = round(WIDTH / 2)
y = round(HEIGHT / 2)
font = pygame.font.SysFont("arial", 100, True, False)
gameover = False
radius = 25
xvel = 8
yvel = -5
height = 75
width = 5
gap = 50
score = 0
speed = 30

# Render Function
def render():
    # Get Variables
    global x
    global y
    global radius
    global mousepos
    global gap
    global font
    global score

    # Clear
    win.fill((0, 0, 0))

    # Ball
    pygame.draw.circle(win, (0, 255, 255), (x, y), radius)  # Ball

    # Pads
    pygame.draw.rect(win, (255, 255, 255), (gap, mousepos[1] - height / 2, width, height))  # Your rectangle
    pygame.draw.rect(win, (255, 255, 255), (WIDTH - gap, y - height / 2, width, height))  # AI

    # Score
    text = font.render(str(score), False, (255, 255, 255))  # Score
    win.blit(text, (WIDTH / 2 - text.get_width() / 2,  10))  # Score

    # Update Display
    pygame.display.update()

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return


# Wait to start game
win.fill((255, 255, 255))
text = font.render("Press SPACE to start.", False, (0, 0, 0))
win.blit(text, (WIDTH / 2 - text.get_width() / 2,  HEIGHT / 2 - text.get_height()))
pygame.display.update()
wait()

# Loop
run = True
while run:
    FPS.tick(60)

    # window closed?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Game Over?
    if gameover:
        pygame.time.delay(1500)
        run = False


    # Speed Up
    if score % 10 == 0:
        if xvel < 0:
            xvel -= 2

        else:
            xvel += 2

        if yvel < 0:
            yvel -= 2

        else:
            yvel += 2

        score += 1

    # Update You
    mousepos = pygame.mouse.get_pos()

    # Update Circle Pos
    if y + yvel not in range(radius, HEIGHT - radius):
        yvel *= -1

    x += xvel
    y += yvel

    if x - xvel - radius < gap + width and y + yvel in range(int(mousepos[1] - height / 2 - radius), int(mousepos[1] + height / 2 + radius)):
        xvel *= -1
        x += radius
        score += 1

    if x + xvel + radius > WIDTH - (gap + width):
        xvel *= -1
        x -= radius

    render()

    # You Lose?
    if x < gap:
        win.fill((255, 255, 255))
        font1 = pygame.font.SysFont("Arial", 100, True, False)
        text = font1.render("You Lose!", False, (255, 0, 0))  # Score
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        gameover = True
pygame.quit()
