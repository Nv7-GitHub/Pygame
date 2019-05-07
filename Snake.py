# Get Random
import random

# Get Pygame
import pygame

pygame.init()

# Initialize Window
WIDTH = 800
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - 1 long - 60 FPS")
pygame.mouse.set_visible(False)
win.fill((255, 255, 255))
FPS = pygame.time.Clock()


class Apple(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def render(self):
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), self.radius)


class Block(object):
    def __init__(self, x, y, direction, width, height, speed, color):
        self.x = x
        self.y = y
        self.direction = direction
        self.width = width
        self.height = height
        self.speed = speed
        self.lastturn = direction
        self.turnpos = [x, y]
        self.color = color

    def update(self):
        if self.direction == "Up":
            self.y -= self.speed

        elif self.direction == "Down":
            self.y += self.speed

        elif self.direction == "Left":
            self.x -= self.speed

        else:
            self.x += self.speed

    def render(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


# Variables
width = 25
height = 25
radius = 15
speed = int(((width + height) / 2) / 5)
snake = [Block(WIDTH / 2, HEIGHT / 2, "Right", width, height, speed, (0, 255, 0))]
apples = []
gameover = False
i = 0


# Render function
def render():
    global snake
    # Clear Screen
    win.fill((255, 255, 255))

    # Render Snake
    i = len(snake) - 1
    while not i == -1:
        snake[i].update()
        snake[i].render()

        i -= 1

    # Render Apples
    for apple in apples:
        apple.render()

    # Update score
    pygame.display.set_caption(f"Snake - {len(snake)} long - {round(FPS.get_fps())} FPS")

    # Update Display
    pygame.display.update()


# Loop
run = True
while run:
    FPS.tick(60)
    # print(FPS.get_fps())

    # window closed?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if gameover:
        pygame.time.delay(1500)
        run = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not snake[0].direction == "Right":
        snake[0].direction = "Left"
        snake[0].lastturn = "Left"
        snake[0].turnpos = [snake[0].x, snake[0].y]

    elif keys[pygame.K_RIGHT] and not snake[0].direction == "Left":
        snake[0].direction = "Right"
        snake[0].lastturn = "Right"
        snake[0].turnpos = [snake[0].x, snake[0].y]

    elif keys[pygame.K_UP] and not snake[0].direction == "Down":
        snake[0].direction = "Up"
        snake[0].lastturn = "Up"
        snake[0].turnpos = [snake[0].x, snake[0].y]

    elif keys[pygame.K_DOWN] and not snake[0].direction == "Up":
        snake[0].direction = "Down"
        snake[0].lastturn = "Down"
        snake[0].turnpos = [snake[0].x, snake[0].y]

    # Make Apples
    while len(apples) < 5:
        apples.append(Apple(random.randint(0 + speed + radius, WIDTH - radius - speed),
                            random.randint(0 + speed + radius, HEIGHT - radius - speed), radius))

    # Snake Touching Apple?
    i = 0
    while i < len(apples):
        if (snake[0].x in range(apples[i].x - radius - width, apples[i].x + radius)) \
                and (snake[0].y in range(apples[i].y - radius - height, apples[i].y + radius)):
            # Hide Apple
            del apples[i]

            # Add another block
            if snake[0].direction == "Up":
                snake.append(Block(snake[0].x, snake[0].y + (height * len(snake)), "Up", width, height, speed,
                                   (0, 255, 255)))

            elif snake[0].direction == "Down":
                snake.append(Block(snake[0].x, snake[0].y - (height * len(snake)), "Down", width, height, speed,
                                   (0, 255, 255)))

            elif snake[0].direction == "Left":
                snake.append(Block(snake[0].x + (width * len(snake)), snake[0].y, "Left", width, height, speed,
                                   (0, 255, 255)))

            else:
                snake.append(Block(snake[0].x - (width * len(snake)), snake[0].y, "Right", width, height, speed,
                                   (0, 255, 255)))

        i += 1

    i = 1
    while i < len(snake):
        if (snake[i - 1].direction == "Up" or snake[i - 1].direction == "Down") and \
                (not snake[i].direction == snake[i - 1].direction):
            if snake[i].x == snake[i - 1].turnpos[0]:
                snake[i].turnpos = [snake[i].x, snake[i].y]
                snake[i].lastturn = snake[i - 1].lastturn
                snake[i].direction = snake[i - 1].lastturn

        elif (snake[i - 1].direction == "Left" or snake[i - 1].direction == "Right") and \
                (not snake[i].direction == snake[i - 1].direction):
            if snake[i].y == snake[i - 1].turnpos[1]:
                snake[i].turnpos = [snake[i].x, snake[i].y]
                snake[i].lastturn = snake[i - 1].lastturn
                snake[i].direction = snake[i - 1].lastturn

        i += 1

    render()

    # You Lose?
    if (not snake[0].x in range(0, WIDTH - width)) or (not snake[0].y in range(0, HEIGHT - height)):
        win.fill((255, 255, 255))
        font = pygame.font.SysFont("Arial", 50, True, False)
        font1 = pygame.font.SysFont("Arial", 100, True, False)
        text = font1.render(f"You Lose!", False, (255, 0, 0))
        text1 = font.render(f"Your Final Score: {len(snake)}", False, (0, 0, 0))
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        win.blit(text1, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2 + text.get_height() + 5))
        pygame.display.update()
        gameover = True

pygame.quit()
