# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:18:48 2024

@author: joana
"""

import matplotlib.pyplot as plt
import DHW_Data_analysis as data #Made by Christian Ghiaus

plt.rcParams["figure.figsize"] = (8, 6)                         # inch
plt.rcParams["figure.figsize"] = data.cm2inch(8 * 2.54, 6 * 2.54)    # cm

fig_no = 0   # figure number

#Get the data with a resample for 10Min + Remove Nan values
df_e = data.files2df(file_type='9-EC', sampling_time='10Min')
df_w = data.files2df(file_type='9-IECS', sampling_time='10Min')
df_em, df_wm= df_e, df_w

# Defining the period of visualization giving the departure date to the arrival date
start, end = '2020-12-07 00:00', '2020-12-12 00:00'

#Resampling for an hour analysis
df_em=df_e.resample("H").mean()
df_wm=df_w.resample("H").mean()

 
#Plot the hourly values from the starting date to the end one for the apartment
data.plot_time(df_em[start:end], df_wm[ start:end], legend='True')
plt.show()
