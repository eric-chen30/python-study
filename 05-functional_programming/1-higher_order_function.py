from functools import reduce


def fn1(x):
    return x * x


def fn2(x, u):
    return x + u


def fn3(x):
    return x % 2 == 0


def not_empty(s):
    return s and s.strip()


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


if __name__ == '__main__':
    # 将list做统一处理
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # map()函数接收两个参数，一个是函数，一个是Iterable，
    r = map(fn1, list1)
    # 结果r是一个迭代器Iterator，是惰性序列，通过list()函数让它把整个序列都计算出来并返回一个list
    print(list(r))
    # map作为高阶函数
    print((list(map(str, list1))))  # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('----------------------')
    # reduce(f, [x1, x2, x3, x4]]) = f(f(f(x1, x2), x3), x4)
    print(reduce(fn2, list1))  # 1+2+3+...+9 = 45
    print('----------------------')
    # filter()函数用于过滤序列
    print(list(filter(fn3, list1)))  # [2, 4, 6, 8]
    print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))  # ['A', 'B', 'C']
    print('----------------------')
    # 用filter求素数
    for n in primes():
        if n < 100:
            print(n)
        else:
            break
    print('----------------------')
    # sorted()函数就可以对list进行排序
    print(sorted([36, 5, -12, 9, -21]))  # [-21, -12, 5, 9, 36]
    # 可以接收一个key函数来实现自定义的排序
    print(sorted([36, 5, -12, 9, -21], key=abs))  # [5, 9, -12, -21, 36]
    # 字符串排序: 默认情况下，对字符串排序，是按照ASCII的大小比较的
    print(sorted(['bob', 'about', 'Zoo', 'Credit']))  # ['Credit', 'Zoo', 'about', 'bob']
    # 忽略大小写排序
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))  # ['about', 'bob', 'Credit', 'Zoo']
    # 反向排序
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))  # ['Zoo', 'Credit', 'bob', 'about']