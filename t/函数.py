'''
a,b=1,2
def f(x,y):
    z = x+y
    return z
print(f(a,b))
'''

'''
def f(arg1,arg2,kwarg1=True,kwarg2=0):
    print(arg1,arg2,kwarg1,kwarg2)
f('h',[1,2])
'''

'''
from math import *
def rang(W1,W2,k,v=864,c=0.95):
    return ((v/c)*k)*log(W1/W2)
print(round(rang(19.34,19.34-4.81,11),1))
'''


'''def somefunc(*args):
    for i in args:
        print(i,end=' ')
somefunc('a','b',2,True,[22,'ss'],{})
'''

'''
from math import *
t=input()
def diff2(f,x,h=1E-6):
    r = (f(x-h)-2*f(x)+f(x+h))/h**2
    return r
print(diff2(sin,t))
'''

'''
t=int(input("请输入:"))
from math import *
#print((lambda x:sin(x) if 0<=x<=2 else cos(x))(10))
def sum_(x):
    if x == 1:
        return x
    else:
        return x+sum_(x-1)
print(sum_(t))
'''

'''
n=int(input())
def rabbits(n):
    if n==1 or n==2:
        return 1
    else:
        return rabbits(n-1)+rabbits(n-2)
print(rabbits(n))
'''

'''
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a   #最大公约数
def lcm(a,b):
    return a*b//gcd(a,b)   #最小公倍数
'''

# lst=list(input());i=int(input());j=int(input());n=len(lst)
# def void_sort(n,a,i,j):
#     temp=[]
#     for k in range(i,j+1):
#         temp.append(lst[k])
#     temp.sort()
#     for k in range(i,j+1):
#         lst[k]=temp[k-i]
#     return lst
# for item in void_sort(n,lst,i,j):
#     print(item,end=' ')


'''
length=int(input());l=int(input());r=int(input());lst=list(input())
def void_sort(n,a,i,j):
    temp=[]
    for k in range(i,j+1):
        temp.append(lst[k])
    temp.sort()
    for k in range(i,j+1):
        lst[k]=temp[k-i]
    return lst
for item in void_sort(length,lst,l,r):
    print(item,end=' ')
    '''


