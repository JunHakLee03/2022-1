#str = '2022Y'
#print(str.title())

###################

#name = ' Hong Gil Dong       \n'
#print(':' + name + ':')
#print(':' + name.strip() + ':')

####################

#import code


#name = 'Hong Gil Dong'
#number = '1 2 3'
#print(number.join(name))
#print(':' + name.center(20) + ':')
#print(':' + name.zfill(20) + ':')
#print(ord('a')) 
#ord는 문자 하나만 입력 받아 헤당 문자의 유니코드를 반환
#print(chr(ord('A')))

#####################

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

#sampleString = 'Good Moring'

#bfile = open('str.bin', 'wb')
#bfile.write(sampleString.encode())
#bfile.close()

#bfile = open('str.bin', 'rb')
#data = bfile.read().decode()
#print(data)
#bfile.close()

#######################

#import struct

#str = 'Good Morning'
#lst = [1, 2, 3, 4, 5, 6, 7]

#byteData = struct.pack('i', len(str))
#byteData += str.encode()
#byteData += struct.pack('i', len(lst))
#for d in lst:
#    byteData += struct.pack('i', d)

#file = open('bdata.bin', 'wb')
#file.write(byteData)
#file.close()

##########################

#import struct

#file = open('bdata.bin', 'rb')
#byteData = file.read()
#file.close()

#strlen = struct.unpack('i', byteData[:4])
#str = byteData[4:4+strlen[0]].decode()
#posIntData = 4 + strlen[0]
#nofInt = struct.unpack('i',
#posIntData[posIntData:posIntData+4])
#lst = struct.unpack('i'*nofInt[0], byteData[posIntData+4:])

#print(str)
#for d in lst:
#    print(d)

#############################    

#다시보자

#import struct
#age = 20
#name = '홍길동'
#height = 178.5
#en_name = name.encode('utf-8')
#fd =open('data.dat','wb')
#fd.write(struct.pack('if%ds' % len(en_name), age, height, en_name))
#fd.close()
#fd = open('data.dat','rb')
#readdata = fd.read()
#fd.close()
#strlen = len(readdata) - struct.calcsize('if')
#data = struct.unpack('if%ds' % strlen, readdata)
#print(data[0], data[1], data[2].decode('utf-8'))

#################################

#이진 파일 입출력
#pickle 모듈 이용
#-쓰기: pickle.dump(data, file_variable)
#-읽기: pickle.load(file_variable)

##################################

#import pickle

#bfile = open('test.bin', 'wb')

#pickle.dump(65, bfile)
#pickle.dump([1, 2, 3], bfile)
#pickle.dump('good', bfile)

#bfile.close()

##################################

#import pickle

#bfile = open('test.bin', 'rb')

#n = pickle.load(bfile)
#lst = pickle.load(bfile)
#s = pickle.load(bfile)

#print(n)
#print(lst)
#print(s)

#bfile.close()

##################################

#이진 파일 파트 전체적으로 다시 보기

##################################

#예외 처리
#종류 -NameError, ZeroDivisionError, FileNotFoundError, IndexError 등

##################################

#try :
#    file = open('data.txt', 'r')

#    lines = file.readlines()
#    for line in lines :
#        print(line)

#except FileNotFoundError :
#    print('파일 data.txt가 없음')

#else:
#    file.close()

#finally:
#    print('실행 완료')

###################################

#class 어떤 것을 특징(속성, 기능)에 따라 분류한 것

#클래스를 정의 할 때 필드와 메소드가 필요
#속성(필드) : 특징을 표현 할 수 있는 값
#기능(메소드) : 특징을 표현 할 수 있는 동작

#class Score:
    
#    def __init__(self):
#        self.point = 0

#    def get(self):
#        return self.point

#    def set(self, point):
#        self.point = point

#세 개의 메소드(기능)(__init__, get, set)
#한 개의 필드(속성)(point)

###########################

#class를 정의 한다고 실제 어떤 것이 만들어지는 것은 아님(설계도)
#객체 : 정의된 class를 이용한여 만든 어떤 것
#인스턴스

