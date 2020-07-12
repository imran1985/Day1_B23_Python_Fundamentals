#!/usr/bin/env python
# coding: utf-8

# In[1]:


students = ['deepak','anushka','kiran','ravi','papi','ram']

print(students)


# In[2]:


type(students)


# In[ ]:


# Introduction to indexing : 0,1,2,3,...

I want to access 'kiran' name in outpu


# In[3]:


print(students[2])


# In[ ]:


#enhnancement of code


# In[4]:


print(students[2].title())


# In[ ]:


# reassignment, adding and removal of element/items in the list


# In[5]:


print(students)


# In[ ]:


# replace kiran with sajid


# In[6]:


students[2] = 'sajid'

print(students)


# In[ ]:


# required to add swapna to the list


# In[7]:


students.append('swapna')

print(students)


# In[8]:


students.append('salman')

print(students)


# In[ ]:


# required to add 'laxmi' at the 3rd index position


# In[9]:


students.insert(3,'laxmi')
print(students)


# In[ ]:


# Removal of element from the list ... req 'deepak' name to delete from the list


# In[10]:


del students[0]

print(students)


# In[ ]:


# POP method ---. it will be creating a carboncopy of deleted item


# In[12]:


x = students.pop()

print(students)


# In[13]:


print(x)


# In[14]:


y = students.pop(3)

print(students)


# In[15]:


print(y)


# In[ ]:




