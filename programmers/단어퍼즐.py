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


if __name__ == '__main__':
    my_solution(["ba","na","n","a"], "banana")