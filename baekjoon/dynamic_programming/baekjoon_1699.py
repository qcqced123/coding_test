import sys


def solution():
    """ 작거나 같은 제곱수들의 합, 100,000,000 (NlogN 이하)

    good input: 43

    idea: dynamic programming or two-pointer
        1) 배열 초기화
        2) 제곱근 배열 구하기
        3) 제곱근 배열 루프 돌리면서, 캐시값 초기화
    """
    N = int(input())
    dp = [0 for _ in range(0, N+1)]  # 인덱스 맞춰주자
    dp[1] = 1

    for i in range(2, N+1):
        cnt = sys.maxsize
        cnt_arr = list(range(1, int(pow(i, 1/2))+1))
        for j in cnt_arr:
            cnt = min(dp[i-j**2] + 1, cnt)
        dp[i] = cnt

    print(dp[-1])


if __name__ == "__main__":
    solution()
