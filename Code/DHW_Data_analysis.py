#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:27:40 2021

@author: cghiaus
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def cm2inch(*tupl):
    """
    Transform centimeters to inches
    Used to set figure size
    """
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i / inch for i in tupl[0])
    else:
        return tuple(i / inch for i in tupl)


def files2df(file_type, sampling_time='10Min'):
    """
    Files from folder "../Data/" to DataFrame
    """
    # Get file names
    folder = "../Data/"
    files = os.listdir(folder)
    # Select file_type
    list_EC = [file for file in files if file_type in file]
    list_EC.sort()

    # Read and resample data at 10 min.
    data = {}
    for file in list_EC:
        df = pd.read_csv(folder + file)
        ts = df.set_index('0')['Value']     # DataFrame -> TimeSeries
        ts.index = pd.to_datetime(ts.index, unit='s')   # index to secondes
        ts = ts.resample(sampling_time).mean()     # resample
        data[file[:-4]] = ts                # file name (but not .extension)

    # Create dataframe
    df = pd.DataFrame(data)
    df = df[~df.isnull().any(axis=1)]       # get row that have no NaN

    # df['mean'] = df.mean(axis=1)            # add column 'mean'
    return(df)


def plot_time(df_e, df_w, mean=True, legend=False):
    """
    All measurements with a mean in read
    DataFrames selected

    - for apartments:
        >>> aparts = range(2)
        >>> plot_time(df_em.iloc[:, aparts], df_wm.iloc[:, aparts])

    - for period
        >>> start, end = '2021-06-01 00:00', '2021-06-04 00:00'
        >>> plot_time(df_em[start:end], df_wm[start:end])

    - period and apartments:
        >>> plot_time(df_em[start:end].iloc[:, aparts],
                       df_wm[start:end].iloc[:, aparts])
    """
    fig, axs = plt.subplots(nrows=2, ncols=1)
    ax = df_e.plot(ax=axs[0], color='b')
    '''
    if mean:
        ax = df_e.mean(axis=1).plot(ax=axs[0],
                                    linewidth=5.0, color='r',
                                    label='Mean')
    '''
    ax.set_xlabel('Time')
    ax.set_ylabel('Power [W]')
    ax.legend(loc='center left', bbox_to_anchor=(1, 1))

    ax = df_w.plot(ax=axs[1], sharex=ax, color='r')
    '''
    if mean:
        ax = df_w.mean(axis=1).plot(ax=axs[1],
                                    linewidth=5.0, color='r',
                                    label='Mean')
    '''
    ax.set_xlabel('Time')
    ax.set_ylabel('Flow rate [l/s]')
    ax.legend(loc='center left', bbox_to_anchor=(1, 1))
    
    # if legend:
    #     ax.legend(loc='center left', bbox_to_anchor=(1, 1))
    # else:
    #     ax.legend([])
    return(fig, axs)


def plot_box(df_e, df_w, mean=True, q2=False, q3=False):
    """
    Parameters
    ----------
    df_e : DataFrame
        Electrical power.
    df_w : DataFrame
        Water flow rate.
    mean : logical, optional
        Inclused column of the means of row of DataFrame.
        The default is True.
    q2 : lgical, optional
        Draws lines between the quantile 0.50 (quartle Q2).
        The default is False.
    q3 : logical, optional
        Draws lines between the quantile 0.75 (quartle Q3).
        The default is False.

    Returns
    -------
    ax : curent axis
    """
    fig, axs = plt.subplots(nrows=2, ncols=1)

    if mean:
        df_e['mean'] = df_e.mean(axis=1)
        df_w['mean'] = df_w.mean(axis=1)

    ax = df_e.plot(kind='box', ax=axs[0],
                   xlabel='Time', ylabel='Power [W]')

    ax = df_w.plot(kind='box', ax=axs[1], sharex=ax,
                   xlabel='Time', ylabel='Flow rate [l/s]')

    if q2:
        q2 = df_e.quantile()
        axs[0].plot(np.arange(len(q2)) + 1, q2, color='r')
        q2 = df_w.quantile()
        axs[1].plot(np.arange(len(q2)) + 1, q2, color='r')

    if q3:
        q3 = df_e.quantile(q=0.75)
        axs[0].plot(np.arange(len(q3)) + 1, q3, color='b')
        q3 = df_w.quantile(q=0.75)
        axs[1].plot(np.arange(len(q3)) + 1, q3, color='b')

    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_xlabel('Apartment')
    # return(ax)
    return(fig, axs)


