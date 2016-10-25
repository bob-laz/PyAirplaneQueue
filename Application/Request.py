"""
Bob Laskowski
Compilers I
10/25/16
Snakes On A Plane

This class defines the data structure Request. A Request is something submitted by a plane for a takeoff time on a
runway. These requests are used by the RequestProcess class to schedule takeoffs for planes. The time units used are
integers of seconds.
"""


class Request:

    def __init__(self, req_id, sub_time, req_start, req_duration):
        self.__id = str(req_id)                     # A string identifying the plane that made the request
        self.__sub_time = int(sub_time)             # The submission time of the request
        self.__req_start = int(req_start)           # The time the plane requests take off, must be >= submission time
        self.__req_duration = int(req_duration)     # The duration the plane requests to use the runway for
        self.__actual_start = 0                     # The time the plane actually starts its takeoff
        self.__actual_end = 0                       # The time the plane finishes taking off

    """
    Override of the str method to define a string representation of a Request object. It will be of the following
    format:

    [Request ID, X, X, X, X, X]

    An example would be:

    [Delta 145, 0, 0, 5, 0, 5]

    Returns a string formatted as described above.
    """
    def __str__(self):
        return "[" + self.__id + ", " + str(self.__sub_time) + ", " + str(self.__req_start) + ", " + \
               str(self.__req_duration) + ", " + str(self.__actual_start) + ", " + str(self.__actual_end) + "]"

    """
    Override of the repr method to define how a Request object is displayed when it is stored in a list of Requests and
    we print out the items of the list in a for loop. It just calls the str method of Request so that it displays the
    same way no matter how we print it out.

    Returns a string formatted as described in str comments.
    """
    def __repr__(self):
        return str(self)

    """
    Returns the integer submission time
    """
    def get_sub_time(self):
        return self.__sub_time

    """
    Returns the integer requested start time
    """
    def get_req_start(self):
        return self.__req_start

    """
    Returns the integer actual start time
    """
    def get_actual_start(self):
        return self.__actual_start

    """
    Returns the string submission ID
    """
    def get_id(self):
        return self.__id

    """
    Returns the integer actual end time
    """
    def get_actual_end(self):
        return self.__actual_end

    """
    Returns the integer requested duration
    """
    def get_req_duration(self):
        return self.__req_duration

    """
    Take in an integer, sets the actual start data attribute
    """
    def set_actual_start(self, start):
        self.__actual_start = start

    """
    Takes in an integer, sets the actual end data attribute
    """
    def set_actual_end(self, end):
        self.__actual_end = end
