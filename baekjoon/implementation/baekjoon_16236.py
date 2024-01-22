import sys

"""
0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
"""

N = int(sys.stdin.readline())
grid = []

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    grid.append(tmp)
    for j, v in enumerate(tmp):
        if v == 9:
            child_idx = [2, j, v]  # [size, row, col]


