#!/usr/bin/env python
# coding: utf-8

# In[18]:


def convert(minutes):
    minutes = minutes % (24 * 60)
    hour = minutes // 60
    minutes %= 60
      
    return "%d hours:%02d minutes" % (hour, minutes)
      
# Driver program
n = 72
print(convert(n))


# In[ ]:




