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

def ack(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    else:
        return
print(ack(3,6))