# coding:utf-8
import codecs
import operator
import numpy as np
import matplotlib.pyplot as plt
import jieba
import extractQQMsg as eqm
import itemClass as ic

# 停用词列表
stopWordsList = []
stopWords = ''
# 发言列表 key：昵称，value:发言次数
speakerList = {}
# 词频列表 key：昵称 value：TermItem
tfList = {}
# 分词列表
wordsList = {}

# 加载停用词列表
stopWords = eqm.loadStopWords()
# 加载语料库
corpusList = eqm.loadFile2List('dataset/20-corpus.txt')

# 加载聊天内容
fp = codecs.open('dataset/20-msg.txt', encoding='utf-8')

speaker = ''
for line in fp.readlines():
    line = line.strip()
    msgType = eqm.isMsgHeaderOrBody(line)
    # 该行是消息头
    if msgType == 'header':
        # 计算每个人的发言频度
        speaker = eqm.extractMsgHeader(line)
        speakerList[speaker] = speakerList.get(speaker, 0) + 1

        # 填充tfList
        if tfList.get(speaker) == None:
            term = ic.TermItem()
            tfList[speaker] = term

    # 该行是消息内容
    elif msgType == 'body':
        if speaker == '':
            continue
        segList = jieba.cut(line)
        # print('/'.join(segList))
        for word in segList:
            word = word.strip()
            if word != '':
                # 整体统计词频
                wordsList[word] = wordsList.get(word, 0) + 1
                # 针对特定speaker，统计词频
                tfList[speaker].tf[word] = tfList[speaker].tf.get(word, 0) + 1


# # 发言人频度倒序排序
# sortedList = sorted(speakerList.iteritems(), key=operator.itemgetter(1), reverse=True)
#
# normalData = []
# for index in range(0, 20):
#     normalData.append(sortedList[index][1])
#     print(sortedList[index][0] + ' --- ' + str(sortedList[index][1]))
#
# plt.bar(np.arange(len(normalData)), normalData)
# plt.show()

# 排除停用词后的分词列表
# normalWordsList = {}
# for word in wordsList:
#     if word not in stopWords:
#        normalWordsList[word] = normalWordsList.get(word, 0) + wordsList[word]
# print('分词条数：' + str(len(normalWordsList)))
#
# # 分词频度倒序排序
# sortedWordsList = sorted(normalWordsList.iteritems(), key=operator.itemgetter(1), reverse=True)
# for wordsIndex in range(0, 50):
#     print(sortedWordsList[wordsIndex][0] + ' --- ' + str(sortedWordsList[wordsIndex][1]))
