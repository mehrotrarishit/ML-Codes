# -*- coding: utf-8 -*-
"""Housing Prices.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M3CN4VSE2cLMdA311pg0LJpLo0-VMgh3
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train1=pd.read_csv("train.csv")

train1

train1.head

train1.describe()

train1.isnull().sum()

train1=train1.drop(["Alley"],axis=1)

train1

train1['PoolQC'].isna().sum()

train1=train1.drop(['PoolQC'],axis=1)

train1

train1['Fence'].isna().sum()

train1['MiscFeature'].isna().sum()

train1=train1.drop(['MiscFeature'],axis=1)

train1

train1.isnull().sum()

train1[train1.columns[train1.isnull().any()]].isnull().sum() * 100 / train1.shape[0]

train1=train1.drop(['Fence'],axis=1)

train1

print(train1['FireplaceQu'])

train1=train1.drop(['FireplaceQu'],axis=1)

train1

train1['MSZoning'].unique()

train1['Street'].unique()

train1['LotShape'].unique()

train1['LandContour'].unique()

train1['Utilities'].unique()

train1['LotConfig'].unique()

train1['SaleType'].unique()

train1['SaleCondition'].unique()

count=(train1['EnclosedPorch']==0).sum()
print(count)

count=(train1['3SsnPorch']==0).sum()
print(count)

train1=train1.drop(['3SsnPorch'],axis=1)

train1

count=(train1['MiscVal']==0).sum()
print(count)

train1=train1.drop(['MiscVal'],axis=1)

train1

count=(train1['PoolArea']==0).sum()
print(count)

train1=train1.drop(['PoolArea'],axis=1)

train1

count=(train1['ScreenPorch']==0).sum()
print(count)

train1=train1.drop(['ScreenPorch'],axis=1)

train1

count=(train1['EnclosedPorch']==0).sum()
print(count)

train1=train1.drop(['EnclosedPorch'],axis=1)

train1

train1=train1.drop(['RoofMatl'],axis=1)

train1

train1=train1.drop(['BsmtFinSF2'],axis=1)

train1=train1.drop(['LowQualFinSF'],axis=1)

train1

train1.dtypes

train1

df=train1.dtypes[train1.dtypes=='object']
df

meanVal = train1['LotFrontage'].mean()
train1['LotFrontage'].fillna(value=meanVal, inplace=True)

meanVal = train1['MasVnrArea'].mean()
train1['MasVnrArea'].fillna(value=meanVal, inplace=True)

meanVal = train1['GarageYrBlt'].mean()
train1['GarageYrBlt'].fillna(value=meanVal, inplace=True)

train1.isnull().sum()

train1['BsmtCond']=train1['BsmtCond'].fillna(train1['BsmtCond'].mode()[0])
train1['BsmtQual']=train1['BsmtQual'].fillna(train1['BsmtQual'].mode()[0])
train1['GarageType']=train1['GarageType'].fillna(train1['GarageType'].mode()[0])
train1['GarageFinish']=train1['GarageFinish'].fillna(train1['GarageFinish'].mode()[0])
train1['GarageQual']=train1['GarageQual'].fillna(train1['GarageQual'].mode()[0])
train1['GarageCond']=train1['GarageCond'].fillna(train1['GarageCond'].mode()[0])
train1['MasVnrType']=train1['MasVnrType'].fillna(train1['MasVnrType'].mode()[0])
train1['MasVnrArea']=train1['MasVnrArea'].fillna(train1['MasVnrArea'].mode()[0])
train1['BsmtExposure']=train1['BsmtExposure'].fillna(train1['BsmtExposure'].mode()[0])

train1['BsmtFinType2']=train1['BsmtFinType2'].fillna(train1['BsmtFinType2'].mode()[0])

df.to_numpy

columns=['MSZoning','Street','LotShape','LandContour','Utilities','LotConfig','LandSlope','Neighborhood',
         'Condition2','BldgType','Condition1','HouseStyle','SaleType',
        'SaleCondition','ExterCond',
         'ExterQual','Foundation','BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1','BsmtFinType2',
        'RoofStyle','Exterior1st','Exterior2nd','MasVnrType','Heating','HeatingQC',
         'CentralAir',
         'Electrical','KitchenQual','Functional','GarageType','GarageFinish','GarageQual','GarageCond','PavedDrive']

def category_onehot_multcols(multcolumns):
    df_final=final_df
    i=0
    for fields in multcolumns:
        
        print(fields)
        df1=pd.get_dummies(final_df[fields],drop_first=True)
        
        final_df.drop([fields],axis=1,inplace=True)
        if i==0:
            df_final=df1.copy()
        else:
            
            df_final=pd.concat([df_final,df1],axis=1)
        i=i+1
       
        
    df_final=pd.concat([final_df,df_final],axis=1)
        
    return df_final

test_df=pd.read_csv("test.csv")
test_id=test_df.Id

test_df['LotFrontage']=test_df['LotFrontage'].fillna(test_df['LotFrontage'].mean())

test_df['MSZoning']=test_df['MSZoning'].fillna(test_df['MSZoning'].mode()[0])
test_df['BsmtCond']=test_df['BsmtCond'].fillna(test_df['BsmtCond'].mode()[0])
test_df['BsmtQual']=test_df['BsmtQual'].fillna(test_df['BsmtQual'].mode()[0])
test_df['FireplaceQu']=test_df['FireplaceQu'].fillna(test_df['FireplaceQu'].mode()[0])
test_df['GarageType']=test_df['GarageType'].fillna(test_df['GarageType'].mode()[0])
test_df['GarageFinish']=test_df['GarageFinish'].fillna(test_df['GarageFinish'].mode()[0])
test_df['GarageQual']=test_df['GarageQual'].fillna(test_df['GarageQual'].mode()[0])
test_df['GarageCond']=test_df['GarageCond'].fillna(test_df['GarageCond'].mode()[0])
test_df['MasVnrType']=test_df['MasVnrType'].fillna(test_df['MasVnrType'].mode()[0])
test_df['MasVnrArea']=test_df['MasVnrArea'].fillna(test_df['MasVnrArea'].mode()[0])
test_df['BsmtExposure']=test_df['BsmtExposure'].fillna(test_df['BsmtExposure'].mode()[0])
test_df['BsmtFinType2']=test_df['BsmtFinType2'].fillna(test_df['BsmtFinType2'].mode()[0])
test_df['Utilities']=test_df['Utilities'].fillna(test_df['Utilities'].mode()[0])
test_df['Exterior1st']=test_df['Exterior1st'].fillna(test_df['Exterior1st'].mode()[0])
test_df['Exterior2nd']=test_df['Exterior2nd'].fillna(test_df['Exterior2nd'].mode()[0])
test_df['BsmtFinType1']=test_df['BsmtFinType1'].fillna(test_df['BsmtFinType1'].mode()[0])
test_df['BsmtFinSF1']=test_df['BsmtFinSF1'].fillna(test_df['BsmtFinSF1'].mean())
test_df['BsmtFinSF2']=test_df['BsmtFinSF2'].fillna(test_df['BsmtFinSF2'].mean())
test_df['BsmtUnfSF']=test_df['BsmtUnfSF'].fillna(test_df['BsmtUnfSF'].mean())
test_df['TotalBsmtSF']=test_df['TotalBsmtSF'].fillna(test_df['TotalBsmtSF'].mean())
test_df['BsmtFullBath']=test_df['BsmtFullBath'].fillna(test_df['BsmtFullBath'].mode()[0])
test_df['BsmtHalfBath']=test_df['BsmtHalfBath'].fillna(test_df['BsmtHalfBath'].mode()[0])
test_df['KitchenQual']=test_df['KitchenQual'].fillna(test_df['KitchenQual'].mode()[0])
test_df['Functional']=test_df['Functional'].fillna(test_df['Functional'].mode()[0])
test_df['GarageCars']=test_df['GarageCars'].fillna(test_df['GarageCars'].mean())
test_df['GarageArea']=test_df['GarageArea'].fillna(test_df['GarageArea'].mean())
test_df['SaleType']=test_df['SaleType'].fillna(test_df['SaleType'].mode()[0])

test_df.drop(['Alley'],axis=1,inplace=True)
test_df.drop(['PoolQC','Fence','MiscFeature'],axis=1,inplace=True)

test_df.shape

train1.shape

test_df=test_df.drop(['FireplaceQu'],axis=1)
test_df=test_df.drop(['3SsnPorch'],axis=1)
test_df=test_df.drop(['MiscVal'],axis=1)
test_df=test_df.drop(['PoolArea'],axis=1)
test_df=test_df.drop(['ScreenPorch'],axis=1)
test_df=test_df.drop(['EnclosedPorch'],axis=1)
test_df=test_df.drop(['RoofMatl'],axis=1)
test_df=test_df.drop(['BsmtFinSF2'],axis=1)
test_df=test_df.drop(['LowQualFinSF'],axis=1)

test_df.shape

final_df=pd.concat([train1,test_df],axis=0)

final_df=category_onehot_multcols(columns)

final_df.shape

final_df =final_df.loc[:,~final_df.columns.duplicated()]

final_df.shape

final_df=final_df.drop(['Id'],axis=1)
train2=final_df.iloc[:1460,:]
test2=final_df.iloc[1460:,:]

train1_x=train2.drop(['SalePrice'],axis=1)

train1_y=train2['SalePrice']
train1_y

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(train1_x,train1_y,test_size=0.2)

from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor(random_state=1)
rf.fit(train1_x,train1_y)

rf.score(x_test,y_test)

train2

test2

test2.isnull().sum()

test2

nan_values = test2[test2.columns[test2.isna().any()]]
print(nan_values)

test2['GarageYrBlt']=test2['GarageYrBlt'].fillna(test2['GarageYrBlt'].mode()[0])
test2=test2.drop(['SalePrice'],axis=1)

y_predict=rf.predict(test2)

y_predict

y_predict.shape

y_predict.reshape(1459,1)

output=pd.DataFrame({"ID":test_id,"SalePrice":y_predict})
output.to_csv('Exercise:Introduction-Version 1.csv',index=False)