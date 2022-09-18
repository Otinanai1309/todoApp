Lets get started
================

Preparation
-----------

Within our project folder we create a virtual environment (with the version of python we want to use).

.. code-block:: console
  :emphasize-lines: 1

  $ virtualenv --python=c:\Python310\python.exe envname

and activate the virtual environment.

.. code-block:: console
  :emphasize-lines: 1

  $ .\envname\scripts\activate


After that Sphinx Installation

.. code-block:: console
    :emphasize-lines: 1

    $ pip install sphinx
    $ mkdir docs
    $ cd docs
    $ sphinx-quickstart
    (install sphinx_rtd_theme)
    $ pip install sphinx_rtd_theme
    (install sphinxcontrib-httpdomain)
    $ pip install sphinxcontrib-httpdomain
    (install sphinx-copybutton)
    $ pip install sphinx-copybutton
    (Install sphinx-toolbox. More infos on https://sphinx-toolbox.readthedocs.io/en/latest/)
    $ pip install sphinx-toolbox

We make the changes to conf.py and index.rst files in order to start writing our documentation.

Install Django 3.2.13 LTS version

.. code-block:: console
  :emphasize-lines: 2

  $ cd ..
  $ pip install Django==3.2.13

Create the django project

.. code-block:: console
  :emphasize-lines: 1

  $ django-admin startproject backend .


Create the git repository

.. code-block:: console
  :emphasize-lines: 1

  echo "# todoApp" >> README.md
  git init
  git add README.md
  git commit -m "first commit"
  git branch -M main
  git remote add origin https://github.com/Otinanai1309/todoApp.git
  git push -u origin main


