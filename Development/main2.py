import sys
import pygame
from pygame.locals import *
import random
from time import sleep

defaultPlayerSprite = pygame.image.load("../Art/spr_Player.png")
defaultAppleSprite = pygame.image.load("../Art/spr_Apple.png")

# Necessary setup before you can start using pygame functionalities:
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

CLOCK   = pygame.time.Clock()
FPS     = 30

BG_COLOUR = [0, 0, 0]
IS_RUNNING = True

class Apple:
    gives_points = 0
    sprite = None
    rectangle = None

    def __init__(self, _gives_points, x = random.randint(0, SCREEN_WIDTH),  y = random.randint(0, SCREEN_HEIGHT), _sprite = defaultAppleSprite):
        self.gives_points = _gives_points
        self.sprite = _sprite
        self.rectangle = _sprite.get_rect()
        self.rectangle.x = x
        self.rectangle.y = y

    def Draw(self):
        SCREEN.blit(self.sprite, self.rectangle)

class Player:
    lives = 0
    points = 0
    speed = 0
    sprite = None
    rectangle = None

    def __init__(self, _lives, _speed, _sprite = defaultPlayerSprite):
        self.lives = _lives
        self.speed = _speed
        self.sprite = _sprite
        self.rectangle = _sprite.get_rect()

    def Update(self):
        #Player Movement
        KEYS_DOWN = pygame.key.get_pressed()

        if (KEYS_DOWN[K_UP]):
            print(str(self.rectangle.y))
            if(self.rectangle.y >= 0):
                self.rectangle.y -= self.speed
        elif (KEYS_DOWN[K_DOWN]):
            print(str(self.rectangle.y))
            if(self.rectangle.y <= SCREEN_HEIGHT - 50):
                self.rectangle.y += self.speed

        if (KEYS_DOWN[K_LEFT]):
            print(str(self.rectangle.x))
            if(self.rectangle.x >= 0):
                self.rectangle.x -= self.speed
        elif (KEYS_DOWN[K_RIGHT]):
            print(str(self.rectangle.x))
            if(self.rectangle.x <= SCREEN_WIDTH - 30):
                self.rectangle.x += self.speed

    def Draw(self):
        SCREEN.blit(self.sprite, self.rectangle)

player = Player(10, 5)

apples = []

#Add 3 apples
for i in range(3):
    apples.append(Apple(5))
    sleep(1)

for apple in apples:
    print("apple x: " + str(apple.rectangle.x) + " y: " + str(apple.rectangle.y))

while IS_RUNNING:
    # ------------------------------------------------
    # EVENT HANDLING:
    # ------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False


    # ------------------------------------------------
    # UPDATE GAME LOGIC:
    # ------------------------------------------------
    player.Update()
    

    # ------------------------------------------------
    # DRAWING INSTRUCTIONS
    # ------------------------------------------------
    SCREEN.fill(BG_COLOUR)
    #Draw player
    player.Draw()
    #Draw apples
    for apple in apples:
        apple.Draw()
    pygame.display.flip()


    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)
