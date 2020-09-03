#!/usr/bin/env python
# coding: utf-8

# # Day 3 Assignment Question1

# In[40]:


alt=int(input("Enter the altitude: "))

if(alt<=1000 and alt>0):
    print("Safe to land")
elif(alt>1000 and alt<5000):
    print("Bring down to 1000")
elif(alt>=5000):
    print("Turn Around")
else:
    print("Enter positive altitude")


# In[ ]:





# 
# # Day 3 Assignment Question2

# In[45]:


for ele in range(1,201):
    if ele>1:
        for i in range(2,ele):
            if (ele%i)==0:
                break
        else:
                print(ele, end=" ")


# In[ ]:




