import sys


def solution():
    """
    idea: dynamic programming
        - 행: 오른쪽 카드 배열
        - 열: 왼쪽 카드 배열
        - if i < j: max(왼대각+i, 위+i)
        - else: max(왼대각, 위)

    feedback:
        - 뒤쪽에서 값을 캐싱해서 사용하는 것보다, 앞쪽 값을 뒤쪽에서 캐싱해줄 수 있음
    """
    # init data structure
    input = sys.stdin.readline
    N = int(input())
    cache = [[0]*(N+1) for _ in range(N+1)]
    card_l = [0] + list(map(int, input().split()))
    card_r = [0] + list(map(int, input().split()))

    # update the dp cache
    for i in range(1, N+1):
        cnt_r = card_r[i]
        for j in range(1, N+1):
            cnt_l = card_l[j]
            if cnt_r < cnt_l: cache[i][j] = cnt_r + max(cache[i-1][j-1], cache[i-1][j], cache[i][j])
            else: cache[i][j] = max(cache[i-1][j-1], cache[i-1][j], cache[i][j])

    answer = 0
    for y in range(1, N+1):
        for x in range(1, N+1):
            answer = max(answer, cache[y][x])
    print(answer)


def solution2():
    """
    idea: dynamic programming
        - 이전 값을 가져와서 현재 값 업데이트하지 말고, 반대로
    """
    # init data structure
    input = sys.stdin.readline
    N = int(input())
    cache = [[0]*(N+1) for _ in range(N+1)]
    card_l = [0] + list(map(int, input().split()))
    card_r = [0] + list(map(int, input().split()))

    # update the dp cache


if __name__ == "__main__":
    solution2()
