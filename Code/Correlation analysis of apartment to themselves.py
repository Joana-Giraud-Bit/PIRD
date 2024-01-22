# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:37:44 2024

@author: joana
"""

import os
import numpy as np
import pandas as pd

folder = r"../Data/"
files = os.listdir(folder)
#Get a list of the different files named IECS
list_IECS = [file for file in files if '-IECS' in file]   
list_IECS.sort()

data = {} #Creation of a dictionary
for file in list_IECS:
    df = pd.read_csv(folder + file) #Read the csv file
    ts = df.set_index('0')['Value']     # DataFrame -> TimeSeries
    ts.index = pd.to_datetime(ts.index, unit='s')   # index to secondes
    ts = ts.resample("10Min").mean()    # resample 10 min
    data[file[:-4]] = ts 
    
df = pd.DataFrame(data)
df = df[~df.isnull().any(axis=1)]  # remove the row with Nan Value

df=df.drop(columns=['25-IECS', '26-IECS', '27-IECS', '35-IECS', '64-IECS', '65-IECS', '67-IECS', '9-IECS' ])
df['mean'] = df.mean(axis=1) 
#print(df)

df=df*3600
print(df)

# Comparing the month of December

df1=df['2020-12-01 00:00:00' : '2020-12-16 00:00:00']
df2=df['2020-12-16 00:10:00' : '2020-12-30 16:00:00']
print(df1)
print(df2)

df_12_corr =df1.corrwith(df2.set_axis(df1.index, axis='index', copy=False)) # Correlation matrice of df1 with df2 changing the index name with the index name of dh1 to compare them
print(df_12_corr)

df3=df1.resample('H').mean()
df4=df2.resample('H').mean()

print(df3.shape)
print(df4.shape)

df4=df4.drop('2020-12-30 13:00:00')
df4=df4.drop('2020-12-30 14:00:00')
df4=df4.drop('2020-12-30 15:00:00')
df4=df4.drop('2020-12-30 16:00:00')

print(df4.shape)

df_34_corr =df3.corrwith(df4.set_axis(df3.index, axis='index', copy=False)) # Correlation matrice of df1h with df2 changing the index name with the index name of dh1 to compare them
print(df_34_corr)


df5=df1.resample('D').mean()
df6=df2.resample('D').mean()

print(df5.shape)
print(df6.shape)

df5=df5.drop('2020-12-16')

df_56_corr =df5.corrwith(df6.set_axis(df5.index, axis='index', copy=False)) # Correlation matrice of df1h with df2 changing the index name with the index name of dh1 to compare them
print(df_56_corr)


df7=df1.resample('5D').mean()
df8=df2.resample('5D').mean()

print(df7.shape)
print(df8.shape)

df7=df7.drop('2020-12-16')

df_78_corr =df7.corrwith(df8.set_axis(df7.index, axis='index', copy=False)) # Correlation matrice of df1h with df2 changing the index name with the index name of dh1 to compare them
print(df_78_corr)

# Correlation of the 3 apartments with themselves and of the mean value of the apartment starting with a comparison between December 2020 and January 2021


df9=df['2020-12-01 00:00:00' : '2020-12-31 00:00:00']
df10=df['2021-01-01 00:00:00' : '2021-01-30 13:00:00']
print(df9.shape)
print(df10.shape)

df_910_corr =df9.corrwith(df10.set_axis(df9.index, axis='index', copy=False)) # Correlation matrice of df1h with df2 changing the index name with the index name of dh1 to compare them
print(df_910_corr)

df11=df9.resample('H').mean()
df12=df10.resample('H').mean()

print(df11.shape)
print(df12.shape)

df12=df12.drop('2021-01-30 13:00:00')

print(df2.shape)

df_1112_corr =df11.corrwith(df12.set_axis(df11.index, axis='index', copy=False)) # Correlation matrice of df1h with df2 changing the index name with the index name of dh1 to compare them
print(df_1112_corr)

df13=df9.resample('10D').mean()
df14=df10.resample('10D').mean()

print(df13.shape)
print(df14.shape)

df13=df13.drop('2020-12-31')
print(df13.shape)

df_1415_corr =df13.corrwith(df14.set_axis(df13.index, axis='index', copy=False)) # Correlation matrice of df1h with df2 changing the index name with the index name of dh1 to compare them
print(df_1415_corr)

# Comparing two dataframe of three months

df15=df['2020-12-01 00:00:00' : '2021-02-28 00:00:00']
df16=df['2021-03-01 00:00:00' : '2021-05-28 04:00:00']
print(df15.shape)
print(df16.shape)


df_1516_corr =df15.corrwith(df16.set_axis(df15.index, axis='index', copy=False)) # Correlation matrice of df1h with df2 changing the index name with the index name of dh1 to compare them
print(df_1516_corr)

df17=df15.resample('H').mean()
df18=df16.resample('H').mean()
print(df17.shape)
print(df18.shape)

df17=df17.drop('2020-12-01 12:00:00')
df17=df17.drop('2020-12-01 13:00:00')
df17=df17.drop('2020-12-01 14:00:00')
df17=df17.drop('2020-12-01 15:00:00')
df17=df17.drop('2020-12-01 16:00:00')
df17=df17.drop('2020-12-01 17:00:00')
df17=df17.drop('2020-12-01 18:00:00')
df17=df17.drop('2020-12-01 19:00:00')

print(df17.shape)

df_1718_corr =df17.corrwith(df18.set_axis(df17.index, axis='index', copy=False)) # Correlation matrice of df1h with df2 changing the index name with the index name of dh1 to compare them
print(df_1718_corr)

df19=df15.resample('D').mean()
df20=df16.resample('D').mean()
print(df19.shape)
print(df20.shape)

df19=df19.drop('2020-12-01')

print(df19.shape)

df_1920_corr =df19.corrwith(df20.set_axis(df19.index, axis='index', copy=False)) # Correlation matrice of df1h with df2 changing the index name with the index name of dh1 to compare them
print(df_1920_corr)

df21=df15.resample('10D').mean()
df22=df16.resample('10D').mean()
print(df21.shape)
print(df22.shape)



df_2122_corr =df21.corrwith(df22.set_axis(df21.index, axis='index', copy=False)) # Correlation matrice of df1h with df2 changing the index name with the index name of dh1 to compare them
print(df_2122_corr)

df23=df15.resample('M').mean()
df24=df16.resample('M').mean()
print(df23.shape)
print(df24.shape)



df_2324_corr =df23.corrwith(df24.set_axis(df23.index, axis='index', copy=False)) # Correlation matrice of df1h with df2 changing the index name with the index name of dh1 to compare them
print(df_2324_corr)


