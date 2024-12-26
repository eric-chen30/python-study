#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

__author__ = 'Vooey Chen'

# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
import functools

if __name__ == '__main__':
    # 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
    int2 = functools.partial(int, base=2)
    print(int2('1000000'))  # 64
    max2 = functools.partial(max, 10)
    print(max2(5, 6, 7))  # 10

"""
    一些规范：
    1，正常函数和变量名是公开的，可以被直接引用，比如：abc，x123，PI等；
    2，类似__xx__这样的变量是特殊变量，可以被直接引用，但有特殊用途，比如__author__，__name__，__doc__等；
    3，类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
"""