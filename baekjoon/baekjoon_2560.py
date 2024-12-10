import sys


def solution():
    """
    idea: prefix sum
        - structure: prefix[i]
            - prefix[i]: i일에 남아 있는 짚신 벌레 숫자
    """
    # get input
    input = sys.stdin.readline
    a, b, d, N = map(int, input().split())
    prefix = [0]*(N+2)

    # update prefix cache
    # 인덱스-1 == 실제 날짜
    for i in range(1, N+2):
        if i < a+1:
            prefix[i] = 1
            continue

        add = i-a if i-a > -1 else 0
        add_ = add-1 if add-1 > -1 else 0

        suspend = i-b if i-b > - 1 else 0
        suspend_ = suspend-1 if suspend-1 > - 1 else 0

        death = i-d if i-d > -1 else 0
        death_ = death-1 if death-1 > -1 else 0

        prefix[i] = (
            prefix[i-1] +
            (prefix[add] - prefix[add_]) -
            (prefix[suspend] - prefix[suspend_]) -
            (prefix[death] - prefix[death_])
        ) % 1000

    print(list(range(N+2)))
    print(prefix)
    print(prefix[N+1] % 1000)


if __name__ == "__main__":
    solution()
