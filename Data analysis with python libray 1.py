#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


#using pandas to read the data from csv file

import pandas as pd
df = pd.read_csv("/Users/arjuntakoria/Downloads/Students.csv")
print(df.head)


# In[9]:


#mandatory steps-

#this command give us the numeric value from the column
#like count,mean,std,min etc...

df.describe()


# In[10]:


#tell us the datatypes of the column

df.info()


# In[12]:


#give us the null values
df.isnull().sum()


# In[17]:


#deleteating unnamed column

df = df.drop(["Unnamed: 0"], axis=1)
print(df.head())


# In[18]:


#tranforming column values

#using replace function 

df["WklyStudyHours"]= df["WklyStudyHours"].str.replace("05-oct","5-10")
df.head()


# In[25]:


#gender distribution chart


#using count plot

plt.figure(figsize=(5,5))

#we storesd in ax to show labels
ax=sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()


# In[26]:


#parent education impact on scores



gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)


# In[29]:


#heat map

sns.heatmap(gb,annot = True)
plt.title("Parent Edu Impact")
plt.show()


# In[ ]:




