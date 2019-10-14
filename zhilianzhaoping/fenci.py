from jieba import analyse
import jieba
import re
from collections import Counter


analyse.set_stop_words("stopwords.txt")


# 引入TF-IDF关键词抽取接口
tfidf = analyse.extract_tags

# 原始文本
text = "岗位职责：1、熟悉负责所属模块的开发建设，包含功能的规划、需求分析设计与技术实现，并进行单元测试；2、根据需求、设计文档完成指定的设计、开发工作；3、修复系统中存在的Bug；4、完成其他交办的各类技术开发任务。岗位要求：1大专以上学历，精通Java语言。熟练oracle,有过erp系统审核流经验优先。2.熟悉Java服务器端开发，了解设计模式，熟悉springmvc、mybatis、3.熟悉javascript、CSS、HTML、jsp、jQuery、html、ajax、bootstrap前端框架与技能，熟悉TCP/IP、HTTP的基本工作原理；4.熟练应用各种开发熟悉工具如Myeclipse,idea，熟练应用各种应用服务器如tomcat；5.熟悉使用Memcached、Redis等缓存技术，有高并发编程经验或具有高校管理软件开发经验者优先；6.阅读并分析过开源框架源码；7.熟悉工作责任心强，具有一定的抗压能力，热爱自己从事的行业，有团队管理经验更佳。"
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


cut_words=""
text.strip('\n')
line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”\、]", "", text)
seg_list = jieba.cut(line, cut_all=False)
cut_words += (" ".join(seg_list))
all_words = cut_words.split()
print(all_words)

# 基于TF-IDF算法进行关键词抽取
c = Counter()
# keywords = tfidf(text)
# print("keywords by tfidf:")
# 输出抽取出的关键词
k = []
for keyword in all_words:
    stopwords = stopwordslist('stopwords.txt')  # 这里加载停用词的路径
    if keyword not in stopwords:
        if len(keyword) >1 and keyword != "\r\n":
            c[keyword] += 1


print('\n词频统计结果：')
for (k,v) in c.most_common(2):# 输出词频最高的前两个词
    print("%s:%d"%(k,v))