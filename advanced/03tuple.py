"""元组的定义"""
t = ('a', 'b', 'c', 'e', 'f', 'g')
t1 = 'a',

"""但是这种不是元组"""
t2 = ('a')

print(type(t))
print(type(t1))
print(type(t2))

"""可以使用内置函数来新建元组,不附带参数，定义的是空元祖"""
t4 = tuple()

"""tuple() 只接受一个参数，多余的会报错"""
# t5 = tuple('kejian', "chenqi")

"""大多数列表操作也可以应用于元组"""
# 通过下表获取元素
char = t[0]
print(char)
# 切片操作
print(t[1:3])
# 不可以尝试去修改元组里的元素，会报错
# t[0] = 'k'

"""不能修改元组元素，但是可以将元组替换为另外一个"""
t = ('A',) + t[1:]
print(t)
print("==============================")

"""元组的赋值部分"""

# 交换元祖
a = '1', '2', '3'
b = ('a', 'b', 'c')
a, b = b, a
print(a)
print(b)

# 上面的方式也可以应用在变量的赋值上面
x, y = 1, 2
print(x)
print(y)

# 更通用的是，右边的表达式可以是任意类型的序列，(字符串，列表，与元组)
addr = 'hellokejian@163.com'
username, domian = addr.split('@')
print(username + ' ' + domian)

"""元组作为返回值"""


def Divmod(x, y):
    return x / y, x % y


result = Divmod(4, 2)
print(result)

"""可变长参数元组"""

print("=====================")


def Printall(*args):
    print(args)


Printall('a', 'b', 'c')
Printall(123, 'b', 'c')

"""收集的反面就是分散，如果某个函数只接受固定个数参数，想要将元组里面的元素传进去一一对应，那么就要采用元组分散的方法了"""


def Add(x, y, z):
    return x + y + z


t = 'A', '380', 'Airplane'
str = Add(*t)
print(str)
