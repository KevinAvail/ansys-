'''v = 5
g = 9.81
t = 0.6
y = v*t-0.5*g*t**2
print(f"{v},{g},{t},%3.2f" % (y))'''

'''c=-10

while c <= 20 :
    F = (9/5)*c+32
    print(F)
    c = c+10'''

#C = 21
#print((9/5)*C+32)

#print(type(9/5))
'''a = round(-4.5)
print(a)'''
#print(-9//5)
#print(-7%2)



'''import math as m
x = 1.2
y = m.sin(x)*m.cos(x)+4*m.log(x)
print(y)'''


'''C = 0
while C<100:
    F = (9/5)*C+32
    print(C,F)

    C = C+10'''

'''p = 17
lst = [2,3,5,7,11,13]
lst.append(p)
print(lst)'''

'''t = 1
while t<=37:
    if t%2==1:
        print(t)
    t = t+1'''

'''from math import *
print(sinh(2*pi))'''

'''from math import *
x = int(input("请输入x的值:"))
sinhx = 0.5*(exp(x*pi)-exp((-x)*pi))
print(sinhx)'''

'''from math import *
a =0.1
b = 0.2
c = a+b
e = 0.3
tol = 1E-15
print(abs(c-e)<tol)'''

'''while True:
    print("德丽莎世界第一可爱")'''

'''C = -20
while C<=40:
    F = (9/5)*C+32
    print(C,F)
    C = C+5'''

'''for c in range(-20,41,5):
    f = (9/5)*c+32
    print(c,f)'''

'''i,p = 1,1
while i<=12:
    p*=i
    i+=1
print(p)'''
#a = int(input("请输入："))
#b = int(input("请输入："))
#c = int(input("请输入："))
#d = int(input("请输入："))
#print(2,"sss",sep="\t\t")
#print(round(3,8))

#from math import *
'''x =int(input("请输入x的值:"))
v0 = 1500
theta = 60*pi/180
y0 = 3
g = 9.81
y = x*tan(theta)-(g*x**2)/(2*(v0**2)*(cos(theta))**2)+y0
print(f"""if v0={v0}m/s,theta={theta},y0={y0}m,x={x}m""")
print("%f" % (y))'''

'''v0 = 1500
theta = 60*pi/180
y0 = 3
g = 9.81
t = []
for x in range(1,100002,10000):
    y = x*tan(theta)-(g*x**2)/(2*(v0**2)*(cos(theta))**2)+y0
    t.append(y)
print(t)
'''


'''Cdegrees = [-5+i*2 for i in range(-5,20,5)]
Fdegrees = [(9/5)*C+32 for C in Cdegrees]
t1 = [Cdegrees,Fdegrees]
t2 = [[C,F] for C,F in zip(Cdegrees,Fdegrees)]
for a in range(len(Cdegrees)):
    print("%3d,%6.1f"%(t1[0][a],t1[1][a]))
for b in range(len(t2)):
    x,y = t2[b]
    print("%3d,%6.1f"%(x,y))
'''

#拷贝jj
# lst1 = ['a','b','c']
# lst2 = [1,2,3,4,5]
# lst2[:] = lst1[:]
# lst1[1] = "x"
# print(lst2)

'''
from math import log as ln
from math import *
def L(x, n):
    s = 0
    for i in range(1, n+1):
        s += (1.0/i)*(x/(1+x))**i
    error_fake = (1.0/(n+1))*(x/(1+x))**(n+1)
    error_exact = ln(x+1)-s
    return s,error_fake,error_exact
x = 5
print(L(x, 10), L(x, 100), ln(1+x))
'''

# 【问题描述】
# 角谷猜想：对于一个正整数，若它为偶数，则除以2，若它为奇数，则乘以3加1，得到一个新的自然数，反复计算下去，若干次后，得到的结果必然为1。完成函数cal的编写，该函数对自然数n进行角谷猜想验证，得到1则返回计算的次数，如果计算次数达到或超过200次都没得到1，则返回200。例如n为12时，计算过程为12，6，3，10，5，16，8，4，2，1，则函数返回9。（提示：如果n=1，则返回0）
#
# 【编程要求】
# 程序运行时，会多次读取键盘输入，并调用函数进行计算，当输入为end时，程序运行结束（见图1）；
# 键盘输入的是正整数，打印出的是函数的返回值；
# 测试用例见图1。

