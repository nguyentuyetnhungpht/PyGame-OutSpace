import pygame

#init pygame
pygame.init()

#Create window
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 550
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Title and icon
pygame.display.set_caption("Star War")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#define color
BACKGROUND_COLOR = (0, 0, 0)


#Player
playerSize = 32
playerIMG = pygame.image.load('player.png')
playerX = 223
playerY = 500
playerChange = 0

def Player(x, y):
    #Draw Image
    screen.blit(playerIMG, (x, y))

#Game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #check keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChange = -0.1
            if event.key == pygame.K_RIGHT:
                playerChange = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChange = 0

    playerX += playerChange
    if playerX <= 0:
        playerX = 0
    if playerX >= SCREEN_WIDTH - playerSize:
        playerX = SCREEN_WIDTH - playerSize
    Player(playerX, playerY)
    pygame.display.update()
    #pygame.display.update() // ok but slow


pygame.quit()