import pygame
import sys
from math import *

def ball(s,col,x,y,angle,d,r):
    if r < 1:
        return
    newAngle = angle + r * .01
    newDist = d + r * .23
    newRadius = r * .965

    ball(s,col,x,y,newAngle,newDist,newRadius)

    nx = int(d * cos(angle))
    ny = int(d * sin(angle))
    pygame.draw.circle(s,col,(int(x+nx),int(y+ny)),int(r))
    pygame.draw.circle(s,col,(int(x-nx),int(y-ny)),int(r))

def main():
    w = 800
    h = 800
    z = w,h
    d = pygame.display
    s = d.set_mode(z)
    pygame.draw.rect(s, (60,60,60), (0,0,w,h))
    
    #args
    if len(sys.argv) > 1:
        depth = int(sys.argv[1])
    else: 
        depth = 1
    
    RED = pygame.Color(255,0,0)

    
    ball(s,RED,int(w/2),int(h/2),0,40,40)
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
