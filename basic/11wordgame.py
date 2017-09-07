# fin = open('d:/words.txt')
# index = 0
# for line in fin:
#     print(line.strip())
#     index += 1
# print(index)

"""打印文件中长度超过20个字符的单词"""


def get_more_than_20():
    fin = open("d:/words.txt")
    for line in fin:
        if len(line) > 20:
            print(line.strip())


# get_more_than_20()

"""输出不含e的单词"""


def has_no_e(str):
    for char in str:
        if char == 'e':
            return False
    return True


def print_without_e():
    fin = open("d:/words.txt")
    for line in fin:
        if has_no_e(line):
            print(line)


# print_without_e()


"""禁止字母"""


def avoids(words, str):
    for char in str:
        if char in words:
            return False
    return True


def print_without():
    index = 0
    avoid_str = input("请输入一个")
    fin = open("d://words.txt")
    for line in fin:
        if avoids(line, avoid_str):
            index += 1
            print(line)
    return index


# num = print_without()
# print(num)


def order(str):
    flag = False
    if len(str) == 1:
        flag = True
        return flag
    ord1 = ord(str[0])
    ord2 = ord(str[1])

    if ord1 == ord2 - 1:
        flag = order(str[1:])

    else:
        return flag
    return flag


print(order("ab"))
