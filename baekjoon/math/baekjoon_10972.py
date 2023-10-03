import sys
"""
[요약]
1) 사전순으로 다음에 오는 순열 구하는 프로그램 작성
    - 1순위: 오름차순
    - 막순위: 내림차순
    - 시간, 메모리, 입력: 1초, 256, 1만
    => 이중 루프는 힘들듯
[전략]
1) Next Permutation Algorithm
"""


def solution():
    n = int(sys.stdin.readline())
    arr, result, checker = list(map(int, sys.stdin.readline().split())), 0, False
    for i in range(n-1, 0, -1):
        if arr[i] > arr[i-1]:
            for j in range(n-1, 0, -1):
                if arr[j] > arr[i-1]:
                    arr[j], arr[i-1] = arr[i-1], arr[j]
                    result = arr[:i] + sorted(arr[i:])
                    checker = True
                    break
        if checker:
            break
    print(-1) if not result else print(*result)


if __name__ == "__main__":
    solution()
