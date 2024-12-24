def range_loop():
    for i in range(10):
        if i == 6:
            break
        print(i)


def loop_print_names():
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        if name == 'Bob':
            continue
        print(name)


# break退出循环，continue退出本次循环
def add_while_loop():
    sum1 = 0
    n = 99
    while n > 0:
        sum1 = sum1 + n
        n = n - 2
    print(sum1)


if __name__ == '__main__':
    range_loop()
    loop_print_names()
    print(list(range(5)))
    add_while_loop()
