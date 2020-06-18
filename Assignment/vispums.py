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

# Upper Left Subplot - Pie Chart contaning num of household records for the different values of HHL Column
# TODO fix circle so not oblong
pie_key=['English','Spanish','Other Indo-European','Asian and Pacific Island languages','Other']
axs[0,0].set_title('Household Languages')
axs[0,0].pie(pums_dataframe.HHL.value_counts().dropna(),startangle=240)
axs[0,0].legend(pie_key,loc="upper left")
axs[0,0].set(ylabel='HHL')

#  Upper Right Subplot - Histogram of HINCP Column with KDE plot superimposed
# Me TODO fix y axis lables, add --k lines, add data after 10^3, fix lower label
# Set the title
axs[0,1].set_title('Distribution of Household Income', fontsize=8)
# Set the x label
axs[0,1].set_xlabel('Household Income($)- Log Scaled', fontsize=8)
# Set the y label
axs[0,1].set_ylabel('Density', fontsize=8)

# Lower Left Subplot - Bar Chart of number of households in thousands for each VEH value[drop NaN]
# Set the title
axs[1,0].set_title('Vehicles Available in Households', fontsize=8)
# Set the x label
axs[1,0].set_xlabel('# of Vehicles', fontsize=8)
# Set the y label
axs[1,0].set_ylabel('Thousands of Households', fontsize=8)
# Get data
pums_bar = pums_dataframe.groupby('VEH')['WGTP'].sum()/1000
# Display Data
axs[1,0].bar(pums_bar.index,pums_bar.values,facecolor='red')

# Lower Right Subplot - Scatter plot of TAXP against VALP
# Me TODO fix x and y axis, fix saturation, add color bar, add right label, fix upper label, fix data


# Display figure
plt.show()

# TODO Save figure to file 'pums.png'
# plt.savefig('pums.png', dpi=None) creates blank file
