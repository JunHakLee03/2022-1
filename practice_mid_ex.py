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

#print('*' * 3)

#print(' ' * 3, '*' * 1)
#print(' ' * 2, '*' * 3)
#print(' ' * 1, '*' * 5)
#print(' ' * 0, '*' * 7)

#print(10/3)
#print('%.2f' % (10/3))

#_age = 0
#print(_age)

#a = 0x10
#b = 0x10
#c = 0b10000
#print(a, b, c)

#d = input()
#print(int(d))
#print(int(d, 2))
#print(int(d, 8))
#print(int(d, 16))

#print('"Welcome to my world"')
#print('Welcome to my world')
#print("'I am your friend'")
#print("I am your friend")

#print( True == 'True' )
#print( "True" == 'True' )
#print('Good' == 'Good')
#print(True == 3>2)
#print(True == (3>2))
#print(3>1 == False)
#print(3>0 == False)

#n = int(input('수 입력: '))
#if n == True :
#    print('Good')
#else:
#    print('Bad')

#print( not False == False )
#print((not False)==False)
#print(not 1 == 2)
#print((not 1)==2)
#print((not 0)==1)
#print(not 1 ==1)

#n = int(input('정수 입력: '))
#if n & 0b1 == 1:
#    print('Good')
#else:
#    print('Nice')

#print(bin(15))
#print(bin(~15))


#a = 3
#a += a
#print(a)

#a = 14
#print(bin(a))
#a |= 0b1
#print(bin(a))

#a = int(input('정수를 입력: '))
#print('Hello' if a & 0b1 != 1 else 'Welcome')

#print(False == 0 )
#print(True == 1)
#print((not 1)==0)

#print(~0b1)
#print(~1)
#print(~10)
#print('Good'=='Good')


#if False:
#    print("good ")
#print('Morning')

#if True:
#    print("Good ")
#else:
#    print('Morning')
#    print('Luck')

#for _ in range(3):
#    print('morning')
#    for j in range(2):
#        print('good')

#total = 0
#while True:
#    n = int(input('수 입력: '))
#    if n == -1:
#        break
#    elif n%2 != 0 :
#        total -= n
#    total += n
#print('짝수의 총 합: ', total)

#lst = [ 1, 2, 3, 4 ]
#for i in lst[:3]:
#    print(i, end = '-순위 ')
#print(lst[-1])

#data = [1, 2, 3, 4, 5, 6, 7, 8]
#data[2:5] = [9]
#print(data)

#friend = ('hong', 20, 'M', [189, 69], [True, 'good'])
#some = [list(friend[1:2]), list(friend[4:])]
#print(some)

#myinfo = {'name':'hong', 'age':20, 'height':178, 'weight':69}
#lst = []
#for (k,v) in myinfo.items():
#    print(v)

#score = {'ko':90, 'ma':99, 'eng':88}
#points = [ i for i in score.values()]
#print(points[2])

#lst = []
#total = 0
#nofn = 0
# while True:
#    n = int(input('양수를 입력'))
#    if n > -1:
#        lst.append(n)
#        nofn = nofn + 1
#    elif n == -1:
#        break
#    elif n < -1:
#        pass
#if nofn == 0:
#    print('입력된 데이터 없음')
#else:
#    for i in lst:
#        total = total + i
#    print(total/nofn)




#dic = {}
#total = 0
#while True:
#    lec = str(input('과목명: '))
#    score = input('점수를 입력: ')
#    if lec == '':
#        break
#    else:
#        dic[lec] = int(score)
#        total = total + int(score)

#print(dic)
#print(len(dic))
#print(total/len(dic))
#for i in dic:
#    print(i,'( ', dic[i], ') : ', '*' * (dic[i] // 10))


#def calcTotal(lst):
#    total = 0
#    for e in lst:
#        total = total + e
#    return total

#total = calcTotal([1,2,3,4,5])
#print(total)

#def output(*v, end = '\n'):
#    for e in v:
#        print(e, end = ' ')
#    print(end = end)

#output(1, end=':')
#output(2, end=':')
#output(3)

#def calcSumAvg(*n):
#    total = 0
#    nofn = 0
#    for i in n:
#        if i >= 0 and i <= 100 :
#            total = total + i
#            nofn = nofn + 1
#        else:
#            pass
#    print(total, total / nofn )

#calcSumAvg(4, 6, 4, 6)

def piramid(n):
    for i in range(0, n):
        print(' ' * (n - i - 1), '*' * (i * 2 - 1))

piramid(10)