'''
def cal(n):
    i=0
    while n!=1:
        if n%2==0:
            n=n/2
            i+=1
        else:
            n=3*n+1
            i+=1
    if i>=200:
        return 200
    else:
        return i
N=input("请输入一个正整数：")
if N=='end':
    pass
else:
    N=int(N)
    while N<=0:
        print("请输入正整数！")
        N = int(input("请输入一个正整数"))
    print(cal(N))
'''

#模拟京东购物

'''
t=[]
for i in range(5):
    a=str(input("请输入商品的编号计及名称："))
    t.append(a)
for j in t:
    print(j)
cart=[]
while True:
    flag=False
    num=str(input("请输入商品的编号："))
    for i in t:
        if num ==i[0:4]:
            flag=True
            cart.append(i)
            print("已添加")
            break
    if not flag and num!='q':
        print("不存在")
    if num =='q':
        break
cart.reverse()
for k in cart:
    print("已选择的商品为：")
'''

#模拟12306订票

'''
dic={'G1569':["北京南—天津南",'18:06','18:39','00:33'],
     'G1567':["北京南—天津南",'18:15','18:49','00:34'],
     'G8917':["北京南—天津西",'18:20','19:19','00:59'],
     'G203':["北京南—天津南",'18:35','19:09','00:34']}  #车次
print("车次\t\t出发站—到达站\t出发时间\t到达时间\t历时时长")
for key,value in dic.items():
    print(key, end='\t')
    for i in value:
        print(i,end='\t')
    print()
num=str(input("请输入要购买的车次："))
ticket=[]
if dic.get(num)==None:
    print("没有这个车次")
else:
    ticket.extend(dic.get(num))
    passenger=str(input("请输入乘车人："))
    ticket.append("乘车人："+passenger)
if ticket!=None:
    print("您已购票成功",ticket)
'''



# x=input(":")
# code = f"""
# def f(x):
#     return {x} """
# print(exec("code"))
# import sys
#
# x=float(sys.argv[2])
# def StringFunction(expr, vars='x'):
#     return eval("lambda "+vars+":"+expr)
# def num_derivative(f, x, h=1E-5):
#     return (f(x+h) - f(x-h))/(2*h)
# from math import *
# f=StringFunction(sys.argv[1],'x')
# print(StringFunction(num_derivative(f,x)))


#***argparse库***
'''
import argparse
parser=argparse.ArgumentParser()#创建一个解析器
parser.add_argument("--v0",type=float,default=5.0,help="initial_velocity")
parser.add_argument("--t",type=float,default=1.0,help="time")
args=parser.parse_args()#读入命令行并解析参数
print(args.v0*args.t)
'''
#练习
'''
from math import *
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--x",type=float,default=1)
parser.add_argument("--g",type=float,default=9.81)
parser.add_argument("--v0",type=float,default=1500)
parser.add_argument("--y0",type=float,default=3)
parser.add_argument("--theta",default=pi/3)
args=parser.parse_args()
print('v0 = %.1f m/s, theta = %.1f radians, y0 = %.1f m, \
             x = %.1f m' % (args.v0, args.theta, args.y0, args.x) )
y = args.x*tan(args.theta) - 1/(2*args.v0**2)*args.g*args.x**2/((cos(args.theta))**2) + args.y0
print('y = %f m' %y)
'''

#***读取文件***
#1的位置   "C:\Users\lenovo\Desktop\1.txt"
'''

l = a.readlines()
k = a.readline()#读一行
print(l)
for l in a:
    print(l)
a.close()
'''

#给列表写进文件
'''
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
values = [467.7, 630.2, 172.8, 103.5, 102.1, 291.6, 0.0, 99.6, 33.3, 1584.5]
infile = open("rain.py",'w')
for i in range(10):
    infile.write(months[i]+" "+str(values[i])+"\n")
s=0
for k in values:
    s+=k
infile.write("Total"+" "+str(s))
infile.close()
'''

#异常处理
'''
try:
    a=float(input("请输入："))
except IndexError:
    print("……")
#如果try里面出现错误，程序会抛出一个一场让后进入except中执行，否则就会跳过except
except ValueError:
    print("shabi")
'''

# months={1:"January",2:"February",3:"Match",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
# year=int(input("请输入年份："))
# month=int(input("请输入月份："))
# print(months[month],year)
# print("Mon Tue Wed Thu Fri Sat Sun")
# days=[31,28,31,30,31,30,31,31,30,31,30,31]
# #if year%4 == 0:
# #   year[1]+=1
# cal=["  ","  "]
# for i in range(1,days[month-1]+1):
#     cal.append(i)   #2022年6月
# t=365*abs(year-2022)
# if year>2022:
#     for i in range(2023,year+1):
#         t+=1
#     dif=

