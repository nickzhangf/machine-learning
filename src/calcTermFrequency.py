# coding: utf-8
# 计算词频
import sys
import json
import jieba
import matplotlib.pyplot as pyplot

reload(sys)
sys.setdefaultencoding('utf-8')

# 读取文件内容
file_object = open('../data/beidou.txt')
black_list_object = open('../data/stop_words.txt')
all_the_text = []
black_words = []
try:
    all_the_text = file_object.read()
    black_words = black_list_object.read()
finally:
    file_object.close()
    black_list_object.close()

print(black_words)

seg_list = jieba.cut(all_the_text, cut_all=False)
# print("/ ".join(seg_list))

hist = { }
for word in seg_list:
    hist[word] = hist.get(word, 0) + 1

print len(hist)

# print json.dumps(hist, encoding="UTF-8", ensure_ascii=False)

# 对词频排序
hist_sorted = sorted(hist.iteritems(), key=lambda d: d[1], reverse=True)
# bar_width = 0.35
# pyplot.bar(range(20), [hist_sorted[i][1] for i in range(20)],bar_width)
# pyplot.show()
print json.dumps(hist_sorted, encoding="UTF-8", ensure_ascii=False)