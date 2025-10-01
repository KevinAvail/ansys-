'''
lst=list(map(int,input().split()))
for i in range(len(lst)):
    t=1
    x=lst[i]
    while t<=x:
       print(t,end=" ")
       t=t+1
    if x!=0:
        print()
'''

'''
r=int(input())
c=int(input())
x=1
for k in range(c):
    for i in range(r):
        if i!=r-1:
            print(x,end=" ")
            x+=1
        else:
            print('PUM')
            x+=1
    print()
'''

'''
N=int(input())
def per(n):
    i=1;temp=[];s=0
    while n%i==0:
        temp.append(i)
        i+=1
    for j in range(len(temp)):
        s+=temp[j]
    return s
t=[];t1=[];lst=[]
for k in range(N):
    b=int(input())
    lst.append(b)
for a in lst:
    if per(a)==a:
        print(a,"is perfect")
    else:
        print(a,"is not perfect")
'''


'''#最小公约数
a=int(input());b=int(input())
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return int(a)
print(gcd(a,b))
'''

'''
user_input1=input("请用逗号分隔：")
n,m,size=map(int,user_input1.split(","))
a=list(input().split(","))
b=list(input().split(","))
b[:size]=a[:size].copy()
for i in b:
    print(i,end=' ')
'''



#拷贝
'''
import copy
a=[1,2,3,[4,5]]
b=[4,5,6,7]
'''
# b[2]=a[3]
# a[3][0]=6
# print(b)   #b中的列表会改变

# b[2:4]=a[2:4]
# a[3][0]=6
# print(b)   #b中的列表会改变

# b=a.copy()
# a[3][0]=6
# print(b)   #b中的列表会改变

# b = copy.copy(a)
# a[3][0]=6
# print(b)   #b中的列表会改变

# b = copy.deepcopy(a)
# a[3][0]=6
# print(b)   #只有deepcopy，b中的列表才不会变


#数组翻转
'''
t=input("请用逗号隔开:")
n,size=map(int,t.split(","))
a=list(map(int,input("请用逗号隔开:").split(",")))
a[:size]=sorted(a[:size],reverse=True)
for i in a:
    print(i,end=' ')
'''

#递归求斐波那契数列的第n项
'''
def F(n):
    if n==1 or n==2:
        return 1
    else:
        return F(n-1)+F(n-2)
print(F(int(input("请输入一个正整数："))))
'''

#得到数组前n个数中不同数的个数
'''
n=int(input());a=list(input().split(","))
def get_unique_count(a,n):
    s=set(a[:n])
    return len(s)
print(get_unique_count(a,n))
'''

#数组排序
'''
n,l,r=map(int,input("请用逗号隔开：").split(","))
a=list(input("请用逗号隔开:").split(","))
def void_sort(a,l,r):
    a[l:r+1]=sorted(a[l:r+1])
    return a
for i in void_sort(a,l,r):
    print(i,end=" ")
'''

#排列***
'''
def dfs (u, num, st):
    global n
    if u > n :
        for i in range (1, n+1):
            print (num[i], end = " ")
        print("")
    else:
        for i in range (1, n+1):
            # print (u, i, st[i])
            if st[i] == False:
                st[i] = True;
                num[u] = i
                dfs (u + 1, num, st)
                st [i] = False

n = int (input())
num = [0]*(n+1)
st = [False]*(n+1)
dfs (1, num, st)
'''

#汉诺塔
'''
def move(n,a,buffer,c):#把n个盘子从a借助buffer移到c
    if n==1:
        print(a,"->",c)
        return
    move(n-1,a,c,buffer)
    move(1,a,buffer,c)
    move(n-1,buffer,a,c)
move(3,"a","b","c")
'''


#辛普森公式近似计算积分
def Simpson(f,a,b,n=500):
    t=0;m=0;h=(b-a)/n
    for i in range(1,int(n/2+1)):
        t+=f(a+(2*i-1)*h)
    for i in range(1,int(n/2)):
        m+=f(a+2*i*h)
    return (h/3)*(f(a)+f(b)+4*t+2*m)
from math import *
'''
#测试函数
def h(x):
    return 1.5*sin(x)**3
def application():
    print('Integral of 1.5*sin^3 from 0 to pi:')
    for n in 2, 6, 12, 100, 500:
        approx = Simpson(h, 0, pi, n)
        print ('n=%3d, approx=%18.15f, error=%9.2E'% (n, approx, 2-approx))

application()
'''
'''
for i in range(10):
    if i :
        print(i)
        break
else:
    print("没有break")
'''


#判断n是否为素数
'''
n=eval(input("请输入大于1的正整数："))
while n<=1 or type(n)!=int:
    print("请输入大于1的正整数")
    n = eval(input("请输入大于1正整数："))
for i in range(2,int(sqrt(n))+1):
    if n%i==0:
        print(f"{n}不是素数")
        break
else:
    print(f"{n}是素数")
'''

##给定矩阵的转置
'''
L=[[1,2,3],[4,5,6],[7,8,9]]
M=[[0]*len(L),[0]*len(L),[0]*len(L)]
for i in range(len(L)):
    for j in range(len(L[i])):
        M[i][j]=L[j][i]
for k in range(len(M)):
    for l in range(len(M[k])):
        print(M[k][l],end=' ')
    print()
#另一种方法
l=[[1,2,3],[4,5,6],[7,8,9]]
m=[list(raw) for raw in zip(*l)]
print(m)
'''

#数组替换
'''
x=[]
for i in range(10):
    n = eval(input("请输入："))
    x.append(n)
for i in range(len(x)):
    if x[i]<=0 or type(x[i])!=int:
        print(f"x[{i}] = ",1)
    else:
        print(f"x[{i}] = ",x[i])
'''

#738.数组填充
'''
N=[]
n=eval(input("请输入一个正整数："))
while type(n)!=int:
    n = eval(input("请输入一个正整数："))
for i in range(10):
    t=n*2**i
    N.append(t)
    print(f"N[{i}] = ",t)
'''


#743数组中的行(可能会错)
'''
L=int(input("请输入一个正整数："))
t=input("求和（s），平均值（m），请输入：")
M=[[0]*12]*12
s=0
for i in range(12):
    for j in range(12):
        m=eval(input("请输入："))
        M[i][j]=m
for k in range(12):
    s+=M[L][k]
if t=="s":
    print(s)
elif t=="m":
    print(s/(12*12))
else:
    print("shabi，输错了!")
    t = input("求和（s），平均值（m），请输入：")
'''


#749数组的上方区域
'''
M=[[0]*12]*12
for r in range(12):
    for c in range(12):
        m=eval(input("请输入："))
        M[r][c]=m
s=0
for i in range(12):
    for j in range(i+1,12-i):
        s+=M[i][j]
print(s)
'''

#741斐波那契数列
'''
n=int(input("请输入一个正整数："))
def F(n):
    if n==0 :
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return F(n-1)+F(n-2)
print(F(n))
'''

#742.最小数和它的位置
'''
L=int(input("请输入；"))
X=[0]*L
for i in range(L):
    X[i]=eval(input("请输入："))
print("Minimum value:",min(X))
print("position:",X.index(min(X)))
'''


#745平方矩阵||（不会T^T）
'''
N=int(input("请输入："))
temp=[]
while N!=0:
    temp.append(N)
    N=int(input("请输入："))
for i in range(N):
    print(i+1,end=" ")
'''






