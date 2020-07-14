#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Introduction to looping statements
working with for loops


# In[ ]:


# required to gree customers on a new year 'wish you a very happy new year'


# In[5]:


bank_customers = ['naveen','papi','ram','karthik','samia','surya','vandana','anushka']

print(f"wish you a very happy new year, {bank_customers[0]}")


# In[6]:


print(f"wish you a very happy new year, {bank_customers[1]}")


# In[10]:


for customer in bank_customers:
    print(f"wish you a very happy new year, {customer}")


# In[ ]:


# general syntax of a for loop:

for tempvar in mainvar:
    print(tempvar)


# In[ ]:


for x in bank_customers:
    print(f"Wish yu a happy new year, {x}")


# In[ ]:


# req to appreciate the students


# In[14]:


Students = ['suman','keerthi','yasmeen','ravi','john','praveen','sajid']

for x in Students:
    print(f"Keep up the good work, {x}")


# In[15]:


for x in Students:
    print(f"Keep up the good work, {x.title()}")


# In[ ]:


# enhancement of code


# In[17]:


for x in Students:
    print(f"Keep up the good work, {x.title()}")
    print(f"I will be looking forward to receive all your practise file of today, {x.title()}")


# In[ ]:


# Line space \n


# In[18]:


for x in Students:
    print(f"Keep up the good work, {x.title()}")
    print(f"I will be looking forward to receive all your practise file of today, {x.title()}.\n")


# In[19]:


for x in Students:
    print(f"Keep up the good work, {x.title()}")
    print(f"I will be looking forward to receive all your practise file of today, {x.title()}.\n")
    
print("Thank you all for showing the interest in learning python")


# In[ ]:


Introduction to Zen of python


# In[22]:


import this


# In[ ]:


# Introduction to organising the list:


# In[23]:


print(Students)


# In[ ]:


# 2 possible ways to do that
1. Temp way
2. Perm way


# In[25]:


print(sorted(Students))


# In[26]:


print(Students)


# In[28]:


Students.sort()
print(Students)


# In[29]:


print(Students)


# In[ ]:




