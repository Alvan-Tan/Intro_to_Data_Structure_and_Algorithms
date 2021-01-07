# stack, last in first out
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

x = stack.pop()
print(x)
print(stack)

# queue, first in first out
from collections import deque
# deque object allows us to add and delete elements from the front and end of a list in constant time

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

x = queue.popleft() #taking out an element from the front
print(x)
print(queue)
