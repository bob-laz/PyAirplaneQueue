class Request:

    # Request time must be >= submission time

    def __init__(self, ID, subTime, reqStart, reqDuration):
        self.__ID = ID
        self.__subTime = int(subTime)
        self.__reqStart = int(reqStart)
        self.__reqDuration = int(reqDuration)
        self.__actualStart = 0
        self.__actualEnd = 0

    def __str__(self):
        return "[" + self.__ID + ", " + str(self.__subTime) + ", " + str(self.__reqStart) + ", " + str(self.__reqDuration) + ", " + str(self.__actualStart) + ", " + str(self.__actualEnd) + "]"

    def __repr__(self):
        return str(self)

    def getSubTime(self):
        return self.__subTime

    def getReqStart(self):
        return self.__reqStart

    def getActualStart(self):
        return self.__actualStart

    def getID(self):
        return self.__ID

    def getActualEnd(self):
        return self.__actualEnd

    def getReqDuration(self):
        return self.__reqDuration

    def setActualStart(self, start):
        self.__actualStart = start

    def setActualEnd(self, end):
        self.__actualEnd = end
