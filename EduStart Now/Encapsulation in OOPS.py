
# private method:

class test:
    def __init__(self):
        self.__update()
    def run(self):
        print ("running")
    def  __update(self):
        print ("I'm updating")
t=test()
t.run()
t.__update()



#private variable

        
class test:
    __a=100
    def drive(self):
        print ("driving")
        print  (self.__a)
t=test()
t.drive()
print (test.__a)


