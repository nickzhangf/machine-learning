# coding: utf-8
# jieba中文分词

import sys
import os
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Result: " + "/ ".join(seg_list))  # 全模式
