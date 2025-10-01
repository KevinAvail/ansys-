'''

data=eval(input("请输入要匹配的数据："))
match data:
    case {1:'kk'}:
        print("字典")
    case [10,20,30]:
        print("列表")
    case 'kk':
        print("字符串")
    case _:
        print("啥也不是")
'''

import sys
a = float(sys.argv[1])
print(a)