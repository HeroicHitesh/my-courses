

list1 = [1,2,3,4]

type(list1)

names = ['Ram', 'Shyam','Razia']

type(names)

for x in names:
    print(x)


list2 = [1,2,'Shyam',True, 2.3]
type(list2)


list1 = [1,2,3,4,5,6,7]

len(list1)

list1[0]

list1[1]

list1[-1]


list1[0:4]

list1 = [1,2,3,4,5,6,7]


list1.clear()

list1 = [1,2,3,4]

list1.append(100)

list1.append(101)


list1.insert(0, 10)

list1.insert(2, 12)

list1.remove(12)

list1 = [1,12,3,12,12]
list1.remove(12)

list1.remove(12)

list1.remove(12)


list1 = [1,12,3,12,12]

while (12 in list1):
    list1.remove(12)

list1 = [1,12,3,12,12]

del (list1[0])


list1 = [10,20,30]

list2 = [100,200,300]


list1.append(list2)



list1 = [10,20,30]

list2 = [100,200,300]

for item in list2:
    list1.append(item)
    


list1 = [10,20,30]

list2 = [100,200,300]

list1.extend(list2)

list1 = [10,20,30]

list2 = [100,200,300]

list1 = list1+list2




list1 = [1,2]
list2 = [10,30]
list3 = [100,200,300]


list4 = list1+list2+list3

list1.extend([list2, list3])

list1.extend(list2+list3)



list1 = [1,3,4,10,4,100,0]
list1.sort()

list1 = [1,3,4,10,4,100,0]
list1.sort(reverse = True)

list1 = [10,20,40]

list1.index(20)

list1 = [10,20,40, 20, 30]


list1.count(20)


list1 = [10,20,30]

list2 = list1 #deep copy


list2.append(101)

list1 = [10,20,30]

list2 = list1.copy() #shallow copy

list2.append(101)


list1.pop()


list1 = [10,20,30]
list1.pop(0)

list1 = [1,2,3]


list1 = ['Ram','Shyam']

list1.remove('Ram')

del list1[0]


list1 = ['Ram','Shyam']

list1.sort()

list1 = ['Ram','Shyam']

list1.sort(reverse = True)


list1[0] = 'Radha'

list1[0]

list1 = [1,2,4]

del list1[-1]

#doc string
def add2(a, b):
    """
    this function adds two numbers
    """
    return a+b

add2(10,20)



def strl(str1):
    return len(str1)

str2 =  'India'

strl(str2)



list1 = ['Priya','Ram','Yiot'] 

#list1.remove('y')





str1 = "mad"

str1[::-1]


def fun1(str1):
    if str1 == str1[::-1]:
        return (True)
    else:
        return (False)


fun1("madam")
fun1('mom')
fun1("teacher")









#list

list1 = [1,2,3,4,5,6]
type(list1)

#use of slicing in list
print (list1[0])

print (list1[-1])

print (list1[0:5])

print (list1[::-1])

print (list1[5])

list1[0] = 10 #list can be modified (mutable)

#adding a new item in list
list1.append(7)

list1.append(100) #it adds the item in last

list1.append("Ram")

list1.insert(1, 200)

list1.remove(200)

list1.remove(1000)

if (1000 in list1):
    list1.remove(1000)
else:
    print ("Item not in the list")
    
list1 = [1,2,3,2,3,4]

list1.remove(2)

list1.remove(2)


list1 = [1,2,3,4,5,6,7]

#list1.remove(3)

list1.remove(list1[2])

del list1[2]


list1 = [1,2,1,10,2,4,2,2,10]

while 2 in list1:
    list1.remove(2)

list1 = [1,2,3,4,5,6]

list1.pop()

list1.pop()

list1.pop(2)



list1 = [1,2,3]

list2 = [10,20,30]

list3  = list1 + list2 #merge of two list


list1.append(list2)



list1 = [1,2,3]
list2 = ['Ram','Shyam']

list1.append(list2)


list1 = [1,2,3]
list2 = ['Ram','Shyam']

