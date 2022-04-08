import turtle
import random

BAR_WIDTH = 20
scores = [88, 80, 95, 100, 75, 65]
turtle = turtle.Turtle()

def drawXYaxis( nOfScore ):
    xOrg = - (nOfScore * 2 + 1) * BAR_WIDTH / 2
    yOrg = - 100
    turtle.penup()
    turtle.goto(xOrg, yOrg )
    turtle.pendown()
    turtle.forward( (nOfScore * 2 + 1) * BAR_WIDTH )
    turtle.goto(xOrg, yOrg )
    turtle.setheading( 90 )
    turtle.forward( 210 )
    for i in range(0,11) :
        turtle.penup()
        turtle.goto(xOrg, i * 20 + yOrg )
        turtle.pendown()
        turtle.setheading( 180 )
        turtle.forward( 10 )
    return xOrg, yOrg # 막대 그래프의 원점 좌표를 반환

def drawBar( xOrg, yOrg, data ) :
    for i in range( 0, len(data) ) :
        turtle.penup()
        turtle.goto( xOrg + (i * 2 + 1) * BAR_WIDTH , yOrg )
        turtle.pendown()
        turtle.fillcolor( random.random(), random.random(), random.random() )
        turtle.begin_fill()
        turtle.setheading( 90 )
        turtle.forward( data[i] * 2 )
        turtle.write( str( data[i] ) )
        turtle.right( 90 )
        turtle.forward( BAR_WIDTH )
        turtle.right( 90 )
        turtle.forward( data[i] * 2 )
        turtle.end_fill()

    turtle.hideturtle()
    
xorg, yorg = drawXYaxis( len( scores ) )
print( xorg, yorg )
drawBar( xorg, yorg, scores )
