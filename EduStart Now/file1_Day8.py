'''def fun1(a,b):
    print (a+b)
fun1(10,20)
'''
'''
def lis(l):
    l.append(10)
    print ("List inside function :",l) 
l=[1,2,3,4]
lis(l)
print ("List outside function : ", l)

'''
'''
def lis(l):
    l=[5,6,7]
    l.append(10)
    print ("List inside function :",l) 
l=[1,2,3,4]
lis(l)
print ("List outside function : ", l)
'''
'''
def details(name,add):
    print (" Name is  :", name)
    print (" address is :", add)
details(add="hyderabad",name="nikhil")
'''
'''
def details(name,idd=125):
    print (" Name is  :", name)
    print (" Id is :", idd)
details("nikhil",100)
details("nikhil")
'''
'''
def fun1(a,b):
    print (a+b)
fun1(10,20)

#lambda ---- ananomyus function

fun1=lambda a,b:a+b
print (fun1(10,20))

'''
'''
def fun1(a,b):
    return (a+b)
a=fun1(10,20)
print (a)

'''   
