import requests
import pandas as pd
import matplotlib.pyplot as plt
from graph import plot_ax_bikes_and_docks

import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')

API_URL = 'https://velibapi-hi7so7se7a-ew.a.run.app/day-station'

def plot_day(code_station, day):
    # Call API
    query = {
            'code_station': code_station,
            'day': day
        }
    response = requests.get(API_URL, params=query).json()

    # Make DF to plot
    df = pd.DataFrame(response)
    df['datetime'] = pd.to_datetime(df.datetime)
    df.set_index('datetime', inplace=True)

    # Plot lines
    ax = plt.subplot()
    plot_ax_bikes_and_docks(ax, df)
    
    plt.title(f"Station n°{code_station} - {day.strftime('%A %d/%m/%Y')}")
    fig = plt.gcf()
    return fig