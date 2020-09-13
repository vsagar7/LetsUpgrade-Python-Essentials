#!/usr/bin/env python
# coding: utf-8

# Day 8 Assignment 1

# In[31]:


def input(ranges):
    def wrapper_fuction():
        print("Enter the range you want to get the Fiboncci series:")
        a = input("Enter how many series you want - ")
        b=int(a)
        ranges(b)
    
    return wrapper_fuction


# In[32]:


@input
def fib(num):
    a=0
    b=1
    s=0
    print(0)
    print(1)
    s=s+b
    a=b
    b=s
    i=0
    while(num>i):
        i=i+1
        print(s)


# In[33]:


fib()


# Day 8 Assignment 1

# In[34]:



get_ipython().run_cell_magic('writefile', 'File.txt', 'Hey i am learning Python with LetsUpgrade')


# In[35]:


f=open("File.txt",'r')
f.read()


# In[36]:


try:
    f.write("You rock")
except:
    print("Permission Denied only read can be done")
finally:
    f.close()


# In[ ]:




