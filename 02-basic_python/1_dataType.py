# 数据类型
# Python允许在数字中间以_分隔,numberOne和numberTwo相等
numberOne = 10000000000
numberTwo = 10_000_000_000

# 对于很大或很小的浮点数要用科学计数法表示，10用e代替
floatA = 1.23e10
floatB = 1.23e-5

PI = 3.141592653589793

if __name__ == '__main__':
    # --------整数-------
    print(numberOne == numberTwo)  # True
    # --------浮点数-------
    print('floatA', floatA, 'floatB', floatB)
    # --------字符串-------
    print('\\\n\\')
    print(r'\\\n\\')  # 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
    print('''
        line1
        line2
        line3
    ''')
    # --------布尔值-------
    print(True and False)  # and or not =》 与、或、非
    print(True or False)
    print(not True)
    # --------常量-------
    print(PI)
