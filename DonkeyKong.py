# Get Pygame
import pygame
pygame.init()


# Initialize Window
WIDTH = 700
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donkey Kong")
FPS = pygame.time.Clock()


# Classes
class Barrel:
    def __init__(self, x, y, radius, start, end, speed):
        self.x = x
        self.y = y
        self.start = start
        self.end = end
        self.radius = radius
        self.speed = speed
        self.direction = 1

    def update(self):
        if self.x + self.radius == self.end:
            self.direction = -1

        if self.x - self.radius == self.start:
            self.direction = 1

        self.x += self.speed * self.direction

    def render(self):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.radius)


# Variables
keys = []
ladderwidth = 26
ladderheight = 100
speed = 5
width = 25
height = 40
x = round(WIDTH / 2)
y = HEIGHT - height - speed
climbing = False
climbingheight = 0
climbdir = 1
barrelradius = 10
gameover = False
jumpspeed = 1
jumpdir = 1
jumping = False
jumpstage = 1
touchingladder = False

# Get Images
ladder = pygame.transform.scale(pygame.image.load("ladder.png"), (ladderwidth, ladderheight))

# Initialize Lists
i = 0
ladders = []
while i < HEIGHT / ladderheight:
    ladders.append(((WIDTH / 4) * i, HEIGHT - speed - ((i + 1) * ladderheight)))
    i += 1

i = 0
floors = []
while i < HEIGHT / ladderheight - 1:
    floors.append((0, HEIGHT - speed - ((i + 1) * ladderheight), WIDTH, height/ 2))
    i += 1

i = 0
barrels = []
while i < HEIGHT / ladderheight:
    barrels.append(Barrel(int(ladders[i][0]), HEIGHT - speed - barrelradius - ((i + 1) * ladderheight), barrelradius,
                          0, WIDTH, speed))
    i += 1


def render():
    # Install variables
    global x
    global y
    global width
    global height
    global barrels

    # Clear Screen
    win.fill((0, 0, 0))

    # Floors
    for pos in floors:
        pygame.draw.rect(win, (255, 255, 0), pos)

    # Ladder
    for pos in ladders:
        win.blit(ladder, pos)

    # Barrels
    for barrel in barrels:
        barrel.update()
        barrel.render()

    # render you
    pygame.draw.rect(win, (0, 255, 255), (x, y, width, height))

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

    # Game Over?
    if gameover:
        pygame.time.delay(1500)
        run = False

    # Key Presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - speed > 0 and not climbing:
        x -= speed

    elif keys[pygame.K_RIGHT] and x + speed + width < WIDTH and not climbing:
        x += speed

    elif keys[pygame.K_SPACE] and not (jumping or touchingladder):
        jumping = True
        jumpspeed = 1
        jumpcount = 1
        jumpdir = 1
        jumpstage = 1

    # Check Climbing Ladders
    for pos in ladders:
        if (x in range(int(pos[0]) - width, int(pos[0]) + ladderwidth)) and (y in range(pos[1], pos[1] + ladderheight)):
            touchingladder = True
            if keys[pygame.K_UP] and not pos[1] == ladders[len(ladders) - 1][1]:
                climbing = True
                climbingheight = pos[1] - height
                climbdir = 1

        else:
            touchingladder = False

        if (x in range(int(pos[0]) - width, int(pos[0]) + ladderwidth)) and (y == pos[1] - height):
            if keys[pygame.K_DOWN] and not y == HEIGHT - height - speed:
                climbing = True
                climbingheight = pos[1] + ladderheight - height
                climbdir = -1

    # Animate Climbing
    if climbing:
        if not y == climbingheight:
            y -= speed * climbdir

        else:
            climbing = False

    # Jumping
    if jumping:
        y -= (jumpspeed ** 2) * jumpdir * 0.5

        if jumpspeed <= 4:
            jumpspeed += 1

        elif jumpspeed > 4 and jumpstage == 1:
            jumpspeed = 1
            jumpstage = 2

        elif jumpspeed > 4 and jumpstage == 2:
            jumpspeed = 1
            jumpdir = -1
            jumpstage = 3

        elif jumpspeed > 4 and jumpstage == 3:
            jumpspeed = 1
            jumpstage = 4

        else:
            jumping = False

    render()

    # Top Floor?
    if y <= floors[len(floors) - 1][1] - height:
        win.fill((255, 255, 255))
        font1 = pygame.font.SysFont("Arial", 100, True, False)
        text = font1.render("You Win!", False, (0, 255, 0))  # Score
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        gameover = True

    # Collision With barrels
    for barrel in barrels:
        if x in range(barrel.x - barrelradius, barrel.x + barrelradius + barrelradius) and\
                y + height == barrel.y + barrelradius:
            win.fill((255, 255, 255))
            font1 = pygame.font.SysFont("Arial", 100, True, False)
            text = font1.render("You Lose!", False, (255, 0, 0))  # Score
            win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            pygame.display.update()
            gameover = True

pygame.quit()
