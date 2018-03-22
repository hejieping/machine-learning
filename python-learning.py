# -*- coding: UTF-8 -*-
import time;
import moduleTest;
import os;
# if else
if(1 == 1):
    print 'asd'
else:
    print False
word = 'word'
print word;
'''
多行注释
'''
# 输出不换行
print 'hello','sad'
# 输出换行
print 'hello'
print 'runoob'
# 字符串操作
str = 'hello';
print str[0:3]
print str[2:]
print str*2
# 列表操作
tempList = ['sad',123,41]
print tempList[0:1]
print tempList
print tempList*2
print 123 in tempList
#元组 只读，不能赋值
tuple = ('tule',213,'machine-learning')
print tuple[0:1]
print tuple
print tuple*2
# 字典
dict = {}
dict['one'] = 1;
dict['two'] = 2;
tinyDict = {'name':'kepping','sex':'male'}
print dict;
print tinyDict
print tinyDict.keys()
print tinyDict.values()
del dict['one']
print dict
# 操作符
brother = 1;
sister = brother;
print brother is sister
# 循环
whileCount = 0
while(whileCount < 3):
    print 'count is',whileCount
    whileCount +=1
for temp in tempList :
    print temp
# 数据类型
strNum = '213'; 
print int(strNum)
print abs(-123)
# 时间和日期
print time.time()
print time.localtime(time.time())
print time.asctime(time.localtime(time.time()))

def printConsole(str2,str1='lalalal'):
    "控制台输出"
    print locals()
    print globals()
    print str1,str2
    return 

printConsole(str2 ='printConsoleTest')
# lambda
sum = lambda a,b:a+b
print sum(1,2)
moduleTest.modulePrint('kepping')
# IO
#str = raw_input("enter something:")
#print str
file = open('IO.text',"r")
print file.read(100)
file.close()
#os.rename("IO.text","IOI.text")
# class
person = moduleTest.Person('kepping',123125)
person.displayCount();
person.displayInfo();
print hasattr(person,'name')
print getattr(person,'name')
print setattr(person,'name','goodBoy')
print getattr(person,'name')
del person