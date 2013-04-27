import sys
import pygame
import numpy as np
shift = np.array([0,-90]) #drawing offset for snowflake
angle = np.pi/3 #angle to turn at in the middle of each line
ROT = np.array([[np.cos(angle),-np.sin(angle)],
                [np.sin(angle), np.cos(angle)]]) #rotation matrix for turning vectors

def endPoint(start, length, angle):
    """Calculate endpoint of a line that starts at loc, with a given length and angle"""
    return np.array([round(start[0] + length*np.cos(angle)), 
                     round(start[1] - length*np.sin(angle))])


def ln(sp, ep, depth, s):
    """Draws a line of the koch snoflake"""
    global turn
    if depth == 0:
        pygame.draw.aaline(s, (0,128,128), (sp+shift).tolist(), (ep+shift).tolist())
    else:
        raw = (ep - sp)/3
        m1 = raw + sp #1/3 the distance of the line
        m2 = raw + m1 #2/3 the distance of the line 
        tip = m1 + np.dot(np.transpose(raw), ROT) #find the tip of the triangle after turning
        #using matrix multiplication

        #if we arent at the base case, substitute each line for four sublines
        ln(sp,  m1,  depth-1, s)
        ln(m1,  tip, depth-1, s)
        ln(tip, m2,  depth-1, s)
        ln(m2,  ep,  depth-1, s)
        
w = 800
h = 800
z = w,h
d = pygame.display
s = d.set_mode(z)
pygame.draw.rect(s, (0,0,0), (0,0,w,w))
#args
if len(sys.argv) > 1:
    depth = int(sys.argv[1])
else: 
    depth = 1

#build snowflake
#distance from walls the snowflake points start at
bound = 100 

#three edge points of the triangle
A = np.array([w/2,     bound])
B = np.array([w-bound, h-bound])
C = np.array([bound,   h-bound])

ln(A, B,  depth, s) #a
ln(B, C,  depth, s) #b
ln(C, A,  depth, s) #c

d.flip()
b = True
while b:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            b = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            b = False

