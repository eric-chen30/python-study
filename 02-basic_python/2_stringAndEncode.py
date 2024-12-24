# 字符串和编码
r = 2.5
s = 3.14 * r ** 2

s1 = 72
s2 = 85
percentTep = (s2 - s1)/s1 * 100

if __name__ == '__main__':
    print(ord('A'), ord('中'), chr(66), chr(25991))
    print(len('apple'))
    print('Hi, %s, you have $%d.' % ('Michael', 1000000))  # 常见占位符 %d %s %f %x
    print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
    print(f'The area of circle with radius {r} is {s:.2f}')
    print('小明成绩从72提升到了85，提升了%f个百分点' % percentTep)
    print('小明成绩从72提升到了85，提升了{0:.1f}个百分点'.format(round(percentTep, 1)))
    print(f'小明成绩从72提升到了85，提升了{percentTep:.1f}个百分点')

