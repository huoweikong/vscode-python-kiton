#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   snake.py
@Time    :   2020/02/07 01:21:07
@Author  :   Ai Qiangyun 
@Version :   1.0
@Contact :   1154282938@qq.com
@License :   (C)Copyright 2019
Device  :   Kiton vscode
'''

# here put the import lib
import sys, time, random, math, pygame
from pygame.locals import *
from pygame.sprite import Sprite
#from MyLibrary import *

class SnakeSegment(MySprite):
    def __init__(self, color=(20,200,20)):
        MySprite.__init__(self)
        imgae =  pygame.Surface((32,32)).covert_aplha()
        imgae.fill((255,255,255,0))
        pygame.draw.circle(image, color, (16,16), 16, 0)
        self.set_image(image)
        MySprite.update(self, 0, 30)

class Snake():
    def __init__(self):
        self.velocity = Point(-1,0)
        self.old_time = 0
        head = SnakeSegment((50,250,50))
        head.X = 12*32
        head.Y = 9*32
        self.segments = list()
        self.segments.append(head)
        self.add_segment()
        self.add_segment()
    def update(self,ticks):
        if ticks > self.old_time + 400:
            self.old_time = ticks
            for n in range(len(self.segments)-1, 0, -1):
                self.segments[n].X = self.segments[n-1].X
            self.segments[n].Y = self.segments[n-1].Y
        self.segments[0].X += self.velocity.x * 32
        self.segments[0].Y += self.velocity.y * 32
        
    def draw(self,surface):
        for segment in  self.segments:
            surface.blit(segment.image, (segment.X, segment.Y))
            
    def add_segment(self):
        last = lem(self.segments) - 1
        segment = SnakeSegment()
        start = Point(0,0)
        if self.velocity.x < 0: start.x =32
        elif self.velocity.x > 0: start.x = -32
        if self.velocity.y < 0: start.y = 32
        elif self.velocity.y > 0: start.y = -32
        segment.X = self.segments[last].X + start.x
        segment.Y = self.segments[last].Y + start.y
        self.segments.append(segment)
        
    for n in range(len(self.segments)-1, 0, -1):
        self.segments[n].X = self.segments[n-1].X
        self.segments[n].Y = self.segments[n-1].Y
class Food(MySprite):
    def __init__(self):
        MySprite.__init__(self)
        image = pygame.Surface((32,32)).convert_aplha()
        image.fill((255,255,255,0))
        pygame.draw.circle(image, (250,250,50),(16,16),16,0)
        self.set_image(image)
        MySprite.update(self,0,30)
        self.X  = random.randint(0,32) * 32
        self.Y  = random.randint(0,17) * 32
        
def game_init():
    global screen, backbuffer, font, timer, snake, food_group
    pygame.init()
    screen = pygame.display.set_mode((24*32,19*32))
    pygame.display.set_caption("Snake Game")
    font = pygame.font.Font(None,30)
    tiemr = pygame.time.Clock()
    
    backbuffer = pygame.Surface((screen.get_rect().width,screen.get_rect().height))
    snake = Snake()
    image = pygame.Surface((60,60)).convert_alpha()
    image.fill((255,255,255,0))
    pygame.draw.circle(image,(80,80,220,70),(30,30),30,0)
    pygame.draw.circle(image,(80,80,250,255),(30,30),30,4)



    food_group = pygame.sprite.Group()
    food = Food()
    food_group.add(food)
screen = pygame.display.set_mode((24*32,18*32))










        
        
        
        