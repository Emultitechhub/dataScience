#!/usr/bin/env python
# coding: utf-8

# # PUTTING DATA TOGETHER - Concatinating Data

# In[6]:


import pandas as pd


# In[7]:


import numpy as np


# In[8]:


myseries1=pd.Series(np.random.rand(5), index=[0,1,2,3,4])
print(myseries1)


# In[11]:


myseries2=pd.Series(np.random.rand(5), index=[5,6,7,8,9])
print(myseries2)


# In[12]:


pd.concat([myseries1,myseries2])


# In[13]:


pd.concat([myseries1, myseries2], axis=1)


# In[16]:


pd.concat([myseries1, myseries2],axis=1, keys=['series1','series2'])


# # Concatenation is application to Data Frame too

# In[17]:


myframe1=pd.DataFrame({'Student Name': ['Michael','Bassey','Christopher'],
                      'Sex':['M','F','M'], 'Age':[10,16,17],
                      'School':['Primary','High Scool','High School']})
myframe1


# In[18]:


myframe2=pd.DataFrame({'Student Name':['Daniella','Enobong','Akpan'],
                      'Class':[9,10,5], 'School':['High School','High School','Primary School'],'Sex':['Female','Female','Male'],
                      'Age':[13,17,6]})
myframe2


# In[19]:


pd.concat([myframe1, myframe2])


# # Merging Data

# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


myframe1=pd.DataFrame({'Student Name': ['Michael','Bassey','Christopher'],
                      'Sex':['M','F','M'], 'Age':[10,16,17],
                      'School':['Primary','High School','High School']})
myframe1


# In[5]:


myframe2=pd.DataFrame({'Student Name':['Daniella','Enobong','Akpan'],
                      'Class':[9,10,5], 'School':['High School','High School','Primary School'],'Sex':['F','F','M'],
                      'Age':[13,17,6]})
myframe2


# In[9]:


pd.merge(myframe1, myframe2, how = 'right')


# In[10]:


pd.merge(myframe1, myframe2, how = 'left')


# In[11]:


pd.merge(myframe1, myframe2, on = 'School')


# In[14]:


pd.merge(myframe1, myframe2, on = 'Student Name')


# In[20]:


pd.merge(myframe1, myframe2, on = 'Age')


# In[30]:


pd.merge(myframe1, myframe2, on='Sex')


# In[31]:


pd.merge(myframe1, myframe2, on='Class')


# In[21]:


myframe1=pd.DataFrame({'Student_Name': ['Michael','Bassey','Christopher'],
                      'Sex':['M','F','M'], 'Age':[10,16,17],
                      'School':['Primary','High School','High School']})
myframe1


# In[23]:


myframe2=pd.DataFrame({'Student Name':['Daniella','Enobong','Akpan'],
                      'Class':[9,10,5], 'School':['High School','High School','Primary School'],'Sex':['F','F','M'],
                      'Age':[13,17,6]})
myframe2


# In[32]:


myframe2.columns=('Student Name2','Class','School2')
myframe1.join(myframe2)


# In[ ]:





# In[ ]:





# #      DATA TRANSFORMATION                                        29/11/2021

# In[19]:


import pandas as pd


# In[20]:


import numpy as np


# In[9]:


# REMOVING UNWANTED DATA AND DUPLICATES


# In[10]:


myframe5= pd.DataFrame({'Student Name': ['Ubong', 'Edidiong', 'Itoro', 'Asuquo','Idara'],
                      'Sex':['M','F','M','M','F'],
                      'Age':[10,16,17,15,20],
                      'School':['Primary', 'High','High','High','University']})
#we use the del to remove an unwanted column,
#we use the drop() function to removve an unwanted rows.
myframe5


# In[11]:


## Suppose we want to drop row index 1


# In[12]:


myframe5.drop(0)


# In[13]:


myframe5.drop(1)


# In[14]:


## To delete a column 


# In[15]:


myframe5= pd.DataFrame({'Student Name': ['Ubong', 'Edidiong', 'Itoro', 'Asuquo','Idara'],
                      'Sex':['M','F','M','M','F'],
                      'Age':[10,16,17,15,20],
                      'School':['Primary', 'High','High','High','University']})
myframe5


# In[16]:


del myframe5['School']
myframe5


# In[17]:


del myframe5['Age']
myframe5


# In[23]:


