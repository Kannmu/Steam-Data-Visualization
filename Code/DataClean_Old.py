import numpy as np

import pandas as pd

import re
import csv
from datetime import datetime

DataPath = "./Data/SteamGamesRaw - Copy.csv"

# RawData = pd.read_excel(DataPath, 0)


def clean_special_characters(text):
    # 清除特殊字符
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    return cleaned_text

def clean_data(file_path):
    # 读取CSV文件
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # 清除特殊字符和重复行
    cleaned_rows = []
    titles = set()
    for row in rows:
        title = clean_special_characters(row['Title'])
        if title not in titles:
            titles.add(title)
            cleaned_rows.append(row)

    # 清除乱码行
    cleaned_rows = [row for row in cleaned_rows if not any(ord(c) > 127 for c in row['Title'])]

    # 将结果保存到CleanedUP.csv文件
    fieldnames = reader.fieldnames
    with open('SteamGamesCleaned.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

# 调用函数进行数据清洗
clean_data(DataPath)