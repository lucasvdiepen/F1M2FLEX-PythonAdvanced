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

    def __init__(self, _sprite, Screen, _x = -1, _y = -1):
        self.sprite = _sprite
        self.rectangle = _sprite.get_rect()
        if(_x == -1 and _y == -1): self.SetRandomPosition(Screen)
        else:
            self.rectangle.x = _x
            self.rectangle.y = _y

    def SetRandomPosition(self, Screen):
        self.rectangle.x = random.randint(0, Screen[0] - 30)
        self.rectangle.y = random.randint(0, Screen[1] - 50)

    def Draw(self, _screen):
        _screen.blit(self.sprite, self.rectangle)

class Apple(BaseObject):
    gives_points = 0

    def __init__(self, _gives_points, Screen, _sprite = defaultAppleSprite, x = -1,  y = -1):
        super().__init__(_sprite, Screen, x, y)
        self.gives_points = _gives_points
        

class Player(BaseObject):
    lives = 0
    points = 0
    speed = 0

    def __init__(self, _lives, _speed, Screen, _sprite = defaultPlayerSprite, x = -1, y = -1):
        if(x == -1 and y == -1):
            x = Screen[0] / 2
            y = Screen[1] / 2
        super().__init__(_sprite, Screen, x, y)
        self.lives = _lives
        self.speed = _speed

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

    def CollisionCheck(self):
        #check if player collided with apples
        for i in range(len(apples) - 1, -1, -1):
            if(self.rectangle.colliderect(apples[i].rectangle)):
                self.points += apples[i].gives_points
                apples.pop(i)
                
        

player = Player(10, 5, SCREEN_SIZE, pygame.image.load("../Art/spr_Player2.png"))

apples = []

#Add 3 apples on random position
for i in range(3):
    apples.append(Apple(5, SCREEN_SIZE))

while IS_RUNNING:

    #Get player input
    KEYS_DOWN = pygame.key.get_pressed()

    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False


    #Update game
    player.Update(KEYS_DOWN)

    #Check for collisions
    player.CollisionCheck()
    
    #Draw
    SCREEN.fill(BG_COLOUR)

    #Draw player
    player.Draw(SCREEN)

    #Draw apples
    for apple in apples:
        apple.Draw(SCREEN)

    #Draws points on screen
    text_surface = myfont.render("Points: " + str(player.points), False, (255, 255, 255))
    SCREEN.blit(text_surface, (10, 5))

    pygame.display.flip()

    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)
