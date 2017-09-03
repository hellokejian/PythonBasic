import math
def check_format(a,b,c,n):
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    if n <= 2:
        return
    if a**n + b**n != c**n:
        print('费马是对的')
    else:
        print('费马是错的')

check_format('1','2','3','4')
