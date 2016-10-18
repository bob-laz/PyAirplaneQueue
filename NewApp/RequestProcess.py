import NewApp.Request as Request
import NewApp.PriorityQ as PriorityQ
import time


class RequestProcess:
    def __init__(self):
        self.q = PriorityQ.PriorityQueue()
        self.inputList = []

    def processInput(self, fileName):
        with open(fileName) as inputFile:
            wholeFile = inputFile.read().splitlines()
            for lines in wholeFile:
                line = lines.split(',')
                for i in range(len(line)):
                    line[i] = line[i].strip()
                self.inputList.append(Request.Request(line[0], line[1], line[2], line[3]))
        for i in self.inputList:
            self.q.push(i, i.getSubTime(), i.getReqStart())
        for i in range(len(self.inputList)):
            self.inputList[i] = self.q.pop()

    @staticmethod
    def calcTimes(aList):
        if len(aList) > 0:
            aList[0].setActualStart(max(int(aList[0].getActualStart()), int(aList[0].getReqStart())))
            for i in range(1, len(aList)):
                offset = aList[i-1].getActualStart() + aList[i-1].getReqDuration()
                if offset > aList[i].getReqStart():
                    aList[i].setActualStart(offset)
                else:
                    aList[i].setActualStart(aList[i].getActualStart())
            for i in range(len(aList)):
                aList[i].setActualEnd(aList[i].getActualStart() + aList[i].getReqDuration())
        return aList

    @staticmethod
    def checkRemoval(currentList, timer):
        for i in currentList:
            if i.getActualEnd() <= timer:
                currentList.remove(i)
        return currentList

    @staticmethod
    def sortByRequestTime(aList):
        q1 = PriorityQ.PriorityQueue()
        for i in aList:
            q1.push(i, i.getReqStart(), i.getSubTime())
        for i in range(len(aList)):
            aList[i] = q1.pop()
        return aList

    def run(self):
        currentList = []
        timer = 0
        while True:
            currentList = self.calcTimes(currentList)
            currentList = self.checkRemoval(currentList, timer)
            for i in self.inputList:
                if i.getSubTime() == timer:
                    currentList.append(i)
            currentList = self.sortByRequestTime(currentList)
            currentList = self.calcTimes(currentList)
            if len(currentList) == 0:
                break
            print(str(timer) + " " + str(currentList))
            time.sleep(1)
            timer += 1


rp = RequestProcess()
rp.processInput("input.txt")
print(rp.run())
