import trees

myDat, labels = trees.createDataSet()
print(myDat)
# shannonEnt = trees.calcShannonEnt(myDat)
# print(shannonEnt)

# retDataSet = trees.splitDataSet(myDat, 1, 1)
# print(retDataSet)

bestFeature = trees.chooseBestFeatureToSplit(myDat)
print(bestFeature)