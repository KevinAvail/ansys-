#列表的索引超出范围会报错
#列表也有索引和切片
#可以用for循环进行遍历
#可以用len拿到列表的长度

#a = ["at","stop","fuck","word",3]
#print(len(a))
#for item in a:
    #print(item)

#*****列表的增删改查
#a.append("我是你爹0")     #添加,在列表的最后面加
#a.insert(1,"watch")     在位置1出插入"watch"
#a.extend(['haihaihai','machao']) #extend合并两个列表，可以批量添加
#print(list.index(44))  #index  获取元素44第一次出现的下标
a=[1,2,3,4]
a.reverse() #反转列表
print(a)
'''s = a.pop(2)   #pop可以返回删除的东西
a.remove("at")***
del a[1]  删除
print(a)
print(s)'''

a = ["at","stop","suck","word","work"]
#a[2] = "shit"    #直接用索引就可以进行修改

#print(a[2])     #直接用索引进行查询
#print(a)
#for t in range(0,len(a)):      方便后面索引时知道循环到第几项了
    #i = a[t]
    #if i.startswith("s"):
     #   new = "f"+i[1:]
      #  a[t] = new

#print(a)



'''a = ["at","stop","fuck","sword","hallo"]
for t in range(len(a)):
    i = a[t]
    if i.startswith("s"):

        new = "f"+i[1:]
        a[t] = new
print(a)'''



#列表是按照存放的顺序保存的
#a = ["at","stop","fuck","word","minecraft"]
#lst = [1,666,3,35434523,67]
#lst.sort()        #对列表进行排序
#lst.sort(reverse=True)   #对列表进行降序排序
#print(lst)


#列表的嵌套
'''lst = ["abc","cpdd","xswl",["awsl","96226",["cmd","what"]]]
lst[3][2][1] =lst[3][2][1].upper()
print(lst)'''

#***列表的循环删除(有坑)
'''lst = ["abc",'awsl','bcd','fff',"xswl","black"]
temp = []
for i in lst:
    if i.startswith("a"):
        temp.append(i)
for a in temp:
    lst.remove(a)
print(lst)'''

'''a = [1,2,3,4,5]
for i in a:
    print(i)
    del a[1]
print(a)'''

#list = ["dfs",99,"大蒜",True]
#list = list+["44",44]  #两个列表相加
#a,b,c,d = list #批量赋值

#print(list)








'''lst = [[j for j in range(10)] for i in range(10)]
for raw in lst:
    for c in raw:
        print(c,end='\t')
    print()




'''

import copy
A=[1,2,3,4]
#B=A[:] #深拷贝
B=copy.deepcopy(A)  #深拷贝
A[1]=10
print(B)
from math import *
print(modf(3.56))  #(0.56,3.0)
print(ceil(3.1))  #4
print(floor(3.9))  #3




