import Request as Request
import PriorityQ as PriorityQ
import time


class RequestProcess:
    def __init__(self, fileName):
        self.inputList = []
        self.fileName = fileName

    def processInput(self):
        with open(self.fileName) as inputFile:
            wholeFile = inputFile.read().splitlines()
            for lines in wholeFile:
                line = lines.split(',')
                for i in range(len(line)):
                    line[i] = line[i].strip()
                self.inputList.append(Request.Request(line[0], line[1], line[2], line[3]))
        q = PriorityQ.PriorityQueue()
        for i in self.inputList:
            q.push(i, i.getSubTime(), i.getReqStart())
        for i in range(len(self.inputList)):
            self.inputList[i] = q.pop()

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

    @staticmethod
    def formatOutput(aList, timer):
        retVal = "At time " + str(timer) + " the queue would look like: "
        if len(aList) > 0:
            if len(aList) == 1:
                if aList[0].getActualStart() <= timer:
                    retVal += aList[0].getID() + " (started at " + str(aList[0].getActualStart()) + ")"
                else:
                    retVal += aList[0].getID() + " (scheduled for " + str(aList[0].getActualStart()) + ")"
                return retVal
            else:
                if aList[0].getActualStart() <= timer:
                    retVal += aList[0].getID() + " (started at " + str(aList[0].getActualStart()) + "), "
                else:
                    retVal += aList[0].getID() + " (scheduled for " + str(aList[0].getActualStart()) + "), "
            for i in range(1, len(aList)-1):
                retVal += aList[i].getID() + " (scheduled for " + str(aList[i].getActualStart()) + "), "
            retVal += aList[len(aList)-1].getID() + " (scheduled for " + str(aList[len(aList)-1].getActualStart()) + ")"
        else:
            retVal += "EMPTY"
        return retVal

    @staticmethod
    def finalPrintout(aList):
        retVal = ""
        if len(aList) > 0:
            for i in range(len(aList)-1):
                retVal += aList[i].getID() + " (" + str(aList[i].getActualStart()) + "-" + str(aList[i].getActualEnd()) + "), "
            retVal += aList[len(aList)-1].getID() + " (" + str(aList[len(aList)-1].getActualStart()) + "-" + str(aList[len(aList)-1].getActualEnd()) + ")"
        else:
            retVal += "Empty input was passed in."
        return retVal

    def run(self):
        self.processInput()
        currentList = []
        finalList = []
        timer = 0
        while True:
            currentList = self.checkRemoval(currentList, timer)
            for i in self.inputList:
                if i.getSubTime() == timer:
                    currentList.append(i)
                    finalList.append(i)
            currentList = self.sortByRequestTime(currentList)
            currentList = self.calcTimes(currentList)
            if len(currentList) == 0 and len(finalList) == len(self.inputList):
                break
            print(self.formatOutput(currentList, timer))
            time.sleep(1)
            timer += 1
        finalList = self.sortByRequestTime(finalList)
        print(self.finalPrintout(finalList))