import time

from helloworld.abstrct import *

print("===========1=============")
if True:
    print("True")
else:
    print("False")
print("===========2=============")

# name = input("please enter your name:")
# print('hello,', name)

print("===========3=============")

print('1024*768 = ', 1024 * 768)

print("===========4=============")

a = -100
if a >= 0:
    print(a)
else:
    print(-a)

print("===========5=============")

print(
    '''
    dfgh
    sdfg
    sdfg
    sdg
    '''
    "sadfa\\sdsa'f dfg %sf" "  asdf"

)

print("===========5=============")

n = 123
f = 456.789
s1 = 'Hello, world \n'
s2 = 'Hello, \'Adam\'\n'
s3 = r'Hello, "Bart" \n '
s4 = r'''Hello,Lisa!'''
s5 = '123' + \
     '456' + \
     '789'

print(n,
      f,
      s1,
      s2,
      s3,
      '\n',
      s4,
      s5,
      '\n'
      '   asdf' '   asdf' ' sd' " asdfasdf"
      )

print("===========6=============")

print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print('中文'.encode('utf-8'))
print('\u4e2d\u6587')
str_th_1 = "ร้อ"
str_th_2 = "วันที่ 8 เดือน 8 วันเหมียวครองโลก มาร่วมแชร์ช่วงเวลาสนุกๆ ไปกับเรา Kitty Live"
str_th_3 = "8 เดือน 8 วันเหมียวครองโลก แบ่งปันช่วงเวลาพิเศษ ความสดใส พูดคุย ร้องเพลงสนุกสนานไปด้วยกันกับความสามารถที่หลากหลาย ด้วยการถ่ายทอดผ่าน Kitty Live"
str_th_4 = "สายแบ๊วห้ามพลาด! Kitty Face ฟังก์ชั่นใหม่ เพิ่มสีสันในการ Live ของคุณให้สนุกสนานมากขึ้น จัดเลย"
print(len(str_th_1))
print(len(str_th_1.encode('utf-8')))
print(len(str_th_3))
print(len(str_th_2.encode('utf-8')))
print("str_th_4 = ", len(str_th_4.encode('utf-8')))

print("===========7=============")

print('Hello, %s' % 'world')

print('Hi, %s, you have $%s.' % ('Hcool', 10000000.001))

print('%.1f' % ((85 - 72) / 72 * 100))

print("===========7=============")

classmates = ['CatHcool', 'hcooll', 'Hcool']

print(len(classmates))

print(classmates[0])

print(classmates[-1])

s = ['Cat', classmates, 'Hcool']

print(len(s))

print(s[1][1][0])

print(s[2][1])

classmates.sort()

print(classmates)

'''
这是tuple
'''
t = (1, 'sdfas', classmates)

print(t)

print("===========8=============")

print(my_abs(-3))

print("===========9=============")

ticks = time.time()

print("当前的时间戳是：", ticks)

localTime = time.asctime(time.localtime(ticks))

print("当前的时间是：", localTime)

inta = -2147485647

print(inta)
