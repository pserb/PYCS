from typing import Any
from Deque import Deque

class DequeImpl(Deque):
    
    # used linked list for faster runtime
    list = []

    def peekFirst(self):
        return self.list[0]
    def peekLast(self):
        return self.list[-1]

    def addFirst(self, e):
        # use linked list
        self.list.insert(0,e)
    def addLast(self, e):
        self.list.append(e)

    def removeFirst(self):
        return self.list.pop(0)
    def removeLast(self):
        return self.list.pop(-1)

    def size(self):
        return len(self.list)
    def isEmpty(self):
        return self.size() < 1

    def removeFirstOccurrence(self, o):
        self.list.remove(o)
        return True

    def __str__(self):
        return f"{self.list}"
