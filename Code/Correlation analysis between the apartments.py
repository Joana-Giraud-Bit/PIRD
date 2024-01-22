# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:42:27 2024

@author: joana
"""

import os
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

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
df = df[~df.isnull().any(axis=1)]  # remove the row with NaN value

df=df*3600
#print(df)

#Time-series analysis

df1=df['2020-12-07 00:00:00' : '2020-12-12 00:00:00']
#print(df1)
df1h = df1.resample("H").mean() 

df1h_corr = df1h.corr() # Correlation matrice of df1h
sn.heatmap(df1h_corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', fmt='.2f') #Creating a scale to visualize the correlation
plt.title('DHW correlation from 07/12 ~ 12/12/2020', fontsize=15) #Add a title to the figure
plt.show() #Plot the figure

df2=df['2020-12-07 00:00:00' : '2020-12-13 00:00:00']
df2h = df2.resample("H").mean() 
df2h_corr = df2h.corr()
sn.heatmap(df2h_corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', fmt='.2f')
plt.title('DHW consumption correlation from 07/12 ~ 13/12/2020', fontsize=15)
plt.show()

df3=df['2021-06-06 00:00:00' : '2021-06-11 00:00:00']
df3h = df3.resample("H").mean() 
df3h_corr = df3h.corr()
sn.heatmap(df3h_corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', fmt='.2f')
plt.title('DHW correlation from 06/06 ~ 11/06/2021', fontsize=15)
plt.show()

#Hour mean analysis

df4=df['2020-12-07 00:00:00' : '2020-12-17 00:00:00']
df4h = df4.resample("H").mean()
df4h = df4h.groupby(df4h.index.time).mean() #Get the mean values of the ten days to get an average on one day
#print(df4h)

f4h_max=df4h.max()
df4h_min=df4h.min()
df4h_standard_deviation=df4h.std()


df4h_minus_std=df4h-df4h_standard_deviation
#print(df4h_minus_std)
#To do: Mettre à 0 les valeurs négatives


df4h_plus_std=df4h+df4h_standard_deviation
#print(df4h_plus_std)

#Plot every mean values

ac= df4h.plot(xlabel='Hour', ylabel='DHW [l/h]')
ac.set_title('Hourly average value of DHW from 07/12 ~ 17/12/2020')
plt.show()


x=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ]) #x represents the hour of the day where the value are taken

#Plot the range of the apartment 25 with its standard deviation and mean value.
plt.plot(x,df4h['25-IECS'].to_numpy(), label='Apart 25', color='blue', ) #Plot the mean value for each apartment
plt.fill_between(x, df4h_minus_std['25-IECS'].to_numpy(), df4h_plus_std['25-IECS'].to_numpy(), color='cornflowerblue') #Plot the standard deviation bands

#Repeat it for each apartments
plt.plot(x,df4h['26-IECS'].to_numpy(), label='Apart 26',color='orange' ) 
plt.fill_between(x, df4h_minus_std['26-IECS'].to_numpy(), df4h_plus_std['26-IECS'].to_numpy(), color='bisque') 

plt.plot(x,df4h['27-IECS'].to_numpy(), label='Apart 27',color='green' ) #Plot the mean value for each apartment
plt.fill_between(x, df4h_minus_std['27-IECS'].to_numpy(), df4h_plus_std['27-IECS'].to_numpy(), color='lightgreen') 

plt.plot(x,df4h['34-IECS'].to_numpy(), label='Apart 34',color='red' ) 
plt.fill_between(x, df4h_minus_std['34-IECS'].to_numpy(), df4h_plus_std['34-IECS'].to_numpy(), color='lightcoral') 

plt.plot(x,df4h['35-IECS'].to_numpy(), label='Apart 35',color='purple' )
plt.fill_between(x, df4h_minus_std['35-IECS'].to_numpy(), df4h_plus_std['35-IECS'].to_numpy(), color='plum') 

plt.plot(x,df4h['36-IECS'].to_numpy(),label='Apart 36', color='sienna' ) 
plt.fill_between(x, df4h_minus_std['36-IECS'].to_numpy(), df4h_plus_std['36-IECS'].to_numpy(), color='sandybrown') 

plt.plot(x,df4h['63-IECS'].to_numpy(),label='Apart 63', color='hotpink' ) 
plt.fill_between(x, df4h_minus_std['63-IECS'].to_numpy(), df4h_plus_std['63-IECS'].to_numpy(), color='lightpink') 

plt.plot(x,df4h['64-IECS'].to_numpy(), label='Apart 64',color='grey' ) 
plt.fill_between(x, df4h_minus_std['64-IECS'].to_numpy(), df4h_plus_std['64-IECS'].to_numpy(), color='lightgrey') 

plt.plot(x,df4h['65-IECS'].to_numpy(), label='Apart 65',color='darkolivegreen' ) 
plt.fill_between(x, df4h_minus_std['65-IECS'].to_numpy(), df4h_plus_std['65-IECS'].to_numpy(), color='darkseagreen') 

plt.plot(x,df4h['67-IECS'].to_numpy(), label='Apart 67',color='cyan' ) 
plt.fill_between(x, df4h_minus_std['67-IECS'].to_numpy(), df4h_plus_std['67-IECS'].to_numpy(), color='lightcyan') 

plt.plot(x,df4h['9-IECS'].to_numpy(), label='Apart 9', color='gold' ) 
plt.fill_between(x, df4h_minus_std['9-IECS'].to_numpy(), df4h_plus_std['9-IECS'].to_numpy(), color='palegoldenrod') 

plt.legend()
plt.xlabel('Hour')
plt.ylabel('DHW [l/h]')
plt.title('Range of DHW of the apartments from 07/12 ~ 17/12/2020')
plt.show()

df4h_corr = df4h.corr()
sn.heatmap(df4h_corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', fmt='.2f')
plt.title('DHW correlation from 07/12 ~ 17/12/2020', fontsize=15)
plt.show()

df5=df['2020-12-08 00:00:00' : '2020-12-18 00:00:00']
df5h = df5.resample("H").mean()
df5h = df5h.groupby(df5h.index.time).mean() #Get the mean values of the ten days to get an average on one day
#print(df5h)
df5h_corr = df5h.corr()
sn.heatmap(df5h_corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', fmt='.2f')
plt.title('DHW correlation from 08/12 ~ 18/12/2020', fontsize=15)
plt.show()

df6=df['2021-06-07 00:00:00' : '2021-06-17 00:00:00']
df6h = df6.resample("H").mean()
df6h = df6h.groupby(df6h.index.time).mean() #Get the mean values of the ten days to get an average on one day
#print(df5h)
df6h_corr = df6h.corr()
sn.heatmap(df6h_corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', fmt='.2f')
plt.title('DHW correlation from 07/06 ~ 17/06/2021', fontsize=15)
plt.show()

df7=df['2021-06-08 00:00:00' : '2021-06-18 00:00:00']
df7h = df7.resample("H").mean()
df7h = df7h.groupby(df7h.index.time).mean() #Get the mean values of the ten days to get an average on one day
#print(df7h)
df7h_corr = df7h.corr()
sn.heatmap(df7h_corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', fmt='.2f')
plt.title('DHW correlation from 08/06 ~ 18/06/2021', fontsize=15)
plt.show()

# Morning and afternoon resample analysis _ 3 hours

df8=df['2020-12-07 00:00:00' : '2020-12-17 00:00:00']
df8h = df8.resample("3H").mean()
df8h = df8h.groupby(df8h.index.time).mean() #Get the mean values of the ten days to get an average on one day
#print(df8h)

ac1= df8h.plot(xlabel='Hour', ylabel='DHW [l/h]')
ac1.set_title('Hourly average value of DHW from 07/12 ~ 17/12/2020')
plt.show()

df8h_corr = df8h.corr()
sn.heatmap(df8h_corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', fmt='.2f')
plt.title('DHW correlation from 07/12 ~ 17/12/2020', fontsize=15)
plt.show()

df9=df['2020-12-08 00:00:00' : '2020-12-18 00:00:00']
df9h = df9.resample("3H").mean()
df9h = df9h.groupby(df9h.index.time).mean() #Get the mean values of the ten days to get an average on one day
#print(df9h)

df9h_corr = df9h.corr()
sn.heatmap(df9h_corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', fmt='.2f')
plt.title('DHW correlation from 08/12 ~ 18/12/2020', fontsize=15)
plt.show()

df10=df['2021-06-07 00:00:00' : '2021-06-17 00:00:00']
df10h = df10.resample("3H").mean()
df10h = df10h.groupby(df10h.index.time).mean() #Get the mean values of the ten days to get an average on one day
#print(df10h)

df10h_corr = df10h.corr()
sn.heatmap(df10h_corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', fmt='.2f')
plt.title('DHW correlation from 07/06 ~ 17/06/2021', fontsize=15)
plt.show()

df11=df['2021-06-08 00:00:00' : '2021-06-18 00:00:00']
df11h = df11.resample("3H").mean()
df11h = df11h.groupby(df11h.index.time).mean() #Get the mean values of the ten days to get an average on one day
#print(df11h)
df11h_corr = df11h.corr()
sn.heatmap(df11h_corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', fmt='.2f')
plt.title('DHW correlation from 08/06 ~ 18/06/2021', fontsize=15)
plt.show()