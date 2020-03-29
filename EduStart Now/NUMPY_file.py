
# coding: utf-8

# # The Numpy array object

# # NumPy Arrays

# In[ ]:


# NUMPY INTRODUCTION


# In[3]:


import numpy as np
a = np.array([0, 1, 2, 3])
print(a)

print(np.arange(10))


# # 1. Creating arrays

# In[ ]:


#1-D

a = np.array([0, 1, 2, 3])

a


# In[ ]:


#print dimensions

a.ndim


# In[ ]:


#shape

a.shape


# In[4]:


len(a)


# In[5]:


# 2-D, 3-D....

b = np.array([[0, 1, 2], [3, 4, 5]])

b


# In[6]:


b.ndim


# In[7]:


b.shape


# In[8]:


len(b) #returns the size of the first dimention


# In[9]:


c = np.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])

c


# In[10]:


c.ndim


# In[11]:


c.shape


# ** 1.2  Functions for creating arrays**

# In[12]:


#using arrange function

# arange is an array-valued version of the built-in Python range function

a = np.arange(10) # 0.... n-1
a


# In[13]:


b = np.arange(1, 10, 2) #start, end (exclusive), step

b


# In[ ]:


#using linspace

a = np.linspace(0, 1, 6) #start, end, number of points

a


# In[14]:


#common arrays

a = np.ones((3, 3))

a


# In[15]:


b = np.zeros((3, 3))

b


# In[ ]:


c = np.eye(3)  #Return a 2-D array with ones on the diagonal and zeros elsewhere.

c


# In[ ]:


d = np.eye(3, 2) #3 is number of rows, 2 is number of columns, index of diagonal start with 0

d


# In[ ]:


#create array using diag function

a = np.diag([1, 2, 3, 4]) #construct a diagonal array.

a


# In[ ]:


np.diag(a)   #Extract diagonal


# In[ ]:


#create array using random

#Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
a = np.random.rand(4) 

a


# In[ ]:


a = np.random.randn(4)#Return a sample (or samples) from the “standard normal” distribution.  ***Gausian***

a


# # 2. Basic DataTypes

# In[ ]:


a = np.arange(10)

a.dtype


# In[ ]:


#You can explicitly specify which data-type you want:

a = np.arange(10, dtype='float64')
a


# In[ ]:


#The default data type is float for zeros and ones function

a = np.zeros((3, 3))

print(a)

a.dtype


# **other datatypes**

# In[ ]:


d = np.array([1+2j, 2+4j])   #Complex datatype

print(d.dtype)


# In[ ]:


b = np.array([True, False, True, False])  #Boolean datatype

print(b.dtype)


# In[ ]:


s = np.array(['Ram', 'Robert', 'Rahim'])

s.dtype


# # 3. Indexing and Slicing

# **3.1 Indexing**

# The items of an array can be accessed and assigned to the same way as other **Python sequences (e.g. lists)**:

# In[ ]:


a = np.arange(10)

print(a[5])  #indices begin at 0, like other Python sequences (and C/C++)


# In[ ]:


# For multidimensional arrays, indexes are tuples of integers:

a = np.diag([1, 2, 3])

print(a[2, 2])


# In[ ]:


a[2, 1] = 5 #assigning value

a


# **3.2 Slicing**

# In[ ]:


a = np.arange(10)

a


# In[ ]:


a[1:8:2] # [startindex: endindex(exclusive) : step]


# In[ ]:


#we can also combine assignment and slicing:

a = np.arange(10)
a[5:] = 10
a


# In[ ]:


b = np.arange(5)
a[5:] = b[::-1]  #assigning

a


# # 4. Copies and Views

# A slicing operation creates a view on the original array, which is just a way of accessing array data. Thus the original array is not copied in memory. You can use **np.may_share_memory()** to check if two arrays share the same memory block. 

# **When modifying the view, the original array is modified as well:**

# In[ ]:


a = np.arange(10)
a


# In[ ]:


b = a[::2]
b


# In[ ]:


np.shares_memory(a, b)


# In[ ]:


b[0] = 10
b


# In[ ]:


a  #eventhough we modified b,  it updated 'a' because both shares same memory


# In[ ]:




a = np.arange(10)

c = a[::2].copy()     #force a copy
c


# NumPy arrays can be indexed with slices, but also with boolean or integer arrays **(masks)**. This method is called **fancy indexing**. It creates copies not views.

# **Using Boolean Mask**

# In[ ]:


a = np.random.randint(0, 20, 15)
a


# **Indexing with an array of integers**

# In[ ]:


a = np.arange(0, 100, 10)

a


# In[ ]:


#Indexing can be done with an array of integers, where the same index is repeated several time:

a[[2, 3, 2, 4, 2]]


# In[ ]:


# New values can be assigned 

a[[9, 7]] = -200

a

