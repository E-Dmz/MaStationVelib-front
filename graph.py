import matplotlib.pyplot as plt
import seaborn as sns

def plot_ax_bikes_and_docks(ax, df):
    
    plt.sca(ax)
    sns.lineplot(data=df, x='datetime', y='bikes', color='green', label='vélos disponibles')
    sns.lineplot(data=df, x='datetime', y='park', color='purple', label='places disponibles')
    
    plt.xlabel('')
    plt.ylabel('')
    plt.legend()
    locs, labels = plt.xticks()
    plt.xticks(locs, [f"{i}:00" for i in range(0,24,3)] + ['0:00'], rotation=45, ha='right')