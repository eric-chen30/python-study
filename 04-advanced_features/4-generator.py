# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 在python中，这种一遍循环一遍计算的机制，称为生成器：generator

# 斐波拉契数列
"""
    注意赋值语句：a, b = b, a + b
    相当于：
    t = (b, a + b) # t是一个tuple
    a = t[0]
    b = t[1]
"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # 定义generator的另一种方法。如果一个函数包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


if __name__ == '__main__':
    # g是一个生成器，而L是一个list
    L = [x for x in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    g = (x for x in range(10))  # <generator object <genexpr> at 0x100a0b340>
    print(L, g)
    # 通过next()函数获得generator的下一个返回值
    print(next(g))  # 0
    print(next(g))  # 1
    print(next(g))  # 2
    print(next(g))  # 3
    # generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
    # 通过for循环来迭代generator
    for n in g:
        print(n)
    print(fib(6))  # <generator object fib at 0x1049717e0>
    f = fib(6)
    print(f)  # <generator object fib at 0x1049717e0>
    o = odd()
    print(next(o))
    print(next(o))
    print(next(o))
    # odd()会创建一个新的generator
    print(next(odd()))  # step 1 1
    print(next(odd()))  # step 1 1
    print(next(odd()))  # step 1 1


