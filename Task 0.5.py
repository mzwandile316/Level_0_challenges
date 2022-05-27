#!/usr/bin/env python
# coding: utf-8

# In[25]:


a = int(input("enter 1st side: "))
b = int(input("enter 2nd side: "))
c = int(input("enter 3rd side: "))

# The perimeter
p = (a + b + c) / 2

# The area 
area = (p*(p-a)*(p-b)*(p-c)) ** 0.5

print("The area is of triangle %0.2f" %area)


# In[ ]:




