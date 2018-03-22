import numpy as np
import operator
import matplotlib
import matplotlib.pyplot as plt
import os

def createDataSet():
    group =  np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2;
    sqDistances = sqDiffMat.sum(axis = 1);
    distances = sqDistances**0.5;
    sortedDistIndicies = distances.argsort()
    classcount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classcount[voteIlabel] = classcount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classcount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = np.zeros((numberOfLines,3))
    classLabelVector = []
    index = 0;
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(np.int(listFromLine[-1]))
        index+=1
    return returnMat,classLabelVector
def autoNorm(dataset):
    minvals = dataset.min(0)
    maxvals = dataset.max(0)
    range = maxvals - minvals
    normDataSet = np.zeros(np.shape(dataset))
    m = dataset.shape[0]
    normDataSet = dataset - np.tile(minvals,(m,1))
    normDataSet = normDataSet/np.tile(range,(m,1))
    return normDataSet,range,minvals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('./MLiA_SourceCode/machinelearninginaction/Ch02/datingTestSet2.txt')
    normat,ranges,minvals = autoNorm(datingDataMat)
    m = normat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0;
    for i in range(numTestVecs):
        classifierResult = classify(normat[i,:],normat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "predict:%d,true: %d" %(classifierResult,datingLabels[i])
        if(classifierResult != datingLabels[i]):
            errorCount +=1.0
    print "total error rate: %f" %(errorCount/float(numTestVecs))

def img2vevtor(filename):
    returnVect = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

def handWritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('./MLiA_SourceCode/machinelearninginaction/Ch02/digits/trainingDigits')
    m = len(trainingFileList)
    trainingMat = np.zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vevtor('./MLiA_SourceCode/machinelearninginaction/Ch02/digits/trainingDigits/%s' % fileNameStr)
    testFileList = os.listdir('./MLiA_SourceCode/machinelearninginaction/Ch02/digits/testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vevtor('./MLiA_SourceCode/machinelearninginaction/Ch02/digits/trainingDigits/%s' % fileNameStr)
        classifierResult = classify(vectorUnderTest,trainingMat,hwLabels,3)
        print "predict: %d, true: %d" % (classifierResult,classNumStr)
        if(classifierResult != classNumStr): errorCount+=1.0
    print "errorCount: %d, errorRate:%f" %(errorCount,errorCount/float(mTest))
    

#group,labels = createDataSet()
#print classify([0,0],group,labels,3)
datingDataMat,datingLabels = file2matrix('./MLiA_SourceCode/machinelearninginaction/Ch02/datingTestSet2.txt')
#print datingDataMat
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*np.array(datingLabels),15.0*np.array(datingLabels))
#plt.show()
normat,ranges,minvals = autoNorm(datingDataMat)
#print normat
#datingClassTest()
#print img2vevtor('./MLiA_SourceCode/machinelearninginaction/Ch02/digits/trainingDigits/0_0.txt')
handWritingClassTest()
