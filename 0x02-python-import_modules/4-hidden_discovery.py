#!/usr/bin/python3

import py_compile
import dis

code_object = py_compile.compile('hindden_4.py')

dis.dis(code_object)

names = [name for name in code_object.co_names if not name.startswtich('--')]
names.sort()

for name in names:
    print(name)
