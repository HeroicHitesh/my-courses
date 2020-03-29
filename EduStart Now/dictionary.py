Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a={1:1,2:2}
>>> a[3]="nikhil"
>>> a
{1: 1, 2: 2, 3: 'nikhil'}
>>> a["nikhil"]="hari"
>>> a
{'nikhil': 'hari', 1: 1, 2: 2, 3: 'nikhil'}
>>> del a["nikhil"]
>>> a
{1: 1, 2: 2, 3: 'nikhil'}
>>> type(a)
<type 'dict'>
>>> a1=a.copy()
>>> a1
{1: 1, 2: 2, 3: 'nikhil'}
>>> a.keys()
[1, 2, 3]
>>> a.values()
[1, 2, 'nikhil']
>>> a.items()
[(1, 1), (2, 2), (3, 'nikhil')]
>>> 
