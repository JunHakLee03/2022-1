print('0~15중 한가지 숫자를 생각해주세요')


#비트 0의 값이 1인 수 중 생각한 수가 있지 확인

print('아래 수 중 생각한 수가 있나요? 네/아니요로 답해주세요')
for a in range(0, 16) :
    if a & 0b1 == 0b1 :
        print( a )

while True :

    answer_bit0 = input( '답: ' )
    if answer_bit0 == '네' :
        answer_bit0 = '1'
        break
    elif answer_bit0 == '아니요' :
        answer_bit0 = '0'
        break
    else :
        print('네/아니요로 답해주세요')


#비트 1의 값이 1인 수 중 생각한 수가 있지 확인

print('아래 수 중 생각한 수가 있나요? 네/아니요로 답해주세요')
for a in range(0, 16) :
    if a & 0b10 == 0b10 :
        print( a )

while True :

    answer_bit1 = input( '답: ' )
    if answer_bit1 == '네' :
        answer_bit1 = '1'
        break
    elif answer_bit1 == '아니요' :
        answer_bit1 = '0'
        break
    else :
        print('네/아니요로 답해주세요')


#비트 2의 값이 1인 수 중 생각한 수가 있지 확인

print('아래 수 중 생각한 수가 있나요? 네/아니요로 답해주세요')
for a in range(0, 16) :
    if a & 0b100 == 0b100 :
        print( a )

while True :

    answer_bit2 = input( '답: ' )
    if answer_bit2 == '네' :
        answer_bit2 = '1'
        break
    elif answer_bit2 == '아니요' :
        answer_bit2 = '0'
        break
    else :
        print('네/아니요로 답해주세요')


#비트 3의 값이 1인 수 중 생각한 수가 있지 확인

print('아래 수 중 생각한 수가 있나요? 네/아니요로 답해주세요')
for a in range(0, 16) :
    if a & 0b1000 == 0b1000 :
        print( a )

while True :

    answer_bit3 = input( '답: ' )
    if answer_bit3 == '네' :
        answer_bit3 = '1'
        break
    elif answer_bit3 == '아니요' :
        answer_bit3 = '0'
        break
    else :
        print('네/아니요로 답해주세요')


#답 추출

answer = '0b' + answer_bit3 + answer_bit2 + answer_bit1 + answer_bit0
answer = int(answer, 2)
print('당신이 생각한 수는 ', answer, '입니다.')