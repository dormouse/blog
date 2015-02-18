
pandas 入门
===========

-  版本号： 0.1
-  创建时间： 2015-02-07 10:26:33
-  修改时间： |today|

建立环境
--------

安装 pandas
~~~~~~~~~~~

::

    sudo apt-get install build-essential python-dev 
    sudo apt-get install python-pandas
    sudo apt-get install python-scipy python-matplotlib python-tables
    sudo apt-get install python-numexpr python-xlrd python-statsmodels
    sudo apt-get install python-openpyxl python-xlwt python-bs4   

安装 ipython-notebook
~~~~~~~~~~~~~~~~~~~~~

::

    sudo pip install "ipython[notebook]"
    sudo pip install pygments

运行 ipython-notebook
~~~~~~~~~~~~~~~~~~~~~

::

    ipython notebook

导入 pandas
-----------

.. code:: python

    import pandas as pd
    import numpy as np

读入数据
--------

.. code:: python

    # 读入 CSV 格式数据
    df_sango = pd.read_csv('test.csv',encoding='utf-8')

复制数据
--------

.. code:: python

    df = df_sango.copy()
    df.head(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 100</td>
          <td> 42</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>  99</td>
          <td> 85</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>  99</td>
          <td> 51</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
      </tbody>
    </table>
    </div>



导出数据
--------

显示数据
--------

.. code:: python

    #显示开头的数据，缺省显示 5 条
    df.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 100</td>
          <td> 42</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>  99</td>
          <td> 85</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>  99</td>
          <td> 51</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 4</td>
          <td> 赵云</td>
          <td>  98</td>
          <td> 88</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 5</td>
          <td> 马超</td>
          <td>  98</td>
          <td> 48</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    #显示开头的数据，指定显示 8 条
    df.head(8)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 100</td>
          <td> 42</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>  99</td>
          <td> 85</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>  99</td>
          <td> 51</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 4</td>
          <td> 赵云</td>
          <td>  98</td>
          <td> 88</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 5</td>
          <td> 马超</td>
          <td>  98</td>
          <td> 48</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>5</th>
          <td> 6</td>
          <td> 典韦</td>
          <td>  98</td>
          <td> 45</td>
          <td>    双铁戟+5武力</td>
        </tr>
        <tr>
          <th>6</th>
          <td> 7</td>
          <td> 许褚</td>
          <td>  98</td>
          <td> 40</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>7</th>
          <td> 8</td>
          <td> 黄忠</td>
          <td>  97</td>
          <td> 66</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    #显示末尾的数据，缺省显示 5 条
    df.tail()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>250</th>
          <td> 251</td>
          <td> 向朗</td>
          <td> 34</td>
          <td> 83</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>251</th>
          <td> 252</td>
          <td> 左慈</td>
          <td> 33</td>
          <td> 98</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>252</th>
          <td> 253</td>
          <td> 曹植</td>
          <td> 32</td>
          <td> 91</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>253</th>
          <td> 254</td>
          <td> 谯周</td>
          <td> 32</td>
          <td> 69</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>254</th>
          <td> 255</td>
          <td> 于吉</td>
          <td> 30</td>
          <td> 97</td>
          <td> NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    #显示末尾的数据，缺省显示 3 条
    df.tail(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>252</th>
          <td> 253</td>
          <td> 曹植</td>
          <td> 32</td>
          <td> 91</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>253</th>
          <td> 254</td>
          <td> 谯周</td>
          <td> 32</td>
          <td> 69</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>254</th>
          <td> 255</td>
          <td> 于吉</td>
          <td> 30</td>
          <td> 97</td>
          <td> NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



操作单元
--------

.. code:: python

    # 单元格赋值
    # 单个单元格赋值
    df.ix[0,u'武力'] = 1001
    df.loc[df.index[1], u'智力']=999
    df.head(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 1001</td>
          <td>  42</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>   99</td>
          <td> 999</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>   99</td>
          <td>  51</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 多单个单元格赋值
    df.loc[df.index[0:2], u'智力'] = [100, 200]
    df.head(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 1001</td>
          <td> 100</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>   99</td>
          <td> 200</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>   99</td>
          <td>  51</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
      </tbody>
    </table>
    </div>



操作列
------

改变列头
~~~~~~~~

使用 columns 属性
^^^^^^^^^^^^^^^^^

.. code:: python

    #用一个列表来显式地指定，列表长度必须与列数一致
    # 示例 1
    df.columns = ['No', 'Name', 'FORCE', 'IQ', 'Artifact']
    df.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>No</th>
          <th>Name</th>
          <th>FORCE</th>
          <th>IQ</th>
          <th>Artifact</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 1001</td>
          <td> 100</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>   99</td>
          <td> 200</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>   99</td>
          <td>  51</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 4</td>
          <td> 赵云</td>
          <td>   98</td>
          <td>  88</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 5</td>
          <td> 马超</td>
          <td>   98</td>
          <td>  48</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 示例 2 ：大写转小写
    df.columns = [c.lower() for c in df.columns]
    df.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>no</th>
          <th>name</th>
          <th>force</th>
          <th>iq</th>
          <th>artifact</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 1001</td>
          <td> 100</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>   99</td>
          <td> 200</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>   99</td>
          <td>  51</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 4</td>
          <td> 赵云</td>
          <td>   98</td>
          <td>  88</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 5</td>
          <td> 马超</td>
          <td>   98</td>
          <td>  48</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



使用 rename 方法
^^^^^^^^^^^^^^^^

.. code:: python

    # 示例 1 ：小写转大写
    df = df.rename(columns=lambda x: x.upper())
    df.tail(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>NO</th>
          <th>NAME</th>
          <th>FORCE</th>
          <th>IQ</th>
          <th>ARTIFACT</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>252</th>
          <td> 253</td>
          <td> 曹植</td>
          <td> 32</td>
          <td> 91</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>253</th>
          <td> 254</td>
          <td> 谯周</td>
          <td> 32</td>
          <td> 69</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>254</th>
          <td> 255</td>
          <td> 于吉</td>
          <td> 30</td>
          <td> 97</td>
          <td> NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 示例 2 ：改变特定的列头
    df = df.rename(columns={'NAME': u'姓名', 'ARTIFACT': u'物品'})
    df.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>NO</th>
          <th>姓名</th>
          <th>FORCE</th>
          <th>IQ</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 1001</td>
          <td> 100</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>   99</td>
          <td> 200</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>   99</td>
          <td>  51</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 4</td>
          <td> 赵云</td>
          <td>   98</td>
          <td>  88</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 5</td>
          <td> 马超</td>
          <td>   98</td>
          <td>  48</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



打印列类型
~~~~~~~~~~

.. code:: python

    types = df.columns.to_series().groupby(df.dtypes).groups
    types



.. parsed-literal::

    {dtype('int64'): ['NO', 'FORCE', 'IQ'],
     dtype('O'): [u'\u59d3\u540d', u'\u7269\u54c1']}



.. code:: python

    # 打印列类型(清晰打印中文)
    types = df.columns.to_series().groupby(df.dtypes).groups
    for key, value in types.items():
        print key,':\t', ','.join(value)

.. parsed-literal::

    object :	姓名,物品
    int64 :	NO,FORCE,IQ


插入列
~~~~~~

.. code:: python

    df = df_sango.copy()
    df.columns = ['no', 'name', 'force', 'iq', 'artifact']
    
    # 方式一：在末尾添加
    df['memo'] = pd.Series('', index=df.index)
    df.head(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>no</th>
          <th>name</th>
          <th>force</th>
          <th>iq</th>
          <th>artifact</th>
          <th>memo</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 100</td>
          <td> 42</td>
          <td>  方天画戟+10武力</td>
          <td> </td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>  99</td>
          <td> 85</td>
          <td> 青龙偃月刀+10武力</td>
          <td> </td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>  99</td>
          <td> 51</td>
          <td>   丈八蛇矛+9武力</td>
          <td> </td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 方式二：在中间插入
    df.insert(loc=2, column='age', value='')
    df.head(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>no</th>
          <th>name</th>
          <th>age</th>
          <th>force</th>
          <th>iq</th>
          <th>artifact</th>
          <th>memo</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> </td>
          <td> 100</td>
          <td> 42</td>
          <td>  方天画戟+10武力</td>
          <td> </td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td> </td>
          <td>  99</td>
          <td> 85</td>
          <td> 青龙偃月刀+10武力</td>
          <td> </td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td> </td>
          <td>  99</td>
          <td> 51</td>
          <td>   丈八蛇矛+9武力</td>
          <td> </td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 根据现有值生成一个新的列
    df.insert(loc = 5 , column='ability', value=df['force'] + df['iq'])
    df.head(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>no</th>
          <th>name</th>
          <th>age</th>
          <th>force</th>
          <th>iq</th>
          <th>ability</th>
          <th>artifact</th>
          <th>memo</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> </td>
          <td> 100</td>
          <td> 42</td>
          <td> 142</td>
          <td>  方天画戟+10武力</td>
          <td> </td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td> </td>
          <td>  99</td>
          <td> 85</td>
          <td> 184</td>
          <td> 青龙偃月刀+10武力</td>
          <td> </td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td> </td>
          <td>  99</td>
          <td> 51</td>
          <td> 150</td>
          <td>   丈八蛇矛+9武力</td>
          <td> </td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 根据现有值生成多个新的列
    # 方法一
    def process_artifact_col(text):
        #根据物品生成物品名称和物品功能两个新的列
        if pd.isnull(text):
            art_name = art_func = np.nan
        else:
            art_name, art_func = text.split('+')
        return pd.Series([art_name, art_func])
    
    df[[u'art_name', u'art_func']] = df.artifact.apply(process_artifact_col)
    df.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>no</th>
          <th>name</th>
          <th>age</th>
          <th>force</th>
          <th>iq</th>
          <th>ability</th>
          <th>artifact</th>
          <th>memo</th>
          <th>art_name</th>
          <th>art_func</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> </td>
          <td> 100</td>
          <td> 42</td>
          <td> 142</td>
          <td>  方天画戟+10武力</td>
          <td> </td>
          <td>  方天画戟</td>
          <td> 10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td> </td>
          <td>  99</td>
          <td> 85</td>
          <td> 184</td>
          <td> 青龙偃月刀+10武力</td>
          <td> </td>
          <td> 青龙偃月刀</td>
          <td> 10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td> </td>
          <td>  99</td>
          <td> 51</td>
          <td> 150</td>
          <td>   丈八蛇矛+9武力</td>
          <td> </td>
          <td>  丈八蛇矛</td>
          <td>  9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 4</td>
          <td> 赵云</td>
          <td> </td>
          <td>  98</td>
          <td> 88</td>
          <td> 186</td>
          <td>        NaN</td>
          <td> </td>
          <td>   NaN</td>
          <td>  NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 5</td>
          <td> 马超</td>
          <td> </td>
          <td>  98</td>
          <td> 48</td>
          <td> 146</td>
          <td>        NaN</td>
          <td> </td>
          <td>   NaN</td>
          <td>  NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 方法二(结果同上，但是没有方法一好)
    for idx, row in df.iterrows():
        art_name, art_func = process_artifact_col(row['artifact'])
        df.ix[idx, 'art_name'], df.ix[idx, 'art_func'] = art_name, art_func
    df.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>no</th>
          <th>name</th>
          <th>age</th>
          <th>force</th>
          <th>iq</th>
          <th>ability</th>
          <th>artifact</th>
          <th>memo</th>
          <th>art_name</th>
          <th>art_func</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> </td>
          <td> 100</td>
          <td> 42</td>
          <td> 142</td>
          <td>  方天画戟+10武力</td>
          <td> </td>
          <td>  方天画戟</td>
          <td> 10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td> </td>
          <td>  99</td>
          <td> 85</td>
          <td> 184</td>
          <td> 青龙偃月刀+10武力</td>
          <td> </td>
          <td> 青龙偃月刀</td>
          <td> 10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td> </td>
          <td>  99</td>
          <td> 51</td>
          <td> 150</td>
          <td>   丈八蛇矛+9武力</td>
          <td> </td>
          <td>  丈八蛇矛</td>
          <td>  9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 4</td>
          <td> 赵云</td>
          <td> </td>
          <td>  98</td>
          <td> 88</td>
          <td> 186</td>
          <td>        NaN</td>
          <td> </td>
          <td>   NaN</td>
          <td>  NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 5</td>
          <td> 马超</td>
          <td> </td>
          <td>  98</td>
          <td> 48</td>
          <td> 146</td>
          <td>        NaN</td>
          <td> </td>
          <td>   NaN</td>
          <td>  NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



改变列值
~~~~~~~~

.. code:: python

    #根据一列的值改变另一列
    df['force'] = df['iq'].apply(lambda x: x + 1)
    df.head(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>no</th>
          <th>name</th>
          <th>age</th>
          <th>force</th>
          <th>iq</th>
          <th>ability</th>
          <th>artifact</th>
          <th>memo</th>
          <th>art_name</th>
          <th>art_func</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> </td>
          <td> 43</td>
          <td> 42</td>
          <td> 142</td>
          <td>  方天画戟+10武力</td>
          <td> </td>
          <td>  方天画戟</td>
          <td> 10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td> </td>
          <td> 86</td>
          <td> 85</td>
          <td> 184</td>
          <td> 青龙偃月刀+10武力</td>
          <td> </td>
          <td> 青龙偃月刀</td>
          <td> 10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td> </td>
          <td> 52</td>
          <td> 51</td>
          <td> 150</td>
          <td>   丈八蛇矛+9武力</td>
          <td> </td>
          <td>  丈八蛇矛</td>
          <td>  9武力</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 同时改变多个列的值
    cols = ['force', 'iq']
    df[cols] = df[cols].applymap(lambda x: x-10)
    df.head(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>no</th>
          <th>name</th>
          <th>age</th>
          <th>force</th>
          <th>iq</th>
          <th>ability</th>
          <th>artifact</th>
          <th>memo</th>
          <th>art_name</th>
          <th>art_func</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> </td>
          <td> 33</td>
          <td> 32</td>
          <td> 142</td>
          <td>  方天画戟+10武力</td>
          <td> </td>
          <td>  方天画戟</td>
          <td> 10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td> </td>
          <td> 76</td>
          <td> 75</td>
          <td> 184</td>
          <td> 青龙偃月刀+10武力</td>
          <td> </td>
          <td> 青龙偃月刀</td>
          <td> 10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td> </td>
          <td> 42</td>
          <td> 41</td>
          <td> 150</td>
          <td>   丈八蛇矛+9武力</td>
          <td> </td>
          <td>  丈八蛇矛</td>
          <td>  9武力</td>
        </tr>
      </tbody>
    </table>
    </div>



操作行
------

.. code:: python

    df = df_sango.copy()
    # 添加一个空行
    df = df.append(pd.Series(
                    [np.nan]*len(df.columns), # Fill cells with NaNs
                    index=df.columns),
                    ignore_index=True)
    df.tail(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>253</th>
          <td> 254</td>
          <td>  谯周</td>
          <td> 32</td>
          <td> 69</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>254</th>
          <td> 255</td>
          <td>  于吉</td>
          <td> 30</td>
          <td> 97</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>255</th>
          <td> NaN</td>
          <td> NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td> NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



空值处理（NaN）
---------------

.. code:: python

    df = df_sango.copy()
    # 计数有空值的行
    nans = df.shape[0] - df.dropna().shape[0]
    print(u'一共有 %d 行出现空值' % nans)
    
    # 填充空值为`无`
    df.fillna(value=u'无', inplace=True)
    df.head()

.. parsed-literal::

    一共有 238 行出现空值




.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 100</td>
          <td> 42</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>  99</td>
          <td> 85</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>  99</td>
          <td> 51</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 4</td>
          <td> 赵云</td>
          <td>  98</td>
          <td> 88</td>
          <td>          无</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 5</td>
          <td> 马超</td>
          <td>  98</td>
          <td> 48</td>
          <td>          无</td>
        </tr>
      </tbody>
    </table>
    </div>



排序
----

.. code:: python

    df = df_sango.copy()
    # 添加一个空行
    df = df.append(pd.Series(
                    [np.nan]*len(df.columns), # Fill cells with NaNs
                    index=df.columns),
                    ignore_index=True)
    # 根据某一列排序（由高到低）
    df.sort(u'智力', ascending=False, inplace=True)
    df.head(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>163</th>
          <td> 164</td>
          <td> 诸葛亮</td>
          <td> 68</td>
          <td> 100</td>
          <td> 兵书二十四篇+9智力</td>
        </tr>
        <tr>
          <th>131</th>
          <td> 132</td>
          <td> 司马懿</td>
          <td> 73</td>
          <td>  99</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>169</th>
          <td> 170</td>
          <td>  庞统</td>
          <td> 66</td>
          <td>  98</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 排序后重新编制索引
    df.index = range(1,len(df.index)+1)
    df.head(3)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>1</th>
          <td> 164</td>
          <td> 诸葛亮</td>
          <td> 68</td>
          <td> 100</td>
          <td> 兵书二十四篇+9智力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 132</td>
          <td> 司马懿</td>
          <td> 73</td>
          <td>  99</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 170</td>
          <td>  庞统</td>
          <td> 66</td>
          <td>  98</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



过滤
----

.. code:: python

    df = df_sango.copy()
    # 根据列类型过滤
    # 只选择字符串型的列
    df.loc[:, (df.dtypes == np.dtype('O')).values].head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>武将</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 吕布</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 关羽</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 张飞</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 赵云</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 马超</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 选择 artifact 为空值的行
    df[df[u'物品'].isnull()].head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>3</th>
          <td> 4</td>
          <td> 赵云</td>
          <td> 98</td>
          <td> 88</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 5</td>
          <td> 马超</td>
          <td> 98</td>
          <td> 48</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>6</th>
          <td> 7</td>
          <td> 许褚</td>
          <td> 98</td>
          <td> 40</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>7</th>
          <td> 8</td>
          <td> 黄忠</td>
          <td> 97</td>
          <td> 66</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>8</th>
          <td> 9</td>
          <td> 庞德</td>
          <td> 97</td>
          <td> 70</td>
          <td> NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 选择`物品`为非空值的行
    df[df[u'物品'].notnull()].head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0 </th>
          <td>  1</td>
          <td> 吕布</td>
          <td> 100</td>
          <td> 42</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1 </th>
          <td>  2</td>
          <td> 关羽</td>
          <td>  99</td>
          <td> 85</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2 </th>
          <td>  3</td>
          <td> 张飞</td>
          <td>  99</td>
          <td> 51</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>5 </th>
          <td>  6</td>
          <td> 典韦</td>
          <td>  98</td>
          <td> 45</td>
          <td>    双铁戟+5武力</td>
        </tr>
        <tr>
          <th>16</th>
          <td> 17</td>
          <td> 孙坚</td>
          <td>  94</td>
          <td> 85</td>
          <td>    古锭刀+7武力</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 根据条件过滤
    df[ (df[u'武力'] >99) | (df[u'智力'] >= 99) ]



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0  </th>
          <td>   1</td>
          <td>  吕布</td>
          <td> 100</td>
          <td>  42</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>131</th>
          <td> 132</td>
          <td> 司马懿</td>
          <td>  73</td>
          <td>  99</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>163</th>
          <td> 164</td>
          <td> 诸葛亮</td>
          <td>  68</td>
          <td> 100</td>
          <td> 兵书二十四篇+9智力</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    df[ (df[u'武力'] >87) & (df[u'智力'] >= 87) ]



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>3 </th>
          <td>  4</td>
          <td> 赵云</td>
          <td> 98</td>
          <td> 88</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>15</th>
          <td> 16</td>
          <td> 张辽</td>
          <td> 95</td>
          <td> 88</td>
          <td> NaN</td>
        </tr>
        <tr>
          <th>19</th>
          <td> 20</td>
          <td> 姜维</td>
          <td> 93</td>
          <td> 96</td>
          <td> NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



切片
----

合并
----

统计：计数，平均，最大，最小，方差，标准差
------------------------------------------

同比，环比
----------

图形化
------


使用另一个 DataFrame 来更新数据
-------------------------------

.. code:: python

    df_1 = df_sango.copy()
    df_2 = df_sango.copy()
    df_2[u'智力'] = df_2[u'智力'].apply(lambda x: x + 10)
    df_1.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 100</td>
          <td> 42</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>  99</td>
          <td> 85</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>  99</td>
          <td> 51</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 4</td>
          <td> 赵云</td>
          <td>  98</td>
          <td> 88</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 5</td>
          <td> 马超</td>
          <td>  98</td>
          <td> 48</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    df_2.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武将</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 吕布</td>
          <td> 100</td>
          <td> 52</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 关羽</td>
          <td>  99</td>
          <td> 95</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 3</td>
          <td> 张飞</td>
          <td>  99</td>
          <td> 61</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 4</td>
          <td> 赵云</td>
          <td>  98</td>
          <td> 98</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 5</td>
          <td> 马超</td>
          <td>  98</td>
          <td> 58</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    df_1.set_index(u'武将', inplace=True)
    df_2.set_index(u'武将', inplace=True)
    df_1.update(other=df_2[u'智力'], overwrite=True)
    df_1.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
        <tr>
          <th>武将</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>吕布</th>
          <td> 1</td>
          <td> 100</td>
          <td> 52</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>关羽</th>
          <td> 2</td>
          <td>  99</td>
          <td> 95</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>张飞</th>
          <td> 3</td>
          <td>  99</td>
          <td> 61</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>赵云</th>
          <td> 4</td>
          <td>  98</td>
          <td> 98</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>马超</th>
          <td> 5</td>
          <td>  98</td>
          <td> 58</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    df_2.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>序号</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
        <tr>
          <th>武将</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>吕布</th>
          <td> 1</td>
          <td> 100</td>
          <td> 52</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>关羽</th>
          <td> 2</td>
          <td>  99</td>
          <td> 95</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>张飞</th>
          <td> 3</td>
          <td>  99</td>
          <td> 61</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>赵云</th>
          <td> 4</td>
          <td>  98</td>
          <td> 98</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>马超</th>
          <td> 5</td>
          <td>  98</td>
          <td> 58</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # 重置 index
    df_1.reset_index(inplace=True)
    df_1.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>武将</th>
          <th>序号</th>
          <th>武力</th>
          <th>智力</th>
          <th>物品</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 吕布</td>
          <td> 1</td>
          <td> 100</td>
          <td> 52</td>
          <td>  方天画戟+10武力</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 关羽</td>
          <td> 2</td>
          <td>  99</td>
          <td> 95</td>
          <td> 青龙偃月刀+10武力</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 张飞</td>
          <td> 3</td>
          <td>  99</td>
          <td> 61</td>
          <td>   丈八蛇矛+9武力</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 赵云</td>
          <td> 4</td>
          <td>  98</td>
          <td> 98</td>
          <td>        NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 马超</td>
          <td> 5</td>
          <td>  98</td>
          <td> 58</td>
          <td>        NaN</td>
        </tr>
      </tbody>
    </table>
    </div>


