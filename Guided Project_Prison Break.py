#!/usr/bin/env python
# coding: utf-8

# Analyzing Data

# ## Prison Helicopter Escapes

# We begin by importing some helper functions.

# In[44]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[45]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'


# In[46]:


data = data_from_url(url)


# Let's print the first three rows

# In[47]:


for row in data[:3]:
    print(row)


# ## Removing the details

# In[48]:


index = 0

for row in data:
    data[index] = row[:-1]
    index += 1


# In[49]:


print(data[:2])


# ## Extracting the Year

# In[50]:


for row in data:
    date = fetch_year(row[0])
    row[0] = date


# In[51]:


print(data[:2])


# ## Attempts per Year

# In[52]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# Let's inspect the min & max year in the data

# In[53]:


print(min_year)
print(max_year)


# Now we'll create a list of all the years ranging from min_year to max_year. Our goal is to then determine how many prison break attempts there were for each year.

# In[54]:


years = []
for year in range(min_year, max_year + 1):
    years.append(year)


# In[55]:


print(years)


# Now we create a list where each element looks like [<year>, 0]

# In[56]:


attempts_per_year = []
for year in years:
    attempts_per_year.append([year, 0])


# Finally we increment the second entry (the one on index 1 which starts out as being 0) by 1 each time a year appears in the data.

# In[57]:


for row in data:
    for year_attempt in attempts_per_year:
        year = year_attempt[0]
        if row[0] == year:
            year_attempt[1] += 1
            
print(attempts_per_year)  


# In[58]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# The years in which the most helicopter prison break attempts occurred were 1986, 2001, 2007 and 2009, with a total of three attempts each.

# ## Attempts by Country

# In[61]:


countries_frequency = df["Country"].value_counts()
print_pretty_table(countries_frequency)


# In[ ]:


By and far, the country with the most helicopter prison escape attempts is France.

