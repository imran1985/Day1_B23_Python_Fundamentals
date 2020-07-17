#!/usr/bin/env python
# coding: utf-8

# In[1]:


alien = {'color':'green','points':5,'start_position':0,'current_position':10}


# In[2]:


print(alien)


# In[3]:


# modify the values in dictionary


# In[4]:


alien['color'] = 'yellow'


# In[5]:


alien['points'] = 10


# In[6]:


print(alien)


# In[7]:


# deleting the key value pairs from the dictionary


# In[8]:


del alien['start_position']


# In[9]:


print(alien)


# In[10]:


# introduction to looping with dictionaries


# In[11]:


fav_languages = {'samreen':'python','ram':'c','suresh':'science','janani':'english','sajid':'python','peter':'cobol'}


# In[19]:


# normal syntax
# for tempvar in mainvar:
# print(tempvar)


# In[21]:


# with dict
# for temp1 temp2 in mainvar.items():
   # print(temp1)
   # print(temp2)


# In[23]:


for x,y in fav_languages.items():
    print(f"key.{x}")
    print(f"Value.{y}")


# In[25]:


for x,y in fav_languages.items():
    print(f"key.{x}")
    print(f"Value.{y}\n")


# In[26]:


# i want to know who all students have taken the survey ? i want only keys


# In[28]:


for x in fav_languages.keys():
    print(f"\n student:{x}")


# In[29]:


# i want to know only the values


# In[39]:


for y in fav_languages.Values():
    print(f"\n Choices:{y}")


# In[ ]:




