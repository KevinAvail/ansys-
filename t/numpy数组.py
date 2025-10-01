import numpy as np
#arr=np.array([1,2]) #整数型数组
#arr=np.array([1.0,2]) #浮点型数组
#print(arr)

'''
arr=np.array([1,2,3])
#arr[0]=10.09  #被同化为整数
#print(arr)  #输出[10  2  3]

arr1=arr.astype(float)  #.astype() 设定数据类型#**
#print(arr1)  #输出[1. 2. 3.]

#print(arr+1) #输出全体+1 #全体共同改变

print(arr+arr1)  # 输出[2. 4. 6.]
'''

'''
arr1=np.ones(3) #传入形状3
print(arr1)  #输出[1. 1. 1.]
arr2=np.ones([1,2]) # 传入形状（1,2）
print(arr2)  #输出[[1. 1.]]
arr3=np.ones([1,1,2])  #传入形状(1,1,2)
print(arr3)  #输出三维数组[[[1. 1.]]]
#.shape查看数组形状
print(arr1.shape) #输出(3,)
print(arr2.shape) #输出(1, 2)
'''


###不同维度数组之间的转换    .reshape()
'''
arr=np.arange(1,10)
arr=arr.reshape(9) #得到长度为9的向量
arr=arr.reshape(-1)  #-1为自动判断
arr=arr.reshape((3,3))  #3行3列的矩阵
print(arr)
'''


###将一维数组升为二维数组
'''
arr1=np.arange(10)  #arange()与range()的参数相同  -->创建[0 1 2 3 4 5 6 7 8 9]
arr2=arr1.reshape(1,10)  #arr2=[[0 1 2 3 4 5 6 7 8 9]]
arr2=arr1.reshape(2,5)   #arr2=[[0 1 2 3 4]/n[5 6 7 8 9]]
arr2=arr1.reshape(1,-1)  #arr2=[[0 1 2 3 4 5 6 7 8 9]]
print(arr2)
'''


###将二维数组降为一维数组
'''
arr2=np.arange(10).reshape(2,5)
print(arr2)
arr1=arr2.reshape(-1)
print(arr1)  #输出[0 1 2 3 4 5 6 7 8 9]
'''


###创建指定数组
'''
arr=np.array([1,2])  #向量
arr1=np.array([[1,2,3]])  #行矩阵
arr2=np.array([[1],[2],[3]])  #列矩阵
'''
'''
arr0=np.zeros(3)  #创建一个长度为3的0向量
arr1=np.zeros((1,3))  #全零数组 传的参数是形状，圆括号和方括号都一样
arr2=np.ones(3) #全一数组
arr3=3.14*np.ones((2,3))  #全3.14数组
print(arr3)  #输出[[3.14 3.14 3.14]\n[3.14 3.14 3.14]]
'''


###创建随机数组np.random
'''
arr1=np.random.random((2,5))  #2行5列 #分布于0~1
#print(arr1)
arr2=(100-60)*np.random.random((2,5))+60  #创建60~100内的随机数组
arr3=np.random.randint(10,100,(1,15)) #randint(low,high,size)
print(arr3) #[[58 80 56 58 67 11 52 86 87 49 72 24 33 63 63]]
arr4=(90*np.random.random((1,15))+10).astype(int)  #.astype()
print(arr4)
#正态分布  (均值，标准差，形状)
arr5=np.random.normal(0,1,(2,3)) #normal(loc,scale,size)
print(arr5)
'''


###数组的索引
'''
arr1=np.arange(1,10) #创建向量
print(arr1[1],arr1[-1])

arr2=np.array([[1,2,3],[4,5,6]]) #创建矩阵
print(arr2[0,2])  #第0行，第2列

arr2[1,1]=100.9  #修改
'''

###花式索引
'''
arr1=np.arange(1,90,10)
print(arr1[[0,2]])  #[ 1 21] 返回第0个和第2个 从矩阵的角度看，返回第0行和第2行
arr2=np.arange(1,17).reshape([4,4])
print(arr2)
print(arr2[[0,1],[2,3]])  #取0行2列和1行3列
print(arr2[[0,1,2],[3,1,0]]) #取0行3列和1行1列和2行0列
# arr2[key] 花式索引中的key是一个矩阵或向量
#arr2[[第一维]，[第二维],[第三维],……[第n维]]
#以下为4维数组的实例
arr4=np.array([[[[1,2],[3,4]],[[5,6],[7,8]]],[[[11,12],[13,14]],[[15,16],[17,18]]]])
#print(arr4[[1,1],[0,1],[1,1],[1,0]])
print(arr2[[[0,1],[1,0]],[[1,1],[1,1]]]) #输出[[2 6]\n[6 2]] 输出了一个二维矩阵
#修改元素需要用到索引，那么一定也有“花式修改”的操作
arr2[[0,1],[1,1]]=100 #将第0行第1列和第1行第1列修改为100
print(arr2)
#花式索引用了2及以上层数的中括号
'''

###掩码
'''
import numpy as np
x=np.array([[[1],[2]],[[2],[3]]])
print(x[x==[1]]) #找到x里面等于[1]的元素
print(x*(x==1))  #创建一个和x同型的0矩阵，然后在x==1的位置填上x相应位置的元素
x = np.array([[[2], [4]], [[1], [5]], [[6], [7]]]); y = np.array([[[0], [4]], [[2], [0]], [[6], [7]]])
z=y*(x!=y)+y*(x==y)*3+x*(y==0)  #做加法相当于多次判断并赋值，最终返回一个
'''

###访问数组切片
#向量的切片
'''
arr1=np.arange(10)
#向量与列表的切片操作完全一致
print(arr1[1:5]) #从第1个到第4个
print(arr1[1:8:2]) #step=2
'''
#矩阵的切片
'''
arr2=np.arange(1,21).reshape([4,5])
print(arr2)
print(arr2[1:3,1:-1]) #[行，列] 依然是不取end
print(arr2[::3,::2])  #跳跃采样，实际上是加了一个step
'''
#提取矩阵的行 --> 列索引拉满
'''
arr3=np.arange(1,21).reshape(4,5)
print(arr3)
print(arr3[1:3,:])  #提取第1~2行
print(arr3[2,:])  #提取第2行
print(arr3[2])  #提取行的时候的简写，不写列，但提取列不能简写
print(arr3[:,2]) #提取第2列 注意，输出是行向量
cut=arr3[:,2]  #cut是向量
cut=cut.reshape((-1,1)) #变成列向量-->只有1列
print(cut)
print(cut.T)  #矩阵的转置
'''
#数组切片只是视图，没有创造新的变量，浅拷贝
'''
arr=np.arange(1,21)
cut=arr[:9]
cut[3]=100 #原数组中的元素也被修改 类似于浅拷贝
print(arr)
arr1=arr
arr1[3]=100 #原数组被修改
print(arr)
cut1=arr[:9].copy()  #创建新数组 .copy()
cut1[3]=100  #不改变原数组
print(arr)
'''




























