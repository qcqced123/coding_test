import sys
from collections import defaultdict


def solution():
    """
    idea: prefix sum with hash structure

    feedback:
        - 진짜 개어렵네, 이걸 실전에서 어떻게 생각해

    reference:
        - https://velog.io/@7h13200/Python%EB%B0%B1%EC%A4%80-2015%EB%B2%88-%EC%88%98%EB%93%A4%EC%9D%98-%ED%95%A94
    """
    # get input data
    input = sys.stdin.readline
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cache = defaultdict(int)

    # init cache dictionary for prefix sum, do prefix sum
    cnt = 0
    answer = 0
    cache[0] = 1
    for element in arr:
        cnt += element
        curr = cache[cnt-K]
        if curr:
            answer += curr

        cache[cnt] += 1
    print(answer)

if __name__ == "__main__":
    solution()
