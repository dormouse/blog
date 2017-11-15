============
Haskell Note
============

:date: 2015-05-18
:modified: 2017-02-03
:slug: haskell-note
:tags: haskell, note
:category: haskell
:author: Dormouse Young

入门
====

安装::

    sudo apt-get install ghc

终端命令::

    ghci

可以用ghci的 :set prompt 来进行修改::

    Prelude> :set prompt "ghci>"
    ghci>

导入模块::

    ghci> :module + Data.Ratio
    或者
    ghci> :m + Data.Ratio

我们探索类型世界的第一步是修改 ghci，让它在返回表达式的求值结果时，打印
出这个结果的类型。使用 ghci 的 :set命令可以做到::

    Prelude> :set +t

取消::

    Prelude Data.Ratio> :unset +t

Haskell 给每个操作符一个数值型的优先级值，从 1 表示最低优先级，
到9表示最高优先级。高优先级的操作符先于低优先级的操作符被应用
(apply)。在 ghci 中我们可以用命令 ``:info`` 来查看某个操作符的
优先级。


How to run the compiler
=======================

::

    % ghc --make Main.hs -o main

The “–make” option tells GHC that this is a program and not just a library
and you want to build it and all modules it depends on. “Main.hs” stipulates
the name of the file to compile; and the “-o main” means that you want to put
the output in a file called “main”.


列表
====

在头部添加元素::

    Prelude> 0:[1,2]
    [0,1,2]
    Prelude> 5:1:2:3:4:[]
    [5,1,2,3,4]

列表的长度::

    Prelude> length []
    0
    Prelude> length [1,2,3]
    3

两个列表相加::

    Prelude> [1,2] ++ [3,4]
    [1,2,3,4]

返回第一个元素，只能用于非空列表::

    Prelude> head [1, 2, 3, 4]
    1

返回除第一个以外，只能用于非空列表::

    Prelude> tail [1, 2, 3, 4]
    [2,3,4]

前 N 个::

    Prelude> take 2 [1, 2, 3, 4, 5]
    [1,2]

前 N 个以外::

    Prelude> drop 2 [1, 2, 3, 4, 5]
    [3,4,5]

嵌套使用::

    Prelude> head (drop 2 "azety")
    'e'

There are three primary list-processing functions:
``map``, ``filter`` and ``foldr`` (also ``foldl``)::

    Prelude> map odd [1,2,3,4]
    [True,False,True,False]

    Prelude> filter odd [1,2,3,4]
    [1,3]

    Prelude> foldr (+) 0 [3,8,12,5]
    28
    Prelude> foldr (*) 1 [4,8,5]
    160
    Prelude> foldr (-) 1 [4,8,5]
    0

    foldr (-) 1 [4,8,5]
    ==> 4 - (foldr (-) 1 [8,5])
    ==> 4 - (8 - foldr (-) 1 [5])
    ==> 4 - (8 - (5 - foldr (-) 1 []))
    ==> 4 - (8 - (5 - 1))
    ==> 4 - (8 - 4)
    ==> 4 - 4
    ==> 0

    Prelude> foldl (-) 1 [4,8,5]
    -16

    foldl (-) 1 [4,8,5]
    ==> foldl (-) (1 - 4) [8,5]
    ==> foldl (-) ((1 - 4) - 8) [5]
    ==> foldl (-) (((1 - 4) - 8) - 5) []
    ==> ((1 - 4) - 8) - 5
    ==> ((-3) - 8) - 5
    ==> (-11) - 5
    ==> -16

.. note::

    ``foldl`` is often more efficient than ``foldr``. However, ``foldr``
    can work on infinite lists, while ``foldl`` cannot. This is because
    before foldl does anything, it has to go to the end of the list. On
    the other hand, ``foldr`` starts producing output immediately. For
    instance, ``foldr (:) [] [1,2,3,4,5]`` simply returns the same list.
    Even if the list were infinite, it would produce output. A similar
    function using ``foldl`` would fail to produce any output.

String
======

A String is a list of Chars::

    Prelude> 'H':'e':'l':'l':'o':[]
    "Hello"
    Prelude> "Hello " ++ "World"
    "Hello World"

Non-string values can be converted to strings using the ``show`` function,
and strings can be converted to non-string values using the ``read``
function::

    Prelude> "Five squared is " ++ show (5*5)
    "Five squared is 25"
    Prelude> read "5" + 3
    8
    Prelude> read "Hello" + 3
    *** Exception: Prelude.read: no parse


元组
====

二元元组取值，注意 ``fst`` 和 ``snd`` 不能作用于三元及以上元组::

    Prelude> fst (1, 'a')
    1
    Prelude> snd (1, 'a')
    'a'

Use a combination of ``fst`` and ``snd`` to extract the character out of the
tuple ``((1,’a’),"foo")`` ::

    Prelude> let xs = ((1,'a'),"foo")
    Prelude> fst (fst xs)
    1
    Prelude> snd (fst xs)
    'a'
    Prelude> snd xs
    "foo"
    Prelude>




