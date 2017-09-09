str_list = ['123', 'hello', 'holly oil', 'mercy']
flag = 'hello' in str_list
flag2 = "hello" in str_list
# print(flag, flag2)

# for ele in str_list:
#     print(ele)

# for i in range(len(str_list)):
#     print(str_list[i])

str_list2 = [1, 2, 3] * 3
# print(str_list2)

"""列表是可变的，可切片的"""
# str_list2 = str_list2[2:6]
# print(str_list2)
# 切割不会使得列表变化
# str_list2[1:2]
# print(str_list2)

"""将字符拆分成数组"""
# s = "this is a example for test"
# list = s.split()
# print(list)

"""拼接元素"""
t = ['my', 'name', 'is', 'kejian']
delimiter = " "
delimiter2 = "-"
str = delimiter.join(t)
str2 = delimiter2.join(t)
# print(str)
# print(str2)

"""相等和相同的定义"""
a = 'banana'
b = 'banana'
# print(a is b)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
# print(list2 is list1)  # 两者相等
# print(list1 == list2)  # 但是两者却不相同

"""引用"""
a = "banana"
a = "apple"
print(a)
