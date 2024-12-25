# 列表生成器:List Comprehensions,是python内置的非常简单却强大的可以用来创建list的生成式
import  os # 导入os模块

if __name__ == '__main__':
    print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print([x * x for x in range(1, 11)])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(m + n for m in 'ABC' for n in 'XYZ')  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
    print([d for d in os.listdir('.')])  # 列出当前目录下的所有文件和目录名
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    print([k + '=' + v for k, v in d.items()])  # ['x=A', 'y=B', 'z=C']
    # if...else
    print([x for x in range(1,11) if x % 2 == 0])
    # 不能在最后的if后面加else，因为跟在for后面的if是一个筛选条件，不能带else
    print([x if x % 2 == 0 else -x for x in range(1, 11)])
