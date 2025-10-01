#集合set表示
#s = {"ii","ds",222,"dadsa"}
'''s.add("ss")
print(type(s))
print(s)    '''#乱序
#t = {"dd",[]}   #list不可hash,会报错
#集合只能存可哈希，即不可变的对象
#print(t)
#可哈希：不可变的数据类型  str,tuple,int,bool……
#不可哈希：可变的数据类型  list,dict,set……
'''s = set()
s.add("js")
s.add("yy")
s.add(33)
s.pop() #       删除最后一个，无用
s.remove(33)   #删除
s.add(32)    #集合里元素的更换需要先删除再添加
print(s)'''

#s = {"ii","ds","jj","dadsa"}
#集合的查询使用for循环
'''for i in s :
    print(i)'''


'''
chaxun = input("请输入你想查询的东西:")
if chaxun in s :
    print(f"有{chaxun}")   #f-string
else :
    print(f"没有{chaxun}")'''

'''
s = {"ii","ds",222,"dadsa"}
t = {'aa','ds','dsff',"dd"}
print(s|t)   #  补集：^    差集：-    交集：&   并集：|
'''
























