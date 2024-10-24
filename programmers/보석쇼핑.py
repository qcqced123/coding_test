import sys


def solution(gems):
    """ 연속 수열, 모든 보석 1개 이상 포함, 가장 짧은 구간, NlogN
    조건을 만족하는 포인터 양끝 구간의 인덱스 리턴

    현재 포인터가 담고 있는 보석 현황도 기억해야 할 듯
    양쪽 대신, 나란히 둘까??

    모든 보석을 포함하고 있는지 판정하는 방법이 좀 까다로운데...?
    따로 플래그 변수를 두고, 사전의 벨류 값이 0 -> 1이 될 때만, 플래그 변수값을 업데이트 하도록 만들어서, 플래그 변수값이 세트값이랑 같을 때를
    플래그 변수 값 깎을 때도, 동일한 논리가 적용되게 설정

    탐색 종료로 설정

    idea: hash + two pointer
        1) 보석 종류: hash 사용
        2) two pointer:
            - 포인터 위치 초기화: 나란히
            - 포인터 이동 조건:
                - 모든 보석 포함 x: right pointer
                - 모든 보석 포함 o: left pointer
            - 포인터 탐색 종료 조건
    """
    INF = sys.maxsize
    answer = [1, INF]

    # init for two pointer
    l, r, cnt = 0, 0, 1
    cache = {k: 0 for k in gems}
    cache[gems[l]] = 1

    # search with two pointer
    while r < len(gems):
        # 모든 보석이 포함된 수열을 찾은 경우
        # 수열 길이 업데이트
        if cnt == len(cache):
            if r - l < answer[1] - answer[0]:
                answer[0] = l + 1
                answer[1] = r + 1

            cache[gems[l]] -= 1
            if not cache[gems[l]]:
                cnt -= 1

            l += 1

        # 수열 못찾은 경우
        else:
            r += 1
            if r < len(gems):
                if not cache[gems[r]]:
                    cnt += 1

                cache[gems[r]] += 1

    return answer


if __name__ == '__main__':
    solution()