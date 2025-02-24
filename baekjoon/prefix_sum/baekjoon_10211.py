import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea:
    """
    for _ in range(int(input())):
        N = int(input())
        arr = [0] + list(map(int, input().split()))
        prefix = [0]*(N+1)

        # init prefix sum array
        prefix = [0]*(N+1)
        for i in range(1, N+1):
            prefix[i] = prefix[i-1] + arr[i]

        # find the maximum
        answer = -INF
        for i in range(1, N+1):
            for j in range(i):
                answer = max(answer, prefix[i]-prefix[j])

        print(answer)


if __name__ == "__main__":
    solution()
