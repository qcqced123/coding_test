import sys



def solution():
    """
    idea: prefix sum
        - structure: prefix[i]
            - prefix[i]: i일에 남아 있는 짚신 벌레 숫자
    """
    def clamp(value, min_value, max_value):
        """ clip the input x value to specific range """
        return max(min(value, max_value), min_value)

    # get input
    INF = sys.maxsize
    input = sys.stdin.readline
    a, b, d, N = map(int, input().split())
    prefix = [0]*(N+2)

    # update prefix cache
    # 인덱스-1 == 실제 날짜
    for i in range(1, N+2):
        if i < a+1:
            prefix[i] = 1
            continue

        prefix[i] += prefix[i-1]
        prefix[i] += prefix[clamp(i-a, 0, INF)] - prefix[clamp(i-a-1, 0, INF)]
        prefix[i] += sum([prefix[clamp(i-a-j, 0, INF)] - prefix[clamp(i-a-j-1, 0, INF)] for j in range(1, b-a)])
        prefix[i] %= 1000

    for i in range(1, N+2):
        prefix[i] -= prefix[clamp(i - d, 0, INF)] - prefix[clamp(i-d-1, 0, INF)]
        prefix[i] %= 1000

    print(prefix)
    print(prefix[N+1]%1000)


if __name__ == "__main__":
    solution()
