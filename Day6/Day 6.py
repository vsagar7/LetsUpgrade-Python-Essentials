#!/usr/bin/env python
# coding: utf-8

# # Day 6 Assignment 1

# In[22]:


class BankAccount():
    def __init__(self,ownerName,balance):
        self.ownerName=ownerName
        self.balance=balance
        
    def deposit(self,balance):
        self.balance=self.balance+balance
        print("Your current balance after deposit is : ",self.balance)
        
        
    
    def withdraw(self,balance):
        if(self.balance>balance):
            self.balance=self.balance-balance
            print("Your current balance after With drawal : ",self.balance)
        else:
            print("Insufficient balance")
                


# In[23]:


obj=BankAccount("sagar",5000)


# In[24]:


obj.deposit(50)


# In[25]:


obj.deposit(855)


# In[26]:


obj.deposit(55000)


# In[27]:


obj.withdraw(60000)


# In[28]:


obj.withdraw(1000)


# # Day 6 Assignment 2
# 

# In[41]:


import math 
class cone():
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    
    def volume(self):
        print(math.pi*self.radius*self.radius*self.height*(1/3))
    
    def surfaceArea(self):
        print(math.pi*self.radius*(self.radius+math.sqrt((self.radius*self.radius)+(self.height*self.height))))


# In[42]:


conObj=cone(3,6)


# In[43]:


conObj.volume()


# In[44]:


conObj.surfaceArea()


# In[ ]:




