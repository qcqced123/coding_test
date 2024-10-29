import sys


def solution(n, times):
    """ NlogN
    idea: two pointer
        - 탐색 기준: 현재 시간에서 처리 가능한 인원(S)
            - S < N: left pointer move
            - S >= N: right pointer move
                - answer update
        - 탐색 범위: range(심사대 최소 시간*(N-1) + 1)
        - 종료 조건: l < r

    question:
        - S 계산을 못하겠음...
        => 현재 시간을 심사대별로 나눈 몫끼리 다 더해주면 되는구나

    feedback:
        - 현재 시간을 심사대별 소요 시간으로 나눈 몫끼리 더하기
        - 제발 배열 선언 좀 하지 말자, 입력 크기가 졸라 큰데 거기다가 배열 선언하면 당연히 터지지 않을까??
    """

    def calculate(v: int):
        """ calculate function of how many people in current time """
        result = 0
        for time in times:
            result += v // time
        return result

    def bisect(arr):
        nonlocal answer
        l, r = 0, arr
        while l < r:
            mid = (l + r) // 2
            if calculate(mid) < n:
                l = mid + 1

            else:
                r = mid
                answer = min(answer, mid)
        return

    answer = sys.maxsize
    minimum = min(times)

    time_arr = minimum * (n - 1)
    bisect(time_arr)
    return answer


if __name__ == '__main__':
    solution(6, [7, 10])
