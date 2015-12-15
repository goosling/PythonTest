__author__ = 'joe'

import time
class Date(object):
    def __init__(self, time = time.ctime()):
        self.time = time
    def choice(self, choiceTime):
        #date = []
        date = self.time.split(" ")
        #print date
        #date = ['Sun', 'Mar', '22', '16:20:04', '2015']
        dateDict = {}
        dateDict['MDY'] = date[1] + '/' +date[2] + '/' + date[4][2:]
        dateDict['MDYY'] = date[1] + '/' +date[2] + '/' + date[4]
        dateDict['DMY'] = date[2] + '/' +date[1] + '/' + date[4][2:]
        dateDict['DMYY'] = date[2] + '/' +date[1] + '/' + date[4]
        dateDict['MODYY'] = date[1] + ' ' +date[2] + ',' + date[4]
        return dateDict[choiceTime]

if __name__ == "__main__":
    date1 = Date()
    while True:
        print "'MDY'-->MM/DD/YY"
        print "'MDYY'-->MM/DD/YYYY"
        print "'DMY'-->DD/MM/YY"
        print "'DMYY'-->DD/MM/YYYY"
        print "'MODYY'-->Mon DD,YYYY"
        choiceTime = raw_input("please enter your choice(q to quit):")
        if choiceTime.lower() == 'q':
            break
        print date1.choice(choiceTime)




