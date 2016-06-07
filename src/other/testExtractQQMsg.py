# coding:utf-8
import operator
import numpy as np
import matplotlib.pyplot as plt
import jieba
import extractQQMsg as eqm

speakerList = {}
fp = open('../dataset/msg0.txt')

for line in fp.readlines():
    line = line.strip()
    speaker = eqm.extractMsgHeader(line)
    # 改行是消息头，计算每个人的发言频度
    if speaker != '':
       speakerList[speaker] = speakerList.get(speaker, 0) + 1
    else:
        segList = jieba.cut(line)
        # print('/'.join(segList))
        for word in segList:
            word = word.strip()
            if word != '':
                print(word)

# # 倒序排序
# sortedList = sorted(speakerList.iteritems(), key=operator.itemgetter(1), reverse=True)
#
# normalData = []
# for index in range(0, 20):
#     normalData.append(sortedList[index][1])
#     print(sortedList[index][0])
#
# plt.bar(np.arange(len(normalData)), normalData)
# plt.show()
