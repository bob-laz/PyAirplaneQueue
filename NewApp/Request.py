class Request:

    # Request time must be >= submission time

    def __init__(self, ID, subTime, reqStart, reqDuration):
        self.ID = ID
        self.subTime = int(subTime)
        self.reqStart = int(reqStart)
        self.reqDuration = int(reqDuration)
        self.actualStart = 0
        self.actualEnd = 0

    def __str__(self):
        return "[" + self.ID + ", " + str(self.subTime) + ", " + str(self.reqStart) + ", " + str(self.reqDuration) + ", " + str(self.actualStart) + ", " + str(self.actualEnd) + "]"

    def __repr__(self):
        return str(self)

    def getSubTime(self):
        return self.subTime

    def getReqStart(self):
        return self.reqStart

    def getActualStart(self):
        return self.actualStart

    def getID(self):
        return self.ID

    def getActualEnd(self):
        return self.actualEnd

    def getReqDuration(self):
        return self.reqDuration

    def setActualStart(self, start):
        self.actualStart = start

    def setActualEnd(self, end):
        self.actualEnd = end