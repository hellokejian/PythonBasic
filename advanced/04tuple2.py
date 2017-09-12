"""一 元组和列表"""

# 可将字符串和列表拉到一起
str = 'kejian'
num = [1, 2, 3, 4, 5, 6]

# iterator = zip(str, num).__iter__()
# while iterator.__next__:
#     print(iterator)

"""可以使用for循环来访问元组的列表"""
tuplelist = [('kejian', 0), ('chenqi', 1), ('kechen', 3)]
for name, num in tuplelist:
    print(name, num)

print("========================")

"""zip 与 for 放在一起使用会怎么样？"""


def zip_for(t1, t2):
    for x, y in zip(t1, t2):
        if x != y:
            return False
    return True


flag = zip_for('kejian', 'kejian')
print(flag)

"""如果要遍历序列中的元素和它们的下标，可以使用内置函数enumerate"""
for index, element in enumerate('kejian'):
    print(index, element)

"""二 字典与元组"""

"""字典的item方法可以将字典的key-value对变成一个元组，接着将字典里的所有元组组成一个列表"""
print("================================")
dictionary = {'a': 0, 'b': 1, 'c': 2}
lists = dictionary.items()
print(lists)

"""逆向思考，如何将一个元组列表变成一个字典，可以使用dict方法"""
tuplelist = [('kejian', 0), ('chenqi', 1), ('kechen', 3)]
resultdict = dict(tuplelist)
print(resultdict)

"""使用zip 与 dict 方法可以创建出一个字典"""
print('==================================')
resultdict = dict(zip(range(6), "kejian"))
print(resultdict)

"""字典方法update接受一个元组列表，并将他们作为键值对添加到现有字典中"""
new_tuple_list = [(6, 'very'), (7, "good")]
resultdict.update(new_tuple_list)
print(resultdict)

"""列表不可以作为字典的键，但是可以使用元组作为字典的键"""
print('================================')
lastname = 'ke'
firstname = 'jian'
resultdict[lastname, firstname] = 'very handsome'
print(resultdict)
# 遍历这种字典的时候，可以使用元组赋值的方式来遍历字典(由于环境原因，下面的语句未能实现效果）
for lastname, firstname in resultdict:
    print(firstname, lastname, resultdict[lastname, firstname])
