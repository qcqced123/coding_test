import sys
"""
[풀이 시간]
1) 06:10 ~ 06:40

[요약]
1) N개의 스위치와 N개의 전구
    - 전구는 켜져 있는 상태와 꺼져 있는 상태 (01)
    - i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 변경
    - 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N
    - 우리가 원하는 상태로 만들려면 최소 몇 번 눌러야 할까
[전략]
1) 옵션 & 최소값 도출: Greedy
    - 최대 10만이라 이중 루프 불가
"""
N = int(sys.stdin.readline())
curr_state = list(map(int, sys.stdin.readline().rstrip()))  # 현재 상태
obj_state = list(map(int, sys.stdin.readline().rstrip()))  # 목표 상태

n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))


def change(A, B):
    L = A[:]
    press = 0
    for i in range(1, n):
        # 이전 전구가 같은 상태면 pass
        if L[i-1] == B[i-1]:
            continue
        # 상태가 다를 경우
        press += 1
        for j in range(i-1, i+2):
            if j<n:
                L[j] = 1 - L[j]
    return press if L == B else 1e9


# 첫번째 전구의 스위치를 누르지 않는 경우
res = change(bulb, target)
# 첫번째 전구의 스위치를 누르는 경우
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
res = min(res, change(bulb, target) + 1)
print(res if res != 1e9 else -1)