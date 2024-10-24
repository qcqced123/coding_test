import heapq


h = []
for i in range(5):
    heapq.heappush(h, (1, i))


for i in range(5):
    heapq.heappush(h, (0, i))

while h:
    vy, vx = heapq.heappop(h)
    print(vy, vx)
