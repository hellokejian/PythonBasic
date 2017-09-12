import os

str = '42'
camels = '%d' % 42
print(type(camels))

cwd = os.getcwd()
print("cwd:", cwd)

print("isdir:", os.path.isdir(cwd))
print("isfile:", os.path.isfile(cwd))

print("exists:", os.path.exists(cwd))

print("listdir:", os.listdir(cwd))

"""打印一个目录下所有的子文件，子文件的子文件等等"""
print('==========================')


def walk(dirname):
    list_files = os.listdir(dirname)
    for filename in list_files:
        path = os.path.join(dirname, filename)
        if os.path.isfile(path):
            print(path)
        else:
            print(path)
            walk(path)


walk('d:/XiaoMi')
