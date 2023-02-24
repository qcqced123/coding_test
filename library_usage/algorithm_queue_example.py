from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.append(8)
print(queue)

queue.popleft() # Stack의 Pop 역할
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)