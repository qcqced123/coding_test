import heapq


def solution(jobs):
    """
    idea: 대기 시간 최소화 (sorting)
        1) 처리 시간 = 대기시간 + 러닝타임
        2) 대기 시간 = 현재 시간 - 요청 시간

    => 처리 시간 = abs(현재 시간 - 요청 시간) + 러닝 타임
    """
    answer = 0
    return answer


if __name__ == '__main__':
    solution([[0, 3], [1, 9], [2, 6]])