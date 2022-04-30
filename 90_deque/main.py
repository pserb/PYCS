from DequeImpl import DequeImpl

deque = DequeImpl()

print("Now using deque as a stack...")
deque.addLast("hey")
deque.addLast("wo")
deque.addLast("ow")
deque.addLast("o")

print(deque.size()) #4
print(deque.removeLast()) #o
print(deque.removeLast()) #ow
print(deque.removeLast()) #wo
print(deque.removeLast()) #hey

print(deque.isEmpty()) #True

print("\nNow using deque as a queue...")
deque.addFirst("hey")
deque.addFirst("wo")
deque.addFirst("ow")
deque.addFirst("o")

print(deque.size()) #4
print(deque.removeLast()) #hey
print(deque.removeLast()) #wo
print(deque.removeLast()) #ow
print(deque.removeLast()) #o

print(deque.isEmpty()) #True

print("\nTesting __str__...")

deque.addFirst("first thing")
deque.addFirst("second")
deque.addFirst("second")
deque.addFirst("three")

print(deque)

deque.removeFirstOccurrence("second")

print(deque)
