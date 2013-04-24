import sys
import pygame

def ln(length, angle, depth, s):
    

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

ln(
d.flip()
b = True
while b:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            b = False

