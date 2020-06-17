# Nathanel Fawcett | Christian Nelson | Lawrence Tiller
# 6/21/2020
# DATA-51100-002, SUMMER 2020
# PROGRAMMING ASSIGNMENT #5 vispums

# Import Statements
#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from pandas import DataFrame
import numpy as np


df=pd.read_csv('ss13hil.csv') #load csv

fig, axs = plt.subplots(2, 2)
fig.set_size_inches(20,16)


# PIE CHART UPPER LEFT
pie_key=['English','Spanish','Other Indo-European','Asian and Pacific Island languages','Other']
axs[0,0].set_title('Household Languages')
axs[0,0].pie(df.HHL.value_counts().dropna(),startangle=240)
axs[0,0].legend(pie_key,loc="upper left")
axs[0,0].set(ylabel='HHL')

# TODO Upper Right Subplot - Histogram of HINCP Column with KDE plot superimposed
# > Use log scale on the x-axis with log spaced bins [np.logspace]
x=df.HINCP.dropna().value_counts()
axs[0,1].set_title('Distribution of Household Income')
axs[0,1].hist(x,bins=np.logspace(1,7),facecolor='green',alpha=.50)
axs[0,1].set(xlabel='Household Income($)- Log Scaled',ylabel='Density')
axs[0,1].set_xscale("log")
axs[0,1].grid(linestyle='dotted')

# TODO Lower Left Subplot - Bar Chart of number of households in thousands for each VEH value[drop NaN]
# > Use WGTP value to count how many households are in each row then divide sum by 1000 to get households in thousands
axs[1,0].set_title('Vehicles Available in Households')
axs[1,0].bar(df.groupby('VEH').WGTP.mean()/1000,df.VEH.value_counts().dropna(),facecolor='red')
axs[1,0].set(xlabel='# of Vehicles',ylabel='Thousands of Households')


# TODO Lower Right Subplot - Scatter plot of TAXP against VALP
# > convert TAXP into numeric values, use lower bounds interval, Use WGTP as the size of each marker, 'o' as marker type, and MRGP as the color value, add colorbar
axs[1,1].set_title('Property Taxes vs Property Values')
axs[1,1].scatter(df.VALP, df.TAXP)
axs[1,1].set(xlabel='Property Values',ylabel='Taxes')


#save
plt.savefig('pums.png', dpi=None)