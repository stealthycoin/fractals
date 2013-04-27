import pygame
import sys

def midpoint(a, b):
    return ((a[0]+b[0])/2.0,(a[1]+b[1])/2.0)


def drawTriangle(s, col, a, b, c):
    pygame.draw.polygon(s, col, (a,b,c), 0)

def sierpinskiTri(s,col,a,b,c,n):
    if n <= 0:
        drawTriangle(s,col,a,b,c)
    else:
        ab = midpoint(a,b)
        bc = midpoint(b,c)
        ac = midpoint(a,c)

        sierpinskiTri(s,col,a,ab,ac,n-1)
        sierpinskiTri(s,col,b,ab,bc,n-1)
        sierpinskiTri(s,col,c,ac,bc,n-1)
        

def main():
    w = 800
    h = 600
    z = w,h
    d = pygame.display
    s = d.set_mode(z)
    pygame.draw.rect(s, (60,60,60), (0,0,w,h))
    
    #args
    if len(sys.argv) > 1:
        depth = int(sys.argv[1])
    else: 
        depth = 1
    
    sierpinskiTri(s,(255,204,0),(w/2,50),(50,h-50),(w-50,h-50),depth)

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
