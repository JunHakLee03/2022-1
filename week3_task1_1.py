#비트 0의 값이 1인 수 출력
print('비트 0의 값이 1인 수는 ')
for a in range(0, 16) :
    if a & 0b1 == 0b1 :
        print( a )
print('입니다.')

#비트 1의 값이 1인 수 출력
print('비트 1의 값이 1인 수는 ')
for a in range(0, 16) :
    if a & 0b10 == 0b10 :
        print( a )
print('입니다.')

#비트 2의 값이 1인 수 출력
print('비트 2의 값이 1인 수는 ')
for a in range(0, 16) :
    if a & 0b100 == 0b100 :
        print( a )
print('입니다.')

#비트 3의 값이 1인 수 출력
print('비트 3의 값이 1인 수는 ')
for a in range(0, 16) :
    if a & 0b1000 == 0b1000 :
        print( a )
print('입니다.')