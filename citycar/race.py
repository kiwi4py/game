#-*- coding:utf-8 -*-
import time

import pygame, sys
from pygame.locals import *

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255, 255, 0)
GRAY = (96, 96, 96)

pygame.init()
#pygame.mixer.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((300, 187))
pygame.display.set_caption('小汽车')


carimg = pygame.image.load('car.png')
hornimg = pygame.image.load('horn.png')
cityimg = pygame.image.load('city.jpg')
direction = 'right'
carx = 10
cary= 150

def drawlight(color):
    if color == RED:
        pygame.draw.circle(DISPLAYSURF, RED,  (290, 150), 10, 0)
    if color == GREEN:
        pygame.draw.circle(DISPLAYSURF, GREEN,  (290, 150), 10, 0)
    if color == YELLOW:
        pygame.draw.circle(DISPLAYSURF, YELLOW,  (290, 150), 10, 0)

def changelight(color):
    print 'color1', color
    if color == RED:
        color = GREEN
    elif color == GREEN:
        color = YELLOW
    else:
        color = RED
    print 'color2', color
    return color

def drawcar(carx, cary):
    DISPLAYSURF.blit(carimg, (carx, cary))

def drawhorn():
    DISPLAYSURF.blit(hornimg, (50, 100))
        
color = GREEN

while True:
    DISPLAYSURF.fill(WHITE)
    drawlight(color)
    drawhorn()
    for i in range(0, 10000):
        if direction == 'right':
            carx += 5
            if carx == 300:
                direction = 'left'
        elif direction == 'left':
            carx -= 5
            if carx == 10:
                direction = 'right'
        if i % 1000 == 0:
            drawcar(carx, cary)
    color = changelight(color)
    pygame.time.wait(100)
    
    pygame.time.wait(100)
    
    color = changelight(color)
    DISPLAYSURF.blit(cityimg, (0, 0))
    drawcar(carx, cary)
    drawlight(color)
        
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #pygame.mixer.music.load('horn.mp3')
            #pygame.mixer.music.play(-1, 0.0)
            #pygame.mixer.music.stop()
            pass
            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
