==========
日期和时间
==========

Python 标准库中的 datetime 模块提供了各种对日期和时间的处理方法。


基本操作
========

::

    In [1]: import datetime

    In [2]: now = datetime.datetime.now()

    In [3]: now
    Out[3]: datetime.datetime(2015, 6, 1, 10, 26, 38, 836099)

    In [4]: now.strftime("%Y-%m-%d %H:%M:%S")
    Out[4]: '2015-06-01 10:26:38'

    In [5]: now.replace(hour=0,minute=0,second=0)
    Out[5]: datetime.datetime(2015, 6, 1, 0, 0, 0, 836099)

    In [6]: now - datetime.timedelta(days=1)
    Out[6]: datetime.datetime(2015, 5, 31, 10, 26, 38, 836099)

转义符说明：

====== ==============================================
转义符 说明
====== ==============================================
%a     本地简化星期名称
%A     本地完整星期名称
%b     本地简化的月份名称
%B     本地完整的月份名称
%c     本地相应的日期表示和时间表示
%d     月内中的一天（0-31）
%H     24小时制小时数（0-23）
%I     12小时制小时数（01-12）
%j     年内的一天（001-366）
%m     月份（01-12）
%M     分钟数（00-59）
%p     本地A.M.或P.M.的等价符
%S     秒（00-59）
%U     一年中的星期数（00-53）星期天为星期的开始
%w     星期（0-6），星期天为星期的开始
%W     一年中的星期数（00-53）星期一为星期的开始
%x     本地相应的日期表示
%X     本地相应的时间表示
%y     两位数的年份表示（00-99）
%Y     四位数的年份表示（000-9999）
%Z     当前时区的名称
%%     %号本身
====== ==============================================


时区转换
========

首先利用 datetime 中提供的 utcnow() 方法获取到当前UTC时间::

    In [1]: from datetime import datetime

    In [2]: utc_now = datetime.utcnow()

    In [3]: utc_now
    Out[3]: datetime.datetime(2015, 5, 30, 3, 3, 59, 153675)

    In [4]: print utc_now.tzinfo
    None

此时 tzinfo 为 None::

    In [5]: from pytz import timezone

    In [5]: tzchina = timezone('Asia/Shanghai')

    In [7]: tzchina
    Out[7]: <DstTzInfo 'Asia/Shanghai' LMT+8:06:00 STD>

    In [8]: utc = timezone('UTC')

    In [9]: utc_now.replace(tzinfo=utc).astimezone(tzchina)
    Out[9]: datetime.datetime(2015, 5, 30, 11, 3, 59, 153675, tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>)

要转换为其他时区，则以此类推。

在 Django 中转换时区::

    In [1]: from django.utils.timezone import utc

    In [2]: from django.utils.timezone import localtime

    In [3]: from datetime import datetime

    In [4]: now = datetime.utcnow().replace(tzinfo=utc)

    In [5]: now
    Out[5]: datetime.datetime(2015, 5, 30, 3, 16, 57, 362481, tzinfo=<UTC>)

    In [6]: localtime(now)
    Out[7]: datetime.datetime(2015, 5, 30, 11, 16, 57, 362481, tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>)


程序暂停
========

函数原型： time.sleep(secs) ，secs 参数代表暂停的秒数。示例::

    import random
    import time
    random.seed()
    time.sleep(random.random()*2)
