import pandas as pd #import pandas

df = pd.read_csv(r'Retail\transaction.csv') #import dataset
df.info()
df.shape
pd.set_option('display.max.columns', 25)
df.head()
df.tail()
df.loc[1000]


#filter and order
df_store1 = df[df['store_id'] == 1] #filtering

specific_data = [48, 49]
df[df['product_id'].isin(specific_data)]

df2 = df.set_index('product_id')
df.filter(items= ['store_id','total'])

df.sort_values(by= 'total', ascending=False) #ordering

#indexing
df.set_index(['store_id','id'],inplace=True)
df.sort_index(ascending=False) 
df.loc[1, 626490]
df.reset_index()

#group by and aggregate
store = df.groupby('store_id').sum('total')

store = df.groupby('store_id').agg({'quantity':['sum','mean'],'total':['sum','mean']})
store

df.groupby(['store_id', 'product_id']).mean('total')
pd.set_option('display.max.rows', 200)

store = df.groupby('store_id').describe()

#merge, join, concatenate
df1 = pd.read_csv(r'Retail\store.csv')
df1

df.merge(df1,how= 'inner', left_on= 'store_id', right_on= 'id')

df3= df.set_index('store_id').join(df1.set_index('id'), lsuffix= 'left', rsuffix= 'right')
df3.set_index('type').groupby('type').sum('total')

#visualization
import numpy as np
import matplotlib.pyplot as plt

df['created_at'] = pd.to_datetime(df['created_at'])
df['month'] = df['created_at'].dt.to_period('M')


df4 = df.set_index('month').groupby('month').sum('total').filter(items= ['created_at', 'total'])
df4.plot.line()
df4

#data cleaning
df5 = pd.read_excel(r'Power BI - Final Project.xlsx')
df5.drop_duplicates()
df5 = df5.drop(columns= ['Browser','OS','City','Country','Referrer'])
df5['Q1 - Which Title Best Fits your Current Role?'] = df5['Q1 - Which Title Best Fits your Current Role?'].str.replace('Other (Please Specify):','')
df5['Q4 - What Industry do you work in?']= df5['Q4 - What Industry do you work in?'].str.replace('Other (Please Specify):','')
df5['Unique ID'] = df5['Unique ID'].apply(lambda x: x[0:5] + '-' + x[5:10] + '-' + x[10:15]+ '-' + x[15:25])
df5[['min_salary','max_salary']] = df5['Q3 - Current Yearly Salary (in USD)'].str.split('-',n=1, expand=True)
