# 迭代: 给定一个list或tuple，通过for循环来遍历，这种遍历成为迭代(Iteration)
from collections.abc import Iterable

if __name__ == '__main__':
    # 在python中遍历是通过for in来完成的
    d = {'a': '1', 'b': '2', 'c': '3'}
    for key in d:
        print(key)
    # 默认情况下，dict迭代的是key，如果要迭代value，可以用for value in d.values()
    for value in d.values():
        print(value)
    # 如果要同时迭代key和value，可以用for k, v in d.items()
    for k, v in d.items():
        print(k, v)
    # 如何判断一个对象是否可迭代，通过collections.abc模块的Iterable类型判断
    print(isinstance('abc', Iterable))
    print(isinstance([1, 2, 3], Iterable))
    print(isinstance(123, Iterable))
    # 如果要对list实现像Java那样的下标循环，python内置的enumerate函数可以把一个list变成索引-元素对
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)
    # for循环里同时引用两个变量
    for x, y in ((1, 1), (2, 4), (3, 9)):
        print(x, y)