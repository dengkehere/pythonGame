import pygame,sys,random,math
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Analog Clock")
screen.fill((0,0,100))
font = pygame.font.Font(None,24)
pos_x = 300
pos_y = 250
radius = 200
angle = 360

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        angle += 1
        if angle >=360:
            angle = 0
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = r, g, b

        x = math.cos( math.radians(angle)) * radius + pos_x
        y = math.sin( math.radians(angle)) * radius + pos_y
        pygame.draw.circle(screen,color,(int(x),int(y)),10,0)
        print angle
        pygame.display.update()