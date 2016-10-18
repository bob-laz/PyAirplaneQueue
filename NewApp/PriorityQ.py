import heapq


class PriorityQueue:
    def __init__(self):
        self._q = []
        self._index = 0

    def push(self, item, priority, priority2):
        heapq.heappush(self._q, (priority, priority2, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._q)[-1]

    def empty(self):
        return len(self._q) == 0

    def printQ(self):
        for item in self._q:
            print(item)

    def QasList(self):
        qList = []
        for item in self._q:
            qList.append(self._q.pop())
        return qList
