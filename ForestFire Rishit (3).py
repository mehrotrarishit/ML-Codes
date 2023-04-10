#!/usr/bin/env python
# coding: utf-8

# In[2]:


train1=pd.read_csv("train.csv")


# In[3]:


train1


# In[4]:


train1.isnull().sum()


# In[5]:


train1=train1.dropna()


# In[6]:


train1.isnull().sum()


# In[7]:


train1_y=train1.pop(train1.columns[-1])


# In[8]:


train1_y


# In[9]:


train1_x=train1.drop(columns=["day","month","year"])


# In[10]:


train1_x


# In[11]:


X=train1_x
Y=train1_y

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2)


# In[12]:


rf = RandomForestClassifier(n_estimators=100)
rf.fit(train1_x,train1_y)


# In[13]:


rf.score(x_test, y_test)


# In[14]:


test1=pd.read_csv("test.csv")


# In[15]:


test1


# In[16]:


test1=test1.drop(columns=["ID","day","month","year"])


# In[17]:


test1


# In[20]:


y_predict=rf.predict(test1)
y_predict.reshape(48,1)


# In[ ]:





# In[ ]:




