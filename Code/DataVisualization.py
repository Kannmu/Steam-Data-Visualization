from ast import Num
from msilib import Feature
import numpy as np

import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns
import sys


from datetime import datetime
import json

# from sympy import true

# import pingouin as pg


print(plt.style.available)
plt.style.use("seaborn-v0_8")

plt.rcParams["font.family"] = ["Times New Roman"]
plt.rcParams["axes.labelsize"] = 14

DataPath = "./Data/SteamGamesCleanedFinal_Modified.csv"

# DataPath = "./SteamGamesCleanedFinal.csv"

RawData = pd.read_csv(DataPath, encoding="ansi")


def Developer():
    data = RawData["Developer"].values

    DevName = []

    

    for i,v in enumerate(data):
        if(type(v) != type("")):
            continue

        if(v not in DevName and len(v) > 1 and len(v) < 20 and "?" not in v):
            print(i,v)
            DevName.append(v)
    
    NameCount = np.zeros(len(DevName))

    for i,v in enumerate(data):
        if(v in DevName):
            print(v)
            NameCount[DevName.index(v)] += 1



    ax.set_title("Number of games per developer", fontweight="bold", fontsize=20)
    # ax.set_xticks([])
    ax.set_yticks([])

    # ax.set_xlabel('Tag',fontweight='bold')
    # ax.set_ylabel('Number of games in total',fontweight='bold')

    ax.grid(zorder=0)

    DevSortIndex = np.argsort(NameCount)

    FirstTenElementIndex = DevSortIndex[-10:]

    FirstTenElement = []
    for i in FirstTenElementIndex:
        FirstTenElement.append(DevName[int(i)])

    print(FirstTenElement)
    print(len(DevName))

    FirstTenElementCount = NameCount[FirstTenElementIndex]

    # Y = np.random.randn((10))
    Y = FirstTenElementCount

    # ax.set_xlim([-1, 12])
    ax.set_ylim([np.min(Y) - 20, np.max(Y) + 20])

    plt.scatter(
        FirstTenElement,
        Y,
        cmap="coolwarm",
        c = FirstTenElementCount,
        s = 5*FirstTenElementCount,
        alpha=0.7,
    )

    for i, e in enumerate(FirstTenElementCount):
        plt.text(
            FirstTenElement[i],
            Y[i],
            s=int(e),
            verticalalignment="center",
            horizontalalignment="center",
            fontsize=14 * FirstTenElementCount[i] / 150
        )
    plt.xticks(rotation=90)
    plt.colorbar()
            


def Review():
    
    # ReviewName = ["Overwhelmingly Positive","Very Positive","Positive","Mostly Positive","Mixed","Mostly Negative","Negative","Very Negative","Overwhelmingly Negative"]

    # ReviewCountList = [0]*9
    # df = df_Date_Sorted["All Reviews Summary"]
    
    # for i,v in enumerate(df):
    #     # print(i,v)
    #     if(v in ReviewName):
    #         print(i,v)
    #         ReviewCountList[ReviewName.index(v)] += 1

    # print(ReviewCountList)

    # ax.set_title(
    #     "Number of reviews in total", fontweight="bold", fontsize=20
    # )
    # ax.set_xlabel("Review Level", fontweight="bold")
    # ax.set_ylabel("Number", fontweight="bold")
    # plt.xticks(rotation=90)
    # ax.grid(zorder=0)

    # plt.bar(ReviewName, ReviewCountList)

    # for i,v in enumerate(ReviewCountList):
    #     plt.text(ReviewName[i],v,str(v),verticalalignment="bottom",
    #         horizontalalignment="center")

    df = df_Date_Sorted["All Reviews Number"]
    # print(df[0])
    ReviewDisList = []
    for i,v in enumerate(df):
        try:
            Num = str(df[i])[2:5]
            Num = Num.strip("% ")
            print(Num)
            Num = float(Num)
            if(Num > 0 and Num <= 100):
                print(i,Num)
                ReviewDisList.append(Num)
        except:
            print("Wrong Data",df.values[i])

    print(len(ReviewDisList))
    ax.set_title("Review distribution", fontweight="bold", fontsize=20)
    ax.set_xlabel("Review(%)", fontweight="bold")
    ax.set_ylabel("Density", fontweight="bold")
    sns.distplot(ReviewDisList)


def Price():
    Prices = df_Date_Sorted["Original Price"].values
    for i, v in enumerate(Prices):
        if v[0] == "$":
            Prices[i] = float(v[1:].replace(",",""))
            if(Prices[i] > 24.4643):
                Prices[i] = 0
        if v == "Free":
            Prices[i] = 0
    # Prices[Prices == "Free"] = 0


    # print(Prices)
    print(np.mean(Prices) , np.std(Prices))
    print(np.mean(Prices) + 3*np.std(Prices))

    ax.set_title("Prices distribution", fontweight="bold", fontsize=20)
    ax.set_xlabel("Price($)", fontweight="bold")
    ax.set_ylabel("Density", fontweight="bold")
    sns.distplot(Prices)


def TypeDistribution():
    Tags = df_Date_Sorted["Popular Tags"].values

    # Features = df_Date_Sorted["Game Features"].values

    Tags = []
    # Features = []

    TagName = []
    # FeatureName = []

    for i, Value in df_Date_Sorted.iterrows():
        print(i)

        try:
            Temp = eval(Value["Popular Tags"])
            for i in Temp:
                if len(i) > 1:
                    if i not in TagName:
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

    for i, v in enumerate(Tags):
        TagCount[TagName.index(v)] += 1

    # for i,v in enumerate(Features):
    # FeatureCount[FeatureName.index(v)] += 1

    print(TagName[np.argmax(TagCount)])
    # print(FeatureName[np.argmax(FeatureCount)])

    TagSortIndex = np.argsort(TagCount)
    # FeatureSortIndex = np.argsort(FeatureCount)

    print(TagCount[TagSortIndex[-3:]])

    ax.set_title("Number of tag occurrences", fontweight="bold", fontsize=20)
    ax.set_xticks([])
    ax.set_yticks([])

    # ax.set_xlabel('Tag',fontweight='bold')
    # ax.set_ylabel('Number of games in total',fontweight='bold')

    ax.grid(zorder=0)

    FirstTenElementIndex = TagSortIndex[-10:]

    FirstTenElement = []
    for i in FirstTenElementIndex:
        FirstTenElement.append(TagName[int(i)])

    FirstTenElementCount = TagCount[FirstTenElementIndex]

    Y = np.random.randn((10))

    ax.set_xlim([-1, 12])
    ax.set_ylim([np.min(Y) - 0.2, np.max(Y) + 0.2])

    plt.scatter(
        FirstTenElement,
        Y,
        cmap="coolwarm",
        c=FirstTenElementCount,
        s=0.06 * FirstTenElementCount,
        alpha=0.7,
    )

    for i, e in enumerate(FirstTenElement):
        plt.text(
            FirstTenElement[i],
            Y[i],
            s=e,
            verticalalignment="center",
            horizontalalignment="center",
            fontsize=14 * FirstTenElementCount[i] / 36587,
        )

    plt.colorbar()


def AllGameNumThroughTime():
    Dates = df_Date_Sorted["Release Date"].values

    CurrentTime = datetime.now()

    StartTime = datetime(year=2002, month=1, day=1)
    # Dates = [dt for dt in Dates if dt <= CurrentTime]

    TimeList = pd.date_range(start=StartTime, end=CurrentTime, periods=None, freq="D")

    Dates_np = np.array(Dates)

    # print(Dates_np[-10:-1 ])

    CountList = np.zeros(len(TimeList))

    for i, T in enumerate(TimeList):
        print(i)
        CountList[i] = np.sum(Dates_np < T)

    ax.set_title(
        "Number of games in total through time", fontweight="bold", fontsize=20
    )
    ax.set_xlabel("Time", fontweight="bold")
    ax.set_ylabel("Number of games in total", fontweight="bold")

    ax.grid(zorder=0)

    ax.plot(TimeList, CountList)


if __name__ == "__main__":
    fig, ax = plt.subplots(figsize=(6, 4.8), dpi=200, facecolor="w")

    RawData["Release Date"] = pd.to_datetime(
        RawData["Release Date"], format="%d-%b-%y", errors="coerce"
    )

    df_Date = RawData[
        RawData["Release Date"].dt.strftime("%d-%b-%y") == RawData["Release Date"]
    ]

    df_Date_Sorted = df_Date.sort_values("Release Date")

    # AllGameNumThroughTime()

    # TypeDistribution()

    # Price()

    # Review()

    Developer()

    plt.show()
