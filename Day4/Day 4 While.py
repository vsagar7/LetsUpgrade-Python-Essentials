#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for i in range(1042000,702648266):
    tmp=i
    s=0
    while tmp>0:
        tmp1=tmp%10
        s=s+(tmp1*tmp1*tmp1)
        tmp=tmp//10;

    if i==s:
        print(i)
        break

        
       
        


# In[ ]:




