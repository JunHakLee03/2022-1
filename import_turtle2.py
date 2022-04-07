#펜 제어 전까지
import turtle
import time
t = turtle.Turtle()

#radius = 100
#t.penup()
#t.sety( - radius )
#t.pendown()
#t.circle( radius )
#t.circle( radius, steps=6 )
#t.penup()
#t.sety( - radius / 2 )
#t.pendown()
#t.circle( radius / 2, extent=180 )

#t.write( 'Hello World', move=False, align= 'left' , font=('Arial', 8, 'normal') )

import turtle
import time
shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic' ]
radius = 100
t = turtle.Turtle()
for shape in shapes :
    t.reset()
    t.write( shape, font=('굴림', 20, 'bold') )
    t.shape( shape )
    t.penup()
    t.sety( - radius )
    t.pendown()
    t.circle( radius )
    t.circle( radius, steps=6 )
    t.penup()
    t.sety( - radius / 2 )
    t.pendown()
    t.circle( radius / 2, extent=180 )
    time.sleep( 2 )

    

