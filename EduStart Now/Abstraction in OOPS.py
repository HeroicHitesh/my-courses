from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def hi(self):
        pass
class B(A):
    def hi(self):
        print ("Say hello")
b=B()
b.hi()