'''
a=int(input('请输入年份：'))
b=int(input('请输入月份：'))
x1=[31,28,31,30,31,30,31,31,30,31,30,31]
x2=['January','February','March','April','May','June','July','August','September','October','November','December']
if (a%4==0 and a%100!=0 or a%400==0):
    x1[1]+=1
print(x2[b-1],a,'\nMon','Tue','Wed','Thu','Fri','Sat','Sun')
r=[' '*3]*(((a-1970)+len(list(filter(lambda x:x%4==0 and x%100!=0 or x%400==0,range(1970,a))))+sum(x1[:b-1])+3)%7)
for i in range(x1[b-1]):
    r.append('%3d'%(i+1))
for i in range(6):
    print(*r[7*i:7*i+7])
'''

'''
import sys
def read():
    try:
        c=float(sys.argv[1])
    except IndexError:
        raise IndexError("index")
    except ValueError:
        raise ValueError("value")
    return c
try:
    c=read()
except (IndexError,ValueError) as e:
    print(e)
    sys.exit(1)
'''
#C:\Users\lenovo\PycharmProjects\pythonProject1\t\课1.py



#输出a,b之间（包括a，b）的素数的个数
'''
a=int(input(":"))
b=int(input(":"))
num=0;delta=0.001
for i in range(a,b+1):
    if i==1:
        continue
    for j in range(2,int(i/2)+1):
        if (i/j)%1<delta: #i/j是整数
            break
    else:
        num+=1
print(num)
'''

'''
n=int(input("请输入一个大于2的正整数n:"))
num=1
if n%2!=0:
    n+=1
while n%2==0:
    if n==1:
        break
    else:
        n=n/2
        num+=1
        if n%2!=0 and n!=1:
            n+=1
print(num)
'''


#最小索引和
'''
def findNumber(list1,list2):
    number=0
    temp=dict({})
    for i in range(len(list1)):
        if list1[i] in list2:
            t=i+list2.index(list1[i])
            temp[t] = i
    number = list1[temp[min(temp.keys())]]
    return number
print(findNumber([1,3,5,11,6,9],[8,26,3,5]))
'''

#输出所有子集
'''
#循环
def powerset(input_set):
    result = [[]]
    # 在此处实现你的方法
    for element in input_set:
        result+=[subset+[element] for subset in result]
    return result
'''
'''
#递归方法
def powerset(input_set):
    result = []
    # 在此处实现你的方法
    # 基础情况：如果输入集为空，则返回包含空集的列表
    if not input_set:
        return [[]]

    # 拿出输入集中的第一个元素
    first = input_set[0]
    # 对剩余的元素递归求解幂集
    rest_powerset = powerset(input_set[1:])

    # 将当前元素添加到每个子集中
    subsets_with_first = [[first] + subset for subset in rest_powerset]

    # 返回包含不含当前元素的子集和含有当前元素的子集
    # rest_powerset: 不含当前元素的集合
    # subsets_with_first: 含当前元素的集合
    return rest_powerset+subsets_with_first
print(powerset([1,2,3]))
'''



#2023第三期第10题不会
# a,b=list(input().split())
# dif=dict({});temp=[]
# for i in range(len(a)):
#     if a[i] in b:
#         temp.append(i)
#     else:
#         if temp==[]:
#             pass
#         else:
#             dif[temp[-1]-temp[0]]=temp[0]
#             temp=[]
# k=dif[max(dif.keys())]
# print(a[dif[k]:dif[k]+k+1])




#2023第三期第9题
'''
def division():
#在下方添加代码
    assert apple>=kid
    i=apple//kid
    spare=apple-i*kid
    print(f"{apple}个苹果平均分给{kid}个小朋友，每人分{i}个，还剩{spare}个。")
#在上方添加代码
while True:
    apple = input("苹果的数量为?")
    kid = input("小朋友的数量为?")
    try:
        apple = int(apple)
        kid = int(kid)
        division()
    except(AssertionError):
        print('苹果数量少于小朋友数量')
    except:
        if apple == "end" or kid == "end":
            break
        else:
            print('apple和kid应该为整数')
'''




#2023第三期第4题
from math import *

'''
def square_numbers(n):

#在下方添加代码
    t=[]
    for i in range(n+1):
        for j in range(i+1):
            if i==j*j:
                t.append(i)
    return t
#在上方添加代码


testcase = [1,10,50,100,200]
for index in range(len(testcase)):
    L = square_numbers(int(testcase[index]))
    print(L)
# 预期输出
# [0, 1]
# [0, 1, 4, 9]
# [0, 1, 4, 9, 16, 25, 36, 49]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
'''


