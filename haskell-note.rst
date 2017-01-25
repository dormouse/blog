Haskell Note
************

:date: 2017-01-25 09:51:42 +08:00
:slug: haskell-note
:tags: haskell
:category: note
:author: Dormouse Young


============
Haskell 笔记
============

:date: 2015-05-18
:modified: 2015-05-18
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
-----------------------

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




