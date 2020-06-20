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

# Adjust hspace for proper veiwing
fig.subplots_adjust(hspace=0.32)

# Upper Left Subplot - Pie Chart contaning num of household records for the different values of HHL Column
pie_key=['English','Spanish','Other Indo-European','Asian and Pacific Island languages','Other']
axs[0,0].set_title('Household Languages', fontsize=8)
axs[0,0].pie(pums_dataframe.HHL.value_counts().dropna(),startangle=242)
axs[0,0].legend(pie_key,loc=2, fontsize=8)
axs[0,0].set_ylabel('HHL', fontsize=8)
axs[0,0].axis('equal')

#  Upper Right Subplot - Histogram of HINCP Column with KDE plot superimposed
# Set the title
axs[0,1].set_title('Distribution of Household Income', fontsize=8)
# Set the x label
axs[0,1].set_xlabel('Household Income($)- Log Scaled', fontsize=8)
# Set the y label
axs[0,1].set_ylabel('Density', fontsize=8)
# Get Data
pums_hist = pums_dataframe.HINCP.dropna()
# Create log spaced bins
bins=np.logspace(1,7,100)
# Set x scale
axs[0,1].set_xscale('log')
# Plot data
axs[0,1].hist(pums_hist,bins,density=True,facecolor='green',alpha=.5)
# KDE plot superimposed
pums_hist.plot(kind='kde',ax=axs[0,1], color ='Black',linestyle='--')

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
# Set the title
axs[1,1].set_title('Property Taxes vs Property Values', fontsize=8)
# Set the x label
axs[1,1].set_xlabel('Property Values($)', fontsize=8)
# Set the y label
axs[1,1].set_ylabel('Taxes($)', fontsize=8)
# Get data
pums_scatter = pums_dataframe[['TAXP','VALP','WGTP','MRGP']].dropna()
# Convert TAXP using interval
taxp_conversions = pd.Series([None, 1,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,
1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,
3400,3500,3600,3700,3800,3900,4000,4100,4200,4300,4400,4500,4600,4700,4800,4900,500,5500,6000,7000,8000,900,10000 ])
for y in range(1,69):
    pums_scatter = pums_scatter.replace(to_replace= y, value= taxp_conversions[y-1])     
# Create colormap
cmap = mpl.colors.LinearSegmentedColormap.from_list("", ["lightblue","white","pink"])
# Graph Data
scatter_data = axs[1,1].scatter(pums_scatter.VALP,pums_scatter.TAXP,marker='o',s=pums_scatter.WGTP/200, c=pums_scatter.MRGP,cmap=cmap)
axs[1,1].set_xlim(0,1200000)
# Add color bar and label
cb = plt.colorbar(scatter_data)
# Set color bar label
cb.set_label(label='First Mortage Payment(Monthly $)',size=6)
# Save figure to file 'pums.png'
plt.savefig('pums.png', dpi=300) 

# Display figure
plt.show()