#【每日一题 2022/03/17】
'''
nums=list(map(int,input(":").split()))
target=int(input(":"))
def towsum(lst,m):
    import copy
    t=copy.deepcopy(lst)
    temp=[]
    for i in lst:
        t.remove(i)
        for j in t:
            if i+j==m:
                temp.append(lst.index(i))
                if i==j:
                    lst[lst.index(i)]=i+1
                    temp.append(lst.index(j))
    assert temp,"你给的什么shabi数据"
    return temp
print(towsum(nums,target))
'''



#2024第二期第6题
'''
a=int(input(":"))
b=int(input(":"))
lst=[]
for i in range(a,b+1):
    s=0
    for j in str(i):
        j=int(j)
        s+=j*j*j
    if i==s:
        lst.append(i)
print(lst)
'''

'''
n=int(input("请输入正整数（n）："))
A=[[0]*n]*n   #初始化A列表
for i in range(n):  #第一层对应行列式的行
    for j in range(n):  #第二层对应行列式的列
        a=eval(input(f"请输入a{i+1}{j+1}的值:"))
        A[i][j] = a
klst=[]
for m in range(n):
    k=eval(input(f"请输入k{m+1}的值:"))
    klst.append(k)
s=0
for i in range(n):  #第一个西格玛
    for j in range(n):   #第二个西格玛
        s+=klst[i]*A[i][j]
print("结论",s==0)
'''

#tupleの易错
'''
s=0
a=[0]*10
for i in tuple(a):
    print(len(a))
    for j in tuple(a):
        s+=1
        a.append(0)
print(len(a))  #得到结果10240
'''


#牢马の掩码练习
'''
import numpy as np
x = np.array([[[2], [4]], [[1], [5]], [[6], [7]]]); y = np.array([[[0], [4]], [[2], [0]], [[6], [7]]])
z=y*(x!=y)+y*(x==y)*3+x*(y==0)
'''

'''
import numpy as np
n=int(input("请输入行列式的阶数:"))
temp=[]
for i in range(n):
    temp.append(list(map(int,input("请输入：").split(' '))))
tarr=np.array(temp)
print(int(np.linalg.det(tarr)),tarr)
'''


#循环
'''
def cal(n):
    i=0
    while n!=1:
        if n%2==0:
            n=int(n/2)
            i+=1
        else:
            n=int(3*n+1)
            i+=1
    if i>200:
        return 200
    else:
        return i
#递归
def cal1(n,i=0):
    while n!=1:
        if n % 2 == 0:
            n = int(n / 2)
            i += 1
        else:
            n = int(3 * n + 1)
            i += 1
        cal(n)
    if i > 200:
        return 200
    else:
        return i

print(cal(24),cal1(24))
print(cal(2345),cal1(2345))
'''



'''
def construct_dict():
    ssddic={}
    mdic={}
    return mdic,ssddic
def solutions(main_memory,ssd,n):
    return None
main_memory, ssd = construct_dict()
print(main_memory)
print(ssd)
mm_chosen, ssd_chosen, price = solutions(main_memory,ssd,2287)
print(mm_chosen,ssd_chosen,price)
mm_chosen,ssd_chosen,price=solutions(main_memory,ssd,2300)
print(mm_chosen,ssd_chosen,price)
'''


#打印九九乘法表
'''
lst=[[]]*9
for i in range(1,10):
    lst[i-1]=[f'{i}*{j}={i*j}' for j in range(i,10)]
print(lst)
'''

import numpy as np


# def student(input_data):
#     result = []
#     # ********* Begin *********#
#     input_data = np.array(input_data)
#     result = input_data[(input_data >= 'A') & (input_data <= 'Z')]
#     # ********* End *********#
#     return result
#
# test=[["d","a","A","p","b","I","C","K"],[['d','F','f',"Q","a"],['a','b','L']]]
# for i in test:
#     print(student(i))




# #(60,60.48),(62,66.22),(58,53.93),(56,57.67),(55,61.04),(57,53.79)
# #(56.5,55.82),(57.5,51.95),(57.663,52.5),(57.6,52.29)
# x=[55,56,56.5,57,57.4,57.5,57.6,58,60]
# y=[61.04,57.67,55.82,53.79,51.61,51.95,52.29,53.93,60.48]
# from matplotlib import pyplot as plt
# plt.plot(x,y)
# plt.show()














