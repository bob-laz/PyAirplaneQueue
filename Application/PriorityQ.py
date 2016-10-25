"""
Bob Laskowski
Compilers I
10/25/16
Snakes On A Plane

This class defines the data structure priority queue. This is done by using Python's heapq adding a push method that
takes in two priorities as well as the item to be pushed and uses these to order the queue.
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self.__q = []           # The list to store the queue in
        self.__index = 0        # The index of the item in the queue

    """
    This method takes in the item to be added to the queue, which can be any data type, as well as a primary priority
    and a secondary priority, which should both be integers.

    The heappush method from heapq is called with the list that stores the queue and then a tuple with the primary and
    secondary priorities, the index and the item to be pushed. The heappush method uses the primary priority first, the
    secondary priority next and finally the index to order the items. No two items will ever have the same index so this
    value is the tie breaker in the case that the primary and secondary priorities are the same for two or more items
    added to the queue. The item with the lowest priority is at the top of the queue (will be popped first). After the
    item is added to the queue, the index is incremented.
    """
    def push(self, item, priority, priority2):
        heapq.heappush(self.__q, (priority, priority2, self.__index, item))
        self.__index += 1

    """
    Uses the heapq heappop method to return the smallest item in the queue (with the lowest priority).

    This function returns the last item in the tuple that is returned by heappop because heappop doesn't necessarily
    know how many priorities you have defined. The last item in this tuple is always the item added to the queue.
    """
    def pop(self):
        return heapq.heappop(self.__q)[-1]

    """
    Returns true if the queue is empty, false otherwise. This is determined by checking to see if the length of the list
    storing the queue is equal to zero. 
    """
    def empty(self):
        return len(self.__q) == 0
