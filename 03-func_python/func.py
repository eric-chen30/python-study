# 定义函数
def main():
    print('Hello, world!')


# 定义一个空函数
def nop():
    pass


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 函数参数设置默认值
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    print(s)


# 默认参数必须指向不变对象
# def add_end(L=[]):
#     L.append('END')
#     return L

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# def person2(name, age, **kw, city, job):
#     print(name, age, city, job)

def person2(name, age, *, city, job):
    print(name, age, city, job)


'''
    参数组合
'''


# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    print(abs(-20) == abs(20))
    print(max(1, -2, 3, -5))
    # 数据类型转换
    print(int('123'), float('12.34'), str(1.23), bool(1), bool(''))
    main()
    print(my_abs(-20))
    # print(my_abs('A'))
    power(5, 3)
    s1 = add_end()
    print(s1)
    s2 = add_end()
    print(s1, s2)
    # 可变参数
    print(calc(1, 2, 3))
    # 如果已经有一个list或tuple，要调用可变参数，python允许在list或tuple前面加一个*号
    print(calc(*[1, 2, 3]), calc(*(1, 2, 3)))
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, **extra)
    # 命名关键字参数
    person2('Jack', 24, city='Beijing', job='Engineer')
    # 递归函数
    print(fact(5))
