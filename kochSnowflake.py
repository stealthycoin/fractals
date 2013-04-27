import math
import sys
import pygame

def endPoint(start, length, angle):
    """Calculate endpoint of a line taht starts at loc, with a given length and angle"""
    return (round(start[0] + length*math.cos(angle)), 
            round(start[1] - length*math.sin(angle)))


def ln(sp, length, angle, depth, s):
    if depth > 0:
        pygame.draw.aaline(s, (255,255,255), sp, endPoint(sp, length / 3, angle))
        ln(sp, length / 3, angle + math.pi / 3, depth - 1, s)
        pygame.draw.aaline(s, (255,255,255), endPoint(sp, 2.0*length/3.0, angle), endPoint(sp, length, angle))



w = 512
z = w,w
d = pygame.display
s = d.set_mode(z)
pygame.draw.rect(s, (0,0,0), (0,0,w,w))
#args
if len(sys.argv) > 1:
    depth = int(sys.argv[1])
else: 
    depth = 1

ln((5,w+10),w-10,0,2,s)
d.flip()
b = True
while b:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            b = False

