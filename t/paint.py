'''
for i in range(1,4):
    for j in range(1,5):
        print("*",end='')
    print()'''#长方形

'''
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()'''#直角三角形

'''
for i in range(5,0,-1):
    for j in range(1,i+1):
        print('*',end='')
    print()'''#倒直角三角形或者如下

'''
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()'''#另一种方法

'''
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print()'''#并列for循环——等腰三角形

#菱形
'''raw = eval(input("请输入行数："))
while raw%2 == 0:
    print("重来")
    raw = eval(input("请输入行数："))
top_raw = int((raw+1)/2)
for i in range(1,top_raw+1):
    for j in range(1,top_raw-i+1):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print()#上半部分的等腰三角形
low_raw = raw-top_raw
for i in range(1,low_raw+1):
    for k in range(1,i+1):
        print(' ',end="")
    for j in range(1,2*(low_raw-i+1)):
        print('*',end='')
    print()#下半部分的倒等腰三角形
'''

'''
line = int(input("请输入菱形的行数:"))
while line%2==0:
    print("请输入奇数")
    line = int(input("请输入菱形的行数:"))
top_line = int((line+1)/2)
for i in range(1,top_line+1):
    for j in range(1,top_line-i+1):
        print(" ",end='')
        if j == top_line-i:
            print('*')
    for k in range(1,3):
        print("*",end=' '*(2*i-1))
    print()
'''


'''空心菱形
raw = eval(input("请输入行数："))
while raw%2 == 0:
    print("重来")
    raw = eval(input("请输入行数："))
top_raw = int((raw+1)/2)
for i in range(1,top_raw+1):
    if i == 1:
        print(' '*(top_raw-2),'*')
    else:
        for j in range(1,top_raw-i+1):
            print(' ',end='')
        for k in range(1,3):
            print('*',end=' '*(2*i-3))
        print()#上半部分的等腰三角形
low_raw = raw-top_raw
for i in range(1,low_raw+1):
    if i == low_raw:
        print(' '*(top_raw-2),'*')
    else:
        for k in range(1,i+1):
            print(' ',end="")
        for j in range(1,3):
            print('*',end=' '*(2*low_raw-2*i-1))
        print()
'''


