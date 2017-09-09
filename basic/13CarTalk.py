# def cartalk1(str):
#     if len(str) < 2:
#         return True
#     if str[0] != str[1]:
#         return False
#     return cartalk1(str[2:])

def findthird(str):
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
        if findthird(line):
            print(line)


# cartalk1()

def findReverse1():
    num = 100000
    while num < 999999:
        num_str = str(num)
        index = len(num_str)
        i = 0
        j = index - 1
        couples = 0
        while j > i:
            if couples >= 2:
                print(num)
            if num_str[i] == num_str[j]:
                couples += 1
                i += 1
                j -= 1
            else:
                j -= 1
                couples = 0
                break
        couples = 0
        i = 0
        j = index - 1
        while i < j:
            if num_str[i] == num_str[j]:
                couples += 1
                i += 1
                j -= 1
            else:
                i += 1
                couples = 0
                break
            if couples == 2:
                print(num)
        num += 1


def findReverse():
    num = 100000
    while num <= 999999:
        num_str = str(num)
        i = 0
        while i < 2:
            j = i + 3
            while j < 6:
                if is_Reversed(num_str[i:j + 1]):
                    print(num_str)
                    break
                else:
                    j += 1
            i += 1
        num += 1


def is_Reversed(str):
    length = len(str)
    index = 0
    while index <= length / 2:
        if str[index] != str[length - index - 1]:
            return False
        index += 1
    return True

    # print(is_Reversed("sksd"))
    # print("kejian"[0:6])


findReverse()
