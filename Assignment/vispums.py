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


# Load ss13hil.csv into a DATAFRAME
pums_dataframe = pd.read_csv('ss13hil.csv')

# Create a figure with 2x2 subplots
fig, axs = plt.subplots(2, 2)

# Set size of figure for display
fig.set_size_inches(20,20)

# Upper Left Subplot - Pie Chart contaning num of household records for the different values of HHL Column
# TODO fix circle so not oblong
pie_key=['English','Spanish','Other Indo-European','Asian and Pacific Island languages','Other']
axs[0,0].set_title('Household Languages')
axs[0,0].pie(pums_dataframe.HHL.value_counts().dropna(),startangle=240)
axs[0,0].legend(pie_key,loc="upper left")
axs[0,0].set(ylabel='HHL')

# Upper Right Subplot - Histogram of HINCP Column with KDE plot superimposed
# TODO fix y axis lables, add --k lines, add data after 10^3
x = pums_dataframe.HINCP.dropna().value_counts()
axs[0,1].set_title('Distribution of Household Income')
axs[0,1].hist(x,bins=np.logspace(1,7),facecolor='green',alpha=.50)
axs[0,1].set(xlabel='Household Income($)- Log Scaled',ylabel='Density')
axs[0,1].set_xscale("log")
axs[0,1].grid(linestyle='dotted')

# TODO Lower Left Subplot - Bar Chart of number of households in thousands for each VEH value[drop NaN]
# > Use WGTP value to count how many households are in each row then divide sum by 1000 to get households in thousands

# TODO Lower Right Subplot - Scatter plot of TAXP against VALP
# > convert TAXP into numeric values, use lower bounds interval, Use WGTP as the size of each marker, 'o' as marker type, and MRGP as the color value, add colorbar

# TODO Display figure
plt.show()

# TODO Save figure to file 'pums.png'