#obj = className()

#obj.method() #반환 값이 없는 경우

#variable = obj.method() #반환 값이 있는 경우

##############################
#class Score:
#    def __init__(self):
#        self.point = 0

#    def get(self):
#        return self.point

#    def set(self, point):
#        self.point = point

#lee = Score()
#lee.point = 88
#print(lee.get())
#lee.set(99)
#print(lee.get())

################################

#메소드는 객체 자신을 첫 번째 매개 변수로 받음
#홀출 할 때 전달하지 않아도 자동으로 전달

#생성자 : 객체 생성 시 자동으로 호출되는 메소드
#주요 목적: 인스턴스 필드 값 초기화
#메소드 처럼 매개변수를 가질 수 있음
#매개변수는 객체 생성 시 전달

#형태
#def __init__(self):
#    statement

################################

#필드의 종류

#클래스 필드: 클래스를 이용하여 모든 객체가 공유 
#메소드 외부에 있음
#className.variable 형태로 사용

#인스턴스 필드 : 각 객체마다 만들어지는 필드 
#객체가 공유 X
#self.variable 형태로 사용

#이름이 동일한 경우 인스턴스 필드 우선

###############################

#class Score:
#    point = 0
    
#    def __init__(self, point=99):
#        self.point = point
#        Score.point = Score.point + 1

#print(Score.point)
#myScore = Score()
#print(Score.point)
#yourScore = Score(100)
#print(Score.point)

#print(myScore.point)
#print(yourScore.point)
#print(Score.point)

##################################

#클래스 상속

#class className(super_class):
#    variable = init_value

#    def __init__(self, paraments):
#        statement

#    def methodName(self, parameters):
#        statement

#class Animal :
#    def sound(self):
#        return 'Unknown'

#class Dog(Animal):
#    def sound(self):
#        return '멍멍'

#class Cat(Animal):
#    def sound (self):
#        return '야옹'

#myPet = Dog()
#yourPet = Cat()
#pet = Animal()

#print(myPet.sound())
#print(yourPet.sound())
#print(pet.sound())

#############################

#윈도우 프로그래밍
#GUI 이용
#tkinter 모듈 이용

#from tkinter import *

#win = Tk() #루트 윈도우 또는 베이스 윈도우 반환

#win.mainloop() #윈도우의 각종 이벤트 처리

############################

#win.title(제목) #윈도우 제목

#win.geometry('widthxheigh+xpos+ypos') #기본 크기와 위치

#win.resizable(width=True, height=Flase) #크기 변경 가능 여부

#Label(window, 옵션) #문자, 이미지 출력
#옵션: 
# - text='문자열' 
# - font= ('폰트이름', 크기)
# - bg= '색깔', fg='색깔'
# - width=크기, height=크기
# - anchor= N, NE, E, SE, S, SW, W, NE, CENTER #anchor(고정시키다)(정렬)
# - image= image
#표시: pack()메소드 호출

##############################

#from tkinter import *
#import time
#class MyWin( Tk ):
#    def __init__(self):
#        super().__init__()
#        self.title('My Window')
#        self.geometry( '400x250' )

#win = MyWin()

#label = Label( win, text='무엇하니',bg='yellow',
#    font=('굴림',24 ),
#    width=20,height=5,anchor='s' )
#label.pack()

#win.mainloop()

##############################

#from tkinter import *

#def btnPress():
#    print('Button is Pressed')

#win = Tk()
#win.title('Sample Window')
#win.geometry('300x250')

#img = PhotoImage(file='img/img2.gif')
#lbName = Label(win, image = img)
#lbName.pack()
#btnTel = Button( win, text = '010-1234-1234,\
#    font=('Times', 30),command=btnPress )

#btnTel.pack()
#win.mainloop()

#################################

#Button(window, 옵션)
#-Label() 옵션과 동일
#command = function
#표시 pack()메소드 호출

##################################

#from tkinter import *

#def btnPress():
#    print('Button is Pressed.')

