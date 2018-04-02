from sklearn.neighbors import KNeighborsClassifier
from sklearn.kernel_ridge import KernelRidge
from sklearn.tree import DecisionTreeClassifier
import numpy as np 

def createAbaloneData():
    fr = open('./data/abalone.data')
    dataMat = []; dataLabel = []
    sexData ={'M':1,'F':-1,'I':0}
    for line in fr.readlines():
        lineArr = line.strip().split(',')
        lineArr[0] = sexData[lineArr[0]]
        dataMat.append(lineArr[:len(lineArr)-1])
        dataLabel.append(lineArr[-1])
    return dataMat,dataLabel

def splitData(dataMat,dataLabel):
    indices = np.random.permutation(len(dataMat))
    dataTrainMat = np.array(dataMat)[100:]; dataTrainLabel = np.array(dataLabel)[100:]
    dataTestMat = np.array(dataMat)[:100]; dataTestLabel = np.array(dataLabel)[:100]
    return dataTrainMat ,dataTrainLabel,dataTestMat,dataTestLabel




dataMat,dataLabel =  createAbaloneData()
dataTrainMat ,dataTrainLabel,dataTestMat,dataTestLabel = splitData(dataMat,dataLabel)

#knn
""" knn = KNeighborsClassifier()
knn.fit(dataTrainMat,dataTrainLabel)
print 'knn accucy',knn.score(dataTestMat,dataTestLabel) """

#line regression
clf = KernelRidge(alpha=2.0)
clf.fit(dataTrainMat,dataTrainLabel)
print 'linear regression accucy',clf.score(dataTestMat,map(float,dataTestLabel))

#tree 
""" tree = DecisionTreeClassifier(random_state=2)
tree.fit(dataTrainMat,dataTrainLabel)
print 'tree accucy',tree.score(dataTestMat,dataTestLabel) """




