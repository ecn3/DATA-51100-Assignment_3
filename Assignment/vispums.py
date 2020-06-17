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

# TODO Create a figure with 2x2 subplots

# TODO Upper Left Subplot - Pie Chart contaning num of household records for the different values of HHL Column
# > No wedge labels, must have legend in upper left corner, correctly rotated

# TODO Upper Right Subplot - Histogram of HINCP Column with KDE plot superimposed
# > Use log scale on the x-axis with log spaced bins [np.logspace]


# TODO Lower Left Subplot - Bar Chart of number of households in thousands for each VEH value[drop NaN]
# > Use WGTP value to count how many households are in each row then divide sum by 1000 to get households in thousands

# TODO Lower Right Subplot - Scatter plot of TAXP against VALP
# > convert TAXP into numeric values, use lower bounds interval, Use WGTP as the size of each marker, 'o' as marker type, and MRGP as the color value, add colorbar

# TODO Display figure

# TODO Save figure to file 'pums.png'

