from math import *


# def funWhile(n):
#     while n > 0:
#         print('Looping')
#         n -= 1
#
#
# funWhile(5)


# def inputFun():
#     while True:
#         line = input('<')
#         if line == 'done':
#             break
#         print(line)
#
#
# inputFun()

def square_root(a, x, epision):
    while True:
        y = (x + a / x) / 2
        print(y)
        # if abs(x - y) <= epision:
        #     break
        if y == x:
            break
        x = y
    return x


result = square_root(25, 3, 0.01)
