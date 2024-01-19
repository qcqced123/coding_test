import sys
import heapq


N = int(sys.stdin.readline())
h = []
for _ in range(N):
    command = int(sys.stdin.readline())
    if not command:
        print(heapq.heappop(h) if h else 0, end='\n')
        continue
    heapq.heappush(h, command)
