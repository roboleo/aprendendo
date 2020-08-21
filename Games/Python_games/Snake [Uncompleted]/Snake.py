import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube():
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color(255,0,0)):
        pass

class snake(object):
    def __init__(self, color, row)
        self.color = color 
        self.head = cube(pos)
        self.body = []
        self.turns = {}
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.R_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.R_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.R_UP]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.R_DOWN]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        for i,c in enumerate(self, body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i==len(self.body) -1:
                    self.turns.pop(p)
            else:
                

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y=0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        pygame.draw.line(surface, (255, 255, 255), (x,0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

        
def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()


def main():
    global width, rows, height
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    #n = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(win)
        

main()