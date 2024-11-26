# test = [1,2,3,4,5]
# hp = test[0]
# hp -= 1
#
# print(hp)
# print(test)
#
#
# # arr = []
# # print(arr[1])
#
#
# test = set()
# test.add(1)
# print(test)
# test.remove(1)
# print(test)
#
#
# test = [(2,14,1), (3,8,1), (5,12,1)]
# test.sort(key=lamb)

from bisect import bisect_left, bisect_right

x = 9
test = [1, 7, 7, 7, 10, 10, 11, 12, 13, 14]

print(bisect_right(test, x))
print(bisect_left(test, x))

# init the data structure
INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
visited = [[-1] * N for _ in range(N)]
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
grid = [list(map(str, input().rstrip())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        grid[i][j] = int(grid[i][j])

# do bfs
answer = INF
q = deque([(0, 0)])
visited[0][0] = 0
while q:
    vy, vx = q.popleft()
    vb = visited[vy][vx]
    for i in range(4):
        ny, nx = vy + dy[i], vx + dx[i]
        if ny == N - 1 and nx == N - 1:
            answer = min(answer, visited[vy][vx])
            continue

        if -1 < ny < N and -1 < nx < N and vb < answer and (visited[ny][nx] == -1 or vb < visited[ny][nx]):
            nb = vb
            if not grid[ny][nx]:
                nb += 1

            visited[ny][nx] = nb
            q.append((ny, nx))

print(answer)
