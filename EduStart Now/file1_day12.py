# raise Error:
try:
   raise NameError ("Nikhil")
except NameError as  e:
    print ("Th Error is handled")
    print (e)
finally:
    print ("Thw final block is this")]

#ImportError

  try:
   import nikhil
except ImportError as  e:
    print ("Th Error is handled")
    print (e)
finally:
    print ("Thw final block is this")]
  

# IndexError 
try:
   a=[1,2,3,4]
   print (a[6[])
except IndexError as  e:
    print ("Th Error is handled")
    print (e)
finally:
    print ("Thw final block is this")]

#ZeroDivisionError

try:
   a=1/0
   print (a)
except ZeroDivisionError as  e:
    print ("Th Error is handled")
    print (e)
finally:
    print ("Thw final block is this")]

# IOError

try:
   f=open("file1.txt","w")
   f.read()
except IOError as  e:
    print ("Th Error is handled")
    print (e)
finally:
    print ("Thw final block is this")]
