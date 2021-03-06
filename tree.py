import pygame
import sys
import math
import random

def endPoint(start, length, angle):
    """Calculate endpoint of a line taht starts at loc, with a given length and angle"""
    return (round(start[0] + length*math.cos(angle)), 
            round(start[1] - length*math.sin(angle)))

def genAngle():
    """Generates an angle from pi10 to 2*pi/3"""
    return (2*math.pi/3 - math.pi/10) * random.random() + math.pi/10
    
def genLength(length):
    """makes a length from 1/2 to 5/6 of a branch in length"""
    return .333333 * random.random() * length + .5 * length

def dColor(color):
    return (max(min(color[0],255),0),
            max(min(color[1]+13,255),0),
            max(min(color[2]+1,255),0))
    

def drawTree(s, color, loc, length, angle, n):
    """Draws a segment of the tree, and then draws more"""
    if n > 0:
        ep = endPoint(loc, length, angle)
        pygame.draw.aaline(s, color, loc, ep, True)

        for x in range(random.randrange(2,5)):
            a = genAngle()
            if (random.random() > .5):
                a = -a
            drawTree(s, dColor(color), ep, genLength(length), angle+a/2, n-1)

def main():
    w = 512
    h = 512
    z = w,h
    d = pygame.display
    s = d.set_mode(z)
    pygame.draw.rect(s, (60,60,60), (0,0,w,h))
    
    #args
    if len(sys.argv) > 1:
        depth = int(sys.argv[1])
    else: 
        depth = 1
    drawTree(s, (0,0,50), (round(w/2),h), h/4, math.pi/2, depth)
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
