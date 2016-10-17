import Application.Request as Request
import Application.PriorityQ as PriorityQ
import sched
import time

class RequestProcess:
    def __init__(self):
        self.q = PriorityQ.PriorityQueue()
        self.inputList = []
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.now = time.time()

    def processInput(self, fileName):
        with open(fileName) as input:
            wholeFile = input.read().splitlines()
            for lines in wholeFile:
                line = lines.split(',')
                for i in range(len(line)):
                    line[i] = line[i].strip()
                self.inputList.append(Request.Request(line[0], line[1], line[2], line[3]))
        durationSum = 0
        for item in self.inputList:
            durationSum += int(item.reqDuration)
            self.scheduler.enterabs(self.now + int(item.reqStart), int(item.subTime), self.processQ)
            self.q.push(item, item.reqStart, item.subTime)
        for i in range(durationSum):
            self.scheduler.enterabs(self.now + i, 0, self.printQStatus)

    def printQStatus(self):
        printVal = ""
        if not self.q.empty():
            for item in self.q.QasList():
                printVal += str(item) + " "
            print(printVal)
        else:
            print("Q is empty")


    def runSched(self):
        self.scheduler.run()

    def processQ(self):
        self.q.pop()

    def determinePriority(self):
        for item in self.inputList:
            self.q.push(item, item.reqStart, item.subTime)

    def printInOrder(self):
        while not self.q.empty():
            print(self.q.pop())


rp = RequestProcess()
rp.processInput("input.txt")
rp.runSched()