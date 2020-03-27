

list1 = [1,2,3,4]

#tuple

t = (1,2,3,4,5)
type(t)

t[0] =  10
#tuple are read only
# immutavble

len(t)

""
''

tt = (10,20,13)

tt.index(20)

ttt = (1,20,3,20,20)
ttt.count(20)
ttt.count(1)

tttt = (2,)
type(tttt)

t = (2.4, 40, True)


t = (20,10,20,3,23)

t.count(20)



x, x = divmod(23, 5) #unpacking




list1 = [1,2,3,4,5]

for item in list1:
    print (item*item)

list2 = []

for item in list1:
    list2.append(item*item)

#list comrehension
[item*item for item in list1]

list1 = [1,2,3,4,5]

list3 = [item+1 for item in list1]



list1 = [1,2,3,4,5]

def f1(x):
    return (x*x)


f1(list1[0])
f1(list1[1])

list(map(f1, list1))
"""
map:
If you already have a list of 
values and you want to do the 
exact same operation on each 
of the elements in the array 
and return the same amount of 
items in the list, in these type
 of situations it is better to 
 use the map method.
"""


list1 = ['Ram','Shyam','Sita']


def f2(str1):
    return len(str1)

list(map(f2, list1))



list1 = [1,2,4,5,6]


def f3(x):
    return x*x*x

list(map(f3, list1))


list1 = [1,20,3,10,4,12]

def f4(x):
    if x < 10:
        return True
    else:
        return False

list(filter(f4, list1))

list(filter(lambda x: x > 10, list1))


list1 = ['Ram','Shyam']

list(map(lambda str1: len(str1), list1))


[len(item) for item in list1]


"""
If you already have list of 
values but you only want to 
have items in the array that 
match certain criteria, in these 
type of situations it is better to 
use the filter method.
"""

list1 = [1,2,3,4,5,6,7,8,9,10]

def f5(x, y):
    return x+y

#reduce
import functools
functools.reduce(f5, list1)

functools.reduce(lambda x, y: x+y, list1)



"""
If you already have list of values, 
but you want to use the values 
in that list to create something 
completely new, in these type of 
situations it is 
better to use the reduce method.
"""

map-reduce

#hadoop - map reduce
#Spark - map reduce
#Databrick

#sanjay ghemawat

functional programming
#recursion - Haskel
map, filter, reduce

erlang - erricson




str1 = "abcd"

list(map(lambda x: x*3, str1))


print ("Forsk"*2)


str1 = "aBcDefg"

list(filter(lambda x: x > 'D', str1))


import functools

functools.reduce(lambda x, y: x+y, [1,2,3,4,5])


str1 = "Forsk"

str2 = ""

for letter in str1:
    if letter not in "aieouAIEOU":
        str2 = str2 + letter





t= (1,2,3,4,5)

t.index(3)

tt = (1,2,1,1,2)

tt.count(2)

ttt = (1,)

type(ttt)




list1 = [1,2,3,4,5,6]

for item in list1:
    print (item*item)

list2 = []

for item in list1:
    list2.append(item*item)

[item*item for item in list1]



list1 = ['Ram','Raju','Ramu']

for item in list1:
    print (len(item))

def f1(str1):
    return len(str1)

list(map(f1, list1))
list(map(len, list1))
list(map(lambda x: len(x), list1))


list1 = [1,10,30,3,20]

def f2(x):
    if x > 10:
        return True
    else:
        return False
    
list(filter(f2, list1))


list2 = ['Jodhpur','Jaipur','Chennai','Dhaka','Lahore']

def f3(str1):
    return 'pur' in str1

list(filter(f3, list2))

list(filter(lambda str1: 'pur' in str1, list2))

list(filter(lambda str1: 'pur' not in str1, list2))


list1 = [1,2,3,4,5,6,7,8,9,10]

import functools

def f4(x, y):
    return x+y*2

functools.reduce(f4, "1234")

#map example

def f1(str1):
    return len(str1)

list1 = ['Ram','Shyam','Sita','Gita']

list(map(f1, list1))


list1 = [10,20,30,50,70]

def f2(x):
    return x > 20

list(map(f2, list1))



#filter example

def f3(x):
    return x % 2 == 0

list1 = [1,2,3,4,5,6,7,8,9,10]

list(filter(f3,  list1))



#filter example
def f4(str1):
    return 'pur' in str1
        
list1 = ['Jodhpur','Jaipur','Bikaner','Kota']

list(filter(f4, list1))

#lambda example
list(filter(lambda str1: 'pur' in str1, list1))


#reduce example
import functools

def f5(x,y):
    return (x+y)

list1 = [1,2,3,4,5,6,7,8,9,10]

functools.reduce(f5, list1)

#lambda usage
functools.reduce(lambda x,y: x+y, list1)

#map reduce usage
#sanjay Ghemawat - Google
#Show the browser
#Hadoop, Spark, Databricks
