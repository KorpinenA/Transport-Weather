import pandas as pd
from pathlib import Path
import numpy as np
from datetime import datetime


root = Path(__file__).resolve().parents[1]


def get_data_frame():
    dataF = pd.read_csv(f"{root}/data/data_forecast.csv", sep='\t', lineterminator='\n')
    dataO = pd.read_csv(f"{root}/data/data_observation.csv", sep='\t', lineterminator='\n')
    return dataF, dataO


def find_same_stations(dataF, dataO):
    siteF = dataF['station'][0:588]
    siteO = dataO['station'][0:1127]
    stations = []
    for i, sF in enumerate(siteF):
        if sF in siteO.values:
            stations.append(sF)
    return np.asarray(stations)


def nesting_stats(dataF):
    week = dataF.loc[(dataF['fctime'] >= 20170523000000) & (dataF['fctime'] < 20170601000000)]
    week_T_air_mean = np.nanmean(week['temp_2'])
    return week_T_air_mean


def get_probability_between(min, max, df):
    df = df.loc[(df['temp_2'] >= min) & (df['temp_2'] <= max)]
    T_road_prob = len(df['temp_r'].loc[df['temp_r'] <= 0])/len(df['temp_r'])
    return T_road_prob


def initialize_case(station, dataF, dataO):
    dataF = dataF.loc[dataF['station'] == station]
    dataO = dataO.loc[dataO['station'] == station]
    dataF = dataF.loc[dataF['fctime'] >= 20170601000000]
    dataF['fctime'] = pd.to_datetime(dataF['fctime'], format='%Y%m%d%H%M%S')
    dataO['time'] = pd.to_datetime(dataO['time'], format='%Y%m%d%H%M%S')
    return dataF, dataO


def remove_nan_index(df, var):
    index_2 = df[var].index[df[var].apply(np.isnan)]
    for i in index_2.values:
        df = df.drop(i)
    return df


def separate_season(season, dataF, dataO):
    seasonO = ''
    seasonF = ''
    if season == 'summer':
        seasonF = dataF.loc[(dataF['fctime'] >= datetime(2017,6,1,0,0,0)) & (dataF['fctime'] <= datetime(2017,8,31,0,0,0))
                            | (dataF['fctime'] >= datetime(2018,5,1,0,0,0))]
        seasonO = dataO.loc[(dataO['time'] >=  datetime(2017,6,1,0,0,0)) & (dataO['time'] <= datetime(2017,8,31,0,0,0))
                            | (dataO['time'] >= datetime(2018,5,1,0,0,0))]
    if season == 'autumn':
        seasonF = dataF.loc[(dataF['fctime'] >= datetime(2017,9,1,0,0,0)) & (dataF['fctime'] <= datetime(2017,11,30,0,0,0))]
        seasonO = dataO.loc[(dataO['time'] >= datetime(2017,9,1,0,0,0)) & (dataO['time'] <= datetime(2017,11,30,0,0,0))]
    if season == 'winter':
        seasonF = dataF.loc[(dataF['fctime'] >= datetime(2017,12,1,0,0,0)) & (dataF['fctime'] <= datetime(2018,3,1,0,0,0))]
        seasonO = dataO.loc[(dataO['time'] >= datetime(2017,12,1,0,0,0)) & (dataO['time'] <= datetime(2018,3,1,0,0,0))]
    if season == 'spring':
        seasonF = dataF.loc[(dataF['fctime'] > datetime(2018,3,1,0,0,0)) & (dataF['fctime'] <= datetime(2018,4,30,0,0,0))]
        seasonO = dataO.loc[(dataO['time'] > datetime(2018,3,1,0,0,0)) & (dataO['time'] <= datetime(2018,4,30,0,0,0))]
    return seasonF, seasonO


def calculate_average(data, length):
    j = 0
    average = []
    for i in range(0, len(data), length):
        if i > 0:
            a = np.nanmean(data[j:i])
            j = i
        if i >= len(data):
            a = np.nanmean(data[j:])
        if j > 0:
            average.append(a)
    return np.asarray(average)


def separate_day_night(dataF, dataO):
    warmin_F = dataF.loc[(dataF['fctime'].dt.hour >= 6) & (dataF['fctime'].dt.hour < 15)]
    warmin_O = dataO.loc[(dataO['time'].dt.hour >= 6) & (dataO['time'].dt.hour < 15)]

    cooling_F = dataF.loc[(dataF['fctime'].dt.hour >= 21) | (dataF['fctime'].dt.hour < 3)]
    cooling_O = dataO.loc[(dataO['time'].dt.hour >= 21) | (dataO['time'].dt.hour < 3)]
    return warmin_F, warmin_O, cooling_F, cooling_O


def average_hour(dataF, dataO, var):
    hourlyF_mean = []
    hourlyO_mean = []
    for i in range(0, 24, 1):
        hourF = dataF.loc[dataF['fctime'].dt.hour == i]
        hourlyF_mean.append(np.nanmean(hourF[var].values))
        hourO = dataO.loc[dataO['time'].dt.hour == i]
        hourlyO_mean.append(np.nanmean(hourO[var].values))
    return np.asarray(hourlyF_mean), np.asarray(hourlyO_mean)
