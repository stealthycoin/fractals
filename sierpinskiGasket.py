from pygame import *


w=256
z=w,w
l=[z]
d=display
s=d.set_mode(z)
for e in l:
    x,y=e
    s.set_at(e,e+e)
    x/=2;y/=2
    l+=(x,y),(x,y+w),(x+w,y+w)
    d.flip()
