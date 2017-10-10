from functools import reduce


def multiply(x, y):
    return x * y


print(reduce(multiply, [1, 2, 3, 4, 5]))

f = lambda x, y: x * y
print(f(2, 3))

print('=========================================')
result = reduce(lambda x, y: x + y, [3, 4, 5])
print(result)

foo = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print('=========================================')
result = filter(lambda x: x % 3 == 0, foo)
for item in result:
    print(item)

print('=========================================')
result = map(lambda x: x * 10 + 1, foo)
for item in result:
    print(item)