myframe5= pd.DataFrame({'Student Name': ['Ubong', 'Edidiong', 'Itoro', 'Asuquo','Idara'],
                      'Sex':['M','F','M','M','F'],
                      'Age':[10,16,17,15,20],
                      'School':['Primary', 'High','High','High','University']})
myframe5


# In[24]:


del myframe5['Sex']
del myframe5['Age']
myframe5


# In[35]:


import pandas as pd 


# In[39]:


import numpy as np


# In[40]:


# Deleting Duplicates
#To detect duplicates, we use the duplicated()function


# In[45]:


item_frame=pd.DataFrame({'Items': ['Ball','Bat','Hockey','Football','Ball'],
                        'Colour':['White','Grey','White','Red','White'],
                        'Price':[100,500,700,200,100]})
item_frame


# In[46]:


item_frame.duplicated()


# In[ ]:


# To display a duplicated entries, we can use the item_frame.duplicated() function as the index to the DataFrame item_frame.


# In[47]:


item_frame[item_frame.duplicated()]


# In[ ]:


# To drop a duplicate, item_frame.drop_duplicates() or


# In[51]:


item_frame.drop(4)


# In[ ]:


# To delete a column


# In[50]:


del item_frame['Colour']
del item_frame['Price']
item_frame


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


# HANDLING OUTLIERS


# In[4]:


student_frame= pd.DataFrame({'Student Name': ['Ubong', 'Edidiong', 'Itoro', 'Asuquo','Idara','Daniel','Isidore'],
                      'Sex':['M','F','M','M','F','M','F'],
                      'Age':[10,16,17,15,20,70,17],
                      'School':['Primary', 'High','High','High','University','High','High']})
student_frame


# In[5]:


student_frame.describe()


# In[ ]:


# Spotting Outliers in a dataset. Using IQR
Q1=25%=0.25
Q2=50%=0.50
Q3=75%=0.75 where k=1.5


# In[31]:


Q1=student_frame.quantile(0.25)
Q3=student_frame.quantile(0.75)
IQR=Q3-Q1
IQR


# In[34]:


Q1=student_frame.quantile(0.25)
Q3=student_frame.quantile(0.75)
IQR=Q3-Q1
IQR
# OBTAINING INTERQUARTILE MULTIPLER
IQR_Mul=IQR*1.5
IQR_Mul


# In[35]:


Q1=student_frame.quantile(0.25)
Q3=student_frame.quantile(0.75)
IQR=Q3-Q1
IQR
# OBTAINING INTERQUARTILE MULTIPLER
IQR_Mul=IQR*1.5
IQR_Mul
# Obtain Your Lower Limit
lower= Q1-IQR_Mul
upper= Q3+IQR_Mul
print('The lower limit is=',lower)
print('The upper limit is=', upper)


# Next, after filtering the Outlier present in your student_frame dataset, we pass in some codes to update the table with the following lines of code

# In[36]:


student_frame= student_frame[student_frame['Age']>int(lower)]
student_frame= student_frame[student_frame['Age']<int(upper)]
student_frame


# Handling Missing or Invalid Data

# In[ ]:


# There are basically three(3) things we can do regarding missing or invalid data
#1. Ignore,
#2. Fill-in
#3. Remove or Drop


# To illustrate

# In[39]:


myseries=pd.Series([10,20,30,None,40,50,np.NaN],index=['a','b','c','d','e','f','g'])
print(myseries.isnull())
myseries


# In[41]:


myseries=pd.Series([10,20,30,None,40,50,np.NaN],index=['a','b','c','d','e','f','g'])
#print(myseries.isnull())
myseries


# To show the indices containig the missing values

# In[42]:


myseries[myseries.isnull()]


# In[ ]:


#Next we can decide to drop the missing values thus


# In[43]:


myseries_dropped=myseries.dropna()
myseries_dropped


# Data Imputation- this is the process of filling missing values in a given dataset

# In[44]:


myseries_filled=myseries.fillna(myseries.mean())
myseries_filled


# We can equally use the Median of the datasets to fill in missing values

# In[48]:


myseries_fill2=myseries.fillna(myseries.median())
myseries_fill2


# In[ ]:





# # DATA MAPPING                    01/12/2021

# In[ ]:


# The Pandas library provides useful data mapping functions to perform numerous operations. 
The mapping is the creation of a list of matches between two values. 
To define a mapping, we can use dictionary objects.
The replace(), the map(), and the rename() are used.


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


data={'object':['ball','pen','pencil','paper','mug'],
      'color': ['blue','green','yellow','red','white'],
     'price': [1.2,1.0,0.6,0.9,1.7]}
myframe=pd.DataFrame(data)
myframe


# In[4]:


mymap={'blue':'dark blue','green':'light green','yellow':'grey'}


# In[5]:


myframe.replace(mymap)


# In[6]:


mymap2={1.2:1.4,0.6:1.8}
myframe.replace(mymap2)


# In[7]:


mymap={'ball':'house','pencil':'toy'}


# In[8]:


myframe.replace(mymap)


# In[9]:


# We can ADD columns to existing dataset


# In[10]:


mymap2={'ball':'round','pencil':'long','pen':'long','mug':'cylindrical','paper':'rectangular'}
myframe['shape']=myframe['object'].map(mymap2)
myframe


# In[11]:


mymap2={'ball':6,'pencil':8,'pen':9,'mug':4,'paper':20}
myframe['quantity']=myframe['object'].map(mymap2)
myframe


# In[12]:


mymap2={'blue':'light','green':'field','yellow':'margarine','red':'blood','white':'white house'}
myframe['color 2']=myframe['color'].map(mymap2)
myframe


# In[13]:


# Making two columns 


# In[14]:


mymap2={'ball':'round','pencil':'long','pen':'long','mug':'cylindrical','paper':'rectangular'}
mymap3={'ball':6,'pencil':8,'pen':9,'mug':4,'paper':20}
myframe['shape']=myframe['object'].map(mymap2)
myframe['quantity']=myframe['object'].map(mymap3)
myframe


# In[15]:


new=myframe['price']*myframe['quantity']
new
#myframe['amount']=new
#myframe


# In[16]:


new=myframe['price']*myframe['quantity']

myframe['sales']=new
myframe


# In[17]:


new=myframe['price']/myframe['quantity']

myframe['price/quantity']=new
myframe


# In[18]:


# To replace Missing values


# In[19]:


myseries=pd.Series([1,2,np.nan,4,5,np.nan])
myseries.replace(np.nan,0)


# In[20]:


# Renaming the Indices of a DataFrame


# In[21]:


data={0:'1st', 1:'2nd', 2:'3rd', 3:'4th', 4:'5th'}
myframe=myframe.rename(data)
myframe


# # DISCRETIZATION AND BINING
# Discretization helps us to divide our large dataset into discrete categories of intervals or range before we can conduct some simple statistical calculations in them.

# In[22]:


readings=[34,39,82,75,16,17,15,74,37,68,
         22,92,99,54,39,96,17,36,91,86]


# In[23]:


intervals=[0,25,50,75,100]


# In[24]:


mycategory=pd.cut(readings, intervals)
mycategory


# In[25]:


pd.value_counts(mycategory)


# In[26]:


#In place of numbers, we can assign Names to the intervals


# In[27]:


names=['Poor','Below Average','Average','Good']
pd.cut(readings, intervals, labels=names)


# In[28]:


pd.qcut(readings, 4)


# In[29]:


pd.value_counts(pd.qcut(readings,4))


# In[ ]:





# In[ ]:





# In[1]:





# # AGGREGATING DATA                                03/12/2021

# In[ ]:


# Aggregation is the process of grouping data together into a list or any other data structure. 
We make use of statistical functions like the mean, median, count, sum to combine several rows together.


# In[30]:


import pandas as pd
import numpy as np


# In[31]:


data={'object':['ball','pen','pencil','paper','mug'],
      'color':['blue','white','red','red','white'],
     'price':[1.2,1.0,0.6,0.9,1.7]}
data
myframe=pd.DataFrame(data)
myframe


# #Notice that the column color has white for two different objects:pen and mug. We may decide to group
# the dataset by the color column so as to gain insight into our data.
# To do this, we may use the groupby( ffunction)

# In[34]:


mygroup=myframe['price'].groupby(myframe['color'])
mygroup.groups


# #The output shows the groups available in our dataset based on their colors.
# We have 3 basic groups by using the attribute groups.
# We can find the mean of the groups by using the attibute groups

# In[35]:


mygroup.mean()


# In[36]:


# Sum


# In[37]:


mygroup.sum()


# In[38]:


# Median


# In[39]:


mygroup.median()


# We can conduct a Hierarchicalgrouping - grouping by more than one column -by typing the following commands

# In[41]:


mygroup2=myframe['price'].groupby([myframe['color'],myframe['object']])
mygroup2.groups


# In[42]:


mygroup2.sum()


# In[45]:


mygroup.diff()


