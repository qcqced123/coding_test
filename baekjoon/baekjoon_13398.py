import sys


def solution():
    """ 연속 수열의 합의 최대, 수 1개 무시 가능(안해도 ㄱㅊ)
    idea: dynamic programming
        - 제약 조건: 수를 1개 이하로 뺄까 말까
            - 행: 숫자
            - 열: 뺀 숫자 개수
    feedback:
        - dp cache 초기화는 -INF으로 해야함

    """
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    cache = [[-INF]*2 for _ in range(N+1)]

    # update the dp cache
    answer = -INF
    for i in range(1, N+1):
        cache[i][0] = max(arr[i], cache[i-1][0] + arr[i])
        cache[i][1] = max(cache[i-1][0], cache[i-1][1] + arr[i])
        answer = max(answer, cache[i][0], cache[i][1])

    print(answer)


if __name__ == "__main__":
    solution()
