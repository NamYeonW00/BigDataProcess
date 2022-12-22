import sys
import numpy as np
import operator
from os import listdir

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(),
		key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

def fileToMatrix(foldername):
	fileList = listdir(foldername)
	numberOfFiles = len(fileList)
	returnMat = np.zeros((numberOfFiles, 1024))
	classLabelVector = []
	for i in range(numberOfFiles):
		f = open(foldername + '/' + fileList[i])
		index = 0
		for line in f.readlines():
			for j in range(32):
				returnMat[i, index + j] = int(line[j])
			index += j
		classLabelVector.append(int(fileList[i].split('_')[0]))
	return returnMat, classLabelVector

trainingDigits = sys.argv[1]
testDigits = sys.argv[2]

trainingMatrix, trainingLabels = fileToMatrix(trainingDigits)

error = 0

testList = listdir(testDigits)
testNum = len(testList)
testMatrix, testLabels = fileToMatrix(testDigits)    

for k in range(1, 21):
	error = 0
	for i in range(testNum):
		result = classify0(testMatrix[i], trainingMatrix, trainingLabels, k)
		if testLabels[i] != result :
			error += 1
	print(int(error / testNum * 100))
