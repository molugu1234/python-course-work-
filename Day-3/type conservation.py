Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
float(a)
10.0
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
complex(a)
(10+0j)
>>> str(a)
'10'
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> a=3.45
>>> float(a)
3.45
>>> complex(a)
(3.45+0j)
>>> str(a)
'3.45'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(a)
TypeError: 'float' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(a)
TypeError: 'float' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(a)
TypeError: 'float' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(a)
TypeError: 'float' object is not iterable
>>> bool(a)
True
>>> bool(0)
False
