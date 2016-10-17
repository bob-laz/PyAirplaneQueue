class Request:

    def __init__(self, ID, subTime, reqStart, reqDuration):
        self.ID = ID
        self.subTime = subTime
        self.reqStart = reqStart
        self.reqDuration = reqDuration
        self.actualStart = 0

    def __str__(self):
        return "[" + self.ID + ", " + str(self.subTime) + ", " + str(self.reqStart) + ", " + str(self.reqDuration) + ", "+ str(self.actualStart) + "]"

    def __repr__(self):
        return str(self)