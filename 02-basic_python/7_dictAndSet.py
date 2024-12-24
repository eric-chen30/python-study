if __name__ == '__main__':
    # --------------dict-----------------
    d = {'Michael': 95, 'Vooey': 100, 'Jack': 66}
    print(d['Michael'])
    d['Adam'] = 91
    print(d)
    # 给字典中已经存在的key赋值会产生覆盖
    d['Vooey'] = 92
    print(d)
    # 如果索引不存在的key会产生报错，所以一般会加上in判断
    print('Vooey' in d, 'Siri' in d)
    # 通过get(key)获取value
    print(d.get('Jack'))
    # 要删除一个key，使用pop(key)，对应的value也会删除
    d.pop('Jack')
    print('删除key为Jack的字段对象后字典:', d)

    ''''
        相比于list：
            1，查找和插入的速度极快，不会随着key的增加而变慢
            2，需要占用大量内存，内存浪费多
    '''

    # --------------set-----------------
    s = {1, 2, 3}
    print(s)
    # 重复元素被自动过滤
    s1 = {1, 2, 2, 3, 4, 4, 5}
    print(s1)
    # 通过add添加元素，如果添加相同元素不生效，remove删除元素
    s1.add(6)
    s1.add(2)
    print(s1)
    s1.remove(1)
    print(s1)

