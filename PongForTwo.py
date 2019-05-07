# Pong - Press Space to start.
# W to move left character up, S to move left character down,
# Up arrow key to move Right character up, Down arrow key to move right character down.
# Author  - Vikar Industries, Lead Programmer:ws Nishant Vikramaditya
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
font = pygame.font.SysFont("comicsans", 100, True, False)
gameover = False
radius = 25
xvel = -8
yvel = -5
height = 75
width = 5
gap = 50
leftscore = 0
rightscore = 0
speed = 30
lefty = HEIGHT / 2
righty = HEIGHT / 2

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
    global lefty
    global righty

    # Clear
    win.fill((0, 0, 0))

    # Ball
    pygame.draw.circle(win, (0, 255, 255), (x, y), radius) # Ball

    # Pads
    pygame.draw.rect(win, (255, 255, 255), (gap, lefty - height / 2, width, height))  # Your rectangle
    pygame.draw.rect(win, (255, 255, 255), (WIDTH - gap, righty - height / 2, width, height))  # AI

    # Score
    lefttext = font.render(str(leftscore), False, (255, 255, 255))  # Score
    righttext = font.render(str(rightscore), False, (255, 255, 255))  # Score
    win.blit(lefttext, (WIDTH / 2 - lefttext.get_width(),  10))  # Score
    win.blit(righttext, (WIDTH / 2 + righttext.get_width(), 10))  # Score

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
    if rightscore % 10 == 0 or leftscore % 10 == 0:
        if xvel < 0:
            xvel -= 2

        else:
            xvel += 2

        if yvel < 0:
            yvel -= 2

        else:
            yvel += 2

        if rightscore % 10 == 0:
            rightscore += 1

        else:
            leftscore += 1

    # Update You
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and lefty - abs(yvel) * 2 > 0:
        lefty -= abs(yvel) * 2

    elif keys[pygame.K_s] and lefty + abs(yvel) * 2 < HEIGHT:
        lefty += abs(yvel) * 2

    if keys[pygame.K_UP] and righty - abs(yvel) * 2 > 0:
        righty -= abs(yvel) * 2

    elif keys[pygame.K_DOWN] and righty + abs(yvel) * 2 < HEIGHT:
        righty += abs(yvel) * 2


    # Update Circle Pos
    if y + yvel not in range(radius, HEIGHT - radius):
        yvel *= -1

    x += xvel
    y += yvel

    if x - xvel - radius < gap + width and y + yvel in range(int(lefty - height / 2 - radius), int(lefty + height / 2 +
                                                                                                   radius)):
        xvel *= -1
        x += radius
        leftscore += 1

    if x + xvel + radius > WIDTH - (gap + width) and y + yvel in range(int(righty - height / 2 - radius),
                                                                       int(righty + height / 2 + radius)):
        xvel *= -1
        x -= radius
        rightscore += 1

    render()

    # Left Lose?
    if x < gap:
        win.fill((255, 255, 255))
        font1 = pygame.font.SysFont("Arial", 100, True, False)
        text = font1.render("Right Wins!", False, (0, 255, 0))  # Score
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        gameover = True

    # Right Lose
    if x > WIDTH - gap:
        win.fill((255, 255, 255))
        font1 = pygame.font.SysFont("Arial", 100, True, False)
        text = font1.render("Left Wins!", False, (0, 255, 0))  # Score
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        gameover = True
pygame.quit()
