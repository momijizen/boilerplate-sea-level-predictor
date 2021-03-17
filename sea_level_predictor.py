import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', index_col=0)

    # Create scatter plot
    plt.figure(figsize=(14,6))
    plt.scatter(df.index, df['CSIRO Adjusted Sea Level'], alpha=0.5)

    # Create first line of best fit
    res = linregress(df.index, df['CSIRO Adjusted Sea Level'])
    year_1880_2050 = np.concatenate((df.index, np.arange(2014,2050)), axis=0)
    plt.plot(year_1880_2050 , res.intercept + res.slope*year_1880_2050, 'r', label='fitted line 1')

    # Create second line of best fit
    res2 = linregress(df.loc['200':].index, df.loc['200':]['CSIRO Adjusted Sea Level'])
    year_2000_2050 = np.concatenate((df.loc['200':].index, np.arange(2014,2050)), axis=0)
    plt.plot(year_2000_2050 , res2.intercept + res2.slope*year_2000_2050, 'g', label='fitted line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()