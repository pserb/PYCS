from typing import Any
from Stack import Stack

class StackImpl(Stack):

    list = []

    def isEmpty(self):
        return len(self.list) <= 0

    def peekTop(self):
        return self.list[-1]

    def pop(self):
        return self.list.pop(-1)

    def push(self, Any):
        self.list.append(Any)
