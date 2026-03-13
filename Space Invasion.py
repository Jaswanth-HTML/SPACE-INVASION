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
py.display.set_icon("🛸")

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