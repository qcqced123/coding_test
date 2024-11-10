import sys


def solution():
    """ 크기가 다른 정육면체 상자들, N**3
    앞 상자가 뒤에 상자 보다 작으면 넣을 수 있음
    바로 뒤에 넣는 것보다, 다다다음에 넣는게 나을 수도 있음, 그리고 이전답을 활용해 현재 답을 만들어야!

    8
    1 6 2 5 7 3 5 6


    1, 2, 3, 5, 6 => 이렇게 5개가 최대임

    idea: dynamic programming
        -
    """
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * N

    for i in range(1, N):
        cnt = arr[i]
        for j in range(i):
            curr = arr[j]
            if curr < cnt:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


if __name__ == "__main__":
    solution()
