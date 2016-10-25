"""
Bob Laskowski
Compilers I
10/25/16
Snakes On A Plane

This class uses the Python time module as well as the Request and PriorityQ classes that I defined, which as also
located in the Application package.

Most of the functionality of the project is within this class. This class takes in an input file when an instance of the
class is created. The run method is the only public method. When called, it verifies the input file is in the correct
format of:

Delta 160, 0, 0, 4
UAL 120, 0, 5, 4
Delta 6, 2, 3, 6

The following parameters are: request identifier, request submission time, time slot requested, length of time
requested. Additional constraints on input include: the request identifier must be a string containing at least one
character, the request submission time, time slot request and length of time requested values must be integers and the
time slot requested must be greater than or equal to the request submission time. The program will not run and will
instead display an error message if invalid input or file format is passed in.

You can use the above input as sample input or create your own.

After the input is verified, each line of the input file is turned into a Request object. The run method then proceeds
to process each request object by scheduling the planes for takeoff based on their requested takeoff time as the first
priority and submission time as the second priority. To break any ties, the order the requests are submitted in the
input file is used as the third priority and will never be equal for any two request objects.
"""

import Request as Request
import PriorityQ as PriorityQ
import time


class RequestProcess:
    def __init__(self, file_name):
        self.__input_list = []          # A list of request objects from the input file
        self.__file_name = file_name    # Name of input file as string (i.e. "input.txt")

    """
    This method verifies the input file ends with the file extension .txt or .csv. It then parses the input file by
    splitting by line and then splitting each line using commas as the delimiter and stripping all white space. It passes
    this list of lists (a list of each line containing a list of, hopefully, the four input values) to validate_input.
    If this function returns true, it creates Request objects for each line of the input files and stores them in the
    input_list data attribute. It then sorts this list by submission time as first priority and requested start time as
    second. It does this by putting these items in a PriorityQ and then popping them off and putting them back into the
    input_list.

    If all of this processing executes successfully, the function returns true, otherwise it returns false.
    """
    def __process_input(self):
        if self.__file_name.endswith('.txt') or self.__file_name.endswith('.csv'):
            with open(self.__file_name) as input_file:
                whole_file = input_file.read().splitlines()
                for i in range(len(whole_file)):
                    whole_file[i] = whole_file[i].split(',')
                    for j in range(len(whole_file[i])):
                        whole_file[i][j] = whole_file[i][j].strip()
            if self.__validate_input(whole_file):
                for item in whole_file:
                    self.__input_list.append(Request.Request(item[0], int(item[1]), int(item[2]), int(item[3])))
                q = PriorityQ.PriorityQueue()
                for i in self.__input_list:
                    q.push(i, i.get_sub_time(), i.get_req_start())
                for i in range(len(self.__input_list)):
                    self.__input_list[i] = q.pop()
                return True
            else:
                return False
        else:
            print("Please ensure input file is a .txt or .csv file")
            return False

    """
    This method takes in a list of a list of strings.

    It verifies that the format matches our above input format. It ensures there are 4 values on each line, that the
    first value is a string and the second, third and fourth are integers.

    This function returns true if the input list is in the correct format, false otherwise.
    """
    @staticmethod
    def __validate_input(input_data):
        for item in input_data:
            if len(item) != 4:
                print(item)
                print("Please ensure your file has 4 values on each line")
                valid_input = False
                break
            if item[0].isdigit():
                print(item)
                print("Please ensure first item of each line is a string")
                valid_input = False
                break
            try:
                item[1] = int(item[1])
            except ValueError:
                print(item)
                print("Please ensure second item of each line is an integer")
                valid_input = False
                break
            try:
                item[2] = int(item[2])
            except ValueError:
                print(item)
                print("Please ensure third item of each line is an integer")
                valid_input = False
                break
            if item[1] > item[2]:
                print(item)
                print("Request time must be >= submission time, cannot request a time that has already passed")
                valid_input = False
                break
            try:
                item[3] = int(item[3])
            except ValueError:
                print(item)
                print("Please ensure fourth item of each line is an integer")
                valid_input = False
                break
            valid_input = True
        return valid_input

    """
    This method takes in a list of Request objects.

    Every request object has additional data attributes for the actual start and actual end time which are 0 upon
    creation. This method calculates what these values should be based on the object's position in the list. It does so
    by setting the first item in the list's actual start to the max of the actual start currently stored in the object
    or the  requested start (in case the plane requests to start later than the actual start assigned to it). This
    allows the queue to have empty slots.

    For every other item in the list, the actual start and requested duration of the previous Request item are added
    together and this becomes the actual start time (or scheduled start time) for the current item. This is the earliest
    the plane may take off and if the plane gets to the front of the queue but has requested a start time later
    than the current time, this will be handled by the max as described above.

    The list of Request objects with data attributes actual start and actual end populated will be returned.
    """
    @staticmethod
    def __calc_times(a_list):
        if len(a_list) > 0:
            a_list[0].set_actual_start(max(int(a_list[0].get_actual_start()), int(a_list[0].get_req_start())))
            for i in range(1, len(a_list)):
                offset = a_list[i - 1].get_actual_start() + a_list[i - 1].get_req_duration()
                if offset > a_list[i].get_req_start():
                    a_list[i].set_actual_start(offset)
                else:
                    a_list[i].set_actual_start(a_list[i].get_actual_start())
            for i in range(len(a_list)):
                a_list[i].set_actual_end(a_list[i].get_actual_start() + a_list[i].get_req_duration())
        return a_list

    """
    This method take in a list of Request objects and the current time (an integer of seconds).

    It checks to see if the length of the current_list passed in is > 0 (so we don't get an error when accessing item 0
    of the list). It then checks to see if the first item in the list's actual end time is <= the current time.

    If conditions are true, the first item of the list is removed and the rest of the list is returned. Otherwise, the
    list is returned unchanged.
    """
    @staticmethod
    def __check_removal(current_list, timer):
        if len(current_list) > 0 and current_list[0].get_actual_end() <= timer:
            current_list.remove(current_list[0])
        return current_list

    """
    This method takes in a list of Request objects.

    It sorts the list using a PriorityQ. The requested start time is used as the first priority and the submission time
    is the second priority with the position in the list as the tie breaker. The items are pushed onto the queue and
    then popped off and put back on the list in the new order.

    A sorted list of Request objects is returned.
    """
    @staticmethod
    def __sort_by_request_time(a_list):
        q1 = PriorityQ.PriorityQueue()
        for i in a_list:
            q1.push(i, i.get_req_start(), i.get_sub_time())
        for i in range(len(a_list)):
            a_list[i] = q1.pop()
        return a_list

    """
    This method takes in a list of Request objects and the current time (an integer in seconds)

    As per the requirements, the program should print out the status of the queue at every time
    interval. The output should be in the format:

    At time X the queue would look like: Request ID (scheduled for/started at X)

    An example would be:

    At time 0 the queue would look like: Delta 160 (started at 0), UAL 120 (scheduled for 5)
    At time 1 the queue would look like: Delta 160 (started at 0), UAL 120 (scheduled for 5)
    At time 2 the queue would look like: Delta 160 (started at 0), Delta 6 (scheduled for 4), UAL 120 (scheduled for 10)
    At time 3 the queue would look like: Delta 160 (started at 0), Delta 6 (scheduled for 4), UAL 120 (scheduled for 10)
    At time 4 the queue would look like: Delta 6 (started at 4), UAL 120 (scheduled for 10)

    This method formats output as above for the current list and time that is passed in. If the list passed in is empty,
    the method returns:

    At time X the queue would look like: EMPTY

    The method returns a string formatted as described above.
    """
    @staticmethod
    def __format_output(a_list, timer):
        ret_val = "At time " + str(timer) + " the queue would look like: "
        if len(a_list) > 0:
            if len(a_list) == 1:
                if a_list[0].get_actual_start() <= timer:
                    ret_val += a_list[0].get_id() + " (started at " + str(a_list[0].get_actual_start()) + ")"
                else:
                    ret_val += a_list[0].get_id() + " (scheduled for " + str(a_list[0].get_actual_start()) + ")"
                return ret_val
            else:
                if a_list[0].get_actual_start() <= timer:
                    ret_val += a_list[0].get_id() + " (started at " + str(a_list[0].get_actual_start()) + "), "
                else:
                    ret_val += a_list[0].get_id() + " (scheduled for " + str(a_list[0].get_actual_start()) + "), "
            for i in range(1, len(a_list)-1):
                ret_val += a_list[i].get_id() + " (scheduled for " + str(a_list[i].get_actual_start()) + "), "
            ret_val += a_list[len(a_list) - 1].get_id() + " (scheduled for " + \
                str(a_list[len(a_list) - 1].get_actual_start()) + ")"
        else:
            ret_val += "EMPTY"
        return ret_val

    """
    This method takes a list of Request objects.

    As per the requirements, the program should print out the request identifiers and the actual start and end times
    of each plane at the end of the program run. The output should be in the following format:

    Request ID (X-X), Request ID (X-X), Request ID (X-X)

    An example would be:

    Delta 160 (0-3), Delta 6 (4-9), UAL 120 (10-13)

    The method returns a string formatted as described above. If empty input was passed in the program instead returns
    the string "Empty input was passed in."
    """
    @staticmethod
    def __final_printout(a_list):
        ret_val = ""
        if len(a_list) > 0:
            for i in range(len(a_list)-1):
                ret_val += a_list[i].get_id() + " (" + str(a_list[i].get_actual_start()) + "-" + str(a_list[i].get_actual_end()) + "), "
            ret_val += a_list[len(a_list) - 1].get_id() + " (" + str(a_list[len(a_list) - 1].get_actual_start()) + "-" + str(a_list[len(a_list) - 1].get_actual_end()) + ")"
        else:
            ret_val += "Empty input was passed in."
        return ret_val

    """
    Run is the only public method in this class and it was drives the program. It uses many of the private methods of
    the class. First, process input is called to populate the data attribute input_list. A current and final list are
    created and the timer is set to 0. The method enters a loop which continually does the following: checks to see if
    any of the requests are finished and need to be removed, checks to see if any new requests have been submitted,
    sorts the requests, calculates the actual start and end times, check to see if all requests have been processed (and
    breaks out of the loop if they have), prints out the current status of the queue, sleeps for one second and then
    increments time. After the queue has been processed, the final output is printed out.
    """
    def run(self):
        if self.__process_input():
            current_list = []
            final_list = []
            timer = 0
            while True:
                current_list = self.__check_removal(current_list, timer)
                for i in self.__input_list:
                    if i.get_sub_time() == timer:
                        current_list.append(i)
                        final_list.append(i)
                current_list = self.__sort_by_request_time(current_list)
                current_list = self.__calc_times(current_list)
                if len(current_list) == 0 and len(final_list) == len(self.__input_list):
                    break
                print(self.__format_output(current_list, timer))
                time.sleep(1)
                timer += 1
            final_list = self.__sort_by_request_time(final_list)
            print(self.__final_printout(final_list))
