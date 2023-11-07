from ast import Num
from msilib import Feature
from turtle import color
import numpy as np

import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns
import sys


from datetime import datetime
import json

from sympy import rotations

# from sympy import true

# import pingouin as pg


print(plt.style.available)
plt.style.use("seaborn-v0_8")

plt.rcParams["font.family"] = ["Times New Roman"]
plt.rcParams["axes.labelsize"] = 14

DataPath = "./Data/SteamGamesCleanedFinal_Modified.csv"

# DataPath = "./SteamGamesCleanedFinal.csv"

RawData = pd.read_csv(DataPath, encoding="ansi")

def TotalPrice():
    TotalPrice = 0
    for i , Value in df_Date.iterrows():
        print(i)
        Prices = 0
        v = Value["Original Price"]
        if v == "Free":
            Prices = 0
        if v[0] == "$":
            Prices = float(v[1:].replace(",", ""))
        if Prices > 10000:
            Prices = 0        
        TotalPrice += Prices

    print(TotalPrice)

def TagVsPrice():
    TagName = []
    for i, Value in df_Date_Sorted.iterrows():
        print(i)
        try:
            Temp = eval(Value["Popular Tags"])
            for j in Temp:
                if len(j) > 1:
                    if j not in TagName:
                        TagName.append(j)
        except:
            print("Wrong Data", Value)
    print(TagName)
    TagPrice = np.zeros(len(TagName))
    TagCount = np.zeros(len(TagName))
    # sys.exit(0)

    for i, Value in df_Date_Sorted.iterrows():
        print(i)
        try:
            Temp = eval(Value["Popular Tags"])
        except:
            continue
        for j in Temp:
            if j in TagName:
                Prices = 0
                v = Value["Original Price"]
                if v == "Free":
                    Prices = 0
                if v[0] == "$":
                    Prices = float(v[1:].replace(",", ""))
                if Prices > 24.4643:
                    Prices = 0
                TagPrice[TagName.index(j)] += Prices
                TagCount[TagName.index(j)] += 1

            # print("Wrong Data",Value)

    Avg = np.array(TagPrice / TagCount)

    SortIndex = list(map(int, np.argsort(-TagPrice)))

    print(TagPrice[SortIndex])

    AvgSortIndex = list(map(int, np.argsort(-Avg)))
    TagName = np.array(TagName)

    print(Avg[AvgSortIndex][:3],TagName[AvgSortIndex][:3])

    ax.set_title("Tag price distribution", fontweight="bold", fontsize=20)
    ax.set_xlabel("Tags", fontweight="bold")
    ax.set_ylabel("Total Price ($)", fontweight="bold")
    plt.xticks(rotation=90)
    plt.bar(TagName[SortIndex][:10], TagPrice[SortIndex][:10], label="Total Price ($)")
    ax.legend(bbox_to_anchor=(0, 1.02), loc="lower left",mode="expand", borderaxespad=0, ncol=1)
    # ax.legend(loc="center right", frameon=True)
    for i, v in enumerate(TagPrice[SortIndex][:10]):
        plt.text(
            TagName[SortIndex][:10][i],
            v,
            str(round(v)),
            verticalalignment="bottom",
            horizontalalignment="center",
        )

    ax2 = ax.twinx()
    ax2.plot(
        TagName[SortIndex][:10],
        Avg[SortIndex][:10],
        color="r",
        marker="o",
        label="Averaged Price ($)",
    )
    ax2.grid(None)
    ax2.set_ylabel("Averaged Price ($)", fontweight="bold")
    # ax2.legend(loc="center right", frameon=True)

    ax2.legend(bbox_to_anchor=(0.8, 1.02), loc="lower right",mode="expand", borderaxespad=0, ncol=1)

def Developer():
    data = RawData["Developer"].values

    DevName = []

    for i, v in enumerate(data):
        if type(v) != type(""):
            continue

        if v not in DevName and len(v) > 1 and len(v) < 20 and "?" not in v:
            print(i, v)
            DevName.append(v)

    NameCount = np.zeros(len(DevName))

    for i, v in enumerate(data):
        if v in DevName:
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
        c=FirstTenElementCount,
        s=5 * FirstTenElementCount,
        alpha=0.7,
    )

    for i, e in enumerate(FirstTenElementCount):
        plt.text(
            FirstTenElement[i],
            Y[i],
            s=int(e),
            verticalalignment="center",
            horizontalalignment="center",
            fontsize=14 * FirstTenElementCount[i] / 150,
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
    for i, v in enumerate(df):
        try:
            Num = str(df[i])[2:5]
            Num = Num.strip("% ")
            print(Num)
            Num = float(Num)
            if Num > 0 and Num <= 100:
                print(i, Num)
                ReviewDisList.append(Num)
        except:
            print("Wrong Data", df.values[i])

    print(len(ReviewDisList))
    ax.set_title("Review distribution", fontweight="bold", fontsize=20)
    ax.set_xlabel("Review(%)", fontweight="bold")
    ax.set_ylabel("Density", fontweight="bold")
    sns.distplot(ReviewDisList)


def Price():
    Prices = df_Date_Sorted["Original Price"].values
    for i, v in enumerate(Prices):
        if v[0] == "$":
            Prices[i] = float(v[1:].replace(",", ""))
            if Prices[i] > 24.4643:
                Prices[i] = 0
        if v == "Free":
            Prices[i] = 0
    # Prices[Prices == "Free"] = 0

    # print(Prices)
    print(np.mean(Prices), np.std(Prices))
    print(np.mean(Prices) + 3 * np.std(Prices))

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

    # Developer()

    # TagVsPrice()

    TotalPrice()

    plt.show()