#win = Tk()
#win.title('sample window')
#win.geometry('300x150')
#win.resizable(width=False, height=True)
#lbName=Label(win, text='010-1234-1234', font=('Times',30))
#lbName.pack()
#btnTel=Button(win, text='010-1234-1234', \
#    font=('Times',30), command=btnPress)

#btnTel.pack()
#win.mainloop()

####################################

#Checkbutton(window, 옵션)
#Button()의 옵션과 동일
#variable = IntVar()_변수
#-버튼 상태를 나타내는 IntVar()의 변수: 선택 - 1, 해제 - 0
#-버튼의 상태를 알 수 있는 제어 변수(control vari.)
#-메소드 : get(), set()
#표시 : pack()메소드 호출

#####################################

#from tkinter import *
#def btnPress():
#    print('Button is Pressed.')
#    print(chk.get())
#win = Tk()
#win.title('Sample Window')
#win.geometry('300x150')
#win.resizable(width = False, height=True)
#lblTel = Label(win, text='010-1234-1234', font=('Times', 30))
#lblTel.pack()

#chk=IntVar()
#chkTel = Checkbutton(win, text='010-1234-1234', \
#    font = ('Times', 30), variable=chk, \
#        command=btnPress)

#chkTel.pack()
#win.mainloop()

#################################

#Radiobutton(window, 옵션)
#옵션: Checkbutton의 옵션과 동일
#variable = IntVar()_변수
#Radiobutton들을 모둠으로 모으는 제어 변수
#동일한 제어 변수를 갖는 Radiobutton은 한 모둠

#value=각_버튼의 값
#버튼이 선택 될 때 제어 변수에 저장될 값
#표시 pack()메소드 호출

###################################

#from tkinter import *
#def btnPress():
#    print('Button is Pressed.')
#    print(chk.get())

#win = Tk()
#win.title('Sample Window')
#win.geometry('300x150')
#win.resizable(width=False, height=True)
#chk = IntVar()
#chk.set(1)
#rbTel=Radiobutton(win, text='010-1234-1234',\
#    variable=chk, value=1, command=btnPress )
#rbTel.pack()
#rbName=Radiobutton(win, text='Hong Gil Dong',\
#    variable=chk, value=2, command=btnPress )
#rbName.pack()
#win.mainloop()

####################################

#Entry(window, 옵션)
#옵션: Label 옵션과 거의 동일
#border : 외곽선
#표시 : pack() 메소드 호출
#이 위젯 변수의 get() 메소드를 이용하여 입력한 문자열 반환

####################################

#from tkinter import *

#def keyin():
#    lbName.configure(text=enName.get())
#    enName.delete(0, len(enName.get()))

#win=Tk()
#win.title('Entry Tester')
#win.geometry('400x300')

#lbName = Label(win, text = 'Unknown')
#enName = Entry(win)
#btnGet=Button(win, text='GET', command=keyin)

#lbName.pack()
#enName.pack()
#btnGet.pack()

#win.mainloop()

###################################

#위젯.pack(배치옵션)
#side = LEFT(또는 RIGHT) : 좌측 정렬
#side = TOP(또는 BOTTOM)
#fill = X : 폭을 창의 크기에 맞춤
#fill = Y : 높이를 창의 크기에 맞춤
#padx=값, pady=값 : 위젯사이 여백
#ipadx=값, ipady=값 : 위젯 내 여백

###################################

#from tkinter import *
#blst = []
#win = Tk()
#win.geometry( '350x250' )

#for i in range(0,4):
#    blst.append(Button(win,text='button %d'%i, bg='#51FFA6'))
#    blst[-1].pack(side=LEFT, fill=Y, padx=10, pady=10)

#win.mainloop()

######################################

#고정 위치 배치
#위젯.place(x=xpos, y=yposd, width=폭, height=높이)

#from tkinter import *
#blst = []
#win = Tk()
#win.geometry( '350x250' )
#for i in range(0,4):
#    blst.append( Button(win,text='button %d'% i,bg='#51FFA6' ) )
#    blst[-1].place(x=i*10, y=i*55, height=50, width=200 )
#win.mainloop()

