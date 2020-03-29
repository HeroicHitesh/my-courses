class A:
    def m1(self):
        print ("Hello")
class B(A):
    def m1(self,a):
        print ("Bye")
b=B()
b.m1("Bye Bye")

