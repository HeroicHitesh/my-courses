
#set

[] - list
() - tuple

s1  = {1,2,3,4,5}

s2 = {3,4,5,6,7}

s1.intersection(s2)

list1 = [1,2,4,4,3,2,10]
set(list1)

str1 = "aaabbbcccddd"
set(str1)


s1  = {1,2,3,4,5}

s2 = {3,4,5,6,7}

s1.union(s2)
s1.intersection(s2)
s1.difference(s2)
s2.difference(s1)

s1.add(8)
s1.remove(8)

s1[0]

a1 = ['Ram','Shyam','Sita']

a2 = ['Ram','Gita']

set(a1).intersection(set(a2))


for item in set(a1):
    print (item)


s1 = {1,True, 2.3, 'Ram'}

s2 = {1, 2.3}


s1.intersection(s2)


#dictionary

countryNames = ['India', 'Pakistan','Japan','England']

capitalNames = ['Delhi','Islamabad','Tokyo','London']


capitalNames[2]

list(zip(countryNames, capitalNames))


dict1 = {'India':"Delhi", 
         'Pakistan':'Islamabad',
         'Japan':'Tokyo',
         'England':'London'}

dict1['India']

dict1['Japan']

dict2 = {
        "DSA" : {"MT1":200, "MT2" : 18},
        "DMS" : 30,
        "OS" : 14,
        20 : "Aman"
        }

dict2["DSA"]["MT1"]


dict2["OS"] = 18


dict1.keys()

dict1.values()

dict1.items()


dict3  = {}
s1 = set()



#file handling


fp = open("words.txt", "r")

print (fp.read())

fp.close()

fp = open("words.txt", "r")

str1 = fp.read()

fp.close()

fp = open("words.txt", "r")
fp.readline()

fp.readline()

fp.readline()

fp.close()

fp = open("words.txt", "r")
fp.readlines()[2]

fp = open("words.txt", "r")
fp.read()

fp.read()

fp.read()



fp  = open("new.py", "w")

fp.write("\n#this is single line comment")

fp.close()


read
write
append





















































s1 = {1,2,3,4,5}

s2 = {3,4,5,6,7}


s1.union(s2)
s1.intersection(s2)
s1.difference(s2)

s1.add(8)
s1.remove(8)



countryNames = ['India','Pakistan','Japan','England']

capitalNames = ['Delhi','Islamabad','Tokyo','London']


list(zip(countryNames, capitalNames))


dict1 = {'India':'Delhi', 'Pakistan':'Islamabad',
         'Japan':'Tokyo','England':'London'}



dict1['India']

dict1['Japan']

dict1.keys()

dict1.values()

dict1.items()


dict1['India'] = 'New Delhi'

del dict1['India']


list1 = [10,20,10,20,3,5,6,20]


dict2 = {}

for item in list1:
    if item not in dict2:
        dict2[item] =  1
    else:
        dict2[item] = dict2[item] + 1
        


#file handling
fp = open('words.txt','r')
print (fp.read())

fp.close()


fp = open('words.txt','r')
fp.readline()
fp.readline()
fp.readline()

fp.close()

fp = open('words.txt','r')


fp.readlines()

fp.close()

fp =  open("new.txt",'w')

fp.writelines(["Forsk Coding School,Jaipur"])
fp.close()



"""
Dictionary Examples

Dictionaries and lists share the 
following characteristics:

Both are mutable.
Both are dynamic. T
hey can grow and shrink as needed.
Both can be nested. 
A list can contain another list. 
A dictionary can contain another dictionary. 
A dictionary can also contain a list, and vice versa.
Dictionaries differ from lists primarily in 
how elements are accessed:

List elements are accessed by their 
position in the list, via indexing.
Dictionary elements are accessed via keys.
"""

capitals = ['Jaipur','Ahemdabad','Mumbai','Bhopal']
#to access the particular capital, you need the index
states = ['Rajasthan','Gujarat','Maharashtra', 'Madhya Pradesh']

list(zip(states, capitals))

#there is easieay way, where we access using 'keys'

capitals = {'Rajasthan' : 'Jaipur',
            'Gujarat' : "Ahemdabad",
            'Maharashtra' : 'Bombday',
            'Madhya Pradesh' : 'Bhopal'
            }

#we can add more
capitals['Haryana'] = 'Chandigargh'
capitals['Punjab'] = 'Chandigargh'

#we can remove also
del capitals['Gujarat']

#we only need keys

capitals.keys()

#we only need values
capitals.values()

#we need both
capitals.items()

#looping
for key in capitals.keys():
    print (key)
    