# In[43]:


mygroup2.diff()


# In[44]:


mygroup2.count()


#     #Insert another index

# In[46]:


myframe2=myframe
myframe2.loc[5]=['pencil','red',0.8]
myframe2


# #We can now group our new frame by color and object as well

# In[47]:


mygroup2=myframe2['price'].groupby([myframe2['color'],myframe2['object']])
mygroup2.groups


# In[48]:


mygroup2.mean()


# In[49]:


mygroup2.sum()


# In[50]:


mygroup2.diff()


# In[51]:


mygroup2.count()


# # Selection of Data
# 

# Sometimes you may have to work with just a subset of your dataset.
# In this case, we select the data of interest from the dataset. Lets see how this work in practice

# In[65]:


myframe4 = pd.DataFrame(np.arange(15).reshape((3,5)),
index = ['row0','row1','row2'],
columns=['col0','col1','col2','col3','col4'])
myframe4


# In[66]:


myframe4.columns


# In[71]:


myframe.index


# In[73]:


myframe4.values


# We can select a single column from ouurbtable thus

# In[74]:


myframe4['col3']


# In[75]:


myframe4['col4']


# In[76]:


myframe4['col0']


# In[77]:


myframe4.col4


# In[78]:


myframe4.col0


# In[79]:


myframe4.col1


# # Working on Rows

# It is possible to extract or select a few rows from our DataFrame. To extract rows with index 1 and 2(3 excluded). We type the following command:

# In[81]:


myframe4[0:4]


# In[82]:


myframe4[0:1]


# In[83]:


myframe4[0:0]


# In[85]:


myframe4[0:4]


# The attribute locate loc accesses the rows by the names of their indices.

# In[86]:


myframe4.loc['row2']


# In[87]:


myframe4.loc['row0']


# We can also give ours rows and columns meaningful names

# In[97]:


myframe4.index.name='x-axis'
myframe4.columns.name='y-axis'
myframe4


# We can add a new column to our existing DataFrame and assign values to it

# In[98]:


myframe4['col5']=np.random.randint(100, size=3)
myframe4


# Finnaly, we can change a single value in our dataframe by selecting that entry or element and updating it. Suppose we want to update element 1 of col1, we write:

# In[101]:


myframe4['col1'][1]=10
myframe4


# In[102]:


myframe4['col3'][0]=5
myframe4


# Similar to the Series dataframe, we can use the isin() to check for membership in our dataframe.

# In[106]:


myframe4.isin([1,4,95])


# If we use the Boolean values returned as indices to the DaataFrame, we get NaN values at positions where our specified values are not present.

# In[107]:


myframe4[myframe4.isin([1,4,95])]


# To delete any column in our DataFrame, we make use of the del() keyword

# In[108]:


del myframe4['col5']
myframe4


# Selecting a single row or multiple row for deletion

# In[166]:


mydata={'Employee Name':['Ashley','Ubong', 'Inyene','Michael', 'Uduak'],
       'Specialization':['Python','Data Science','Data Preparation','Data Analysis','Machine Learning'],
       'Experience(Years)':[3,5,8,2,4],
       'Gender':['F','M','F','M','F']}
myframe=pd.DataFrame(mydata) # note capital D and F in DataFrame() constructor.
myframe


# In[150]:


mydata={'Employee Name':['Ashley','Ubong', 'Inyene','Michael', 'Uduak'],
       'Specialization':['Python','Data Science','Data Preparation','Data Analysis','Machine Learning'],
       'Experience(Years)':[3,5,8,2,4],
       'Gender':['F','M','F','M','F']}
myframe=pd.DataFrame(mydata) # note capital D and F in DataFrame() constructor.
myframe


# We can select just a few columns from the dataframe in any arbitary order, using the columns option. Note the columns will always be displayed in the order we specify irrepective of how they are stored in the dictionary object

# In[163]:


myframe2= pd.DataFrame(mydata, columns=['Employee Name','Experience(Years)'])
myframe2


# In[167]:


myframe[myframe['Experience(Years)']>=4]


# In[168]:


myframe[myframe['Gender']=='F']


# In[169]:


myframe[myframe['Gender']=='M']


# We can select a single row or multiple rows from a DataFrame. Suppose we are interested in those employees having more four years of experience. We use the following command for the selection.

# In[132]:


myframe


# #Transposing data: Finally, we can 

# In[170]:


myframe[myframe['Specialization']=='Python']


# In[171]:


myframe.T


# In[ ]:




