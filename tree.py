from turtle import *
from time import sleep

ht()
speed('fastest')
left(90)
bgcolor("black")
colormode(255)

def c(p):
    if 0 > round(p[0]*0.001*255+100):
        c1=0
    else:
        c1 = round(abs(round(p[0]*0.001*255+100)))

    if 0 > round(p[1]*0.001*255+100):
        c2=0
    else:
        c2 = round(abs(round(p[1]*0.001*255+100)))
    
    if 0 > round(p[0]*-0.001*255+100):
        c3=0
    else:
        c3 = round(abs(round(p[0]*-0.001*255+100)))
        
    return (c1,c3,c2)

def tree(size, levels, angle,m):
    tracer(0,0)  #comment these lines out to visualize when calculations are done 
    
    if levels == 0:
        return 
        
    forward(size)
    color(c(pos()))
    right(angle)
    tree(size*m,levels-1,angle,m)
    left(angle*2)
    tree(size*m,levels-1,angle,m)
    right(angle)
    
    up()
    backward(size)
    down()
    
    update() #comment these lines out to visualize when calculations are done

up()
sety(-427) # change to your screen -res/2
down()
tracer(0,0)
color(c(pos()))
tree(160,19,32,0.8)
update()

mainloop()
