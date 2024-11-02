import sys


def solution(routes):
    """
    제발 문제를 좀 읽으면서 풀었으면 좋켔어,,,, 잘 읽으면서 풀었으면, 금방 풀었잖아..........
    """
    answer = 0
    routes.sort(key=lambda x: x[1])

    last_camera = -sys.maxsize
    for i, j in routes:
        if last_camera < i:
            answer += 1
            last_camera = j

    return answer


if __name__ == '__main__':
    solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]])
