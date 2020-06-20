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
pums_hist.plot(kind='kde',ax=axs[0,1], color ='k',linestyle='--')

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
def get_taxp_mapping_dict():
    taxp_dict = {}
    taxp_dict[1] = np.NaN
    taxp_dict[2] = 1
    taxp_dict[63]=5500
    counter = 50
    for key in range (3,23):
        taxp_dict[key]=counter
        counter += 50
    for key in range (23,63):
        taxp_dict[key] = counter+50
        counter += 100
    counter = counter - 50
    for key in range (64,69):
        taxp_dict[key] = counter+1000
        counter += 1000
    return taxp_dict

taxp_dict = get_taxp_mapping_dict()
for y in range(1,69):
    pums_scatter['TAXP'] = pums_scatter['TAXP'].replace(to_replace= y, value= taxp_dict[y]) 

# Create colormap
cmap = mpl.colors.LinearSegmentedColormap.from_list("", ["lightblue","white","pink"])
# Graph Data
scatter_data = axs[1,1].scatter(pums_scatter.VALP,pums_scatter.TAXP,marker='o',s=pums_scatter.WGTP/10, c=pums_scatter.MRGP,cmap='seismic',alpha=0.15)
axs[1,1].set_xlim(0,1200000)
axs[1,1].ticklabel_format(style='plain')
# Add color bar and label
cb = plt.colorbar(scatter_data, format='%li')
# Set color bar label
cb.set_label(label='First Mortage Payment(Monthly $)',size=6)
# Save figure to file 'pums.png'
fig.set_size_inches(14, 7)
plt.savefig('pums.png', dpi=100) 

# Display figure
plt.show()