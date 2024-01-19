# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:23:52 2024

@author: joana
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Average DHW used per day

folder = r"../Data/DataVillefontaine/"
files = os.listdir(folder)
list_IECS = [file for file in files if '-IECS' in file]
list_IECS.sort()

data = {} #Creation of a dictionary
for file in list_IECS:
    df = pd.read_csv(folder + file)
    ts = df.set_index('0')['Value']     # DataFrame -> TimeSeries
    ts.index = pd.to_datetime(ts.index, unit='s')   # index to secondes
    ts = ts.resample("10Min").mean()    # resample 10 min
    data[file[:-4]] = ts                # file name (but not .extension)
    
df = pd.DataFrame(data)
df = df[~df.isnull().any(axis=1)]       # Remove the row with Nan Value

df['mean'] = df.mean(axis=1)  
df=df*3600
#print(df)

df1h = df.resample("H").mean() #Resample the data for one hour
df1h = df1h.groupby(df1h.index.time).mean() #Work out the mean values of every values for the different hours
av = np.sum(df1h, axis=0) #Sum all the mean values of one apartment

ax = av.plot(kind='bar', xlabel='Apartments', ylabel='Flow rate [l/day]')
ax.set_title('Average electrical consumption of the apartment per day')
plt.show()

ac=df1h.plot(xlabel='Hour', ylabel='DHW consumption [l/h]')
ac.set_title('Average DHW consumption of the apartments per day')
plt.show()

# Average electrical consumption of the apartments of the city of Villefontaine

list_EC = [file for file in files if '-EC' in file]
list_EC.sort()

dataBis = {} #Creation of a dictionary
for file in list_EC:
    df = pd.read_csv(folder + file)
    ts = df.set_index('0')['Value']     # DataFrame -> TimeSeries
    ts.index = pd.to_datetime(ts.index, unit='s')   # index to secondes
    ts = ts.resample("10Min").mean()    # resample 10 min
    dataBis[file[:-4]] = ts                # file name 
    
df1 = pd.DataFrame(dataBis)
df1 = df1[~df1.isnull().any(axis=1)]       # Remove the row with Nan Value

df1['mean'] = df1.mean(axis=1)

df2h = df1.resample("H").mean() #Resample the data for one hour
#print(df2h)
df2h = df2h.groupby(df2h.index.time).mean() #Work out the mean values of every values for the different hours
#print(df2h)
av1 = np.sum(df2h, axis=0) #Sum all the mean values of one apartment
#print(av1)

ax1= av1.plot(kind='bar', xlabel='Apartments', ylabel='Electrical consumption [W per day]')
ax1.set_title('Average electrical consumption of the apartment per day.')
plt.show()

ac1=df2h.plot(xlabel='Hour', ylabel='Electrical consumption [W]')
ac1.set_title('Average electrical consumption of the apartments per day')
plt.show()