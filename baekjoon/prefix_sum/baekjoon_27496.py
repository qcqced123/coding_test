import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: prefix sum + sliding window

    question:
        - 아니 연속 시간 아니었어??

    """
    N, L = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    l = 1
    cnt = 0
    answer = 0
    for i in range(1, N+1):
        cnt += arr[i]
        if i > L:
            cnt -= arr[l]
            l += 1

        if 129 <= cnt <= 138:
            answer += 1

    print(answer)

if __name__ == "__main__":
    solution()
