from time import sleep

import pygame
import sys
import math
from pygame.locals import *
pygame.init()

modePosition = 600,500
screen = pygame.display.set_mode(modePosition)
pygame.display.set_caption("The Pie Game - Press 1,2,3,4")
myfont = pygame.font.Font(None,60)
bgcolor = 155,155,155
pie1 = False
pie2 = False
pie3 = False
pie4 = False

circleCenter = modePosition[0]/2,modePosition[1]/2
pieColor = 100,100,100
pieWidth = 10
pieRadius = 200
piePosition = circleCenter[0] - pieRadius, circleCenter[1] - pieRadius, pieRadius*2, pieRadius*2

def drawPieNum(numContent,numPositon,numColor=pieColor):
    textImg = myfont.render(numContent,True,numColor)
    screen.blit(textImg,numPositon)

def drawPie(start_angle,end_angle,endPosition1,endPosition2):
    start_angle = math.radians(start_angle)
    end_angle = math.radians(end_angle)
    pygame.draw.line(screen,pieColor,circleCenter,endPosition1,pieWidth)
    pygame.draw.line(screen,pieColor,circleCenter,endPosition2,pieWidth)
    pygame.draw.arc(screen,pieColor,piePosition,start_angle,end_angle,pieWidth)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYUP and event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_1:
                pie1 = True
            elif event.key == pygame.K_2:
                pie2 = True
            elif event.key == pygame.K_3:
                pie3 = True
            elif event.key == pygame.K_4:
                pie4 = True

        screen.fill(bgcolor)
        #draw pie num
        drawPieNum("1",(circleCenter[0] + pieRadius/2 , circleCenter[1] - pieRadius/2))
        drawPieNum("2",(circleCenter[0] - pieRadius/2 , circleCenter[1] - pieRadius/2))
        drawPieNum("3",(circleCenter[0] - pieRadius/2 , circleCenter[1] + pieRadius / 2))
        drawPieNum("4",(circleCenter[0] + pieRadius/2 , circleCenter[1] + pieRadius / 2))

        #draw pie
        if pie1:
            drawPie(0, 90, (circleCenter[0] + pieRadius, circleCenter[1]), (circleCenter[0], circleCenter[1] - pieRadius))
        if pie2:
            drawPie(90, 180, (circleCenter[0], circleCenter[1] - pieRadius), (circleCenter[0] - pieRadius, circleCenter[1]))
        if pie3:
            drawPie(180, 270, (circleCenter[0] - pieRadius, circleCenter[1]), (circleCenter[0], circleCenter[1] + pieRadius))
        if pie4:
            drawPie(270, 360, (circleCenter[0], circleCenter[1] + pieRadius), (circleCenter[0] + pieRadius, circleCenter[1]))
        if pie1 and pie2 and pie3 and pie4:
            pieColor = 0, 255, 0
        #screen.blit(textImage,(100,100))
        pygame.display.update()
