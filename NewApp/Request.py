class Request:

    # Request time must be >= submission time

    def __init__(self, req_id, sub_time, req_start, req_duration):
        self.__id = req_id
        self.__sub_time = int(sub_time)
        self.__req_start = int(req_start)
        self.__req_duration = int(req_duration)
        self.__actual_start = 0
        self.__actual_end = 0

    def __str__(self):
        return "[" + self.__id + ", " + str(self.__sub_time) + ", " + str(self.__req_start) + ", " + \
               str(self.__req_duration) + ", " + str(self.__actual_start) + ", " + str(self.__actual_end) + "]"

    def __repr__(self):
        return str(self)

    def get_sub_time(self):
        return self.__sub_time

    def get_req_start(self):
        return self.__req_start

    def get_actual_start(self):
        return self.__actual_start

    def get_id(self):
        return self.__id

    def get_actual_end(self):
        return self.__actual_end

    def get_req_duration(self):
        return self.__req_duration

    def set_actual_start(self, start):
        self.__actual_start = start

    def set_actual_end(self, end):
        self.__actual_end = end
