import Request as Request
import PriorityQ as PriorityQ
import time

# TODO: input validation
# TODO: add comments


class RequestProcess:
    def __init__(self, file_name):
        self.__inputList = []
        self.__fileName = file_name

    def __process_input(self):
        with open(self.__fileName) as inputFile:
            whole_file = inputFile.read().splitlines()
            for lines in whole_file:
                line = lines.split(',')
                for i in range(len(line)):
                    line[i] = line[i].strip()
                self.__inputList.append(Request.Request(line[0], line[1], line[2], line[3]))
        q = PriorityQ.PriorityQueue()
        for i in self.__inputList:
            q.push(i, i.get_sub_time(), i.get_req_start())
        for i in range(len(self.__inputList)):
            self.__inputList[i] = q.pop()

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
        self.__process_input()
        current_list = []
        final_list = []
        timer = 0
        while True:
            current_list = self.__check_removal(current_list, timer)
            for i in self.__inputList:
                if i.get_sub_time() == timer:
                    current_list.append(i)
                    final_list.append(i)
            current_list = self.__sort_by_request_time(current_list)
            current_list = self.__calc_times(current_list)
            if len(current_list) == 0 and len(final_list) == len(self.__inputList):
                break
            print(self.__format_output(current_list, timer))
            time.sleep(1)
            timer += 1
        final_list = self.__sort_by_request_time(final_list)
        print(self.__final_printout(final_list))
