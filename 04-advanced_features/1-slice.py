# 切片(取list或tuple的部分元素)

if __name__ == '__main__':
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    # 取前3个元素
    r = []
    for i in range(3):  # 循环获取前3个元素
        r.append(L[i])
    print(r)
    print(L[0:3])  # 从索引0开始取，直到索引3为止，但不包括索引3
    print(L[:3])  # 如果第一个索引是0，还可以省略
    print(L[-1])  # 取倒数第一个元素
    print(L[-2:])  # 取倒数两个元素
    L1 = list(range(100))
    print(L1[:10:2])  # 前10个数，每两个取一个
    print(L1[:])  # 复制一个list
    print(L1[::5])  # 所有数，每5个取一个

    # tuple也是一种list，唯一区别是tuple不可变
    print((0, 1, 2, 3, 4, 5)[:3])
    print('ABCDEFG'[:3])  # 字符串也可以看成是一种list，每个元素就是一个字符