def plot_hist(df_em, df_wm, mean=True, legend=False):
    fig, axs = plt.subplots(nrows=2, ncols=1)

    # Electric power
    df_em_mean = df_em.groupby(df_em.index.time).mean()
    ax = df_em_mean.plot(kind='bar', ax=axs[0],
                         xlabel='Time', ylabel='Power [W]')
    if mean:
        df_em_mean = df_em.mean(axis=1)
        df_em_mean = df_em_mean.groupby(df_em_mean.index.time).mean()
        ax = df_em_mean.plot(kind='bar', ax=axs[0],
                             xlabel='Time', ylabel='Power [W]', alpha=0.33,
                             label='Mean')
    ax.set_xticklabels(ax.get_xticks())
    ax.legend(loc='center left', bbox_to_anchor=(1, 1))

    # Water flow rate
    df_wm_mean = df_wm.groupby(df_wm.index.time).mean()
    ax = df_wm_mean.plot(kind='bar', ax=axs[1],
                         xlabel='Time', ylabel='Power [W]')
    if mean:
        df_wm_mean = df_wm.mean(axis=1)
        df_wm_mean = df_wm_mean.groupby(df_wm_mean.index.time).mean()

        ax = df_wm_mean.plot(kind='bar', ax=axs[1], sharex=ax,
                             xlabel='Time', ylabel='Flow rate [l/s]',
                             alpha=0.33, label='Mean')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.set_xlabel('Hour of the day')
    ax.set_xticklabels(ax.get_xticks())
    ax.legend(loc='center left', bbox_to_anchor=(1, 1))
    
    # if legend:
    #     ax.legend(loc='center left', bbox_to_anchor=(1, 1))
    # else:
    #     ax.legend([])
    return(fig, axs)


# # Get data
# df_e = files2df(file_type='-EC', sampling_time='5Min')
# df_e.drop('8--EC', inplace=True, axis=1)    # apart. '8' not in IECS
# df_w = files2df(file_type='IECS', sampling_time='10Min')

# plt.rcParams["figure.figsize"] = (8, 6)                         # inch
# plt.rcParams["figure.figsize"] = cm2inch(8 * 2.54, 6 * 2.54)    # cm
# To reset
# plt.rcParams["figure.figsize"] = plt.rcParamsDefault["figure.figsize"]

# # All measurements
# df_em, df_wm = df_e, df_w
# plot_time(df_em, df_wm, legend=True)
# # Plot selected apartments
# aparts = range(2)
# plot_time(df_em.iloc[:, aparts], df_wm.iloc[:, aparts])
# # Plot selected time interval
# start, end = '2021-06-01 00:00', '2021-06-04 00:00'
# plot_time(df_em[start:end], df_wm[start:end])
# # Plot selected time interval and apartment
# fig, axs = plot_time(df_em[start:end].iloc[:, aparts],
#                      df_wm[start:end].iloc[:, aparts],
#                      mean=False, legend=True)
# df_em[start:end].mean(axis=1).plot(ax=axs[0],
#                                    linewidth=3.0, color='r', alpha=0.33,
#                                    label='Mean')
# df_wm[start:end].mean(axis=1).plot(ax=axs[1],
#                                    linewidth=3.0, color='r', alpha=0.33,
#                                    label='Mean')

# # Hourly  consumption for each apartment
# df_em = df_e.resample("H").mean()
# df_em = df_em.groupby(df_em.index.time).mean()
# df_wm = df_w.resample("H").mean()
# df_wm = df_wm.groupby(df_wm.index.time).mean()
# plot_box(df_em, df_wm)

# # Hourly distributio of consumption over 24h for all apartments
# df_em = df_e.resample("H").mean()
# df_em = df_em.groupby(df_em.index.time).mean().T

# df_wm = df_w.resample("H").mean()
# df_wm = df_wm.groupby(df_wm.index.time).mean().T


# fig, axs = plot_box(df_em, df_wm, mean=False, q2=True, q3=True)
# axs[1].set_xticklabels(axs[1].get_xticks())
# axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=0, )
# axs[1].set_xlabel('Hour of the day')


# Histograme of data grouped by hours
# df_em = df_e.resample("H").mean()
# df_wm = df_w.resample("H").mean()

# plot_hist(df_em, df_wm, mean=True, legend=True)
