========
列表操作
========

列表推导（过滤）
================

过滤偶数方法::

    numbers = [1,2,3,4,5,6]
    even = []
    for number in numbers:
        if number%2 == 0:
            even.append(number)

推导方式过滤::

    numbers = [1,2,3,4,5,6]
    even = [number for number in numbers if number%2 == 0]

倒序列表
========

::

    >>> a = [1,2,3]
    >>> a[::-1]
    [3, 2, 1]

判断一个列表是否为空
====================

::

    if mylist:
        # Do something with my list
    else:
        # The list is empty

排序
====

在包含某元素的列表中依据某个属性排序是一个很常见的操作。例如这里我们先创建
一个包含 person 的 list ::

    class Person(object):
        def __init__(self, age):
            self.age = age

    persons = [Person(age) for age in (14, 78, 42)]

传统的方式是::

    def get_sort_key(element):
        return element.age

    for element in sorted(persons, key=get_sort_key):
        print "Age:", element.age

更加简洁、可读性更好的方法是使用 Python 标准库中的 operator 模块::

    from operator import attrgetter
    for element in sorted(persons, key=attrgetter('age')):
        print "Age:", element.age

attrgetter 方法优先返回读取的属性值作为参数传递给 sorted 方法。operator
模块还包括 itemgetter 和 methodcaller 方法，作用如其字面含义。

同时迭代两个列表
================

::

    nfc = ["Packers", "49ers"]
    afc = ["Ravens", "Patriots"]
    for teama, teamb in zip(nfc, afc):
        print teama + " vs. " + teamb
    >>> Packers vs. Ravens
    >>> 49ers vs. Patriots

带索引的列表迭代
================

::

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for index, team in enumerate(teams):
        print index, team
    >>> 0 Packers
    >>> 1 49ers
    >>> 2 Ravens
    >>> 3 Patriots

初始化列表的值
==============

::

    items = [0]*3
    print items
    >>> [0,0,0]

列表转换为字符串
================

::

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    print ", ".join(teams)
    >>> 'Packers, 49ers, Ravens, Patriots'

获取列表的子集
==============

有时，你只需要列表中的部分元素，这里是一些获取列表子集的方法::

    x = [1,2,3,4,5,6]
    #前3个
    print x[:3]
    >>> [1,2,3]
    #中间4个
    print x[1:5]
    >>> [2,3,4,5]
    #最后3个
    print x[3:]
    >>> [4,5,6]
    #奇数项
    print x[::2]
    >>> [1,3,5]
    #偶数项
    print x[1::2]
    >>> [2,4,6]

