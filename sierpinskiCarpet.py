import sys
import pygame

def sq(dim, level, s):
    if level == 0:
        return
    else:
        x,y,w,h = dim
        w3, h3 = w/3, h/3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    pygame.draw.rect(s, (255,255,255), (x+w3,y+h3,w3,h3))
                else:
                    sq((x+i*w3,y+j*h3,w3,h3), level-1, s)

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
sq((0,0,w,w), depth, s)
d.flip()
b = True
while b:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            b = False

