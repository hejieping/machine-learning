def modulePrint(str):
    print str

class Person :
    "HUMAN"
    emCount = 0;
    def __init__(self,name,salary):
        self.name = name;
        self.salary = salary;
        Person.emCount += 1;
    
    def __del__(self):
        print 'Person destory'

    def displayCount(self):
        print 'emCount:',Person.emCount
    
    def displayInfo(self):
        print self.name,self.salary