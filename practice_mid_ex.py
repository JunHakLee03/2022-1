#s1 = '%6d %-6d' % (10, 20)
#s2 = '%7.2f : %07.2f' % (3.14, 4.14)
#s3 = '%6x : %6x' % (0xf, 15)
#print(s1)
#print(s2)
#print(s3)

#s='0b01001'
#print(int(s, 2))

#n = True
#m = 'True'
#print(n, type(n))
#print(m, type(m))

#a = 2 > 3
#b = 2 < 4
#print(a, b)

#n = '홍길동\n\\ \' \" \n '
#print(n)

#n = -1
#m = 1
#n = n >> 1
#m = m >> 1
#print(n, bin(n))
#print(m, bin(m))
#n, m = n >> 1, m >> 1
#print(n, bin(n))
#print(m, bin(m))
#n , m = n << 2 , m << 2
#print(n, bin(n))
#print(m, bin(m))

#total = 0
#for i in range(0, 100) :
#    if i % 5 != 0:
#        continue
#    total += i

#print('Total= ', total)


#n = 10
#m = (4 + 6)
#p = (10)
#q = (4+6,)
#r = (10,)
#print(type(n))
#print(type(m))
#print(type(p))
#print(type(q))
#print(type(r))

#def area(w, h) :
#    return w * h

#print( area(2, 3) )

#version = 1.0

#def newVersion(v) :
#    version = v
#    print( 'My version = %.1f' % version )

#def printVersion() :
#    print('Hello.Current ver. : %.1f' % version )

#printVersion()
#newVersion( 1.5 )
#printVersion()


#number = 0
#check = 1
#for a in range (0, 4):
#    for i in range (1, 16) :
#        if i & check != 0 :
#            print(i, end=" ")
#    print('생각한 숫자가 있나')
#    answer = input('Y/N: ')
#    while True :
#        if answer == 'Y' :
#            number = number | check
#            break
#        elif answer == 'N' :
#            break
#        else:
#            answer = input('Y/N으로 대답하시오: ')
#    check = check * 2
#print('예측: ', number)

#import turtle
#import random
#import math
#t = turtle.Turtle()

#def drawsquare(x):
#    for _ in range(0, 4):
#        t.forward(x)
#        t.left(90)
#    t.home

#def drawcircle(radius, extent = 90, color = 'Blue'):
#    t.penup()
#    t.goto(radius, 0)
#    t.pendown
#    t.left(90)
#    t.pencolor(color)
#    t.circle(radius, extent)

#x = 0
#y = 0
#number = 0
#def getrandxy():
#    global x
#    global y
#    x = random.randint(0, 200)
#    y = random.randint(0, 200)

#def getsqrt(x, y):
#    return math.sqrt(x ** 2 + y ** 2)

#drawsquare(200)
#drawcircle(200)

#for _ in range(0, 500):
#    getrandxy()
#    if getsqrt(x, y) <= 200:
#        number = number + 1
#        t.penup
#        t.goto(x, y)
#        t.pendown
#        t.dot(3, 'Red')

#print(number)

#print(1+2, 1-2, 2*3, 5/3, 10%3)

#n1 = float(input())
#n2 = float(input())
#print(n1 + n2, n1 - n2, n1 * n2, n1 / n2)

