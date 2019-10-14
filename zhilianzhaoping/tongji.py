import jieba
import numpy as np
import pandas as pd

data = open("input.txt").readlines()


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def processs(data):
    cut_words = []
    sentence_seged = jieba.cut(data.strip())
    stopwords = stopwordslist('stopwords.txt')  # 这里加载停用词的路径
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                cut_words.append(word)
    return cut_words


cut_words = processs(data)

total_words = []
for each in cut_words:
    total_words.append(each)

n = np.unique(total_words, return_counts=True)
s = pd.Series(data=n[1], index=n[0])
result = s.sort_values(ascending=False)
print(result)
