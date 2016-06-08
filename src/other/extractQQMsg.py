# coding:utf-8
import codecs
import re
import jieba

stopWordsFileName = 'dataset/chinese-stopwords.txt'

# 解析消息头，提取发言者昵称
def extractMsgHeader(line):
    line = line.strip()
    splitLine = line.split(' ')[-1].strip()
    # 【学弱】有这种称号的，去除
    speaker = splitLine.split(u'】')[-1].strip()
    return speaker

# 判断消息头/消息内容
def isMsgHeaderOrBody(line):
    line = line.strip()
    if line == '':
        return ''
    # 如果包含时间格式，确定该行是消息头（包含昵称信息）
    pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{1,2}:\d{1,2}:\d{1,2}')
    result = re.match(pattern, line)
    if result:
        return 'header'
    else:
        return 'body'

# 加载文件，填充到列表
def loadFile2List(fileName):
    file = codecs.open(fileName, encoding='utf-8')
    lineList = []
    for word in file.readlines():
        lineList.append(word.strip())
    file.close()
    return lineList

# 加载停用词列表
def loadStopWords():
    stopWordsList = loadFile2List(stopWordsFileName)
    stopWordsString = ''.join(stopWordsList)
    return stopWordsString

# 创建语料库
def createCorpusLib(inputFileName, outputFileName):
   inputFile = codecs.open(inputFileName, encoding='utf-8')
   outputFile = codecs.open(outputFileName, 'a+', encoding='utf-8')

   stopWordsString = loadStopWords()
   corpus = set()   # 语料

   # 读取聊天记录，分词将，构建语料库
   for line in inputFile.readlines():
        line = line.strip()
        msgType = isMsgHeaderOrBody(line)
        if msgType == 'body':
             segList = jieba.cut(line)
             corpus.update(segList)

   corpusList = list(corpus)

   # 将语料库写入文件
   for word in corpusList:
       if word not in stopWordsString:
           outputFile.write('%s\n' % word)

   inputFile.close()
   outputFile.close()


# 生成语料库
# createCorpusLib('dataset/20-msg.txt', 'dataset/20-corpus.txt')
