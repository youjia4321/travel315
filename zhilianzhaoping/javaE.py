import requests
import json
import re
from lxml import etree
import csv
from jieba import analyse
import pandas as pd
import numpy as np

analyse.set_stop_words("stopwords.txt")  # 停用词
# 引入TF-IDF关键词抽取接口
tfidf = analyse.extract_tags


def parse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/69.0.3497.100 Safari/537.36',
    }
    try:
        resp = requests.get(url, headers=headers)
        html = resp.text
        return html
    except:
        pass


def dealJson(data):
    results = json.loads(data)
    jsonData = results["data"]["results"]
    return jsonData


def dealContent(jsonData, writer, total_words):
    for data in jsonData:
        info = {}
        # content = []
        info['position'] = data['city']['display'].replace(" ", "")
        # info['positionUrl'] = data['positionURL']
        info['salary'] = data['salary'].replace(" ", "")
        info['jobName'] = data['jobName'].replace(" ", "")
        if re.findall("java", data['jobName'].lower()):
            # print(data['positionURL'])
            job = dealPositionInfo(data['positionURL'])
            count(job, total_words=total_words)
            info['jobRequirement'] = job
            writer.writerow((info['position'], info['salary'], info['jobName'], info['jobRequirement']))
        else:
            continue


def dealPositionInfo(url):
    resp = parse(url=url)
    html = etree.HTML(resp)
    jobRequirement = html.xpath("//div[@class='pos-ul']//text()")
    jobRequirement_words = ''.join(jobRequirement).replace("\xa0", "").replace("\n", "").replace(" ", "")
    keyword = keywords(jobRequirement_words)
    return keyword


def count(data, total_words):
    for word in data:
        total_words.append(word)


def keywords(text):
    key = []
    keywords = tfidf(text)
    for keyword in keywords:
        key.append(keyword)
    return key


def countE(total):
    n = np.unique(total, return_counts=True)
    s = pd.Series(data=n[1], index=n[0])
    result = s.sort_values(ascending=False)
    df = pd.DataFrame(result).reset_index()
    df.columns = ['高频词', '频次']
    to_save = df[df["频次"] >= 50]
    to_save.to_csv("keywords_tongji.csv", index=0)


if __name__ == '__main__':
    from datetime import datetime
    startTime = datetime.now()
    total_words = []
    fp = open("java.csv", 'a', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('地点', '薪资', '职位', '岗位需求'))
    for page in range(35):
        url = "https://fe-api.zhaopin.com/c/i/sou?start="+str(page*90)+"&pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.37975790&x-zp-page-request-id=d537080296884aafa75b99b445371ad6-1551230768934-382901"
        print(url)
        data = parse(url=url)
        jsonData = dealJson(data)
        # print(jsonData)
        dealContent(jsonData, writer, total_words)
    print("正在统计词频...")
    # print(total_words)
    countE(total_words)
    endTime = datetime.now()
    print(startTime, endTime)
    print("统计完成...")

