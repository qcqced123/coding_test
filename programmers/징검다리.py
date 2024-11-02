def solution(distance, rocks, n):
    """
    idea: binary search
        - 탐색 대상/범위: 시작 to 종점
        - 포인터 이동 조건: 현재 거리값을 "최소 거리"로 만들려면, 바위를 몇개 빼야 하는가 (S)
            - if S > N: right pointer backward
            - else: left pointer forward
        - 바위 몇개 빼야 하는지 카운트

    """
    answer = 0
    rocks.sort()
    l, r = 0, distance
    while l <= r:
        mid = (l+r) // 2
        prev, delete = 0, 0
        for rock in rocks:
            # 현재 거리값보다, 계산한 거리가 짧으면 안되니까, 돌 빼버려야지
            if rock - prev < mid:
                delete += 1

            else:
                prev = rock

            if delete > n:
                break

        if delete > n:
            r = mid - 1

        else:
            answer = mid
            l = mid + 1

    return answer


if __name__ == '__main__':
    print(solution(25, [2, 14, 11, 21, 17], 2))
