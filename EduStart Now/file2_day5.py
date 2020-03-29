Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={1:"nikhil",2:"raju"}
>>> d
{1: 'nikhil', 2: 'raju'}
>>> d={"nikhil":1,"raju":2}
>>> d
{'nikhil': 1, 'raju': 2}
>>> a={1:1,3:3,2:2}
>>> a
{1: 1, 3: 3, 2: 2}
>>> a[4]:4
>>> a
{1: 1, 3: 3, 2: 2}
>>> a[4]=4
>>> a
{1: 1, 3: 3, 2: 2, 4: 4}
>>> a={1:1,2:2,2:5}
>>> a
{1: 1, 2: 5}
>>> a.keys()
dict_keys([1, 2])
>>> a.values()
dict_values([1, 5])
>>> a.items()
dict_items([(1, 1), (2, 5)])
>>> a1=a.copy()
>>> a1
{1: 1, 2: 5}
>>> a
{1: 1, 2: 5}
>>> a[8]=45
>>> a
{1: 1, 2: 5, 8: 45}
>>> type(a)
<class 'dict'>
>>> del a[8]
>>> a
{1: 1, 2: 5}
>>> 
