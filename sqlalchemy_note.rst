
sqlalchemy note
===============

.. code:: python

    import sqlalchemy
    sqlalchemy.__version__




.. parsed-literal::

    '1.1.4'



.. code:: python

    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:', echo=True)
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()
    from sqlalchemy import Column, Integer, String
    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)
        password = Column(String)
    
        def __repr__(self):
            return "<User(name='%s', fullname='%s', password='%s')>" % (
                self.name, self.fullname, self.password)

.. code:: python

    User.__table__




.. parsed-literal::

    Table('users', MetaData(bind=None), Column('id', Integer(), table=<users>, primary_key=True, nullable=False), Column('name', String(), table=<users>), Column('fullname', String(), table=<users>), Column('password', String(), table=<users>), schema=None)



.. code:: python

    Base.metadata.create_all(engine)


.. parsed-literal::

    2016-12-01 13:16:22,948 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
    2016-12-01 13:16:22,949 INFO sqlalchemy.engine.base.Engine ()
    2016-12-01 13:16:22,950 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
    2016-12-01 13:16:22,951 INFO sqlalchemy.engine.base.Engine ()
    2016-12-01 13:16:22,953 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("users")
    2016-12-01 13:16:22,954 INFO sqlalchemy.engine.base.Engine ()
    2016-12-01 13:16:22,955 INFO sqlalchemy.engine.base.Engine 
    CREATE TABLE users (
    	id INTEGER NOT NULL, 
    	name VARCHAR, 
    	fullname VARCHAR, 
    	password VARCHAR, 
    	PRIMARY KEY (id)
    )
    
    
    2016-12-01 13:16:22,957 INFO sqlalchemy.engine.base.Engine ()
    2016-12-01 13:16:22,958 INFO sqlalchemy.engine.base.Engine COMMIT


