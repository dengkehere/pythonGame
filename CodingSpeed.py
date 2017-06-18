import random

import pygame
import sys
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Keyboard Demo")

font1 = pygame.font.Font(None,24)
font2 = pygame.font.Font(None,20)
white = 255,255,255
yellow = 255,255,0
correct_answer = random.randint(97,122)
seconds = 11
score = 0
clock_start = 0
game_over = False
def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_RETURN]:
        if game_over:
            score = 0
            seconds = 11
            clock_start = time.clock()
            game_over = False
            correct_answer = random.randint(97, 122)

    current = time.clock() - clock_start
    speed = score * 60
    if seconds - current <= 0:
        game_over = True
    else:
        if keys[correct_answer]:
            correct_answer = random.randint(97,122)
            score += 1
    screen.fill((0, 100, 0))
    print_text(font1, 0, 0, "Let`s see how fast you can type!")
    print_text(font2, 0, 20, "Try to keep up for 10 seconds...")
    print_text(font1, 500, 0, "Key: "+ chr(correct_answer))
    if game_over:
        print_text(font1,0,160,"Press Enter to start...")
    if not game_over:
        print_text(font1,0,80, "Time: "+str(seconds - current))
    print_text(font1, 0 ,100,"Speed: " + str(speed) + " letters/min")
    pygame.display.update()

