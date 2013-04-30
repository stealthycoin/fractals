import pygame
import sys
import numpy as np
    

scale = 0.5*np.sqrt(2)
dangle = np.pi / 4

ROT1 = np.array([[np.cos(dangle), -np.sin(dangle)],
                [np.sin(dangle),   np.cos(dangle)]])
ROT2 = np.array([[np.cos(-dangle), -np.sin(-dangle)],
                [np.sin(-dangle),   np.cos(-dangle)]])

def dColor(color):
    return (max(min(color[0]-8,255),0),
            max(min(color[1]+2,255),0),
            max(min(color[2]-1,255),0))
    
def drawTree(s, pts, size, angle, color, n):
    """Draws a segment of the tree, and then draws more"""
    if n >= 0:
        shift = np.array([size*np.cos(angle),
                          size*-np.sin(angle)])

        pygame.draw.polygon(s, color, [pts[0],
                                       pts[0]+shift,
                                       pts[1]+shift,
                                       pts[1]])

        v = pts[0] - pts[1]
        v *= scale
        v1 = np.dot(ROT2, np.transpose(v))
        pts1 = np.array([pts[0]+v1,
                         pts[0]])
        drawTree(s, pts1, size*scale, angle + dangle, dColor(color), n-1)

        
        v2 = np.dot(ROT1, np.transpose(v))
        pts2 = np.array([pts[0]+v2+v2,
                         pts[0]+v2])

        drawTree(s, pts2, size*scale, angle - dangle, dColor(color), n-1)


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

    size = h/4
    offset = 10
    pts = (np.array([w/2-size/2, h-size-offset]), #top left
           np.array([w/2-size/2, h-offset])) #bottom left



    drawTree(s, pts, size, 0, (116,86,16), depth)
    d.flip()

    #save to disk
    if args['s'] != None:
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
