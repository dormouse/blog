===========
django note
===========

运行程序::

    python manage.py runserver
 
初始化 model::

    python manage.py makemigrations polls
    python manage.py sqlmigrate polls 0001
    python manage.py migrate
    python manage.py createsuperuser

model 修改三步走

#. 在 models.py 中修改 model

#. 运行 python manage.py makemigrations 来创建 migrations

#. 运行 python manage.py migrate 实施数据库变动

查询示例::

    from legosets.models import LegoSet, Vendor, Discount
    a = LegoSet.objects.filter(number__contains='88')


ORM 用字典作为参数，保存数据
============================

创建新的实例
------------

原来是这样的::

    mymodel = MyModel(title=data_dict['title'],body=data_dict['body'])
    mymodel.save()

现在可以是这样的::

    mymodel = MyModel(**data_dict)
    mymodel.save()

    # OR

    MyModel.objects.create(**data_dict)

.. attention::
   字典数据里面的 key 一定要与 model field 对应，否则就会报错。

如果还有一些其他的扩展字段，也是可以加在里面的，但 `**data_dict` 必须放在
最后::

    mymodel  =MyModel(extra='hello', extra2='world', **data_dict)
    mymodel .save()


更新数据
--------

::

    mymodel=MyModel.objects.get(pk=pk)
    mymodel.__dict__.update(data_dict )
    mymodel.save()

    # OR

    MyModel.objects.filter(pk=pk).update(**data_dict )
