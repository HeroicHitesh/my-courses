Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20.2
>>> c=int(b)
>>> c
20
>>> d=float(a)
>>> d
10.0
>>> type(d)
<class 'float'>
>>> a=2+3J
>>> e=complex(a)
>>> e
(2+3j)
>>> f=int(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    f=int(a)
TypeError: can't convert complex to int
>>> a=10
>>> b=complex(a)
>>> b
(10+0j)
>>> 
