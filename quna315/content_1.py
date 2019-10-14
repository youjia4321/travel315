import requests
import json
import re
from lxml import etree
import csv


# 分析网页,抓取信息,json处理
def parse(url):
    headers = {
        'Host': 'travel315.people.com.cn',
        'Referer': 'http://travel315.people.com.cn/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    html = resp.text
    if html.startswith(u'\ufeff'):
        html = html.encode('utf8')[3:].decode('utf8')
    results = json.loads(html)
    jsonData = results["comps"]
    return jsonData


# 18,17,16年的总统计
def parseContent(data):
    fp = open("threeYear.csv", 'w', newline='', encoding='ansi')
    writer = csv.writer(fp)
    writer.writerow(('提交时间', '主题', '分类', '被投诉地区', '状态', '转交部门'))
    staus_code = {
        "1": "处理中",
        "2": "已处理/待反馈",
        "3": "已完结",
        "4": "已反馈"
    }
    for content in data:
        try:
            if re.findall("2018", content["c_create_time"]) or re.findall("2017", content["c_create_time"]) or re.findall("2016", content["c_create_time"]):
                if content["c_prev"] == "去哪儿网":
                    url = 'http://travel315.people.com.cn/interface/select/data_show_xml.php?c_id='+content['c_id']
                    print(url)
                    contents = parse_details(url)
                    writer.writerow((content["c_create_time"].replace(" ", "."), contents, content["c_type"], content["c_prev"], staus_code[content["c_stat"]], content["c_to"]))
                    
                else:
                    pass
            else:
                pass
        except:
            continue


def parse_details(url):
    try:
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        html = resp.text
        partten = re.compile(r'<c_context><!\[CDATA\[<p.*?>(.*?)</p>\]\]></c_context>', re.S)
        content = re.findall(partten, html)
        content = content[0].replace("&nbsp;",'').replace(" ", "").replace(";", ":")
        xhtml = etree.HTML(content)
        last_word = xhtml.xpath("//text()")
        last_words = ''.join(last_word)
        return last_words
    except:
        pass


if __name__ == "__main__":
    url = "http://travel315.people.com.cn/interface/select/data_idx.php?_=1551332664931"
    results = parse(url)
    parseContent(results)
    print("处理完成，已储存至threeYear.csv文件")