for item in list2:
    list1.append(item)
    
list1 = [1,2,3]
list2 = ['Ram','Shyam']
    
list1 = list1 + list2

list1 = [1,2,3]
list2 = ['Ram','Shyam']

list1.extend(list2)





list1 = [10,20,30,40]

list2 = []

for item in list1:
    list2.append (item*item)


list(range(1,21))

list1 = []

for item in list(range(1,21)):
    if (item % 2 == 0):
        list1.append(item)


list(range(21,1, -1))



list1 = [10,3,2,19,4]


list1.sort(reverse = True)



list1.reverse()



list1 = [10,3,2,19,4,4]

list1.index(19)

list1.count(4)

list1.index(4)


[]
() = tuple

tp = (1,2,3,4)
type(tp)

#read only/immutable

#const

tp[0]

tp[0:4]



#functions

def f1(a,b):
    return (a+b)


print (f1(10,23)) #calling

ist1 = []

while (True):
    
    name = input("Enter the name: ")
    
    if not name:
        break
    
    list1.append(name)




list1 = [1,2,3]
list2 =[10,20,30]

list3 = [list1[0]] + [list2[0]]



list1 = [1,2,3,4,5,6]

while (True):

    value = input("Enter the value to remove")
    
    if not value:
        break
    
    if int(value) in list1:
        list1.remove(int(value))
    else:
        print ("item not in list")


data = "1 2 3 4 5"



list1 = data.split()




list1 = [10,12,7,9]

list1.sort()

list1.sort(reverse = True)


list1 = [1,2,3,4,3,5]

list1.remove(list1[-2])

list1.pop(-2)



list1 = [10,20,30,40]

for index, item in enumerate(list1):
    print(index, item)
    
        
tp = tuple(list1)



list1 = [10,20,30,40]

list2 = list1

list2.append(50)

list1 = [10,20,30,40]
list2 =  list1.copy()







list1 = [1,2,3,4,3,5]


list2 = []

for index, item in enumerate(list1):
    if item == 3:
        list2.append(index)
    




list1 = ["ram","shyam"]

list2 = []

for name in list1:
    list2.extend(list(name))





list1 = [1,2,'eat','sleep','repeat']

print (type(list1))

type(list1[0])

type(list1[-1])




list1 = ['Ram','Shyam','Sita']

list1.pop()














list1 = [1,2,3,4,5,6]

list1[0]
list1[0:4]

list1[-1]

list1[::-1]

list1[5:0:-2]

#membership functions

1 in list1
1 not in list1

10 in list1

10 not in list1


#looping
for item in list1:
    print(item)
    

#appending the items in list
#lists are mutable
#they can be modified

list1.append(7) #adds the item at last

list1.insert(0,100)

list1.remove(7)

list1.pop()

list1 = [1,2,3]
list2 = [10,20,30]

list3 = list1+list2

list1.append(list2) #nested list

list1.extend(list2)



list1 = [1,2,30,20,4]
list1.sort()

list1.sort(reverse=False)


list1.reverse()

min(list1)

max(list1)

len(list1)

list1[0] = 1000




#few example
#append squares in list
list1 = [10,20,30,40,50]

list2 = []

for item in list1:
    list2.append(item*item)
    
#append even numbers in list2
list2 = []    
for number in range(1,10):
    if number % 2 == 0:
        list2.append(number)
        
#delete all occurences of 2
list1 = [1,2,1,2,3,5,2]

while (2 in list1):
    list1.remove(2)
    


#tuples are immutable

tuple1 = (1,2,3,4,5)
type(tuple1)
len(tuple1)

#indexing is same as list
tuple1[0]

tuple1[-1]

tuple1[0] = 10 #not allowed,read only

#single value as tuple

tp = (1)  #int

tp = (1,) #tuple



#functions
def f1(a,b):
    return (a+b)

print (f1(2,3))

def f2(a,b=5):
    return (a+b)

print(f2(2,3))
print(f2(10))


def f3(str1):
    return (len(str1))

print (f3('familyman'))