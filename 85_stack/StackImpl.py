from typing import Any
from Stack import Stack

class StackImpl(Stack):

    list = []

    def isEmpty(self):
        return self.list.count() <= 0

    def peekTop(self):
        return list[-1]

    def pop(self):
        return list.pop(-1)

    def push(self, Any):
        list.append[Any]
