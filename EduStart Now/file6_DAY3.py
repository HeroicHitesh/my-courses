Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="nikhil"
>>> a.upper()
'NIKHIL'
>>> a.lower()
'nikhil'
>>> a.isupper()
False
>>> a.islower()
True
>>> a.capitalize()
'Nikhil'
>>> a=" nikhil"
>>> a.capitalize()
' nikhil'
>>> a="nikhil"
>>> len(a)
6
>>> a.index("i")
1
>>> a.isalpha()
True
>>> a.isdigit()
False
>>> a="1236"
>>> a.isdigit()
True
>>> a.isalnum()
True
>>> a="##$"
>>> a.isalnum()
False
>>> a="nikhil"
>>> a[2]="h"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a[2]="h"
TypeError: 'str' object does not support item assignment
>>> a.replace("k","h")
'nihhil'
>>> a="hellohellohello"
>>> a.replace("l","h",5)
'hehhohehhohehlo'
>>> a.split("l")
['he', '', 'ohe', '', 'ohe', '', 'o']
>>> "#".join(a)
'h#e#l#l#o#h#e#l#l#o#h#e#l#l#o'
>>> a
'hellohellohello'
>>> a.count("l")
6
>>> a.find("l")
2
>>> a.find("l",5,7)
-1
>>> a.find("l",5,10)
7
>>> 
