# 匿名函数:
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

def build(x, y):
    return lambda: x * x + y * y

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
L1 = list(filter(lambda x: x % 2 == 1, range(1, 20)))

if __name__ == '__main__':
    f = lambda x: x * x
    print(f(5))  # 25
    result = build(3, 4)
    print(result())  # 25
    print(L)
    print(L1)