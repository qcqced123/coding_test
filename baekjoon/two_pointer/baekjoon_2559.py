import sys


def solution():
    """ '연속 구간' 부분합, 최대값 구하기, 구간 크기가 고정 (슬라이딩 윈도우), NlogN
    idea 1: sliding window
        1) only sliding window
            - TC: O(N*K)
            - 당연히 실패
            - sum을 쓰지말자

        2) sliding window with two-pointer
            - 합을 이루는 원소는 양끝만 바뀐다는 점을 이용
            - 초기값으로 합을 구해두면 시간 복잡도를 줄일 수 있음
            - 두 포인터는 윈도우의 양끝을 가리켜야 함
    """
    N, K = map(int, sys.stdin.readline().split())  # nums, window size
    nums = list(map(int, sys.stdin.readline().split()))

    initializer = sum(nums[0:K])  # 초기값 세팅
    result = initializer
    for i in range(1, N-K+1):  # N*
        l = i-1
        r = i+K-1
        initializer = initializer - nums[l] + nums[r]
        result = max(result, initializer)

    print(result)


if __name__ == "__main__":
    solution()
