#!/usr/bin/env python
# coding: utf-8

# In[4]:


# introduction to tuple datatype
#Definition-- An immutable list is called as tuple
#how to define a tuple ---> ()  paranthesis
#tuple is classified as an immutable data type


# In[6]:


dimensions = (200,50)

print(dimensions)


# In[7]:


type(dimensions)


# In[8]:


# req 200, .... 250


# In[11]:


dimesnions [0] = 250


# In[14]:


dimensions = (10,20,30,40,50)

print (dimensions)


# In[16]:


print(dimensions[2])


# In[19]:


for x in dimensions:
    print(x)


# In[21]:


# introduction to dictionary datatype: --- dict
# definition: A dictionary is nothing but the data defined in key value pairs ***
# how to define a dictionary ---> {} flower bracket/curley bracket
# it is an mutable datatype
# it is used in almost every real world object based application.


# In[22]:


# req to build a game
# alien ---> 5


# In[23]:


alien = {'color':'green','points':5}


# In[24]:


type(alien)


# In[25]:


print(alien)


# In[26]:


# keys will be acting as indexing point


# In[27]:


useraccount_1 = {'username':'codetraining01','fname':'code','lname':'training','pwd':'12345'}


# In[30]:


print(useraccount_1['username'])


# In[31]:


print(useraccount_1['pwd'])


# In[32]:


useraccount_1['location'] = 'farzi code'


# In[33]:


print(useraccount_1)


# In[ ]:




