import pygame as py
import random as rd
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

py.init()

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = py.image.load("Bg Space Image.png")

py.display.set_caption("Space Invader")
icon = py.image.load("U.F.O. Image.png")

player_image = py.image.load("Space Fighter Ship Image.png")
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemy_image = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enimies = 6

for _i in range(num_of_enimies):
    enemy_image.append(py.image.load("Alien Image.png"))
    enemyX.append(rd.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(rd.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bullet_image = py.image.load("Bullet Image.png")
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

score_value = 0
font = py.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

over_font = py.font.Font('freesansbold.ttf', 32)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y) )
 
def game_over_text():
    over_text = over_font.render("!GAME!OVER!", True, (255, 255, 255))
    screen.blit(over_text, (200, 255))

def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

running = "True"
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    for event in py.event.get():
        if event.type == py.QUIT:
            running = "False"
        if event.type == py.KEYDOWN:
            if event.type == py.K_LEFT:
                playerX_change = -5
            if event.type == py.K_RIGHT:
                playerX_change = 5
            if event.type == py.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == py.KEYUP and event.key in [py.K_LEFT, py.K_RIGHT]:
            playerX_change = 0
        
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

    for i in range(num_of_enimies):
        if enemyY[i] > 340:
            for j in range(num_of_enimies):
                enemyY[j] = 2000
            game_over_text()
            break
    
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        if is_collision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = rd.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = rd.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    py.display.update()