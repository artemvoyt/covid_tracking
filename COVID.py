#!/usr/bin/env python
# coding: utf-8

# In[226]:


import pandas as pd
from datetime import timedelta, date, datetime

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

# In[459]:


url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
df = pd.read_csv(url)


# In[460]:


df = df.drop(columns = ['Province/State', 'Lat', 'Long'])


# In[461]:


countries = ['Italy', 'France', 'Germany', 'US', 'China', 'Russia']
df = df.loc[df['Country/Region'].isin(countries)]
df      


# In[462]:


start_dt = date(2020, 1, 22)
end_dt = date.today()- timedelta(1)


# In[463]:


for dt in daterange(start_dt, end_dt):
    df[dt.strftime("%-m/%-d/%y")+' sum'] =     df[dt.strftime("%-m/%-d/%y")].groupby(df['Country/Region']).transform('sum')
    df = df.drop(columns = dt.strftime("%-m/%-d/%y"))
# df = df.drop(columns = '1/22/20')
df = df.drop_duplicates()


# In[464]:


df


# In[465]:


df.columns = df.columns.str.replace(" sum", "")


# In[466]:


df


# In[467]:



        
diff = []
for dt in daterange(start_dt, end_dt):
#     diff = df[dt.strftime("%-m/%-d/%y")].set_index(dt.strftime("%-m/%-d/%y"))
#     diff = pd.DataFrame(diff)
   diff.append(df[dt.strftime("%-m/%-d/%y")])
diff = pd.DataFrame(diff).T   
# diff
# diff = pd.concat([diff, df['Country/Region']], axis=1)
diff


# In[468]:


diff_1 = diff.diff(axis = 1)
diff_1


# In[469]:


diff_2 = diff_1.diff(axis = 1)
diff_2


# In[470]:


diff_2 = pd.concat([df['Country/Region'], diff_2], axis=1)


# In[471]:


diff_2


# In[475]:


csv_name = "COVID_2nd_derivative.csv"
diff_2.to_csv(csv_name)


# In[473]:


diff.to_excel("COVID_raw.xlsx")
diff_1.to_excel("COVID_1st_derivative.xlsx")

with open('last_updated.txt', 'w') as f:
    f.write(datetime.now())

# In[ ]:




