n = int(input('피라미드 층수를 입력 하시오: '))
star = 1
blank = n-1
if star<=n :
    for a in range(0, n) :
        print(' ' * blank + '*' * star)
        star = star + 2
        blank = blank - 1

#git bash로 수정된 문장