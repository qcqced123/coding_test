from itertools import permutations
import sys

# Input
n = int(input())
data = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

# Max, Min Init
max_value = 1e-9
min_value = -1e-9

# DFS
def dfs(i, now):
    global max_value, min_value, add, sub, mul, div # 전역변수로 선언 => Sub Routine Call 과정에서 해당 변수들을 업데이트 해주려고

    # 모든 연산자를 전부 사용한 경우 => 최대, 최소값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = min(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1

        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1

        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1

        if div > 0:
            div -= 1
            dfs(i+1, int(now / data[i]))
            div += 1

dfs(1, data[0])
print(max_value)
print(min_value)