import numpy as np

import pandas as pd

import re
import csv
from datetime import datetime

DataPath = "./SteamGamesCleanedFinal.csv"
df = pd.read_csv(DataPath)

# # 将NaN值替换为空字符串
# df['Release Date'] = df['Release Date'].fillna('')

# # 统一Release Date列内的日期格式为mm/dd/yy
# df['Release Date'] = df['Release Date'].apply(lambda x: re.sub(r'(\d{1,2}) (\w{3}), (\d{4})', r'\2 \1, \3', str(x)))    
# df['Release Date'] = df['Release Date'].apply(lambda x: re.sub(r'(\d{1,2})/(\d{1,2})/(\d{4})', r'\2/\1/\3', str(x)))
# df['Release Date'] = df['Release Date'].apply(lambda x: re.sub(r'Q(\d) (\d{4})', r'\1/1/\2', str(x)))

# 删除Link列和"Minimum Requirements"列
# df = df.drop(['Link', 'Minimum Requirements'], axis=1)

# 转换Release Date列中仅有年份的数据
# df['Release Date'] = df['Release Date'].apply(lambda x: re.sub(r'^(\d{4})$', r'1/1/\1', str(x)))
df = df[df['Release Date'] != 'Maybe']
# # 清除特殊字符和乱码字符
# df['Release Date'] = df['Release Date'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', str(x)))
# df['Title'] = df['Title'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', str(x)))

# 清除Title列中内容重复的行
# df = df.drop_duplicates(subset=['Title'])

# 清理Popular Tags列与Game Features列中没有被[]框起来的行
# df = df[df['Popular Tags'].str.contains(r'\[.*\]')]
# df = df[df['Game Features'].str.contains(r'\[.*\]')]

# 将结果另存为CleanedUP.csv文件
df.to_csv('SteamGamesCleanedFinal.csv', index=False)