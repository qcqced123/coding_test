import sys


def solution():
    """ NlogN, 연속 부분 배열의 합
    idea: sliding window
    """
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # sliding window
    window = M
    init_ = sum(arr[:window])
    answer = init_
    for i in range(1, N-window+1):
        cnt = init_ - arr[i-1]
        cnt += arr[i+window-1]
        answer = max(answer, init_)
        init_ = cnt

    print(answer)


if __name__ == "__main__":
    solution()
