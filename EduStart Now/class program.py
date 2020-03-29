'''class:  blueprint for defining the objects
object: it is instance of a class

class :  attributes   ----> variables
            behaviour   -----> methods

'''

#__init__ -----> constructor
'''
class Employee:
    a=10
    def details(self,name,add,loc):
        b=100
        self.name=name
        self.add=add
        self.loc="Ameerpet"
        print (b)
    def display(self):
        print ("name is: ",self.name)
        print ("address is :", self.add)
        print ("location is :",self.loc)
    def __del__(self):
        print ("This is printed when an object is deleting")
e=Employee()
e.details("nikhil","raju","Panjagutta")
e.display()
print (Employee.a)
e1=Employee()
del e1
'''

#single Inheritance

class A:
    def Hi(self):
        print ("Hi")
class B(A):
    def Hello(self):
        print ("Bye")
class C(B,A):                      #C(B): -----> Multilevel     #C(B,A): -----> Multiple 
    def Hey(self):
        print ("Hey")
c=C()
c.Hey()
c.Hello()
c.Hi()
a=A()
a.Hi()
b=B()
b.Hi()
b.Hello()




    



