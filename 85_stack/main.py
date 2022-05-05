from StackImpl import StackImpl 

stack = StackImpl()

stack.push("a")
stack.push("b")
stack.push("c")
stack.push("d")
stack.push("e")
stack.push("f")
stack.push("g")

# g
print(stack.pop())
# f
print(stack.pop())
# e
print(stack.pop())
# d
print(stack.pop())
# c
print(stack.pop())
# b
print(stack.pop())
# a
print(stack.pop())

# true
print(stack.isEmpty())
