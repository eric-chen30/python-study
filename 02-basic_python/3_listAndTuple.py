students = ['Michael', 'Bob', 'Tracy']
# list中数据元素类型可以不相同，也可以是数组
s1 = ['python', 'java', ['asp', 'php'], 'scheme']
s2 = ['apple', 123, True]

if __name__ == '__main__':
    # ------------list--------------
    print('总共有%d个学生，最后一个学生名字为%s' % (len(students), students[-1]))
    # append 新增一个student
    students.append('Vooey')
    print(students)
    # 把指定元素插到指定位置
    students.insert(1, 'Jack')
    print(students)
    # 删除末尾元素
    students.pop()
    print(students)
    # 删除指定位置元素
    students.pop(1)
    print(students)
    # 替换某个索引的元素值
    students[-1] = 'Vooey'
    print(students)
    # s2可以看组一个二维数组，获取php
    print(s1[2][1])
    # 空数组的长度为0
    print(len([]))
    # ------------tuple--------------
    '''
        tuple一旦初始化不可修改
        可以通过索引获取指定元素，但没有append、insert和索引位置替换等方法
        优点：不可变，更安全
    '''
    # 定义一个只有一个元素的tuple,输出也会有,隔开以避免歧义,t=(1)定义的是数字1而不是tuple
    t = (1,)
    print(t)
    # tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
    t1 = ('a', 'b', ['A', 'B'])
    t1[2][0] = 'X'
    t1[2][1] = 'Y'
    print(t1)
    # ------------practice--------------
    L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Bob']
    ]
    # 输出Apple、Python、Bob
    print(L[0][0], L[1][1], L[2][2])