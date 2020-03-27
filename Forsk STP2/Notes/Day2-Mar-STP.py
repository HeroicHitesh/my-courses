

#this is single line comment

"""
this is multi line
comment
"""

#scanf

name = input("Enter the name: ")
type(name)

age = input("Enter the age: ")

age = int(age)

age = int(input("Enter the age: "))


str1 = "Forsk Jaipur"

len(str1)

print (str1[1])

str1[0:10]
str1[1:5] #1,2,3,4

str1[-2]

print (str1[0:10:2])

str2 = "Corona Outbreak in China"
str2[0:15:2]

#slicing

str2[-1]

str2[3:]

str2[:10]

str2[0:15:1]
str2[:] #str2
str2[::1]

str2[::-1] #reverse order printing
str2[1:15:1]

str1 = "Forsk Jaipur"
print (str1.upper())
print (str1.lower())


str1[0] = 'f'
#strings are read only in Python
#immutable

str1[0:10].lower()
str1[0:10].upper()


str1 = "Forsk Coding School India"

list1 = str1.split('o')

str1 = "Forsk Jaipur"

list1 = str1.split()

"$".join(list1)




str1 = "Forsk"
str2 = "Jaipur"

print (str1+str2)

print (str1 + " " + str2)

print(str1,str2)




str1 = "Forsk Jaipur"
str1.find('J')
str1.find('pur')
str1.index('pur')
"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string "RESTART", replace all the R with $ 
    except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T

"""

str1 = 'forsk'
str1.replace('f','F')

sys.getsizeof(str1)

a = 10
sys.getsizeof(a)

b = 2.3
sys.getsizeof(b)


for1 = 'forsk'



str1 = "Himalay Rajwani"

list1 = str1.split()

print (list1)
list1[1]

"$".join(list1)



str1 = "RESTART"

str1 = input("Enter the string: ")


str1 = "      Jaipur India      "
str1.strip()



str1 = "RESTART"
str1[0]+str1[1:].replace('R','$')

len(str1)




str1 = "India"
str2 = "Cricket"



str3 = str1+" "+str2











































"""
if
else
elif
"""
#version 1
marks =  int(input("Enter your marks: "))
#type(marks)

if (marks >= 33):
    print ("Pass")
    print ("Congrats!")
else:
    print ("Fail")
    print ("Better luck next time")
    

#version 2
    
marks =  int(input("Enter your marks: "))

if marks >= 60:
    print ("First Division")

if marks < 60 and marks >= 45:
    print ("Second division")
    
if marks < 45 and marks >= 33:
    print ("Third Division")
   
if marks < 33:
    print ("Fail")


#version 3
#version 2
    
marks =  int(input("Enter your marks: "))

if (marks >= 60):
    print ("First Division")
elif marks < 60 and marks >= 45:
    print ("Second division")
elif marks < 45 and marks >= 33:
    print ("Third Division")
else:
    print ("Fail")

#here




bmi = 20

"""
18 - 24 => weight is OK
18 => underweight
24 => Overweight
"""

bmi = float(input("Enter your bmi: "))
if bmi >= 24:
    print ("Overweight")
elif bmi < 24 and bmi > 18:
    print ("Weight is OK")
else:
    print ("Underweight")


"""
# Clean the Messy salary into integers for Data Processing
salary = '$876,001' 

Hint:
    Remove the $
    Remove the ,
    Convert into integer
"""
#version 01
salary = '$876,001'
type(salary)
salary = salary[1:]

list1 = salary.split(",")

salary = "".join(list1)

salary = int(salary)

#version 2
salary = '$876,001'

salary = int("".join(salary[1:].split(",")))



weight = float(input("Enter your weight in kgs: "))

height = float(input("Enter your height in meters: "))

bmi = weight/(height*height)

print (bmi)




distance = 80
avg = 18
price = 80

fuel_consumed = float(distance/avg)

cost = fuel_consumed*price

print (cost)



# Today code challenge
"""
Take the age as input from the user 
and print whether he is a 
infant, Child , 
Adult,  Senior Citizen
0 - 1 is Infant
> 1 and < than 18 is Child 
> 18 and < 60 is Adult
> 60 is Senior Citizen 
"""


str1 = "madam"

if len(str1) > 4:
    print ("long")
elif len(str1) <= 4 and len(str1) >= 2:
    print ("medium")
else:
    print ("short")
    

#check if string is palindrome or not

str1 = "madam"
str1[::-1]

if (str1 == str1[::-1]):
    print ("Palindrome")
else:
    print ("not palindrome")
    

number = "10,000,000"

number = int(number) #this will not work

list1 = number.split(",")

number = "".join(number.split(","))

number = int("".join(number.split(",")))

#number.split(",")


a =  42

import sys

print (sys.getsizeof(a))




age = int(input("Enter your age:" ))
if age > 0 and age <= 4:
    print("infant" )


str1 = "RIET Ajmer Road Jaipur"
list1 = str1.split()

len(list1)






#Looping
"""
Iteration:
Looping:
    Indefinite iteration (while)
    Definite iteration (for each)


"""

number = 0

while (number < 10):
    number = number + 1
    if (number == 5):
        break
    print (number)

print ("Loop ended")

number  = 0

while (number < 10):
    number = number + 1
    if (number == 5):
        continue
    print(number)

while (True):
    marks = input("Enter the marks: ")
    
    if (not marks):
        break
    
    marks = int(marks)
    
    if (marks >= 33):
        print("Pass")
    else:
        print ("Fail")






while (True):
    
    age = input("Enter the age: ")
    
    if (not age):
        break
    
    age = float(age)
    
    if (age > 0 and age <= 1):
        print ("Infant")
    elif (age > 1 and age <= 18):
        print ("Child")
    elif (age > 18 and age <= 60):
        print ("Adult")
    else:
        print ("Senior Citizen")




# For loop

students = ['Ram','Shyam','Sita','Gita']

for a in students:
    print (a)

list(range(10, 15))



for x in range(1,11):
    print (x)

for x in range(1,11):
    if x == 5:
        break
    print(x)
    
for x in range(1,11):
    if x == 5:
        continue
    print(x)
    

list(range(1,20))


str1 = "Forsk Coding School"

for char in str1:
    print (char)


 
list(range(10))
  

"""
can u give example of 'for loop' 
for making Patterns ****
"""

list1 = [10,20,30]

for item in list1:
    print (item**2)


sir we can use && operator wher 
and is written in if-else

and or




list(range(1,10,2))

list(range(10,0,-1))






list1= ['Ram','Shyam','Sita','Gita']

for name in list1:
    if name == 'Shyam':
        print ("Rama")
        continue
    print (name)

ord('a')









