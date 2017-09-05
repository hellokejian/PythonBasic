# def pringstr(str):
#     index = 0
#     while index < len(str):
#         print(str[index])
#         index += 1
#
#
# pringstr("kejian")
#
# def reverse(str):
#     index = len(str)-1
#     while index >= 0:
#         print(str[index])
#         index -= 1
#
# reverse("kejian")

# def forUseage(str):
#     for char in str:
#         print(char)
#
# forUseage("kejian")

# def addLetter():
#     prefixes = "JKLMNOPQ"
#     suffux = "ack"
#     for letter in prefixes:
#         if letter == 'O' or letter == 'Q':
#             print(letter + 'u' + suffux)
#         else:
#             print(letter + suffux)
#
#
# addLetter()

# def slice(str):
#     # s[m,n]从位置m开始,切到n位置,但不包括下标为n的那个元素
#     result = str[1:len(str)-1]
#     print(result)
#
# slice("kejian")

# print("kejian"[:])  # 全部切下来

# def find(word, letter, begin):
#     if begin >= len(word):
#         return -1
#     index = begin
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index += 1
#     return -1
#
#
# print(find("administrator", 'i', 4))

# print("kejian".upper())

# index = "kejian".find('e')
# print(index)

# print("administrator".find("st", 7, 9))

# print("to be honest, i am very pleased to see you".count("to", 5, 7))

"""strip"""
# print("  kejian ".strip())

""" 新的代码注释,学到了吧,哈哈"""

"""replace"""
# print("AppleStore".replace('Apple', "Oppo"))

"""in"""
# print("mi" in 'administrator')

"""字符串的关系操作符"""
print("apple" < "orange")
print("Apple" < "apple")
