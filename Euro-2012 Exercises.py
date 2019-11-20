#!/usr/bin/env python
# coding: utf-8

# 
# 
# ### Step 1. Import the necessary libraries

# In[27]:


import pandas as pd


# ### Step 2. Import the dataset Euro_2012_stats_TEAM

# ### Step 3. Assign it to a variable called euro12.

# In[176]:


euro12 = pd.read_csv("Euro_2012_stats_TEAM.csv")
euro12


# ### Step 4. Select only the Goal column.

# In[162]:


euro = (euro12['Goals'])
euro


# ### Step 5. How many team participated in the Euro2012?

# In[145]:


euro = len(euro12)
print("Numbers of Team participated: ",euro)


# ### Step 6. What is the number of columns in the dataset?

# In[178]:


euro = len(euro12.columns)
print("Numbers of Columns: ",euro)


# ### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

# In[34]:


discipline = pd.read_csv("Euro_2012_stats_TEAM.csv" , usecols = ['Yellow Cards', 'Red Cards'])
discipline


# ### Step 8. Sort the teams by Red Cards, then to Yellow Cards

# In[146]:


euro1 = discipline.sort_values(by=['Red Cards' , 'Yellow Cards'])
euro1


# ### Step 9. Calculate the mean Yellow Cards given per Team

# In[149]:


e = df["Yellow Cards"].mean()
print("Mean Yellow Card Given per Team: %.1f" %e)


# ### Step 10. Filter teams that scored more than 6 goals

# In[150]:


is_6 = euro12['Goals']>6
euro_6 = euro12[is_6]
print(euro_6.head)


# ### Step 11. Select the teams that start with G

# In[155]:


euro = euro12[5:7]
euro


# ### Step 12. Select the first 7 columns

# In[156]:


euro = euro12.iloc[:,0:7]
euro


# ### Step 13. Select all columns except the last 3.

# In[157]:


euro = euro12.iloc[:,:-3]
euro


# ### Step 14. Present only the Shooting Accuracy from England, Italy and Russia

# In[158]:


euro = euro12.loc[[3,7,12],["Team","Shooting Accuracy"]]
euro


# ### Step 15. Use apply method on Goal Column to make a new column called Performance, using following conditions
# 
# 1. If Goals are less than or equal to 2, peformance is **Below Avg**
# 2. If Goals are more than 2 and less than or equal to 5, peformance is **Average**
# 3. If Goals are more than 5 and less than or equal to 10, peformance is **Above Average**
# 4. If Goals are more than 10 then peformance is **Excellent**

# In[159]:


def performance(x):
    if x <= 2:
        return "Below Average"
    elif x > 2 and x <= 5:
        return "Average"
    elif x > 5 and x <= 10:
        return "Above Average"
    elif x > 10:
        return "Excellent"
euro12["Performance"] = euro12["Goals"].apply(performance)
euro12[["Team","Goals","Performance"]]


# In[ ]:




