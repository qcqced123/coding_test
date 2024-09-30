import sys


def solution():
    """ 100,000,000 (N^3)
    condition:
        1) 수열의 원소들이 다른 수열 내에서 순서대로 등장
        2) 사전 순으로 나중
            - 오름차순 기준 (첫번쨰 원소->두번쨰 원소-> ....)
            - 공집합도 공통 부분 수열로 간주
            - 길이가 서로 다른 수열끼리 첫번째 원소말고 다른 원소로 비교할 떄, 없는 원소는 0으로 간주함, 그래서 앞자리가 같으면
              길이가 짧은게 앞쪽 순서
        => 공통 부분 수열 중, 사전 순으로 가장 후순위

1
10
8
8 4 10 1 10 8 2 4

9
5 4 3 1 5 3 7 5 5
8
5 7 2 1 3 5 4 3

    idea:
        1) LCS
        2) LCS 배열 선형 탐색
    """
    N = int(input())
    A = [0] + list(map(int, sys.stdin.readline().split()))

    M = int(input())
    B = [0] + list(map(int, sys.stdin.readline().split()))

    cache = [[0]*(M+1) for _ in range(N+1)]
    num_cache = [[""]*(M+1) for _ in range(N+1)]

    for y in range(1, N+1):
        for x in range(1, M+1):
            if A[y] == B[x]:
                cache[y][x] = cache[y-1][x-1] + 1
                num_cache[y][x] = num_cache[y-1][x-1] + f"{str(B[x])} "
                continue

            else:
                if cache[y-1][x] > cache[y][x-1]:
                    cache[y][x] = cache[y-1][x]
                    num_cache[y][x] = num_cache[y-1][x]
                else:
                    cache[y][x] = cache[y][x-1]
                    num_cache[y][x] = num_cache[y][x-1]

    cnt = list(map(int, num_cache[-1][-1][:-1].split(" ")))
    print(cnt)
    for l in range(len(cnt)-1):
        if cnt[l] < cnt[l+1]:
            cnt = cnt[l+1:]
            break

    print(len(cnt))
    print(*cnt)


if __name__ == "__main__":
    solution()
