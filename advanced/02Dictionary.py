import random

"""字典类似于列表，but more通用，列表下表必须是整数，但是字典下标可以是任意类型"""
fin = open("D:/WorkSpace(kejian)/Pycharm/PythonBasic/basic/12word.txt")

"""create a dictionary"""
dict1 = dict()

"""add new element"""
dict1['first'] = 'kejian'


def save_to_dict():
    for line in fin:
        # print(line)
        dict1[line.strip()] = str(random.uniform(10, 20))


"""get the length of dictionary key-value pair"""
length = len(dict1)

"""make sure whether a key is in the dictionary"""
flag = 'first' in dict1

"""how to make sure whether a value is in the dictionary"""
vals = dict1.values()

"""use dictionary as a counter of the times of each letter"""


def histograms(str):
    d = dict()
    for char in str:
        if char in d:
            d[char] += 1
        else:
            dict[char] = 1
    return d


"""字典的键值对存储没有固定顺序"""

"""反向查找"""

"""字典和列表"""


def inverse_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = key
        else:
            inverse[val].append(key)
    return inverse


d = inverse_dict(histograms("suckmyass"))
print(d)

save_to_dict()
print(dict1)
print('aa' in dict1)
