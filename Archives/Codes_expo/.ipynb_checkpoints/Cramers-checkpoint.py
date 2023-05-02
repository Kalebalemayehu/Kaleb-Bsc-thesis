#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from pandas import read_csv


# In[6]:


#Open Dataset
series = read_csv(r"D:\Jacobs\Lecture\Data Analytics for SCM\2020\04_Sources\Exploratory Data Analysis and Preprocessing\Datasets\PhonePreferences.csv")



# In[7]:


#In this cas there is only two variables, however even if there were more you would use the following 
#to select the fields you want to compare
myfield1 = series['Phone preference']
myfield2 = series['Sex']


# In[19]:


#Get a quick look of the count 
contTable = pd.crosstab(myfield1, myfield2)



# In[11]:


#Researchpy package to calculate Cramér's
#get_ipython().system('pip install researchpy')


# In[12]:


import researchpy


# In[16]:


crosstab, results = researchpy.crosstab(myfield1, myfield2, test='chi-square')


# In[17]:


results


# In[21]:


#We can see that Cramér's V = 0.2414, to identify the degree of the results we need to fiend the degree of freedom
#df = (r-1)(c-1)
df= (contTable.shape[0]-1)*(contTable.shape[1]-1)
df


# In[ ]:


#df = 2, according to the table, a 0.2414 will have a medium association

