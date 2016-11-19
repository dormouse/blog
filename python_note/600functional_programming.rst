==========
函数式编程
==========

lambda
======

lambda 语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。
lambda 语句构建是一个函数对象::

    In [1]: f = lambda x: x * 2 

    In [2]: f(8)
    Out[2]: 16

    In [3]: f
    Out[3]: <function __main__.<lambda>>

filter
======

filter(function or None, sequence) -> list, tuple, or string

Return those items of sequence for which function(item) is true.  If
function is None, return the items that are true.  If sequence is a tuple
or string, return the same type, else return a list::

    In [4]: foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

    In [5]: filter(lambda x: x % 3 == 0, foo)
    Out[5]: [18, 9, 24, 12, 27]

map
===

map(function, sequence[, sequence, ...]) -> list
    
Return a list of the results of applying the function to the items of the
argument sequence(s)::

    In [6]: map(lambda x: x * 2 + 10, foo)
    Out[6]: [14, 46, 28, 54, 44, 58, 26, 34, 64]

If more than one sequence is given, the function is called with an argument
list consisting of the corresponding item of each sequence, substituting
None for missing values when not all sequences have the same length::

    In [7]: foo1 = [1]*9

    In [8]: map(lambda x,y:x+y, foo, foo1)
    Out[8]: [3, 19, 10, 23, 18, 25, 9, 13, 28]

If the function is None, return a list of the items of the sequence
(or a list of tuples if more than one sequence)::

    In [9]: nfc = ["Packers", "49ers"]

    In [10]: afc = ["Ravens", "Patriots"]

    In [11]: map(None, nfc, afc)
    Out[11]: [('Packers', 'Ravens'), ('49ers', 'Patriots')]

reduce
======

reduce(function, sequence[, initial]) -> value
    
Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty::

    In [9]: reduce(lambda x, y: x + y, foo)
    Out[9]: 139

reduce 函数在 python3 中已经不属于 build-in 了，而是在 functools 模块下，
如需使用，需要从functools模块中引入。

