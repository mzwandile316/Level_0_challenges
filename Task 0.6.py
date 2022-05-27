#!/usr/bin/env python
# coding: utf-8

# In[7]:


num_1=int(input("Enter 1st number: "));

num_2=int(input("Enter 2nd number: "));

num_3=int(input("Enter 3rd number: "));

def maxium():

    if(num_1>=num_2) and (num_1>=num_3):

        largest = num_1

    elif(num_2>=num_1) and (num_2>=num_3):

         largest = num_2

    else:

         largest = num_3

    print("The maximum number is : ",largest)

maxium()


# In[8]:


## Bonus
num_1=int(input("Enter 1st number: "));

num_2=int(input("Enter 2nd number: "));

num_3=int(input("Enter 3rd number: "));

num_4=int(input("enter 4th number: "));

def maxium():

    if(num_1>=num_2) and (num_1>=num_3) and (num_1 >= num_4):

        largest = num_1

    elif(num_2>=num_1) and (num_2>=num_3) and (num_2 >= num_4):

         largest = num_2
    
    elif(num_3 >= num_2) and (num_3>=num_1) and (num_3 >= num_4):
        
        largest = num_3

    else:

         largest = num_4

    print("The maximum number is : ",largest)

maxium()


# In[ ]:




