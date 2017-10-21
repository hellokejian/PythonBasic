from numpy import *

print(sin(2 * pi))
'''模块优化'''
import py_compile
py_compile.compile('yield_test.py', 'yield_test_opti.pyc')