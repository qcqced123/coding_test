import sys


def solution(n):
    """ 하노이 탑, 재귀
    idea: back tracking, stack
        1) stack 구현을 recursive call로
            - [src, end] 과정 자체를 프린팅
            - range(1, n+1).reverse()

        2) 스택 내부 구현
            append: 스택이 비었거나, < 가장 위에 원소


    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12946
    """
    answer = []
    sys.setrecursionlimit(10 ** 6)

    def recursive_func(n: int, src: int, to: int, mid: int) -> None:
        # end point
        if n == 1:
            answer.append([src, to])
            return

        recursive_func(n - 1, src, mid, to)
        answer.append([src, to])
        recursive_func(n - 1, mid, to, src)
        return

    recursive_func(n, 1, 3, 2)
    return answer


if __name__ == '__main__':
    solution()