# 有返回函数
from math import *


# def area(radius):
#     temp = 2*math.pi*radius
#     return temp
#
# area1 = area(5)
# print(area1)

# def distance(x1,y1,x2,y2):
#     dist = sqrt((x2-x1)**2 + (y2-y1)**2)
#     return dist
# a = distance(1,2,4,6)
# print(a)

# def hypotenuse(a,b):
#     c = sqrt(a**2 + b**2)
#     return c
#
# result = hypotenuse(3,4)
# print(result)

# def factorial(n):
#     if (n == 0) :
#         return 1
#     # elif (n==1) :
#     #     return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(4))

# def factorial(n):
#     if not isinstance(n,int):
#         print('only defined for integer')
#     if n < 0:
#         print('not defined for negative integer')
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(4))

# def factorial(n):
#     space = ' '*4*n
#     print(space,'factorial',n)
#     if n == 0:
#         print(space,'factorial',1)
#         return 1
#     else:
#         recurse = n*factorial(n-1)
#         print(space,'returning',recurse)
#         return recurse
# factorial(5)

# def b(z):
#     prod = a(z,z)
#     print(z,prod)
#     return prod
# def a(x,y):
#     x = x + 1
#     return x*y
# def c(x,y,z):
#     total = x + y + z
#     square = b(total)**2
#     return square
# x = 1
# y = x + 1
# print(c(x, y + 3, x + y))

def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    else:
        return


# print(ack(3, 6))

'''关键字参数'''


def register(name, age, **more):
    print('name:', name, 'age:', age, 'other:', more)


register('kejian', 18, city='anqiang')

'''和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去'''
extra = {'city': 'wuhu', 'job': 'nurse'}
register('chenqi', 20, city=extra['city'], job=extra['job'])

'''当然，上面复杂的调用可以用简化的写法'''
print('---also chenqi---')
register('chenqi', 20, **extra)

'''命名关键字参数'''
'''对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部检查'''
'''以上述函数为例，如果我们想检查是否有我们想要的参数'''


def person(name, age, *kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print(name, age, kw)


'''如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下'''
'''和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数'''


def person2(name, age, *, city, job):
    print(name, age, city, job)


'''调用方式如下:'''
'''person('Jack', 24, city='Beijing', job='Engineer')'''

'''如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了'''


def person3(name, age, *args, city, job):
    print(name, age, args, args, city, job)


'''命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错'''
print("------person3------")
'''person3('Jack', 24, 'Beijing', 'Engineer')'''
'''命名关键字必须要提供参数，否则会报错'''
'''person3('chenqi', 20)'''
person3('chenqi', 20, city='wuhu', job='nurse')

'''命名关键字参数可以有缺省值，从而简化调用'''


def person4(name, age, *, city='wuhu', job):
    print(name, age, city, job)


'''由于命名关键字参数city具有默认值，调用时，可不传入city参数：'''
print("------person4------")
person4('chenqi', 20, job='nurse')
'''省略了city参数'''

'''参数组合'''
'''在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。'''
'''但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数'''

'''
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''
