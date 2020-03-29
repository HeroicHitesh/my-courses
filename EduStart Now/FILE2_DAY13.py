import sqlite3

conn = sqlite3.connect('nikhil.db')
print ("Opened database successfully");

#conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
#conn.execute("DELETE from COMPANY where ID = 2;")
conn.execute("DROP  TABLE  COMPANY")
conn.commit
print ("Total number of rows updated :")

cursor = conn.execute("SELECT  * from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("AGE=",row[2])  
   print ("ADDRESS = ", row[3])
   print ("SALARY = ", row[4], "\n")

print ("Operation done successfully")
conn.close()
