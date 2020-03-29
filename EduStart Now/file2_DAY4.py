Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[1,2,3,4,5]
>>> a[2]=a[3]
>>> a
[1, 2, 4, 4, 5]
>>> a=[1,2,3,4,5]
>>> a.append(10)
>>> a
[1, 2, 3, 4, 5, 10]
>>> a.insert(5,100)
>>> a
[1, 2, 3, 4, 5, 100, 10]
>>> b=[6,7,8]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 100, 10, 6, 7, 8]
>>> b.extend(a)
>>> b
[6, 7, 8, 1, 2, 3, 4, 5, 100, 10, 6, 7, 8]
>>> a
[1, 2, 3, 4, 5, 100, 10, 6, 7, 8]
>>> a=[1,2,3,4,5,3,4,5,6,7,7]
>>> a.count(5)
2
>>> len(a)
11
>>> a.index(5)
4
>>> type(a)
<class 'list'>
>>> a="nikhil"
>>> b=list(a)
>>> b
['n', 'i', 'k', 'h', 'i', 'l']
>>> del a[2]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    del a[2]
TypeError: 'str' object doesn't support item deletion
>>> b
['n', 'i', 'k', 'h', 'i', 'l']
>>> del b[2]
>>> b
['n', 'i', 'h', 'i', 'l']
>>> b.remove("h")
>>> b
['n', 'i', 'i', 'l']
>>> b.pop()
'l'
>>> b.pop(0)
'n'
>>> b
['i', 'i']
>>> a=[1,2,6,4,3,9,7]
>>> a.sort()
>>> a
[1, 2, 3, 4, 6, 7, 9]
>>> a=[1,2,6,4,3,9,7]
>>> b=sorted(a)
>>> b
[1, 2, 3, 4, 6, 7, 9]
>>> a
[1, 2, 6, 4, 3, 9, 7]
>>> 
