# Get Pygame
import pygame
pygame.init()

# Initialize Window
WIDTH = 852
HEIGHT = 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
win.fill((255, 255, 255))


class player(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.origy = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def render(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))

            else:
                win.blit(walkLeft[0], (self.x, self.y))

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # Draw Hitbox: pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)\

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = self.origy
        self.walkCount = 0
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("-5", 1, (255, 0, 0))
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(1)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def render(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('Gamedata/R1E.png'), pygame.image.load('Gamedata/R2E.png'), pygame.image.load('Gamedata/R3E.png'), pygame.image.load('Gamedata/R4E.png'), pygame.image.load('Gamedata/R5E.png'), pygame.image.load('Gamedata/R6E.png'), pygame.image.load('Gamedata/R7E.png'), pygame.image.load('Gamedata/R8E.png'), pygame.image.load('Gamedata/R9E.png'), pygame.image.load('Gamedata/R10E.png'), pygame.image.load('Gamedata/R11E.png')]
    walkLeft = [pygame.image.load('Gamedata/L1E.png'), pygame.image.load('Gamedata/L2E.png'), pygame.image.load('Gamedata/L3E.png'), pygame.image.load('Gamedata/L4E.png'), pygame.image.load('Gamedata/L5E.png'), pygame.image.load('Gamedata/L6E.png'), pygame.image.load('Gamedata/L7E.png'), pygame.image.load('Gamedata/L8E.png'), pygame.image.load('Gamedata/L9E.png'), pygame.image.load('Gamedata/L10E.png'), pygame.image.load('Gamedata/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def render(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # Draw Hitbox: pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel

            else:
                self.vel = self.vel * -1
                self.walkCount = 0

        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel

            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1

        else:
            self.visible = False


# Initialize Clock and Characters
projectiles = []
shootLoop = 0
height = 64
width = 64
vel = 5
score = 0
font = pygame.font.SysFont("sanserif", 30, True, False)
character = player(WIDTH / 2, HEIGHT - (height + vel), height, width, vel)
enemy = enemy(WIDTH / 5, HEIGHT - (height + vel), width, height, WIDTH - 50)
clock = pygame.time.Clock()

# Get Images
walkRight = [pygame.image.load('Gamedata/R1.png'), pygame.image.load('Gamedata/R2.png'), pygame.image.load('Gamedata/R3.png'), pygame.image.load('Gamedata/R4.png'), pygame.image.load('Gamedata/R5.png'), pygame.image.load('Gamedata/R6.png'), pygame.image.load('Gamedata/R7.png'), pygame.image.load('Gamedata/R8.png'), pygame.image.load('Gamedata/R9.png')]
walkLeft = [pygame.image.load('Gamedata/L1.png'), pygame.image.load('Gamedata/L2.png'), pygame.image.load('Gamedata/L3.png'), pygame.image.load('Gamedata/L4.png'), pygame.image.load('Gamedata/L5.png'), pygame.image.load('Gamedata/L6.png'), pygame.image.load('Gamedata/L7.png'), pygame.image.load('Gamedata/L8.png'), pygame.image.load('Gamedata/L9.png')]
bg = pygame.image.load('Gamedata/bg.jpg')
char = pygame.image.load('Gamedata/standing.png')

# Get Sounds
bulletSound = pygame.mixer.Sound("GameData/bullet.wav")
hitSound = pygame.mixer.Sound("GameData/hit.wav")

music = pygame.mixer.music.load("GameData/music.mp3")
pygame.mixer.music.play(-1)


# Render Function
def render():
    # Render background
    win.blit(bg, (0, 0))

    # Render Character
    character.render(win)

    # Render Enemy
    enemy.render(win)

    # Render Text
    text = font.render(f"Score: {score}", 1, (0, 0, 0))
    win.blit(text, (WIDTH - (10 + text.get_width()),  10))

    # Render Projectiles
    for projectile in projectiles:
        projectile.render(win)

    # Refresh Display
    pygame.display.update()


# Set up the loop
run = True
while run:
    # FPS
    clock.tick(27)

    if character.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and character.hitbox[1] + character.hitbox[3] > enemy.hitbox[1] and enemy.visible:
        if character.hitbox[0] + character.hitbox[2] > enemy.hitbox[0] and character.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
            character.hit()
            score -= 5

    if shootLoop > 0:
        shootLoop += 1

    if shootLoop > 5:
        shootLoop = 0

    # window closed?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Projectiles
    for bullet in projectiles:
        if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1] and enemy.visible:
            if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                enemy.hit()
                hitSound.play()
                score += 1
                projectiles.pop(projectiles.index(bullet))

        if bullet.x < WIDTH and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            projectiles.pop(projectiles.index(bullet))

    # Move Character
    keys = pygame.key.get_pressed()  # Keys Pressed
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if character.left:
            facing = -1
        else:
            facing = 1

        if len(projectiles) < 10:
            projectiles.append(projectile(round(character.x + character.width // 2), round(character.y + character.height // 2) + 5, 6, (255, 0, 0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and character.x > character.vel:
        character.x -= character.vel
        character.left = True
        character.right = False
        character.standing = False

    elif keys[pygame.K_RIGHT] and character.x < WIDTH - character.width - character.vel:
        character.x += character.vel
        character.right = True
        character.left = False
        character.standing = False

    else:
        character.standing = True
        character.walkCount = 0

    if not character.isJump:
        if keys[pygame.K_UP]:
            character.isJump = True

    else:
        if character.jumpCount >= -10:
            neg = 1
            if character.jumpCount < 0:
                neg = -1

            character.y -= (character.jumpCount ** 2) * 0.5 * neg
            character.jumpCount -= 1

        else:
            character.isJump = False
            character.jumpCount = 10

    # Render
    render()
pygame.quit()