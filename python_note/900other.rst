====
其他
====

Logger
======

::

    import logging
    logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(name)s %(levelname)s %(message)s')
    LOG = logging.getLogger('test')
    LOG.debug('调试信息')
    LOG.info('有用的信息')
    LOG.warning('警告信息')
    LOG.error('错误信息')
    LOG.critical('严重错误信息')

* %(name)s Logger的名字
* %(levelno)s 数字形式的日志级别
* %(levelname)s 文本形式的日志级别
* %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
* %(filename)s 调用日志输出函数的模块的文件名
* %(module)s 调用日志输出函数的模块名
* %(funcName)s 调用日志输出函数的函数名
* %(lineno)d 调用日志输出函数的语句所在的代码行
* %(created)f 当前时间，用UNIX标准的表示时间的浮点数表示
* %(relativeCreated)d 输出日志信息时的，自Logger创建以来的毫秒数
* %(asctime)s 字符串形式的当前时间。默认格式是“2003-07-0816:49:45,896”。逗号后面的是毫秒
* %(thread)d 线程ID。可能没有
* %(threadName)s 线程名。可能没有
* %(process)d 进程ID。可能没有
* %(message)s 用户输出的消息

读取 Excel 文件内容
===================

::

    import xlrd
    workbook = xlrd.open_workbook(filename) #打开文件
    sheetcount = workbook.nsheets #文件内sheet的数量
    sheet = workbook.sheet_by_index(i) #获得某个sheet，第一个sheet索引为0
    rowcount = sheet.nrows #最大行数
    colcount = sheet.ncols #最大列数

交换变量
========

::

    x = 6
    y = 5
    x, y = y, x
    print x
    >>> 5
    print y
    >>> 6

if 语句在行内
=============

::

    print "Hello" if True else "World"

连接
====

下面的最后一种方式在绑定两个不同类型的对象时显得很cool::

    nfc = ["Packers", "49ers"]
    afc = ["Ravens", "Patriots"]
    print nfc + afc
    >>> ['Packers', '49ers', 'Ravens', 'Patriots']
    print str(1) + " world"
    >>> 1 world
    print `1` + " world"
    >>> 1 world
    print 1, "world"
    >>> 1 world
    print nfc, 1
    >>> ['Packers', '49ers'] 1

数字技巧
========

::

    #除后向下取整
    print 5.0//2
    >>> 2
    # 2的5次方
    print 2**5
    >> 32

    #注意浮点数的除法
    print .3/.1
    >>> 2.9999999999999996
    print .3//.1
    >>> 2.0

数值比较
========

::

    x = 2
    if 3 > x > 1:
        print x
    >>> 2
    if 1 < x > 0:
        print x
    >>> 2

60 个字符解决 FizzBuzz
======================

前段时间Jeff Atwood 推广了一个简单的编程练习叫FizzBuzz，问题引用如下：
写一个程序，打印数字1到100，3的倍数打印Fizz来替换这个数，5的倍数打印Buzz，
对于既是3的倍数又是5的倍数的数字打印FizzBuzz。这里就是一个简短的，有意思
的方法解决这个问题::

    for x in range(101):print"fizz"[x%3*4::]+"buzz"[x%5*4::]or x

计数时使用 Counter 对象
=======================

这听起来显而易见，但经常被人忘记。对于大多数程序员来说，数一个东西是一项
很常见的任务，而且在大多数情况下并不是很有挑战性的事情——这里有几种方法
能更简单的完成这种任务。

Python的collections类库里有个内置的dict类的子类，是专门来干这种事情的::

    >>> from collections import Counter
    >>> c = Counter('hello world')
    >>> c
    Counter({'l': 3, 'o': 2, ' ': 1, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})
    >>> c.most_common(2)
    [('l', 3), ('o', 2)]

集合
====

除了python内置的数据类型外，在collection模块同样还包括一些特别的用例，在
有些场合Counter非常实用。如果你参加过在这一年的Facebook HackerCup，你甚至
也能找到他的实用之处::

    from collections import Counter
    print Counter("hello")
    >>> Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

迭代工具
========

和collections库一样，还有一个库叫itertools，对某些问题真能高效地解决。
其中一个用例是查找所有组合，他能告诉你在一个组中元素的所有不能的组合方式::

    from itertools import combinations
    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for game in combinations(teams, 2):
    print game
    >>> ('Packers', '49ers')
    >>> ('Packers', 'Ravens')
    >>> ('Packers', 'Patriots')
    >>> ('49ers', 'Ravens')
    >>> ('49ers', 'Patriots')
    >>> ('Ravens', 'Patriots')

False == True
=============

比起实用技术来说这是一个很有趣的事，在python中，True和False是全局变量，因此::

    False = True
    if False:
        print "Hello"
    else:
        print "World"
    >>> Hello

创建一次性的、快速的小型web服务
===============================

python 内置一个命令::

	python -m SimpleHTTPServer

有时候，我们需要在两台机器或服务之间做一些简便的、很基础的RPC之类的交互。
我们希望用一种简单的方式使用B程序调用A程序里的一个方法——有时是在另一台
机器上。仅内部使用。

我并不鼓励将这里介绍的方法用在非内部的、一次性的编程中。我们可以使用一种
叫做XML-RPC的协议 (相对应的是这个Python库)，来做这种事情。

下面是一个使用SimpleXMLRPCServer模块建立一个快速的小的文件读取服务器的例子::

    from SimpleXMLRPCServer import SimpleXMLRPCServer

    def file_reader(file_name):
        with open(file_name, 'r') as f:
            return f.read()

    server = SimpleXMLRPCServer(('localhost', 8000))
    server.register_introspection_functions()
    server.register_function(file_reader)
    server.serve_forever()

客户端::

    import xmlrpclib
    proxy = xmlrpclib.ServerProxy('http://localhost:8000/')
    proxy.file_reader('/tmp/secret.txt')

漂亮的打印出JSON
================

为了能让JSON数据表现的更友好，我们可以使用indent参数来输出漂亮的JSON。
当在控制台交互式编程或做日志时，这尤其有用::

    >>> import json
    >>> print(json.dumps(data))  # No indention
    {"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": true}, {"age": 29, "name": "Joe", "lactose_intolerant": false}]}
    >>> print(json.dumps(data, indent=2))  # With indention{
      "status": "OK",
      "count": 2,
      "results": [
        {
          "age": 27,
          "name": "Oz",
          "lactose_intolerant": true
        },
        {
          "age": 29,
          "name": "Joe",
          "lactose_intolerant": false
        }
      ]
    }

同样，使用内置的pprint模块，也可以让其它任何东西打印输出的更漂亮。


