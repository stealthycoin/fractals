import sys
import pygame
import numpy as np

def even(n):
    if n % 2 == 0:
        return 1
    return 0

def odd(n):
    return  (even(n) + 1) % 2

def drawLine(s, color, start, end, n):
    if n >= 0:
        length = np.linalg.norm(end - start)
        shift = np.array([even(n)*length/(2*np.sqrt(2)), 
                          odd(n)*length/(2*np.sqrt(2))])
        pygame.draw.line(s, color, start, end)


        drawLine(s, color, start + shift, start - shift, n - 1)
        drawLine(s, color, end + shift, end - shift, n - 1)
        

def main():
    w = 500
    h = 300
    z = w,h
    d = pygame.display
    s = d.set_mode(z)
    pygame.draw.rect(s, (60,60,60), (0,0,w,h))
    
    #args
    if len(sys.argv) > 1:
        depth = int(sys.argv[1])
    else: 
        depth = 1


    drawLine(s, (0,200, 100), np.array([w/4.0, h/2.0]), np.array([w/4.0+w/2.0,h/2.0]), 2*depth+1)
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
