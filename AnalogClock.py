import pygame,sys,math,random
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("AnalogClock")
font = pygame.font.Font(None,24)
def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

pos_x = 300
pos_y = 250
radius = 200
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.fill((0,100,0))
    pygame.draw.circle(screen,(0,0,100),(pos_x,pos_y),radius,1)
    pygame.draw.circle(screen,(100,100,100),(pos_x,pos_y),10,0)
    for n in range(1,13):
        angle = math.radians(n*(360/12) - 90)
        num_x = math.cos(angle) * radius
        num_y = math.sin(angle) * radius
        print_text(font,int(num_x)+pos_x,int(num_y)+pos_y,str(n))
    pygame.display.update()
