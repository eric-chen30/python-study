# 返回函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 如果不需要立即求和，而是根据需要再计算，可以先不返回结果而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum

def inc():
    x = 0
    def inc_inner():
        nonlocal x  # nonlocal关键字用来在函数或其他作用域中使用外层(非全局)
        x =  x + 1
        return x
    return inc_inner


if __name__ == '__main__':
    f = lazy_sum(1, 3, 5, 7, 9)
    print(f)  # <function lazy_sum.<locals>.sum at 0x000001F7D3C8F0D0>
    print(f())  # 25
    # 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
    f1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
    print(f1 == f2)  # False
    # f1()和f2()的调用结果互不影响
    print('----------------------')
    # 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
    f11 = inc()
    print(f11())  # 1
    print(f11())  # 2

