
url parse note
==============

.. code:: python

    from urllib.parse import urlparse, urljoin
    url = 'http://www.dapenti.com/blog/more.asp?name=xilei&id=116635'

.. code:: python

    urlparse(url)




.. parsed-literal::

    ParseResult(scheme='http', netloc='www.dapenti.com', path='/blog/more.asp', params='', query='name=xilei&id=116635', fragment='')



.. code:: python

    urlparse('ggg.gif')




.. parsed-literal::

    ParseResult(scheme='', netloc='', path='ggg.gif', params='', query='', fragment='')



.. code:: python

    urljoin(url, 'ggg.gif')




.. parsed-literal::

    'http://www.dapenti.com/blog/ggg.gif'



