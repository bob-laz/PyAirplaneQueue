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

        # durationSum = 0
        # for item in self.inputList:
        #     durationSum += int(item.reqDuration)
        #     self.scheduler.enterabs(self.now + int(item.reqStart), int(item.subTime), self.processQ)
        #     self.q.push(item, item.reqStart, item.subTime)
        # for i in range(durationSum):
        #     self.scheduler.enterabs(self.now + i, 0, self.printQStatus)

    def calcTimes(self, aList):
        startTime = max(aList[0].getActualStart(), aList[0].getReqStart())
        return startTime

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
