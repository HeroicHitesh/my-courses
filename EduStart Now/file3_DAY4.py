Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(1,2,3,4,"nikhil")
>>> a[2]=5
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[2]=5
TypeError: 'tuple' object does not support item assignment
>>> a
(1, 2, 3, 4, 'nikhil')
>>> a[0]
1
>>> a[1]
2
>>> a[1:4]
(2, 3, 4)
>>> a[-1]
'nikhil'
>>> a[ : :-1]
('nikhil', 4, 3, 2, 1)
>>> a.index(3)
2
>>> a.index("nikhil")
4
>>> a.count(1)
1
>>> 
