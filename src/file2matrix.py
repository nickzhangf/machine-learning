# coding:utf-8
# 读取数据表

import sys
import os
from numpy import *

reload(sys)
sys.setdefaultencoding('utf-8')

def file2matrix(path, delimiter):
    recordList = []
    fp = open(path, 'rb')
    content = fp.read()
    fp.close()
    rowList = content.splitlines()

    recordList = [map(eval, row.split(delimiter)) for row in rowList if row.strip()]
    return mat(recordList)

recordMat = file2matrix('data.txt', '\t')
print shape(recordMat)
print recordMat