import Request as Request
import PriorityQ as PriorityQ
import time

"""
Bob Laskowski
Compilers I
10/23/16
Snakes On A Plane

This class uses the python time module as well as the Request and PriorityQ classes that I defined, which as also
located in the Application package.



"""


class RequestProcess:
    def __init__(self, file_name):
        self.__input_list = []
        self.__file_name = file_name

    def __process_input(self):
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

    @staticmethod
    def __check_removal(current_list, timer):
        for i in current_list:
            if i.get_actual_end() <= timer:
                current_list.remove(i)
        return current_list

    @staticmethod
    def __sort_by_request_time(a_list):
        q1 = PriorityQ.PriorityQueue()
        for i in a_list:
            q1.push(i, i.get_req_start(), i.get_sub_time())
        for i in range(len(a_list)):
            a_list[i] = q1.pop()
        return a_list

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
            ret_val += a_list[len(a_list) - 1].get_id() + " (scheduled for " + str(a_list[len(a_list) - 1].get_actual_start()) + ")"
        else:
            ret_val += "EMPTY"
        return ret_val

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
