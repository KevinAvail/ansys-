#dic = {'Chinese':'Mrs.li','math':'Mr.zhu','English':'Carmen'}
dic=dict(Chinese = 'Mrs.li',math = 'Mr.zhu',English = 'Carmen')
#r=dic.pop("Chinese") #返回Mrs.li

'''
#temp=dic #dic会改变
temp=dic.copy() #dic不会变
temp["Chinese"]='Mr.li'
print(dic)
'''

#print(dic.keys())  #输出dict_keys(['Chinese', 'math', 'English'])
#print(list(dic.keys()))  #把字典中所有的key拿出来并装到列表里面
#print(list(dic.items()))  #把字典中所有的东西拿出来并装到列表里面

#遍历
'''
for key,value in dic.items():
    print(key,value)
'''
'''
for i in dic:
    print(i) #输出的是key
'''

#根据key排序
'''
temp=sorted(dic)
print(temp)
'''

#字典的key必须是可哈希的数据类型
#a,b =(1,2)   ##解构（解包）元组和列表都可以执行此操作

###字典的增删改查

'''
dic['帅哥'] = "贾佳浩"   #增：  dic[key] = value

dic['帅哥'] = "旭巍"    #原来的那个value被顶替了（改）；和列表有点像

dic.pop('帅哥')  #删：   dic.pop[key]

dic.setdefault('attention','at ease')  #设置默认值
# 如果以前已经有了attention作为key，那么setdefault就没用了
#print(dic)

print(dic['帅哥'])  #查询,如果key不存在，程序会报错,确定了key可以用
print(dic.get('帅哥'))   #同样是查询,但不会报错，返回none，不确定key可以用
'''

'''
#字典的嵌套
wangfeng={"name":"wangfeng"
     ,"age":18,
     "wife":{
          "name":"Zhangziyi",
          "age":18,
          "hobby":"不知道",
     "assistant":{
          "name":"teriri",
          "age":34,
          "hobby":"play"
     }

     },"chidren":[
          {"name":"1","age":21},
          {"name":"2","age":19},
          {"name":"3","age":15}

     ]
          }
#wangfeng妻子的助手的名字
print(wangfeng["wife"]["assistant"]["name"])
#给wangfeng第二个孩子加一岁
wangfeng["chidren"][1]["age"]=wangfeng["chidren"][1]["age"]+1
print(wangfeng["chidren"][1]["age"])
'''

#字典的循环删除
'''dic = {'Chinese':'Mrs.li',
        "余建兵":"审题要仔细",
       '大math':'Mr.zhu',
       '大English':'Carmen'}
temp=[]#用一个空列表把要删除的key装起来
for a in dic:
    if a.startswith("大"):
        temp.append(a)#dictionary changed size during iteration
        #循环的时候变了会报错
for i in temp :
    dic.pop(i)

print(dic)
'''

'''
dic = {'Chinese':'Mrs.li','math':'Mr.zhu','English':'Carmen'}
dic.popitem() #随机获得一个key-value对，并删除
dic.clear() #清除所有key-value对
r = dic.pop(1,'Carmen')
print(r)
'''

###读取文件到字典
'''
infile = open("tt/temp",'r',encoding='utf-8')
dics={}
for k,v in [tuple(i.strip().split("：")) for i in infile]:
    dics[k]=float(v)
print(dics)
'''



#课堂练习  fighters.txt
'''
data={}
infile=open("tt/fighters.txt",'r',encoding='utf-8')
content=[item.split() for item in infile.readlines() if item.strip()]
for i in range(1,len(content[0])):
    data1={}
    for j in range(1,len(content)):
        data1[content[j][1]]=content[j][i+1]
    data[content[0][i]]=data1
infile.close()
value=list(data.values())
for i in value:
    for k in i.keys():
        if i[k]!='no':
            i[k]=float(i[k])
print(data)
'''





