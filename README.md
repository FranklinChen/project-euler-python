# Python solutions to [Project Euler](http://projecteuler.net/) problems

This also serves as an example of how to set up a Python package using [`distribute`](http://pythonhosted.org/distribute/).

I used this [helpful Python packaging tutorial](http://www.scotttorborg.com/python-packaging/) as a guide, and also I made use of this [guide to repository structure](http://kennethreitz.org/exposures/repository-structure-and-python) in order to separate the tests from the main package.

## To run tests

I recommend using [`nose`](http://nose.readthedocs.org/en/latest/) for testing.

```
$ python setup.py nosetests
```

## To install the package `project_euler`

```
$ python setup.py install
```

## To run an answer

Answer scripts are installed where `distribute` installs them (for me it is `/usr/local/share/python`). If you have the script directory in your `PATH`, you should be able to run

```
$ project_euler_answer1
```
