from math import *
# v=map(float,input().split())
# u=[];p=[];w=[]
# for i in v:
#     u.append(i**3)
#     p.append(cos(i))
#     w.append((i**3)*cos(i)+3)
# print(u)
# print(p)
# print(w)
'''
def f(x):
    return x**3
'''
'''
n = 5 # no of points
dx = 1.0/(n-1) # x spacing in [0,1]
xlist = [i*dx for i in range(n)]
ylist = [f(x) for x in xlist]
pairs = [[x, y] for x, y in zip(xlist, ylist)]
'''


import numpy as np
'''
x=np.arange(5)
print(x) # [0,1,2,3,4]
x=np.arange(1,5)
print(x) # [1,2,3,4]
x=np.arange(1,5,2)
print(x) # [1,3]
y=np.arange(5,dtype=float)
print(y) # [0. 1. 2. 3. 4.]
'''

'''
b=np.array([1,2,3]) # 将[1,2,3]转化为数组 会copy出一个副本，对b操作不会影响原列表
c=np.asarray(b) # 类似于浅拷贝
'''

'''
a=np.linspace(1,8,8)
print(a) # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

a[[1,6,7]]=10
print(a) # [ 1. 10.  3.  4.  5.  6. 10. 10.]

a[range(2,8,3)]=-2
print(a) # [ 1. 10. -2.  4.  5. -2. 10. 10.]

print(a<0) # [False False  True False False  True False False]
# 对数组中每个元素进行运算

print(a[a<0]) # [-2. -2.] 找到符合条件的元素

a[a<0]=a.max()
print(a) # [ 1. 10. 10.  4.  5. 10. 10. 10.]

print(isinstance(a,np.ndarray)) # 判断a是不是np.ndarray的一个实例
'''

'''
y=np.array([0,2,3])
y=np.sin(y)
print(y)
'''



'''
def f(x):
    return x**2*np.exp(-0.5*x)*np.sin(x-np.pi/3)
A=np.linspace(0,4*np.pi,100)
print(f(A))
'''


'''
a=np.array([1,2,3,4,5])
x=a  #x会变
#x=a[:] #x会变
a[-1]=1000
print(x)
'''




#二维数组
'''
a=np.zeros([3,4]) #创建一个三行四列的零数组
print(a.shape) #(3,4)
a[0,0]=1
a[1][2]=2
print(a)
'''

#t=np.linspace(1,30,30).reshape(5,6)
#print(t[1:-1:2,2:])





###曲线绘图***
import matplotlib.pyplot as plt

g = 9.81; v0 = 381; y0 = 1.9; theta = 60*np.pi/180
'''
def Y(x, v0, y0, theta):
   return x*np.tan(theta)-1/(2*v0**2)*g*x**2/((np.cos(theta))**2)+y0
xArray = np.arange(1,13002,100,float) # 构造等差x数组
yArray = Y(xArray, v0, y0, theta) # 向量化
plt.plot(xArray,yArray)  # 基于横纵坐标点集连线绘制曲线
plt.axis([-100,13000,-100, 6000]) # 设置坐标轴范围
plt.xlabel("x"); plt.ylabel("y")  # 设置坐标轴标题
#plt.savefig("shell_trace.pdf")   # 保存绘制的图片到本地
plt.show()  # 显示绘制的曲线
'''

'''
t=np.linspace(-np.pi,np.pi,1000)
x=16*(np.sin(t))**3
y=13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
plt.plot(x,y,"r-")
plt.plot(x+10,y,"r--")
plt.show()
'''
#title() --> 整个图的名字



###绘制阶跃函数曲线
'''
def H(x):
    return 0 if x<0 else 1
    '''
#用循环解决
'''
def h(x):
    r=np.zeros(len(x))
    for i in range(len(x)):
        r[i]=H(x[i])
    return r
'''
#函数向量化
#hv=np.vectorize(H)

#np.where()
'''
def hv(x):
    return np.where(x<0,0.0,1.0)  #用嵌套where进行多条件判断
xArray = np.linspace(-10,10,1000) # 构造等差x数组
yArray = hv(xArray) # 向量化
plt.plot([-10,0],[0,0],'b-',[0,10],[1,1],'b-') #绘制多条曲线
#plt.plot([-10,0,0,10],[0,0,1,1]) #画线段[左端点，右端点]，[下端点，上端点]
#plt.plot(xArray,yArray,"r")  # 基于横纵坐标点集连线绘制曲线
plt.axis([xArray[0],xArray[-1],-2, 2]) # 设置坐标轴范围
plt.xlabel("x"); plt.ylabel("y")  # 设置坐标轴标题
#plt.savefig("shell_trace.pdf")   # 保存绘制的图片到本地
plt.show()  # 显示绘制的曲线
'''


#曲线动画
def norm(x,s):
    return np.exp(-x**2/(2*s**2))/np.sqrt(2*np.pi)/s
#cla() --> 清空当前图形中所有内容
import matplotlib.animation as an
'''
实现动画的主要相关函数
import matplotlib.animation as animation
ani = animation.FuncAnimation
(fig,	\ # the target figure	
func,	\ # update function	
frames,\ # data source
interval,\ # time interval,ms
...	\ # other parameters	
)
#FuncAnimation 的意义:每隔interval时间，从 frames中取下一个参数调用func，并用其返回的结果(一组曲线)更新fig
'''
'''
fig = plt.figure() # 创建一个画布
t=np.linspace(-5,5,200)
line,=fig.add_subplot(111).plot(t,norm(t,0.5),color='b')
print(line)
'''


###绘图的基本步骤与函数名

