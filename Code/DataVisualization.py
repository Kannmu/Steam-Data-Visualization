from math import sin
from msilib import Feature
import numpy as np

import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns
import sys

from scipy.optimize import curve_fit
from datetime import datetime
import json

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

def TypeDistribution():
    Tags = df_Date_Sorted["Popular Tags"].values
    
    # Features = df_Date_Sorted["Game Features"].values
    
    Tags = []
    # Features = []

    TagName = []
    # FeatureName = []

    for i,Value in df_Date_Sorted.iterrows():
        print(i)
    
        try:
            Temp = eval(Value["Popular Tags"])
            for i in Temp:
                if(len(i)>1):
                    if(i not in TagName):
                        TagName.append(i)
                    Tags.append(i)

            # Temp = eval(Value["Game Features"])
            # for i in Temp:
            #     if(len(i)>1):
            #         if(i not in FeatureName):
            #             FeatureName.append(i)
            #         Features.append(i)
        except:
            print("Wrong Data")
            # pass
    print(TagName)
    # print(FeatureName)

    TagCount = np.zeros(len(TagName))
    # FeatureCount = np.zeros(len(FeatureName))


    for i,v in enumerate(Tags):
        TagCount[TagName.index(v)] += 1
    
    # for i,v in enumerate(Features):
        # FeatureCount[FeatureName.index(v)] += 1


    print(TagName[np.argmax(TagCount)])
    # print(FeatureName[np.argmax(FeatureCount)])

    TagSortIndex = np.argsort(TagCount)
    # FeatureSortIndex = np.argsort(FeatureCount)

    print(TagCount[TagSortIndex[-3:]])

    ax.set_title("Number of tag occurrences",fontweight='bold',fontsize = 20)
    ax.set_xticks([])
    ax.set_yticks([])

    # ax.set_xlabel('Tag',fontweight='bold')
    # ax.set_ylabel('Number of games in total',fontweight='bold')

    ax.grid(zorder = 0)

    FirstTenElementIndex = TagSortIndex[-10:]

    FirstTenElement  = []
    for i in FirstTenElementIndex:
        FirstTenElement.append(TagName[int(i)])

    FirstTenElementCount = TagCount[FirstTenElementIndex]
    
    Y = np.random.randn((10))

    ax.set_xlim([-1,12])
    ax.set_ylim([np.min(Y)-0.2,np.max(Y)+0.2])


    plt.scatter(FirstTenElement, Y,  cmap='coolwarm',c = FirstTenElementCount,s = 0.06* FirstTenElementCount,alpha  = 0.7)

    for i , e in enumerate(FirstTenElement):
        plt.text(FirstTenElement[i], Y[i],s = e,verticalalignment="center",horizontalalignment="center",fontsize = 14*FirstTenElementCount[i]/36587)

    plt.colorbar()

def AllGameNumThroughTime():

    Dates = df_Date_Sorted["Release Date"].values

    CurrentTime = datetime.now()

    StartTime = datetime(year=2002,month=1,day=1)
    # Dates = [dt for dt in Dates if dt <= CurrentTime]

    TimeList = pd.date_range(start = StartTime, end = CurrentTime, periods=None, freq='D')

    Dates_np = np.array(Dates)

    # print(Dates_np[-10:-1 ])
    
    CountList = np.zeros(len(TimeList))

    for i, T in enumerate(TimeList):
        print(i)
        CountList[i] = np.sum(Dates_np < T)

    

    ax.set_title("Number of games in total through time",fontweight='bold',fontsize = 20)
    ax.set_xlabel('Time',fontweight='bold')
    ax.set_ylabel('Number of games in total',fontweight='bold')

    ax.grid(zorder = 0)

    ax.plot(TimeList,CountList)


if __name__ == "__main__":
    
    fig,ax = plt.subplots(figsize = (6,4.8),dpi=200,facecolor="w")

    RawData["Release Date"] = pd.to_datetime(RawData["Release Date"],format='%d-%b-%y', errors='coerce')

    df_Date = RawData[RawData['Release Date'].dt.strftime('%d-%b-%y') == RawData['Release Date']]

    df_Date_Sorted = df_Date.sort_values("Release Date")

    # AllGameNumThroughTime()

    TypeDistribution()

    plt.show()

