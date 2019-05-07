# Get Pygame
import pygame
import random
pygame.init()

# Initialize Window
WIDTH = 500
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bricks")
win.fill((0, 0, 0))
FPS = pygame.time.Clock()

# Initiallize Variables
x = int(WIDTH / 2)
y = int(HEIGHT / 2)
xvel = 10
yvel = -5
radius = 25
width = 75
height = 15
rectx = WIDTH / 2 + width / 2
gameover = False
brickwidth = 50
brickheight = 25
bricks = []
font = pygame.font.SysFont("arial", 100, True, False)
i = 0
ione = 0
brick = 0

# Brick
class Brick(object):
    def __init__(self, x, y, width, height, color, win):
        self.x = x
        self.y = y
        self.win = win
        self.height = height
        self.width = width
        self.color = color
        self.visible = True

    def delete(self):
        self.visible = False

    def render(self):
        if self.visible:
            pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.height))

def color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# Make Bricks
while i in range(0, int(HEIGHT / brickheight)):
    while ione in range(0, int(WIDTH / brickwidth)):
        brick = Brick(ione * brickwidth, i * brickheight, brickwidth, brickheight, color(), win)
        bricks.append(brick)

        ione += 1
    i += 1


# Render function
def render():
    global x
    global y
    global radius
    global width
    global height
    global rectx

    # Clear
    win.fill((255, 255, 255))

    # Ball
    pygame.draw.circle(win, (0, 255, 255), (x, y), radius)

    # You
    pygame.draw.rect(win, (0, 0, 0), (rectx, HEIGHT - 50, width, height))

    for brick in bricks:
        brick.render()

    # Update
    pygame.display.update()

# Loop
run = True
while run:
    FPS.tick(60)

    # window closed?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if gameover:
        run = False
        pygame.time.delay(1000)

    # Collision With Walls
    if not x + xvel in range(radius, WIDTH - radius) or y + yvel - radius < 0:
        if not x + xvel in range(radius, WIDTH - radius):
            xvel *= -1

        else:
            yvel *= -1

    # Ball Touching You?
    if y + yvel > HEIGHT - 50 - height and x in range(int(rectx - height / 2 - radius), int(
            rectx + height / 2 + radius)):
        yvel *= -1

    x += xvel
    y += yvel

    # Update Your Pos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rectx - abs(xvel) * 2 > 0:
        rectx -= abs(xvel)

    if keys[pygame.K_RIGHT] and rectx + width + abs(xvel) * 2 < WIDTH:
        rectx += abs(xvel)

    # Collision with bricks
    for brick in bricks:
        if y < brick.y and x in range(brick.x, brick.x + brick.width) and brick.visible:
            brick.visible = False

    render()

    # You lose?
    if y > HEIGHT - 50:
        win.fill((255, 255, 255))
        text = font.render("You Lose!", False, (255, 0, 0))
        win.blit(text, (WIDTH / 2 - text.get_width() / 2,  HEIGHT / 2 - text.get_height() / 2))
        gameover = True
        pygame.display.update()
pygame.quit()
