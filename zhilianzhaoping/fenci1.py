import jieba

# jieba.load_userdict('userdict.txt')

# 创建停用词list


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('stopwords.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += "\n"
    return outstr


if __name__ == '__main__':
    inputs = open('input.txt', 'r', encoding='utf-8')
    outputs = open('output.txt', 'w')
    for line in inputs:
        line_seg = seg_sentence(line)  # 这里的返回值是字符串
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()

