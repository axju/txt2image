=========
txt2image
=========

.. image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
  :alt: Gitter
  :target: https://gitter.im/axju/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link

Make it easy to add text to an image.


Install
-------
::

  pip install txt2image


Examples
--------
Take a look in the example folder. The first example only shows the different
tools you can use to create your own images. For the second example you need the
package requests.::

  pip install requests

The third example shows the QuoteImage-class.

Development
-----------
Clone repo::

  git clone https://github.com/axju/txt2image.git

Create virtual environment and update dev-tools::

  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade wheel pip setuptools twine tox

Install local::

  pip install -e .

Run some tests::

  tox
  python setup.py test

Publish the packages::

  python setup.py sdist bdist_wheel
  twine upload dist/*
