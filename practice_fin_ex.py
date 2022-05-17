#파일
#file_variable = open(파일명, 모드)
#r(read), w(write), r+(read/write)
#a(append)
#t(text file), b(binary file)
#file_variable.close()

#화면 출력 
#print()
#파일 출력
#file_variable.write(문자열)
#file_variable.writelines(문자열_리스트)

########################

#import random

#tfile = open('data.txt', 'w')
#for i in range(0, 5):
#        tfile.write(str(random.randint(0,100)) +' ')
        ##문자열로 변환 해야 함! 
#tfile.close()
#print('End of Program')

########################

#lst = ['Good', 'Morning', '좋은 아침\n']

#myFile = open('test.txt', 'w')

#myFile.write('뭐하니?\n')
#myFile.writelines(lst)

#myFile.close()

#print('File Write End... ')

########################

#키보드 입력 
# input(): 문자열 반환
#파일 입력 
# file_variable.read() 모든 문자 읽음
# file_variable.read(n) n개 문자 읽음
# file_variable.readline() 한 줄 읽음
# file_variable.readlines() 모든 줄 읽어서 리스트 반환

########################

#rfile = open('test.txt', 'r')
#done = False

#while not done :
#    linedata = rfile.readline()
#    if linedata == '':
#        done = True
#    else:
#        print(linedata, end='')

#rfile.close

#########################

#file = open('data.txt', 'r')
#nums = file.read().split()

#total = 0

#for n in nums:
#    print(n)
#    total += int(n)

#print('Total = %d' % total)

########################

#바이너리 파일 binary file
#바이트 단위로 파일 저장, 읽기

#저장한 데이터를 바이트열로 변환
#struct 모듈의 pack() 이용
#stuct.pack(fmt, v1, v2, v3, ...)
# 인자: 
    #fmt: 변환할 형식, 정수 - i, 실수 - d
    #v1, v2, v3: 변환할 값
# 반환: 바이트 스트림
#문자열은 encode() 이용
#string.encode()
#string.encode('utf-8')

#이진 파일에서 읽은 바이트열을 원래 데이터로 복원
#수 데이터는 stuct 모듈의 unpack() 이용
# 인자:
    #fmt: 변환할 형식, 정수 - i, 실수 - d
    #data: 데이터로 복원할 바이트 스트림
# 반환: 복원된 데이터 튜플
#문자열은 decode() 이용
#string.decode()
#string.decode('utf-8')

########################

#포맷 문자열

#데이터-바이트 간 변환 방법
#바이트 순서 지정
    #여러 바이트로 표현되는 데이터를 위한 변환된 바이트 순서
#포맷 문자열의 첫번째 글자로 지정
    # < : 리틀 엔디언 (역순)
    # > : 빅 엔디언 (순차)
    # # : 네트워크(빅 엔디언)
    # @ : 프로세서에 종속(생략시 기본, x86, AMD)

#형식: n(반복 수)Z(형식 문자)
#예) struct.pack('>ih', 1, -1)

#######################

#ustr ='\u03b8\u2022'
#print(len(ustr), ustr)
#bb = ustr.encode('utf-8')
#print(bb)
#print(bb.decode('utf-8'))

#######################

#이진 파일 데이터 입출력
#파일 열기 - open()에서 'rb' 또는 'wb' 사용
#파일 읽기/쓰기 - read()/write()
#파일 닫기 - close()

#######################

sampleString = 'Good Moring'

bfile = open('str.bin', 'wb')
bfile.write(sampleString.encode())
bfile.close()

bfile = open('str.bin', 'rb')
data = bfile.read().decode()
print(data)
bfile.close()

#######################

