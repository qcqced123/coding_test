import sys
from collections import deque, defaultdict


def solution():
    """ N^2 * M^2
    arr index: 곡 순서
    arr element: '인덱스'번째 곡을 연주하기 전에 바꿀 수 있는 볼륨

    시작 볼륨이 P라면 현재 인덱스의 곡은 P+v[i] or P-v[i] 볼륨만 사용가능함
    3 5 10
    5 3 7

    idea: dynamic programming
        - 일반적인 dp 보단, 그냥 세트 하나 만들어서 넣고 빼고 하자
    """
    input = sys.stdin.readline
    N, S, M = map(int, input().split())  # 곡 개수, 시작 볼륨, 최대 볼륨
    arr = [0] + list(map(int, input().split()))

    # do dynamic programming
    cache = deque([S])
    for i in range(1, N+1):
        cnt = arr[i]
        for j in range(len(cache)):
            curr = cache.popleft()
            add = curr + cnt
            sub = curr - cnt
            if add <= M:
                cache.append(add)

            if sub >= 0:
                cache.append(sub)

    answer = max(cache) if cache else -1
    print(answer)


def solution2():
    return


if __name__ == "__main__":
    solution()
