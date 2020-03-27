

#Data Types in Python

a = 10

type(a)

b = 2.3
type(b)

c = True
type(c)

d = "Forsk"
type(d)

e = 'Forsk'
type(e)

f = 'F'
type(f)

g = "F"
type(g)

h = None
type(h)

"""
int
float
str
bool
None - null

"""

a = 0


name = input("Enter the name: ")

print (name)

type(name)


age = input("Enter the age: ")


type(age)

age = int(age)







#include <math.h>

import math

math.sqrt(16)

dir(math)
help(math.pow)


import math

math.pow(2, 8)


from math import sqrt
sqrt(16)


import math as mt
mt.sqrt(16)


from math import sqrt as st
st(10)

sq = math.sqrt(17)

print (sq)


num = input("Enter the number: ")

type(num)

num = float(num)

import math

print (math.sqrt(num))

raw_input - str
input - int

input() - str
type casting


































































# this is single comment
"""
this is multi line
comment.
"""


# Integer
my_var = 8
type(my_var)
id(my_var)

# Float
my_var = 26.5
type(my_var)
id(my_var)

# String
my_var = "FORSK"
type(my_var)
id(my_var)
  
# Boolean
my_var = True
type(my_var)
id(my_var)
  
# NoneType
my_var = None
type(my_var)
id(my_var)





'''Taking Integer Input from user'''
age = input ( "Enter your Age > ")
print (age)
print (type(age))
  
age = int(age)
print (age)
print (type(age))


# Best Practice 
age = int(input ( "Enter your Age > "))
print (age)
print (type(age))


'''Taking Floating Point Input from user''' 
temperature  = input ( "Enter your temperature of your city > ")
print (temperature)
print (type(temperature))

  
temperature = float(temperature)
print (temperature)
print (type(temperature))




# Best Practice 
temperature  = float(input ( "Enter your temperature of your city > "))
print (temperature)
print (type(temperature))


'''Taking String Input from user using input function '''
name = input ( "Enter your Name >")
print (name)
print (type(name))




'''Importing Modules'''
 
import math



math.sqrt (16)
math.log (16,2)  
math.cos (0)
math.isnan(90)


'''How to use package Aliasing in python''' 
import math as MT
 
MT.sqrt (16)
MT.log (16,2)  
MT.cos (0)


'''How to use specific functions from packages or modules in python '''
from math import sqrt
sqrt (16)


'''How to use specific functions from packages or modules and also aliasing'''
from math import sqrt as square 
square (16)


'''How to find the function within the Module/Package'''
dir ( math )

'''How to find the help for a function of a module/package'''
help (math.sqrt)



str1 = "Jaipur India"
type(str1)

#check the length of string
#strlen
print (len(str1))

print (str1[0])

print (str1[1])

print (str1[0:10])

print (str1[0:5])

print (str1[-1])

print (str1[-2])


str1 = "Jaipur India"
print (str1[0:10:2])

print (str1[0:10:1])
print (str1[0:10])

#slicing in Python

print (str1[:])

print (str1[4:])

print (str1[:10])

print (str1[::2])
print (str1[::-1]) #reverse order printing


str1 = "Jaipur India"

str1[0] = 'j'

#strings in Python are read ONLY
#Immutable

str1 = "Jaipur India"

print (str1.lower())

print (str1.upper())

str2 = str1.upper()

print (str2)


str1.index("pur")



str1 = "Jaipur India"
str1.count('a')


str1 =  "Jaipur India"
str1.index("Jp")

del str1

print (str1)

str1 = "Jaipur India"

del str1[0]


str1 = "   Forsk Coding School   "
print (str1)
print (len(str1))

str2 = str1.strip()
print (len(str2))


str1 = "Forsk Coding School Jaipur"

list1 = str1.split()

str1 = "Jaipur Rajasthan"
list1 = str1.split()

list1 = ["Forsk","Jaipur"]

print (len(list1))

" ".join(list1)


"#".join(list1)

str2 = " ".join(list1)

str1 = "jaipur India"
str1.replace('j','J')

"""
# Clean the Messy salary into integers for Data Processing
salary = '$876,001' 

Hint:
    Remove the $
    Remove the ,
    Convert into integer
"""

str1 = "Jaipur Kota Bundi"
str1.split()

list1 = str1.split("K")
type(list1)

list(str1)

del str1[0]


str2 = str1[1:]







str1 = "Jaipur India"

index = str1.index("p")

str1[index:].split()


list1 = ['Delhi', 'India']
"Delhi India"

" ".join(list1)


a = 2.3
print (type(a))


str1 = "Jaipur"

list1 = list(str1)


str1 = "1000 5000"

list1 = str1.split()

int1 = int(list1[0])

int2 = int(list1[1])


print ("RJ"+" "+str(14))

print ("RJ", 14)




str1 = "jaipur india"


str1.upper()


list1 = ['Jaipur', 'Jodhpur']

" ".join(list1)



str1 = "Jaipur"

index = str1.index("p")

print (str1[:index]+ str1[index+1:])




