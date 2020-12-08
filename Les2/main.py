import sys
import pygame
from pygame.locals import *
import random
from time import sleep

defaultPlayerSprite = pygame.image.load("../Art/spr_Player.png")
defaultAppleSprite = pygame.image.load("../Art/spr_Apple.png")

# Necessary setup before you can start using pygame functionalities:
pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

CLOCK   = pygame.time.Clock()
FPS     = 30

BG_COLOUR = [0, 0, 0]
IS_RUNNING = True

class BaseObject:
    sprite = None
    rectangle = None

    def __init__(self, _sprite = defaultPlayerSprite):
        self.sprite = _sprite
        self.rectangle = _sprite.get_rect()

    def Draw(self, _screen):
        _screen.blit(self.sprite, self.rectangle)

    def SetRandomPosition(self, Screen):
        self.rectangle.x = random.randint(0, Screen[0] - 30)
        self.rectangle.y = random.randint(0, Screen[1] - 50)

    def SetSpriteByPath(self, path):
        self.sprite = pygame.image.load(path)
        self.rectangle = self.sprite.get_rect()

    def PrintPosition(self):
        print(str(self.rectangle.x) + ", " + str(self.rectangle.y))

    def PrintObject(self):
        print("Dit object is een: ")

class Player(BaseObject):
    lives = 0
    points = 0
    speed = 0

    def __init__(self, _lives, _speed, _sprite = defaultPlayerSprite):
        super().__init__(_sprite)
        self.lives = _lives
        self.speed = _speed
        self.rectangle.x = SCREEN_WIDTH / 2
        self.rectangle.y = SCREEN_HEIGHT / 2

    def PrintPosition(self):
        print("Player position x: " + str(self.rectangle.x) + " y: " + str(self.rectangle.y))

    def PrintObject(self):
        super().PrintObject()
        print("Speler")

    def Update(self, KEYS_DOWN):
        #Player Movement

        if (KEYS_DOWN[K_UP]):
            if(self.rectangle.y >= 0):
                self.rectangle.y -= self.speed
        elif (KEYS_DOWN[K_DOWN]):
            if(self.rectangle.y <= SCREEN_HEIGHT - 50):
                self.rectangle.y += self.speed

        if (KEYS_DOWN[K_LEFT]):
            if(self.rectangle.x >= 0):
                self.rectangle.x -= self.speed
        elif (KEYS_DOWN[K_RIGHT]):
            if(self.rectangle.x <= SCREEN_WIDTH - 30):
                self.rectangle.x += self.speed

baseObject = BaseObject()

player = Player(10, 5, pygame.image.load("../Art/spr_Player2.png"))

baseObject.PrintPosition()

player.PrintPosition()

player.PrintObject()

while IS_RUNNING:
    #Get player input
    KEYS_DOWN = pygame.key.get_pressed()

    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False


    #Update game
    player.Update(KEYS_DOWN)
    
    #Draw
    SCREEN.fill(BG_COLOUR)

    #Draw player
    player.Draw(SCREEN)

    pygame.display.flip()

    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)
