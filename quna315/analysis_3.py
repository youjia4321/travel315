import re
import numpy as np
import pandas as pd
from jieba import analyse

# 引入关键词抽取接口 使用textrank算法
textrank = analyse.textrank


def read(path):
    data = pd.read_csv(path, encoding="gbk")
    df = pd.DataFrame(data)
    return df


def keywords(text):
    try:
        key = []
        # 对文本进行textrank关键词提取
        keywords = textrank(text)
        for keyword in keywords:
            key.append(keyword)
        # 最后返回一个list
        return key
    except:
        pass


# 2018年数据处理
def count2018(data):
    total_words = []
    for i in range(len(data)):
        if re.findall("2018", data["提交时间"][i]):
            c_title = keywords(data["主题"][i])
            try:
                for words in c_title:
                    total_words.append(words)
            except:
                pass

    print("正在统计2108年高词频...")
    n = np.unique(total_words, return_counts=True)
    s = pd.Series(data=n[1], index=n[0])
    result = s.sort_values(ascending=False)
    df = pd.DataFrame(result).reset_index()  # 设置索引值
    df.columns = ['高频词', '频次']  # 设置列名
    to_save = df[df["频次"] >= 50]  # 找出频次在10以上的关键词
    to_save.to_csv("2018.csv", index=0, encoding="ansi")  # 存储到csv文件（下面同理）


# 2017年数据处理
def count2017(data):
    total_words = []
    for i in range(len(data)):
        if re.findall("2017", data["提交时间"][i]):
            c_title = keywords(data["主题"][i])
            try:
                for words in c_title:
                    total_words.append(words)
            except:
                pass


    print("正在统计2107年高词频...")
    n = np.unique(total_words, return_counts=True)
    s = pd.Series(data=n[1], index=n[0])
    result = s.sort_values(ascending=False)
    df = pd.DataFrame(result).reset_index()
    df.columns = ['高频词', '频次']
    to_save = df[df["频次"] >= 30]
    to_save.to_csv("2017.csv", index=0, encoding="ansi")


# 2016年数据处理
def count2016(data):
    total_words = []
    for i in range(len(data)):
        if re.findall("2016", data["提交时间"][i]):
            c_title = keywords(data["主题"][i])
            try:
                for words in c_title:
                    total_words.append(words)
            except:
                pass


    print("正在统计2106年高词频...")
    n = np.unique(total_words, return_counts=True)
    s = pd.Series(data=n[1], index=n[0])
    result = s.sort_values(ascending=False)
    df = pd.DataFrame(result).reset_index()
    df.columns = ['高频词', '频次']
    to_save = df[df["频次"] >= 16]
    to_save.to_csv("2016.csv", index=0, encoding="ansi")


if __name__ == "__main__":
    path = "threeYear.csv"
    df = read(path)
    count2018(df)
    count2017(df)
    count2016(df)
    print("处理完成，已储存至对应csv文件")