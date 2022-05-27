#!/usr/bin/env python
# coding: utf-8

# Problem 01 : temperature in Celsius and returns the temperature in Fahrenheit

# In[7]:


## The formula is F = (9/5) * C + 32

celsius = float(input("Enter temperature in celsius: "))
Fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, Fahrenheit))


# Problem 02 : another function that does the opposite (Fahrenheit to Celsius)

# In[9]:


## The formula if C = (5/9) * F - 32

Fahrenheit = float(input("Enter temperature in fahrenheit: "))
Celsius = (Fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(Fahrenheit, Celsius))


# In[ ]:




