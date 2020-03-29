Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={1,2,3,"nikhil",(1,2)}
>>> 
>>> s
{(1, 2), 1, 2, 3, 'nikhil'}
>>> s={1,2,3,8,6}
>>> s
{1, 2, 3, 6, 8}
>>> s={1,2,[1,2]}
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s={1,2,[1,2]}
TypeError: unhashable type: 'list'
>>> s={1,2,3,4,2,3,4,5,6}
>>> s
{1, 2, 3, 4, 5, 6}
>>> s={}
>>> type(s)
<class 'dict'>
>>> s=set()
>>> type(s)
<class 'set'>
>>> s={1,2,3,4,5}
>>> s.add(10)
>>> s
{1, 2, 3, 4, 5, 10}
>>> s.add(6)
>>> s
{1, 2, 3, 4, 5, 6, 10}
>>> s.update([7,8,9])
>>> s
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> s.remove(5)
>>> s
{1, 2, 3, 4, 6, 7, 8, 9, 10}
>>> s.discard(7)
>>> s
{1, 2, 3, 4, 6, 8, 9, 10}
>>> s={1,2,4}
>>> s.remove(2)
>>> s.remove(100)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.remove(100)
KeyError: 100
>>> s.discard(4)
>>> s
{1}
>>> s.discard(100)
>>> s
{1}
>>> s={1,2,4,5,7,8}
>>> s.pop()
1
>>> a={1,2,3}
>>> b={3,4,5}
>>> a.union(b)
{1, 2, 3, 4, 5}
>>> a.intersection(b)
{3}
>>> a.difference(b)
{1, 2}
>>> a.symmetric_difference(b)
{1, 2, 4, 5}
>>> 