#########################################

#프레임: 다른 위젯을 포함 할 수 있는 사각 영역 위젯
#- 위젯 배치가 한 종류가 아닌 경우에 사용
#Frame(parent)
#표시: pack() 메소드 호출

#from tkinter import *

#w = Tk()
#w.title('GUI Test')
#w.geometry('300x200')

#lst = []
#for i in range(0, 5):
#    lst.append(Label(w, text = 'TEXT %d'%i))

#frame = Frame(w)

#lst.append(frame)

#b1 = Button(frame, text='BUTTON' )
#b2 = Button( frame, text='WHAT' )
#b1.pack(side=LEFT)
#b2.pack()

#for obj in lst :
#    obj.pack(side = BOTTOM)

#w.mainloop()

###############################

#이벤트
#종류: 클릭(아무 버튼, 왼쪽, 오른쪽, 휠)
#마우스 포인터가 위젯으로 들어 올 때
#마우스 포인터가 위젯에서 나갈 때
#키보드 키를 누를 때

#이벤트 처리
#위젯과 이벤트를 처리할 함수를 연결
#위젯.bind(이벤트코드, 처리함수)

#from tkinter import *

#def click(event):
#    print('Mouse Clicked : %d' %\
#        (event.num))

#def drag(event):
#    print('Mouse Drag : %dx%d' %\
#        (event.x, event.y))

#win = Tk()
#win.title('Event Handler')
#win.geometry('250x200')
#win.bind('<Button-1>', click)
#win.bind('<B1-Motion>', drag)

#win.mainloop()

##################################

#from tkinter import *

#def keyin(event):
#    print('Key in : ' + event.char)
#    if event.char == 'e':
#        exit()

#def main():
#    win = Tk()
#    win.geometry('400x300')
#    win.bind('<Key>', keyin)
#    Label(win, text='Key Event Tester').pack()
#    win.mainloop()

#main()

###################################

#메뉴
#menu = Menu(parent_widget)
#파라미터: parent_widget: 메뉴가 표시될 상위 위젯

#최상위 윈도에 메뉴 넣기
#-메뉴바 형태로 표현됨
#-Tk() 객체의 config() 메소드 이용
#win.config(menu=menu_obj)

#Menu의 서브메뉴 넣기
#menu.add_cascade(label='menu title', menu = menuobj)

#Menu의 메누 아이템 넣기
#선택하면 기능 실행
#menu.add_command(label='menu title', command=fn)

###############################

#메뉴 작성 단계

#1. Menu 위젯 생성
#-메뉴바로 사용할 위젯

#2. 최상위 윈도에 1에서 작성한 위젯 등록
#win.config(menu=menubar)

#3. Menu 위젯 생성
#menubar(or parentmenu).add_cascade(label='title str', menu=widget)
#menuwidget.add_command(label='title str', command=fn)

################################

from tkinter import *

topwin = None
def initwin():
    global topwin
    topwin = Tk()
    topwin.title( 'Menu Testing' )
    topwin.geometry( '300x250' )

def fn():
    print('Menu processing')

def mkmenu() :
    menubar = Menu( topwin )
    topwin.config( menu=menubar )

    filemenu = Menu( menubar )
    editmenu = Menu( menubar )

# for File menu
    filemenu.add_command( label='New', command=fn )
    projmenu = Menu( filemenu )
    projmenu.add_command( label='Save' )
    projmenu.add_command( label='Open' )
    filemenu.add_cascade( label='Project', menu=projmenu )
    filemenu.add_separator()
    filemenu.add_command( label='Exit', command=exit )

# for Edit menu
    editmenu.add_command( label='Copy', command=fn )
    editmenu.add_command( label='Cut' )
    editmenu.add_command( label='Paste' )

    menubar.add_cascade( label='File', menu=filemenu )
    menubar.add_cascade( label='Edit', menu=editmenu )

def apploop():
    topwin.mainloop()

if __name__ == '__main__' :
    initwin()
    mkmenu()
    apploop()