for values in capitals.values():
    print (values)
    
for key, values in capitals.items():
    print (key, values)


#lets take one example
list1 = ['one','one','two','three','one','two']

dict1 = {}

for item in list1:
    if item not in dict1:
        dict1[item] = 1
    else:
        dict1[item] = dict1[item] + 1
        
print (dict1)




"""
Sets is like a list without duplicate values
 
unordered collection of unique items
no duplicate data
No indexing and No Slicing applicable

Good way to remove duplicate values from a list 
"""

'''Creating empty set'''
empty_set = set()
print(empty_set)
print(type(empty_set))

empty_set = {} #will create an empty dictionary 
print(type(empty_set))


a = { 1,2,2,3,3,4,5 }
print(type (a) ) 
print (a)   
# will print set ( {1 2 3 4 5 } )
# It removes the duplicate values from the list 

 
a  = set("abcdef")
print (a)

a = {'a','b','c','d','e','f'}   # not a dictionary
print (a)




'''Set Operations''' 
# ( add, clear, copy, difference, discard, remove, union, intersection)
# ( isdisjoint, issubset, issuperset, pop )
s1 = {1,2,3,4,5}
print (s1)

s1.add(6)   # add() function can be used to add element to a set
print (s1)

s1.update ([6,7,8])
print (s1) 
 
s2 = {7,8,9}
s1.update([6,7,8],s2)
print (s1)
 
s1.remove(5) # if it doesnt exits it will give Keyerror
print(s1)

s1.discard(5) # this won’t throw key error  
print(s1)

s1.remove(5) # if it doesnt exits it will give Keyerror
print(s1)


"""
It is similar to Mathematical sets.
  Union 
  Difference
  Intersection 
"""

s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}
# They have some unique values
# They have overlapping values 


'''Question: get a set of values which are in all in these sets''' 
# Using Intersection method of Set we can find this
 
s4 = s1.intersection(s2) 
print (s4) # which are common in s2 and s1 {2,3}
s5 = s4.intersection(s3)
print (s5)

# Short Cut
s4 = s1.intersection(s2,s3) 
print (s4) # which are common in s3, s2 and s1 {3}

#s1 & s2 for intersection

'''Question: get a set of values which are different in all these sets''' 
# Using Difference  method of Set we can find this

#s1 - s2 for difference

s4 = s1.difference(s2) 
print (s4) # which is present in s1 but not present in s2 {1}


s4 = s2.difference(s1) 
print (s4) # which is present in s2 but not present in s1 {4}
 

s4 = s3.difference(s1,s2) 
print (s4) # which is present in s3 but not present in s1or s2 {5}
 

'''Symmetric Difference removes which are common in both'''

s4 = s1.symmetric_difference(s2) 
print (s4) #   differences from both sets    {1,4} 

s4 = s2.symmetric_difference(s1) 
print (s4) #   differences from both sets    {1,4} 


'''REAL WORLD USAGE OF SETS'''

'''Question: remove duplicate values from a list''' 
l1 = [1,2,3,1,2,3]

# You need to traverse the list one by one and create another empty list and 
# check whether it is present in that or no and add it 
# or a simple solution using sets which is more efficient 

l2 = list ( set ( l1 ) ) 
print (l2)


"""
Enumerate

"""


list1 = ['Ram','Shyam','Sita','Gita']


for item in list1:
    print (item)


index = 0

for item in list1:
    print (index, item)
    index = index + 1


for index, item in enumerate(list1):
    print (index, item)
    
for index, item in enumerate(list1, start = 10):
    print (index, item)
    

#why file handling
str1 = "Forsk"
a = 20
list1 = [1,2,3,4,5]
dict1 = {}

#they all are available stack

#saving the info to database

#file handling - writing data to file
#reading the data from file



"""
int a =  0;  #stack

int * ptr = malloc(100); #heap
ptr #stack
"""
"""
file types: text files, binary files
text file : .txt
binary file: jpeg, png, mp3, 

#Kivi - for Android app dev

"""

#reading the data from text file

file = open("words.txt","r")
str1 = file.read()
str1
print (str1)

file.close()


file = open("words.txt","r")
str1 = file.readline()
print(str1)

str1 = file.readline()
print(str1)

file.close()

file = open("words.txt","r")
file.readlines()



#read,readline, readlines

file = open("new.txt","w")
file.write("Forsk Coding School")
file.close()

#modes: r,w,a

file = open("new.txt",'w')
file.writelines(['Forsk\n','School\n'])
file.close()

file = open("new.txt",'a')
file.write("Jaipur")
file.close()

