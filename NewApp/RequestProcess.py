import NewApp.Request as Request
import NewApp.PriorityQ as PriorityQ


class RequestProcess:
    def __init__(self):
        self.q = PriorityQ.PriorityQueue()
        self.inputList = []


    def processInput(self, fileName):
        with open(fileName) as input:
            wholeFile = input.read().splitlines()
            for lines in wholeFile:
                line = lines.split(',')
                for i in range(len(line)):
                    line[i] = line[i].strip()
                self.inputList.append(Request.Request(line[0], line[1], line[2], line[3]))
        for i in self.inputList:
            self.q.push(i, i.getSubTime(), i.getReqStart())
        for i in range(len(self.inputList)):
            self.inputList[i] = self.q.pop()
        for i in self.inputList:
            print(i)

    def calcTimes(self, aList):
        aList[0].setActualStart(max(aList[0].getActualStart(), aList[0].getReqStart()))
        for i in range(1, len(aList)):
            offset = aList[i-1].getActualStart() + aList[i-1].getReqDuration()
            if offset > aList[i].getReqStart():
                aList[i].setActualStart(offset)
            else:
                aList[i].setActualStart(aList[i].getActualStart())
        for i in range(len(aList)):
            aList[i].setActualEnd(aList[i].getActualStart() + aList[i].getReqDuration())
        return aList

    def printQStatus(self):
        printVal = ""
        if not self.q.empty():
            for item in self.q.QasList():
                printVal += str(item) + " "
            print(printVal)
        else:
            print("Q is empty")


rp = RequestProcess()
rp.processInput("input.txt")
