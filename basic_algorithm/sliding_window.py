import time
from collections import deque

""" sliding window
1) linear search: max()
2) priority queue search
"""

# 1) linear search with max()
src = time.time()

k = 3
arr = [1, 3, -1, -3, 5, 3, 6, 7]
result = []

for i in range(len(arr) - k + 1):
    result.append(max(arr[i:i + k]))

end = time.time()

print(f"Execution Time: {src - end}")
print(f"Result: {result}")

# 2) queue opt

src = time.time()

k = 3
arr = [1, 3, -1, -3, 5, 3, 6, 7]
result, window, curr_max = [], deque(), float('inf')
for i, v in enumerate(arr):
    window.append(v)
    if i < k - 1:  # continuously push element into deque until max length of window
        continue

    if curr_max == float('inf'):
        curr_max = max(window)
    elif v > curr_max:
        curr_max = v

    result.append(curr_max)
    if curr_max == window.popleft():
        curr_max = float('inf')

end = time.time()
print(f"Execution Time: {src - end}")
print(f"Result: {result}")