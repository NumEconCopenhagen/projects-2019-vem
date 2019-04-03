import pydst
Dst = pydst.Dst(lang='en')
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import ipywidgets as widgets

Dst.get_data(table_id = 'NKN1')
Dst.get_variables(table_id = 'NKN1')
df = Dst.get_data(table_id = 'NKN1', variables = {'TRANSAKT':['B1GQK'],'PRISENHED':['LKV_M'],'SÆSON':['Y'],'TID':['*']})
df

df1 = df.drop('TRANSAKT',1)
df2 = df1.drop('PRISENHED',1)
df3 = df2.drop('SÆSON',1)
df3

time = df3['TID']
gdp  = df3['INDHOLD']

gdp.replace('..',np.nan, inplace=True)
gdp.dropna(inplace=True)
gdp1 = gdp.iloc[:].astype(float)

def RollingMean(X):
    plt.figure(figsize=(14,7))
    plt.locator_params(which='x', tight=True, nbins=10)
    plt.xlabel('Year and quarter', size=18)
    plt.ylabel('GDP', size=18)
    plt.plot(time[4:],gdp1.rolling(window=X, center=True).mean(), label='GDP, moving average (X periods)')
    plt.plot(time[4:], gdp1, label='GDP, observed')
    plt.title('GDP - Observed and Moving Average', size=25)
    plt.legend(loc='upper left')
    plt.xticks(time[4:], rotation='vertical')
    plt.locator_params(axis='x', nbins=len(time[4:])/2)
widgets.interact(RollingMean, X=widgets.IntSlider(min=0,max=12,step=1,value=6))

gdp1.rolling(X, center=True).mean()
