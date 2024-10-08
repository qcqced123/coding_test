import sys


def my_solution(strs, t):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12983

    args:

    solution:
        1) 주어진 단어 조각 => 문장 완성
          - 단어 조각 무한개
        => t를 완성하기 위해 사용해야 하는 단어 조각의 최소값

    implementation:
        1) Dynamic Programming: Top-Down Approach
          - Recursive Call 사용
          - 역시나 시간초과
          - Memoization 도입
    """
    sys.setrecursionlimit(10 ** 5)
    answer = [999999999999999999]

    def top_down(curr: str, goal: str, count: int):
        if curr == t:
            answer[0] = min(answer[0], count)
            return

        for candidate in strs:
            if goal.startswith(candidate):
                top_down(curr + candidate, goal[len(candidate):], count + 1)

    top_down('', t, 0)
    answer = answer[0] if answer[0] != 999999999999999999 else -1
    return answer


def solution(strs, t):
    """  """
    length = len(t)
    dp, sizes = [0] + [float('inf')] * length, set(len(s) for s in strs)
    for i in range(1, length + 1):
        for size in sizes:
            if i - size >= 0 and t[i - size:i] in strs:
                dp[i] = min(dp[i], dp[i - size] + 1)

    return dp[-1] if dp[-1] != float('inf') else -1


def solution2(strs, t):
    """ 최소 문자열 개수
    idea: dynamic programming

    optimization point:
        1) strs 자료구조 변경:
            - 변경 이전: 리스트 (평균 140ms)
            - 변경 이후: 세트 (평균 40ms)

    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12983
    """
    test_strs = set(strs)
    INF = sys.maxsize
    dp = [0] + [INF] * len(t)
    for i in range(len(t)):
        for j in range(5):
            cnt = i - j
            if cnt > -1 and t[cnt:i + 1] in test_strs:  # optimization point (changing to set)
                forward = len(t[cnt:i + 1])
                dp[i + 1] = min(dp[i + 1 - forward] + 1, dp[i + 1])
    answer = -1 if dp[-1] == INF else dp[-1]
    return answer


if __name__ == '__main__':
    my_solution(["ba","na","n","a"], "banana")