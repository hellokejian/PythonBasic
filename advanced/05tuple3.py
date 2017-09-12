"""元组的比较"""
print((0, 1, 2) < (0, 3, 4))

"""将单词列表的单词按长度排序"""


def sort_by_length(words):
    origin_tuple = []
    for word in words:
        origin_tuple.append((len(word), word.strip()))
    origin_tuple.sort() # reverse=True
    new_tuple = []
    for len1, word1 in origin_tuple:
        new_tuple.append((len1, word1))
    return new_tuple


file = open("D:/WorkSpace(kejian)/Pycharm/PythonBasic/basic/12word.txt")
tuple2 = sort_by_length(file)
for length, word in tuple2:
    print(length, '-', word, '\n')
