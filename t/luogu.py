#马拦过河卒
'''
def f(x,y):
    if x==1 and y==1:
        return 2
    if (x==1 and y==0) or (x==0 and y==1):
        return 1
    else:
        return f(x-1,y)+f(x,y-1)
bx,by,cx,cy=list(map(int,input().split()))
'''


#反向输出一个三位数
'''
n=int(input(":")[::-1])
print(n)
'''


#质因数分解
'''
n=int(input(":"))
x=[]
for i in range(2,n):
    if n%i==0:
        x.append(i)
print(max(x))
'''


#计算矩阵边缘元素之和
'''
m,n=map(int,input(":").split())
lst=[[]]*m
s=0
for i in range(m):
    lst[i]=list(map(int,input(":").split()))
for i in range(1,m-1):
    for j in [0,-1]:
        s+=lst[i][j]
s+=sum(lst[0])+sum(lst[-1])
print(s)
'''


#计算矩阵的鞍点（所在行的最大值，并且是所在列的最小值）
'''
m,n=map(int,input(":").split())
lst=[[]]*m #m行n列
result=[]
for i in range(m):
    lst[i]=list(map(float,input(":").split()))
for i in range(m):
    for j in range(n):
        if lst[i][j]==max(lst[i]):
            c=[lst[t][j] for t in range(m)]
            if lst[i][j]==min(c):
                result.append([i+1,j+1,lst[i][j]])
if result:
    for i in result:
        for j in i:
            print(j,end=' ')
else:
    print('not found')
'''


#图像相似度
'''
m,n=map(int,input(":").split())
lst1=[[]]*m #m行n列
lst2=[[]]*m
for t in [1,2]:
    exec(f'for i in range(m):\n lst{t}[i]=list(map(int,input(":").split()))')
s=0
for i in range(m):
    for j in range(n):
        if lst1[i][j]==lst2[i][j]:
            s+=1
print('%.2f' % (100*s/(m*n)))
'''


#矩阵转置
'''
import numpy as np
lst=[[1,2],[3,4]]
lst=np.array(lst).T
print(lst)
'''


#B2108图像模糊处理
'''
m,n=map(int,input(":").split())
lst=[[]]*m #m行n列
for i in range(m):
    lst[i]=list(map(float,input(":").split()))
for i in range(1,m-1):
    for j in range(1,n-1):
        lst[i][j]+=lst[i-1][j]+lst[i+1][j]+lst[i][j+1]+lst[i][j-1]
        lst[i][j]=int(lst[i][j]/5)
print(lst)
'''


#统计数字字符个数
'''
s=input(":")
n=0
for i in s:
    if i.isdigit():
        n+=1
print(n)
'''


#找到第一个只出现一次的字符
'''
s=input(":")
for i in range(len(s)):
    if s[i] not in s[:i]+s[i+1:]:
        print(s[i])
        break
else:
    print('no')
'''


# B2112剪刀石头布
'''
n=int(input(":"))
def f(p1,p2):
    if p1==p2:
        return 'Tie'
    else:
        temp=[ord(p1[0]),ord(p2[0])]
        v=max(temp)
        i=temp.index(v)
        del temp[i]
        x=temp[0]
        if v-x==1:
            return 'Player1'
        else:
            return 'Player2'
t=[]
for i in range(n):
    t.append(input(":").split())
for i in t:
    print(f(i[0],i[1]))
'''


# B2115密码翻译
'''
s=list(input(":"))
for i in range(len(s)):
    if (65<=ord(s[i])<90) or (97<=ord(s[i])<122):
        s[i]=chr(ord(s[i])-1)
    elif ord(s[i]) in [90,122]:
        s[i]=chr(ord(s[i])-25)
print(''.join(s))
'''


# B2116加密的病历单
'''
s=input(':')
def f(s):
    up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low=up.lower()
    for i in range(len(s)): #翻转大小写
        if s[i] == s[i].upper():
            s[i]=s[i].lower()
        else:
            s[i]=s[i].upper()
    s=s[::-1]  #逆序储存
    for i in range(len(s)):  #循环左移
        if s[i] in up:
            ind=up.index(s[i])+3 #原文的位置
            if ind>25:
                s[i]=up[ind-26]
            else:
                s[i]=up[ind]
        else:
            ind1 = low.index(s[i]) + 3  # 原文的位置
            if ind1 > 25:
                s[i] = low[ind1 - 26]
            else:
                s[i] = low[ind1]
    return s
print(''.join(f(list(s))))
'''


# B2117整理药名
'''
n=int(input(":"))
for i in range(n):
    s=list(input(":"))
    a=True
    for j in range(len(s)):
        if s[j]=='-' or s[j].isdigit():
            pass
        else:
            if a:
                a=False
                s[j]=s[j].upper()
            else:
                s[j]=s[j].lower()
    print(''.join(s))
'''


# B2118验证子串
'''
s1=input(":");s2=input(":")
if s1 in s2:
    print(f'{s1} is substring of {s2}')
else:
    print('No substring')
'''


# B2119删除单词后缀
'''
s=input(":")
if s.endswith('er') or s.endswith('ly'):
    s=s[:-2]
elif s.endswith('ing'):
    s=s[:-3]
else:
    pass
print(s)
'''


# B2123字符串p型编码
'''
s=input(":")
ps=''
num=1
for i in range(len(s)):
    if i==len(s)-1:
        ps=ps+f'{num}{s[i]}'
    elif s[i]==s[i+1]:
        num+=1
    else:
        ps=ps+f'{num}{s[i]}'
        num=1
print(ps)
'''


# B2124判断字符串是否为回文
'''
s=input(":")
if s==s[::-1]:
    print('yes')
else:
    print('no')
'''

# 2125最高分数的学生姓名
'''
N=int(input(":"))
dic={}
for i in range(N):
    p,n=input(":").split()
    p=int(p)
    dic[p]=n
print(dic[max(dic.keys())])
'''

# B2126连续出现的字符
'''
k=int(input(":"))
s=input(":")
t={}
for i in s:
    num=0
    for j in range(len(s)):
        if s[j]==i:
            num+=1
        if num==k:
            t[i]=j
            break
if len(t)==1:
    print(list(t.keys())[0])
elif len(t)>1:
    for i,j in t.items():
        if j==min(t.values()):
            print(i)
            break
else:
    print('no')
'''

'''
x=1.5
def f(n):
    if n==1:
        return x
    else:
        return f(n-1)**(3)-1
for i in range(1,6):
    print(f(i))
'''








