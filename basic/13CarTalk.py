# def cartalk1(str):
#     if len(str) < 2:
#         return True
#     if str[0] != str[1]:
#         return False
#     return cartalk1(str[2:])

def findtwice(str):
    if len(str) < 6:
        return False
    index = 0
    couples = 0
    while index < len(str) - 1:
        if couples == 3:
            return True
        if str[index] != str[index + 1]:
            couples = 0
            index += 1
        else:
            index += 2
            couples += 1
    return False


def cartalk1():
    fin = open("D:/WorkSpace(kejian)/Pycharm/PythonBasic/basic/12word.txt")
    for line in fin:
        if findtwice(line):
            print(line)


cartalk1()
