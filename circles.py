import pygame
import sys
import numpy as np
import random as r


def shiftR(rad):
    angle = 2 * np.pi * r.uniform(0,1)
    return np.array([rad * np.cos(angle),
                     rad * np.sin(angle)])
                


def drawCircle(s, color, center, radius, n):
    if n > 0:
        drawCircle(s, color, center + shiftR(radius), radius/2, n-1)
        drawCircle(s, color, center + shiftR(radius), radius/2, n-1)
        drawCircle(s, color, center + shiftR(radius), radius/2, n-1)
        drawCircle(s, color, center + shiftR(radius), radius/2, n-1)
    else:
        c = (int(center.tolist()[0]), int(center.tolist()[1]))
        pygame.draw.circle(s, color, c, int(radius), 2)


def argHandler(arglist):
    arguments = {}
    key = "program"
    for argument in arglist:
        if key == None and argument.startswith("-"):
            key = argument[1:]
            arguments[key] = None
        elif key != None:
            arguments[key] = argument
            key = None
    return arguments
    
def useArg(args, key, default=None):
    try:
        return args[key]
    except KeyError:
        return default

def main():
    args = argHandler(sys.argv)
    w = int(useArg(args, 'w', 800))
    h = int(useArg(args, 'h', 800))
    z = w,h
    d = pygame.display
    s = d.set_mode(z)
    pygame.draw.rect(s, (60,60,60), (0,0,w,h))
    
    depth = int(useArg(args, 'depth', 1))

    drawCircle(s, (100,0,188), np.array([w/2, h/2]), w/2, depth)
    drawCircle(s, (188,0,100), np.array([w/2, h/2]), w/2, depth)
    drawCircle(s, (100,200,188), np.array([w/2, h/2]), w/2, depth)
    drawCircle(s, (116,86,16), np.array([w/2, h/2]), w/2, depth)
    d.flip()

    #save to disk
    if useArg(args, 's') != None:
        pygame.image.save(s, args['s'])
    
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