##绘制函数图像

'''
#1.准备参数：
def Y(x, v0, y0, theta):  #构造函数
   return x*np.tan(theta)-1/(2*v0**2)*g*x**2/((np.cos(theta))**2)+y0
xArray = np.arange(1,13002,100,float) #创建x列表或数组
yArray = Y(xArray, v0, y0, theta) #创建y列表或数组
# 可能需要定义一个函数处理x得到y
# 如果x是数组，则用np.vectorize(函数名)向量化，或者使用numpy里面的数学运算，
#2.绘图：
n=2 #n是曲线的条数
line=[0]*n #用于legend
labels=[]  #图例的标签
line[0],=plt.plot(xArray,yArray,'r',label='one')  # 基于横纵坐标点集连线绘制曲线
# 绘制多条曲线就多个plot，plot里面可以传labels=''，用于添加曲线的标签
#plt.plot(x,y,'color--',label='') #画图、设置颜色、设置虚线或直线、设置轴标题
line[1],=plt.plot(xArray,yArray+1000,'b',label='two')
plt.axis([-100,13000,-100, 10000]) # 设置坐标轴范围,[xlow,xhigh,ylow,yhigh]
plt.xlabel("x"); plt.ylabel("y")  # 设置坐标轴标题
plt.xticks([1000,2000,3000,4000,5000],['a','b','c','d','e'],rotation=45)  #设置x轴刻度 y同理
#plt.xticks(ticks,labels,rotation)
plt.xlim(0,15000)  #x轴显示范围 y轴同理
plt.legend(line,labels=labels,title='Title',loc='upper left') #设置图例
# 添加图例并设置图例的标题、图例的位置
# 如果有多条曲线，则需要传line列表和labels标签列表，通过line=bar()[0]的方式获得line
plt.title('Title')  #设置图像的标题
#plt.savefig("shell_trace.pdf")   # 保存绘制的图片到本地
plt.show()  # 显示绘制的曲线
'''

'''
##绘制柱状图
x=[1,2,3]  #x表示x轴标量序列 可以是列表、元组或一维数组  #x可以是['a','b','c']之类的非纯数字序列
height=[1,2,3]  #柱形高度，y轴标量序列
#1.普通条形图：
#plt.bar(x, height, color='r', width=0.8, alpha=0.7, bottom=None, align='center', data=None, linewidth=1)
# width表示柱形宽度，color表示柱形颜色，alpha表示柱形间距，align表示柱形的对齐方式
# xticks xlabel savefig xlim与绘制函数相同
#2.条形图的堆叠：
height1=[4,5,6]
width=0.2
plt.bar(np.array(x),height,width=width,color='b')
#plt.bar(x,height1,bottom=height,color='r') #在同一竖直线上，上下紧凑
plt.bar(np.array(x)+width,height1,width=width) #左右相邻
#添加图例的方法见绘制函数legend部分
plt.show()
'''

'''
##绘制饼状图
#plt.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None, radius=None, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, data=None)
# x是绘制的序列数据（比如占比），explode表示突出的部分，labels表示各部分的标签
# autopct参数表示用数值标记楔形，可指定显示方式且标记在内部
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs'] # 标签列表
sizes = [15, 30, 45, 10] # 绘制数据
explode = (0, 0.1, 0, 0)  # 只突出第二个切块，偏移比例为0.1 (i.e. 'Hogs')
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# shadow表示添加阴影，startangle表示旋转角度
plt.axis('equal')  # 用于显示为一个长宽相等的饼图
plt.show() #展示图像
'''


'''
##多子图绘制
#设置画布：
from math import sin, radians #导入数学计算库
x = range(0, 361)  #创建 0-360 的整数列表
y = [sin(radians(e)) for e in x] #获得 x 对应的正弦值，以列表存储
plt.figure(figsize=[8,5]) #在绘图之前设置画布大小，宽为 8 英尺，高为 5 英尺
plt.plot(x,y)
plt.show()
#绘制子图：
# 第一种：整个绘图区域被分成 nrows 行和 ncols 列，index 表示第几个图
#plt.subplot(nrows, ncols, index, **kwargs)
# 第二种：pos 是三位数的整数，其中第一位是行数，第二位是列数，第三位是子图的索引
#plt.subplot(pos, **kwargs)
# 第三种：添加子图 ax
#plt.subplot(ax)
#这种做法不需要用figure来设置画布
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)
plt.subplot(211) # 绘图区域被分为 2 行 1 列，接下来绘制第一幅图
plt.plot(t, s1)
ax2 = plt.subplot(212) # 绘制第二幅图
plt.plot(t, 2*s1)
plt.show()
'''

##总结
# 1.数据处理，创建x数组或列表，创建或求得y数组或列表
# 2.画图，设置color,label,legend,xticks,axis,xlim,xlabel
# 特殊地，有legend(line,labels,loc=),figure,subplot,axis('equal')
# shadow=True,startangle=90,width=,alpha=,align=
# 3.保存图片或者展示图片 savefig('文件名') , show()


#狗追兔子
'''
n=int(input(":"))
t=np.linspace(0,50,n)
raby=3*t;rabx=[20]*n
plt.plot(rabx,raby,'b')
dogx=np.linspace(0,20,n)
dogy=np.zeros(n)
for i in range(n):
    if i>1:
        dogy[i]=dogx[i-1]+((raby[i]-dogy[i-1])/(20-dogx[i]))*(dogx[i]-dogx[i-1])
    else:
        dogy[i]=dogx[i]
plt.ylim(0,100)
plt.plot(dogx,dogy,'r')
plt.show()
'''