def solution(stones, k):
    """ 밟을 때마다 줄어듦, 한 번에 최대 k칸까지 건너뛰기 가능, 최단거리 최우선, 2억, 20만, NlogN

    idea: bisect, two-pointer
        - 탐색 대상/범위: (가장 작은 돌 ~ 가장 큰 돌)
        - 포인터 이동 기준: 현재 원소값을 시작점으로, 연속 증가하지 않는 수열의 개수 (S)
            - S >= K: right pointer backward
            - S < K: left pointer forward
    feedback:
        - 처음에 세팅한게 결국 맞았던거고, 대충 내 머리로 계산해보고 안되겠다 싶어서 던진건데....
        - 처음에 시간계산을 잘못했구나, NlogN이 되는게 맞고, 여기서 N은 5만이네, 그니까 시간 초과가 안나지
    """
    def get_longest_down(v: int) -> int:
        result = 0
        for stone in stones:
            if v > stone:  # 건너뛰기 정의 생각해보면, 미만만 잡는게 맞음
                result += 1
                if result >= k:
                    return 0
            else:
                result = 0

        return 1

    answer = 0
    l, r = 0, max(stones)
    while l <= r:
        mid = (l + r) // 2
        if get_longest_down(mid):
            answer = mid
            l = mid + 1
        else:
            r = mid - 1

    return answer


if __name__ == '__main__':
    solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
