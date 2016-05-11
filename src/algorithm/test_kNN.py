import kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy import *

# group, labels = kNN.createDataSet()
# print(group)
# print(labels)
#
# result = kNN.classify0([0, 0], group, labels, 1)
# print(result)

datingDataMat, datingLabels = kNN.file2Martix('../dataset/datingTestSet2.txt')

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15.0*array(datingLabels))
# plt.show()

normalMat, ranges, minVals = kNN.autoNorm(datingDataMat)
print minVals



