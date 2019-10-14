from jieba import analyse
import pandas as pd

# 引入关键词抽取接口 使用textrank算法
textrank = analyse.textrank


def read(path):
    data = pd.read_csv(path, encoding="gbk")
    df = pd.DataFrame(data)
    for i in range(len(df)):
        text = df["主题"][i]
        keyword = keywords(text)
        df["主题"][i] = keyword
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


if __name__ == '__main__':
    path = "threeYear.csv"
    df = read(path)
    df.to_csv("keywords.csv", index=0, encoding="ansi")
    print("处理完成，已储存至keywords.csv文件")