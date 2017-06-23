import pandas as pd

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})
#load data
def read_header(f_name):
    """read head to find where data starts"""
    with open(f_name, 'r', encoding='ISO-8859-1') as f:
        # if this breaks look for different encoding and write try block
        _ = f.readline()
        line = f.readline().rstrip()
        line_nb = int(line.split(':')[1])
    return line_nb

def cv_data_load(f_name):
    """load the data! calling read_header to find which rows to skip"""
    line_nb = read_header(f_name)
    return pd.read_csv(f_name, skiprows=line_nb-1, delimiter='\t')

def plot_data(df, ref='SCE', cycle=2, ax=None):
    """plot the data
    cycle = 'all' to plot all use (eg. for polymerizations ) or if data frame
    is already cut up
    ax=None will make new graph, ax=ax will plot data on the same plot assuming
     that plot generated using ax = plot_data(df) when making the first graph"""

    if type(cycle) not in [list, tuple]:
         cycle = [cycle]
    if ax is None:
        fig, ax = plt.subplots(1, 1)
        ax.set_xlabel(' E / V vs ' + ref)
        ax.set_ylabel(' I / mA')
    if cycle  == 'all':
        # Set up x and y values
        x = df.loc[:, 'Ewe/V']
        y = df.loc[:, '<I>/mA']
    if type(cycle) == list:
        x = df.loc[df['cycle number'].isin(cycle), 'Ewe/V']
        y = df.loc[df['cycle number'].isin(cycle), '<I>/mA']

    # else:
    #     # Get indices for cycle of interest
    #     inds = df['cycle number'] == cycle
    #     # Set up x and y values
    #     x = df.loc[inds, 'Ewe/V']
    #     y = df.loc[inds, '<I>/mA']
    # Populate plot
    ax.plot(x, y)

    return ax

#To correct for the reference (like from vs SCE to vs NHE) do something like following
    # df_cut['Ewe/V'] -= 0.5
#similar can be done to make stacks of CVs
#
