def solution():
    """ 정의: 반드시 '연속'하는 부분 문자열이어야
    idea: dynamic programming
        - if 서로 같은 문자일떄, dp[i][j] = dp[i-1][j-1] + 1
            - 이 떄, 정답도 갱신

    question:
        - python3에서 59%에 메모리 터짐
        - pypy3에서는 통과... 뭐지 심지어 pypy3이 일반적으로 메모리 더 먹는데.... 뭐지.....
    """
    # get input
    A = "." + input().rstrip()
    B = "." + input().rstrip()

    # do dynamic programming
    answer = 0
    size_a, size_b = len(A), len(B)
    cache = [[0]*size_a for _ in range(size_b)]
    for i in range(1, size_b):
        for j in range(1, size_a):
            if B[i] == A[j]:
                cache[i][j] = cache[i-1][j-1] + 1
                answer = max(answer, cache[i][j])
    print(answer)


if __name__ == "__main__":
    solution()
