import sys


def solution():
    """ <= NlogN
    idea: dynamic programming with prefix sum
        - 제약 조건: 밑장 뺀 횟수
        - dp[i][j]: i번 밑장을 뺐고, j번째 카드까지 고려 했을 때 점수의 최대값

    feedback:
        - 여기서 말하는 밑장이라는게, 지금 배분해야하는 윗장으로 바로 아래칸
        - 이건 문제가 설명을 그지 같이 적어둔 것도 한 몫하네
    """
    # get input data
    input = sys.stdin.readline
    N = int(input())
    cards = list(map(int, input().split()))

    # init dp, prefix array
    my = 0
    for i in range(0, N, 2):
        my += cards[i]

    enemy = my
    answer = my
    for i in range(N-2, 1, -2):
        enemy -= cards[i]
        enemy += cards[i-1]
        answer = max(answer, enemy)

    enemy = my
    for i in range(N-1, 0, -2):
        enemy += cards[i]
        enemy -= cards[i-1]
        answer = max(answer, enemy)

    print(answer)


if __name__ == "__main__":
    solution()
