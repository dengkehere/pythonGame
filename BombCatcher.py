import sys
import pygame
import random
from pygame.locals import *
import  time
pygame.init()

class Vector:
    def __init__(self,dirx,diry,speed):
        self.dirx = dirx
        self.diry = diry
        self.speed = speed

class Catcher:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def left_move(self,dis = 30):
        self.x -= dis
        if self.x < 0:
            self.x = 0
    def right_move(self,dis = 30):
        self.x += dis
        if self.x + self.width >600:
            self.x = 600 - self.width

class Bomb:
    def __init__(self,x,y,radius):
        self.radius = radius
        self.x = x
        self.y = y
        self.position = (x,y)
        self.vector = self.init_vector()
        self.last_move = time.clock()

    def init_vector(self):
        dir = [1, -1]
        x = dir[random.randint(0, 1)]
        y = 1
        speed = 5
        return Vector(x, y, speed)
    def move(self,catcher):
        if time.clock() - self.last_move < 0.05:
            return
        self.x += self.vector.dirx*self.vector.speed
        self.y += self.vector.diry*self.vector.speed
        self.collision_detection(catcher)
        self.last_move = time.clock()
    def collision_detection(self,catcher):
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vector.dirx *= -1
        if self.x + self.radius > 600:
            self.x = 600 - self.radius
            self.vector.dirx *= -1
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vector.diry *= -1
        if self.y + self.radius > 500:
            self.y = 500 - self.radius
            self.vector.diry *= -1
        if self.x + self.radius > catcher.x and self.x - self.radius < catcher.x + catcher.width and self.y + self.radius > catcher.y:
            self.vector.diry *= -1;

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("BombCatcher")
bomb = Bomb(100,20,10)
catcher = Catcher(random.randint(0,500),480,80,20)
left_move = right_move = True
while True:
    screen.fill((100, 100, 100))
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    pygame.draw.circle(screen,(100,0,0),(bomb.x,bomb.y),bomb.radius)
    pygame.draw.rect(screen,(0,100,0),(catcher.x,catcher.y,catcher.width,catcher.height))
    keys = pygame.key.get_pressed()
    if keys[K_a] == False:
        left_move = True
    if keys[K_d] == False:
        right_move = True
    if keys[K_a] and left_move:
        catcher.left_move()
        left_move = False
        print "left_move"
    if keys[K_d] and right_move:
        catcher.right_move()
        right_move = False
        print "right_move"
    bomb.move(catcher)
    pygame.display.update()