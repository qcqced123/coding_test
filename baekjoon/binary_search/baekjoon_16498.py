import sys


def solution2():
    """ 벌점 == 그룹의 최대-최소
        idea: bisect
            - bisect 대신에 그냥 루프 돌려서, 차이가 최소인 원소 찾기
    """
    INF = sys.maxsize
    input = sys.stdin.readline
    A, B, C = map(int, input().split())
    player_a = list(map(int, input().split()))
    player_b = list(map(int, input().split()))
    player_c = list(map(int, input().split()))

    # do sort
    player_a.sort(), player_b.sort(), player_c.sort()

    # find the minimum solution
    answer = INF
    size = len(player_a)
    size_b = len(player_b)
    size_c = len(player_c)

    # get element from B, C
    for i in range(size):
        cnt = player_a[i]
        cnt_b, cache_b = 0, INF
        cnt_c, cache_c = 0, INF
        for j in range(size_b):
            curr = abs(cnt-player_b[j])
            if curr < cache_b:
                cnt_b = player_b[j]
                cache_b = curr

        for k in range(size_c):
            curr = abs(cnt - player_c[k])
            if curr < cache_c:
                cnt_c = player_c[k]
                cache_c = curr

        answer = min(answer, max(cnt, cnt_b, cnt_c)-min(cnt, cnt_b, cnt_c))

    print(answer)


def solution3():
    """ 통과 하면 안될거 같은뎁...
    """
    INF = sys.maxsize
    input = sys.stdin.readline
    A, B, C = map(int, input().split())
    player_a = list(map(int, input().split()))
    player_b = list(map(int, input().split()))
    player_c = list(map(int, input().split()))

    # do sort
    player_a.sort(), player_b.sort(), player_c.sort()

    # find the minimum solution
    answer = INF
    size = len(player_a)
    size_b = len(player_b)
    size_c = len(player_c)

    # get element from B, C
    for i in range(size):
        cnt = player_a[i]
        cnt_b, cache_b = 0, INF
        for j in range(size_b):
            curr = abs(cnt - player_b[j])
            if curr < cache_b:
                cnt_b = player_b[j]
                cache_b = curr

        for k in range(size_c):
            answer = min(answer, max(cnt, cnt_b, player_c[k]) - min(cnt, cnt_b, player_c[k]))

    print(answer)
    return


if __name__ == "__main__":
    solution3()
