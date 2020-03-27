# Matplotlib
# NumPy - Numerical Python
# Pandas - Panel Data Set


"""
Basics of Matplotlib
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]

y = [1,2,3,4,5,6,7,8,9,10]


# Setting the title
plt.title("A Line Graph")
# Setting the X Label 
plt.xlabel("X")
# Setting the Y Label
plt.ylabel("Y")
# Displaying the Grid
plt.grid(True)
# Changing the x axes limits of the scale
plt.xlim(0, 10)
# Changing the y axes limits of the scale
plt.ylim(0, 10)
# Or
plt.axis([0, 10, 0, 10])
# Showing the points on the graph
plt.scatter(x, y)
# Simple Line plot
plt.plot(x, y)
plt.show()
plt.savefig("scatter.jpg")

plt.show()


# Changing the color of the line
plt.plot(x, y, color='green') # #000000
plt.plot(x, y, color="#FF0000") # #000000

# Changing the style of the line
plt.plot(x, y, linestyle='dashed') # solid dashed  dashdot dotted

# For Plotting Scatter Plot
plt.plot(x, y, 'd', color='red') # o  .  , x  +  v  ^  <  >  s d 


"""
Introduction to NumPy
"""


a = [0,1,2,3,4,5,6,7,8]
print (type(a))
print (a)  
# it always prints the values with comma seperated , thats list


# Convert your list data to NumPy arrays
import numpy as np

x = np.array( a ) 
print (type(x))

print (x)
# it always prints the values WITHOUT comma seperated , thats ndarray


# to print the data type of the elements of array 
print (x.dtype)


# to print the dimension of the array 
print (x.ndim)

# to print the shape of the array 
# returns a tuple listing the length of the array along each dimension
# For a 1D array, the shape would be (n,) 
# where n is the number of elements in your array.
print (x.shape)


# Shows bytes per element 
print (x.itemsize)

# reports the entire number of elements in an array
print(x.size)

# returns the number of bytes used by the data portion of the array
print (x.nbytes)



# Array Indexing will always return the data type object 
print (x[0])
print (x[2])
print (x[-1])




"""
Reshaping is changing the arrangement of items so that shape of the array changes
Flattening, however, will convert a multi-dimensional array to a flat 1d array. And not any other shape.
"""

# Reshaping to 2 Dimensional Array - 3 Rows and 3 Columns
x = x.reshape(3,3)
print (x)


print (x.ndim)
print (x.shape)


# Due to reshaping .. none of the below has changed 
print (x.dtype)
print (x.itemsize)
print(x.size)
print (x.nbytes)


# Reshaping to 3 Dimensional Arry -  3 layers of 3 Rows and 3 Columns 
x = np.array( [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27] )
print(x)

print (x.ndim)
print (x.shape)

print (x.dtype)
print (x.itemsize)
print(x.size)
print (x.nbytes)


x = x.reshape(3,3,3)
 
print (x)
print (x.ndim)
print (x.shape)


print (x.dtype)
print (x.itemsize)
print(x.size)
print (x.nbytes)

       
"""
For 1D array, shape return a  tuple with only 1 component (i.e. (n,))
For 2D array, shape return a  tuple with only 2 components (i.e. (n,m))
For 3D array, shape return a  tuple with only 3 components (i.e. (n,m,k) )
"""



"""
Arrays Operations - Basic operations apply element-wise. 
The result is a new array with the resultant elements.
Operations like *= and += will modify the existing array.
"""

import numpy as np
a = np.arange(5) 
print (a)

b = np.arange(5) 
print(b)

x = a + b
print (x) 

x = a - b
print (x)




'''Import Python Libraries'''
import pandas as pd


'''Create an Empty Series'''
s = pd.Series()
print (type(s))
print (s)



'''Create a Series from list'''
s = pd.Series(['a','b','c','d'])
print (type(s))
print (s)
# We did not pass any index, so by default, 
# it assigned the indexes ranging from 0 to len(data)-1, i.e., 0 to 3.


'''Customised Index value'''
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)


'''Accessing Data from Series with Position'''
# Data in the series can be accessed similar to that in an ndarray.
# No doubt we have given indexes, but we are accessing using position 
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print (s)

#retrieve the first element
print (s[0])

#retrieve the first three element
print (s[:3])


#retrieve the last three element
print (s[-3:])




'''A Data frame is a two-dimensional data structure''' 
# data is aligned in a tabular fashion in rows and columns.
# You can think of it as an SQL table or a spreadsheet data representation


import pandas as pd

#Create an Empty DataFrame
df = pd.DataFrame()
print (df)


# Create a DataFrame from Lists

df = pd.DataFrame([1,2,3,4,5])
print (df) 



# Create a DataFrame from List of Lists
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)




import pandas as pd
#Read csv file
df = pd.read_csv("Salaries.csv")

# Not a good technique to print the Data Frame
print (df)


df.info()


#number of dimensions
df.ndim   


#return a tuple representing the dimensionality
df.shape 


#number of elements
df.size 


#List first 5 records
df.head()


#Try to read the first 10, 20, 50 records;
#Can you guess how to view the last few records;


df.tail(5)


# Gives the row Indexes
df.index


#list the column names / column Indexes
df.columns 


#Check types for all the columns
df.dtypes


#list the row labels/index and column names
df.axes


#numpyrepresentation of the data
df.values 



#return max/min values for all columns
df.max() 
df.min()

#return max/min values for all numeric columns
df.mean()
df.median()
df.std()

#What are the mean values of the first 50 records in the dataset?
df.head(50).mean()

#returns a random sample of the data frame
df.sample(5) 



# Accessing data using position
df.iloc[:,2]

# Accessing data using index
df.loc[:,'phd']
 
# This is the best practice 
df['phd']


#Select column rank and salary:
df[['rank','salary']]


# Find unique values in a Series / Column
df['rank'].unique()
df['discipline'].unique()
df['sex'].unique()
list1 = df['sex'].unique().tolist()


# To know the count of male and female candidates
df['sex'] 
df['sex'].value_counts()
df['sex'].value_counts(normalize = True)


#Find how many values in the salary column which are non NaN (use count method);
df['salary'].count()
df['phd'].count()


# Boolean Indexing
# Find those rows which has null values in salary/phd column
df['salary'].isnull()
df[df['salary'].isnull()]

df['phd'].isnull()
df[df['phd'].isnull()]
  



"""
Data Frame: filtering

To subset the data we can apply Boolean indexing. 
This indexing is commonly known as a filter. 
For example if we want to subset the rows in which the salary
 value is greater than $120K:

"""

# Boolean Indexing in Pandas
# select only those professors who has salary more than 120000
df['salary'] > 120000
df_sub= df[(df['salary'] > 120000) ]
df_sub

#or

df.loc[df['salary'] > 120000]


# to display only the selected series/column
df.loc[df['salary'] > 120000,'salary']



#filter using multiple columns

df_sub= df[(df['salary'] > 120000) & \
           (df['phd'] > 10) & \
           (df['sex'] == 'Female' )
           ]
df_sub
# Or

df.loc[(df['salary'] > 120000) & \
           (df['phd'] > 10) & \
           (df['sex'] == 'Female' )]





"""
Analysis of Salaries Data ( Hand On Activity )

1. Which Male and Female Professor has the highest and the lowest salaries
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
4. Missing phd - should be mean of the matching service 
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
7. Who are the senior and junior most employees in the organization.
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K
"""
