#!/usr/bin/env python
# coding: utf-8

# In[29]:


#LIST and its functions 
lis=[1,1,2,"a",1.2,"sagar","Python Learner"]
lis


# In[8]:


#count the number of values
lis.count(1)


# In[17]:


#append the object to list
lis.append("Hi LetUpgrade")
lis


# In[22]:


#Removes last object from the list and gives the value
lis.pop()


# In[24]:


#Remove thegiven object
lis.remove(1.2)
lis


# In[26]:


#Reverse the list
lis.reverse()
lis


# In[31]:



#Dictionary and its function
dic={
    "name":"Sagar",
    "age":26,
    "City":"Hyd",
    "Sal":"60000"
}
dic


# In[33]:


#Give all the keys of dic object
dic.keys()


# In[34]:


#Give all the Key value as tuple of dic object
dic.items()


# In[35]:


#Give all the values of dic object
dic.values()


# In[36]:


#Gives the value for given key
dic.get("Sal")


# In[38]:


#CLear the dictionary
dic.clear()
dic


# In[42]:


#SETS and its finction
sett={1,3,12,1,3}


# In[53]:


#Add the element to set
sett.add(55)
sett


# In[50]:


#remove the element to set
sett.discard(3)
sett


# In[52]:


#Remove random elements
sett.pop()


# In[55]:


#remove specified element
sett.remove(55)


# In[57]:


#Shallow copy 
sett1=sett.copy()
sett1


# In[91]:


#Tupple and its function
tup2 = (1,2,3,4,5);
tup1 = (1, 2,2, 3, 4, 5 );


# In[92]:


tup2


# In[96]:


#Counts the number of given elements
a=tup1.count(2);
a


# In[99]:


#Give the index of elemet
b=tup2.index(5);
b


# In[100]:


#Length of given tuple
len(tup1)


# In[101]:


#Minimum value in given tuple
min(tup1)


# In[102]:


#maximum value in given tuple
max(tup1)


# In[118]:


#String and its methods
str="LetsUpgrade is the best Number 1 platform to learn"


# In[119]:


str


# In[120]:


#splits the string into String array
str.split(" ")


# In[121]:


#Converts the string to upper case
str.upper()


# In[122]:


#Return true if string contain number only
str.isdigit()


# In[115]:


#Converts the string to lower case
str.lower()


# In[116]:


#Converts the the first letter to capital
str.capitalize()


# In[ ]:




