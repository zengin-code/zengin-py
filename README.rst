==============================
ZenginCode
==============================

|github| |version|

The python implementation of ZenginCode.

ZenginCode is datasets of bank codes and branch codes for japanese.

Installation
==============

.. code-block:: bash

 $ pip install zengin_code

Usage
==============

.. code-block:: python

 from zengin_code import Bank

 Bank.all # => OrderedDict([(u'0001', <zengin_code.bank.Bank object at 0x1044173d0>), ...

Development
==============

Testing
---------------

.. code-block:: bash

 $ pip install tox
 $ tox

Contributing
===============

Bug reports and pull requests are welcome on GitHub at https://github.com/zengin-code/zengin-py

License
===============

The package is available as open source under the terms of the `MIT License <http://opensource.org/licenses/MIT>`_ .


.. |github| image:: https://github.com/zengin-code/zengin-py/actions/workflows/update.yml/badge.svg
    :target: https://github.com/zengin-code/zengin-py/actions/workflows/update.yml

.. |version| image:: https://img.shields.io/pypi/v/zengin_code.svg
    :target: http://pypi.python.org/pypi/zengin_code/
    :alt: latest version
