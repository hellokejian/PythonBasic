def machine(x, y):
    print("制作一个%d元的%s味道的ice cream" % (x, y))


machine(5, 'chocolate')
l = [6, 'stawberry']
machine(*l)
d = {'x': 10, 'y': 'apple'}
machine(**d)
