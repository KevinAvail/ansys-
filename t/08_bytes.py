'''
1.字符集和编码
    0 1 <=>二进制转化成十进制<=>7529875
    电脑如何存储文字信息
    01010101001010 <=> a
    ascii 编排了128个文字符号 只需要7个0和1就可以表示，但前面还加了一个0，=>总共有8位
    1bytes => 8bits
    ANSI => 一套标准，每个字符 16bit,2byte
    中国 gb2312编码 gbk编码
    unicode:万国码
    utf:可变长度的unicode，可以进行数据的传输和存储

    总结：
        ascii: 8bit,1byte
        gbk: 16bit,2byte(windows默认)
        unicode(万国码):32bit,4byte
        utf-8:              mac默认
            英文：8bit,1byte
            欧洲：16bit,2byte
            中文：24bit,3byte

    gbk和utf-8不能直接进行转化
    gbk -> 文字 -> utf-8       (转化)

2.bytes
    程序员平时遇到的所有的数据最终单位都是字节(byte)


'''
"""
s="周杰伦"
bs1=s.encode("gbk")     #b'\xd6\xdc\xbd\xdc\xc2\xd7' byte类型
bs2=s.encode("utf8")    #b'\xe5\x91\xa8\xe6\x9d\xb0\xe4\xbc\xa6'
print(bs1)
print(bs2)
"""

#怎么把一个gbk的字节转化成utf-8的字节
gbk = b'\xd6\xdc\xbd\xdc\xc2\xd7'
utf_8=b'\xe5\x91\xa8\xe6\x9d\xb0\xe4\xbc\xa6'
#先变成文字符号（字符串）
a = gbk.decode("gbk")  #解码
s = a.encode("utf-8")   #重新编码
print(s)

#  byte.decode()     解码
#  str.encode()       编码





