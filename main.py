import pygame
import random
import math

from pygame import mixer

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
enemyIMG = []
enemyX = []
enemyY = []
enemyChangePosX = []
enemyChangePosY = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH))
    enemyY.append(random.randint(50, SCREEN_HEIGHT - (SCREEN_HEIGHT / 2)))
    enemyChangePosX.append(0.05)
    enemyChangePosY.append(20)


def Enemy(x, y, i):
    # Draw Image
    screen.blit(enemyIMG[i], (x, y))


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
def isCollision_Enemy_Bullet(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 28:
        return True
    else:
        return False

# def isCollision_Enemy_Player(enemyX, enemyY, playerX, playerY):
#     distance = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
#     if distance < 28:
#         return True
#     else:
#         return False


#SCORE
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 25)
textX = 10
textY = 10
def Show_Score(x, y):
    text = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(text, (x, y))



#Sound
mixer.music.load('background.wav')
mixer.music.play(-1) #-1 play alway

#GAME OVER
over = pygame.font.Font('freesansbold.ttf', 40)

def Show_Over():
    text = over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH/2 - 110, SCREEN_HEIGHT/2-50))


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
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
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


    # Bullet Moverment
    if bulletY <= 0:
        bulletY = 480
        bullet_State = 'ready'
    if bullet_State is 'fire':
        fire_Bullet(bulletX, bulletY)
        bulletY -= bulletChangePosY * 2

    # Enemy moving
    for i in range(num_of_enemies):
        #Game over
        if enemyY[i] > (SCREEN_HEIGHT-100):
            for j in range(num_of_enemies):
                enemyY[j] = 1000
            Show_Over()
            break

        enemyX[i] += enemyChangePosX[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - enemySize:
            enemyChangePosX[i] *= -1
            enemyY[i] += enemyChangePosY[i]
        #Collision_Bullet
        collision_bullet = isCollision_Enemy_Bullet(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision_bullet:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_State = 'ready'
            enemyX[i] = random.randint(0, SCREEN_WIDTH-enemySize)
            enemyY[i] = random.randint(50, SCREEN_HEIGHT - (SCREEN_HEIGHT / 2))
            score_value += 1
        # # Collision_Player
        # collision_player = isCollision_Enemy_Player(enemyX[i], enemyY[i], playerX, playerY)
        # if collision_player:
        #     enemyX.remove(i)
        #     enemyX.remove(i)

        #Draw enemy
        Enemy(enemyX[i], enemyY[i], i)

    # Draw on screen
    Player(playerX, playerY)
    Show_Score(textX, textY)
    pygame.display.update()
    # pygame.display.update() // ok but slow

pygame.quit()
