def fab(max):
    a, b, n = 0, 1, 0
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


# fab(10)


def yieldfun(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield (b)
        a, b = b, a + b
        n = n + 1


def f():
    print('one')
    yield 1
    print('two')
    yield 2
    print('three')
    yield 3


g = f()
a = g.__next__()
print(a)
a = g.__next__()
print(a)
a = g.__next__()
print(a)
