import numpy as np
import pygame
import sys
import math
import random

def endPoint(start, length, angle):
    return (round(start[0] + length*math.cos(angle)), 
            round(start[1] - length*math.sin(angle)))

def genAngle():
    """Generates an angle from pi/2 to pi/6"""
    return (2*math.pi/3 - math.pi/10) * random.random() + math.pi/10
    

def drawTree(s, loc, length, angle, n):
    if n > 0:
        ep = endPoint(loc, length, angle)
        pygame.draw.aaline(s, (255,150,255), loc, ep)
        a = genAngle()
        drawTree(s, ep, 2*length/3, angle+a/2, n-1)
        drawTree(s, ep, 2*length/3, angle-a/2, n-1)

def main():
    random.seed()
    w = 512
    h = 512
    z = w,h
    d = pygame.display
    s = d.set_mode(z)
    pygame.draw.rect(s, (0,0,0), (0,0,w,h))
    
    #args
    if len(sys.argv) > 1:
        depth = int(sys.argv[1])
    else: 
        depth = 1
    pygame.draw.rect(s, (0,0,0), (0,0,w,w))
    drawTree(s, (round(w/2),h), h/4, math.pi/2, depth)
    d.flip()
        
    b = True
    while b:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                b = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    b = False
                    
if __name__ == "__main__":
    main()
