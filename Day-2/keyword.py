Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import keyword
>>> print(keyword.kwlist)# list of all keywords
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a=7
>>> b=14
>>> c=21
>>> a
7
>>> b
14
>>> c
21
>>> a=b=c=7
>>> a
7
>>> b
7
>>> c
7
>>> a,b,c=7,14,21
>>> a
7
>>> b
14
>>> c
21
>>> a,b=b,a
>>> a
14
>>> b
7
>>> b
7
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a
NameError: name 'a' is not defined
