from typing import Tuple, List


def my_solution(num):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12943

    implementation:
        1) 최적의 부분 구조 찾기: 문제에서 주어짐
        2) 종료조건, 필요한 값 빼내기
    """
    answer = [0]

    def recursive_call(curr: int, count: int):
        if count > 500:
            answer[0] = -1
            return

        if curr == 1:
            answer[0] = count
            return

        if not curr % 2:
            recursive_call(curr / 2, count + 1)
        else:
            recursive_call(curr * 3 + 1, count + 1)

    recursive_call(num, 0)
    return answer[0]


def solution(num):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12943

    implementation:
        1) 최적의 부분 구조 찾기: 문제에서 주어짐
        2) 종료조건, 필요한 값 빼내기
    """
    def recursive_call(curr: int, count: int):
        if curr == 1:
            return count

        if count == 500:
            return -1

        if not curr % 2:
            return recursive_call(curr / 2, count + 1)  # 이렇게 return을 활용해보자
        else:
            return recursive_call(curr * 3 + 1, count + 1)

    return recursive_call(num, 0)


if __name__ == '__main__':
    solution()