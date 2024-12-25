# 迭代器
"""
    可以直接作用于for循环的数据类型有以下几种：
        一类是集合数据类型，如list、tuple、dict、set、str等；
        一类是generator，包括生成器和带yield的generator function。
    这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
    可以使用isinstance()判断一个对象是否是Iterable对象

    生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
    把list、dict、str等Iterable变成Iterator可以使用iter()函数
"""

from collections.abc import Iterator, Iterable

if __name__ == '__main__':
    # print(isinstance([], Iterable))
    # print(isinstance({}, Iterable))
    # print(isinstance('abc', Iterable))
    # print(isinstance((x for x in range(10)), Iterable))
    # print(isinstance(100, Iterable))
    print('------------------------')
    print(isinstance([], Iterator))
    print(isinstance({}, Iterator))
    print(isinstance('abc', Iterator))
    print(isinstance((x for x in range(10)), Iterator))
    print(isinstance(100, Iterator))
    # 生成器不仅可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值
    print('------------------------')
    print(isinstance(iter([]), Iterator))
    print(isinstance(iter({}), Iterator))
