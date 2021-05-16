#!/usr/bin/env python
# coding: utf-8

# ## AUTHOR - RIYA DAGA
# 
# GRIP- THE SPARKS FOUNDATION
# 
# Data Science & Business Analytics Internship
# 
# Exploratory Data Analysis
# TASK-3 : Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’
# 
# As a business manager, try to find out the weak areas where one can work to make more profit. Explore and derive all business problems from data.

# In[46]:


#importing libraries to be used.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings as wg
wg.filterwarnings("ignore")


# In[18]:


#reading the dataset.
df = pd.read_csv(r"C:\Users\reeya\Downloads\SampleSuperstore.csv")


# In[19]:


df.columns


# In[20]:


# data preprocessing.
df.describe()


# In[21]:


df.info()


# In[22]:


#checking for missing values. 
df.isnull().sum()


# In[23]:


#checking for duplicate values.
df.duplicated().sum()


# In[24]:


#deleting the duplicate values.
df.drop_duplicates(inplace=True)
df.head()


# In[25]:


#rechecking duplicate values.
df.duplicated().sum()


# In[26]:


#removing the unnecessary column.
df.drop(['Postal Code'],axis=1,inplace=True)


# In[27]:


df.columns


# # Exploratory Data Analysis

# In[28]:


#checking correlation
df.corr()


# In[29]:


#checking covariance
df.cov()


# In[30]:


#finding pairwise correlation between columns and visualing using heatmaps.
fig, axes = plt.subplots(1,1, figsize = (6,4))
sns.heatmap(df.corr())
plt.show()


# ### Observation- There is a negative correlation between Discount and Profit. As discount increases Profit decreases.

# In[90]:


sns.barplot(x=df.Discount,y=df.Profit)


# ### Observation- When we compare the profit with respect to discounts, all the discounts above 20% is facing a major loss.

# In[95]:


plt.figure(figsize =(8,6))
df.groupby(by ='Region')['Profit'].sum().plot(kind = 'pie',autopct='%1.1f%%',explode=(0.1, 0, 0,0),colors = ['pink', 'yellowgreen', 'lightblue', 'yellow'])
plt.show()


# ### Observation- From the above pie chart it is visible that the Central region has the lowest profit whereas the West has the highest profit. So in order to increase profit we must focus on Central and South region.

# In[77]:


sns.barplot(x=df.Region, y=df.Profit/df.Sales,hue=df.Category)


# ### Observation- Furniture and Office Supplies faces loss in Central region whereas Technology is making profit in every region.

# In[74]:


sns.pairplot(df, hue = "Segment")


# In[92]:


plt.figure(figsize=(10,10))
df.groupby('Segment')['Profit','Sales'].agg(['sum']).plot.bar()
plt.show()


# ### Observation- Consumer has the highest profit & sales and Home Office has the least.

# In[91]:


((df['Ship Mode'].value_counts()/len(df['Ship Mode']))*100).plot(kind="bar", color="yellow")


# ### Observation- Maximum number of shipments belong to tha standard class whereas, very less number of shipments are done on the same day (10%).

# In[68]:


dataplot = df.groupby(['State'])['Sales', 'Profit'].sum()
dataplot.plot.bar(figsize = (20,10))


# ### Observation- We can see California has highest sales and profit followed by New York.

# In[88]:


df.groupby(by ='City')['Profit'].sum().sort_values(ascending = False)[521:].plot(kind = 'bar',color='blue')
plt.show()


# ### Observation- In order to increase profit we must focus on Philadelphia since it has the lowest profit.

# In[76]:


plt.figure(figsize=(50,20))
df.groupby('Sub-Category')['Profit'].agg(['sum']).plot.bar()
plt.show()


# ### Observation- Tables and Bookcases sub-category faces huge loss.
THANK YOU!