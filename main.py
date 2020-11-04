import pygame
import random
import math

# init pygame
pygame.init()

# Create window
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and icon
pygame.display.set_caption("Star War")
icon = pygame.image.load('icontitle.png')
pygame.display.set_icon(icon)

# define color
BACKGROUND_COLOR = (0, 0, 0)

# Background image
backgroundIMG = pygame.image.load('background.jpg')

# Player
playerSize = 48
playerIMG = pygame.image.load('player.png')
playerX = 225
playerY = 445
playerChangeX = 0


def Player(x, y):
    # Draw Image
    screen.blit(playerIMG, (x, y))


# Enemy
enemySize = 28
enemyIMG = pygame.image.load('enemy.png')
enemyX = random.randint(0, SCREEN_WIDTH)
enemyY = random.randint(50, SCREEN_HEIGHT - (SCREEN_HEIGHT / 2))
enemyChangePosX = 0.05
enemyChangePosY = 20


def Enemy(x, y):
    # Draw Image
    screen.blit(enemyIMG, (x, y))


# Bullet
# Read - not display on screen
# Fire - displayed
bulletSize = 16
bulletIMG = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 445
bulletChangePosX = 0
bulletChangePosY = 0.1
bullet_State = "ready"


def fire_Bullet(x, y):
    global bullet_State
    bullet_State = "fire"
    # Draw Image
    screen.blit(bulletIMG, (x + (playerSize / 2 - bulletSize / 2), y))

#Check distance
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 28:
        return True
    else:
        return False

# Game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    screen.blit(backgroundIMG, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChangeX = -0.1
            if event.key == pygame.K_RIGHT:
                playerChangeX = 0.1
            if event.key == pygame.K_SPACE:
                if bullet_State is 'ready':
                    #Get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_Bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChangeX = 0

    # Move and Boundaries player
    playerX += playerChangeX
    if playerX <= 0:
        playerX = 0
    if playerX >= SCREEN_WIDTH - playerSize:
        playerX = SCREEN_WIDTH - playerSize

    # Enemy moving
    enemyX += enemyChangePosX
    if enemyX <= 0 or enemyX >= SCREEN_WIDTH - enemySize:
        enemyChangePosX *= -1
        enemyY += enemyChangePosY

    # Bullet Moverment
    if bulletY <= 0:
        bulletY = 480
        bullet_State = 'ready'
    if bullet_State is 'fire':
        fire_Bullet(bulletX, bulletY)
        bulletY -= bulletChangePosY
    #Collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_State = 'ready'

    # Draw on screen
    Enemy(enemyX, enemyY)
    Player(playerX, playerY)

    pygame.display.update()
    # pygame.display.update() // ok but slow

pygame.quit()
