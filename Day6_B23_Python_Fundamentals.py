#!/usr/bin/env python
# coding: utf-8

# In[1]:


students = ('anjali','harish','kartika','naveen','ram','samia','suresh','vandana')

len(students)


# In[2]:


# introduction to if else condition
# if name is vandana --> total capital
# all other name I want to get printed in title case


# In[3]:


for x in students:
    if x == 'vandana':
        print(x.upper())
    else:
        print(x.title())


# In[4]:


# introduction to slicing of list


# In[5]:


print(students)


# In[6]:


# 2 students of each group i wanted to make
# general syntax of a slicing
# variable [startvalue:stopvalue:stepcount]
# always last value is exclusive


# In[7]:


print(students[0:2])


# In[9]:


print(students[2:4])


# In[10]:


print(students[4:6])


# In[11]:


print(students[6:8])


# In[12]:


print(students)


# In[16]:


# req i want to create a slice every alternate student starting from begining


# In[13]:


print(students[0:8:2])


# In[15]:


print(students[0:8:3])


# In[17]:


# introduction to negative indexing ! ....0,1,2...


# In[18]:


print(students)


# In[19]:


print(students[7])


# In[20]:


# -1, -2, -3 .....


# In[21]:


print(students[-1])


# In[22]:


print(students[-2])


# In[23]:


# how to reverse a list by using indexing


# In[24]:


print(students[::-1])


# In[ ]:




