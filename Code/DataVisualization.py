import numpy as np

import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns
import sys

from datetime import datetime

# from sympy import true

# import pingouin as pg



print(plt.style.available)
plt.style.use("seaborn-v0_8")

plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams["axes.labelsize"] = 14


DataPath = "./Data/SteamGamesCleanedFinal_Modified.csv"

# DataPath = "./SteamGamesCleanedFinal.csv"

RawData = pd.read_csv(DataPath,encoding="ansi")

HeatMapResolution = 1000



def AllGameNumThroughTime():
    
    RawData["Release Date"] = pd.to_datetime(RawData["Release Date"],format='%d-%b-%y', errors='coerce')

    df_Date = RawData[RawData['Release Date'].dt.strftime('%d-%b-%y') == RawData['Release Date']]

    df_Date_Sorted = df_Date.sort_values("Release Date")

    Dates = df_Date_Sorted["Release Date"].values

    CurrentTime = datetime.now()

    # Dates = [dt for dt in Dates if dt <= CurrentTime]

    TimeList = pd.date_range(start = Dates[0], end = CurrentTime, periods=None, freq='D')

    Dates_np = np.array(Dates)

    # print(Dates_np[-10:-1 ])
    
    CountList = np.zeros(len(TimeList))

    for i, T in enumerate(TimeList):
        print(i)
        CountList[i] = np.sum(Dates_np < T)

    fig,ax = plt.subplots(figsize = (6,4.8),dpi=200,facecolor="w")

    ax.set_title("Number of games in total through time",fontweight='bold',fontsize = 20)
    ax.set_xlabel('Time',fontweight='bold')
    ax.set_ylabel('Number of games in total',fontweight='bold')

    ax.grid(zorder = 0)

    ax.plot(TimeList,CountList)
    plt.show()







if __name__ == "__main__":
    AllGameNumThroughTime()


