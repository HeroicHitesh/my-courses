'''class A:
    def hi(self):
        print ("Say Hi")
class B(A):
    def hi(self):
        print ("Say hello")
b=B()
b.hi()

'''
# overriding without inheritance based on object execution happens

class A:
    def hi(self):
        print ("Say Hi")
class B:
    def hi(self):
        print ("Say hello")
def common(test):
    test.hi()
a=A()    
b=B()
common(a)
common(b)


