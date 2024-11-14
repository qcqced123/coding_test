import sys


def solution():
    """ 특정 위치만 자르기 가능, 조각 개수별 가장 작은 조각의 최대값, 돌 빼기 문제랑 똑같네

    idea: binary search
        - 탐색 대상/범위: 케익 길이, 0 to L
        - 탐색 기준: 현재 기준값을 '최소값'으로 만드는데 몇번 잘라야 하는가?
            - 조각 개수가 아니라, 자른 횟수임
            - 자를 횟수 카운트 하려면 세트가 나을 것 같다고 생각했는데 틀림
    """
    # init data structure
    input = sys.stdin.readline
    N, M, L = map(int, input().split())  # 자르기 횟수, 위치 개수, 총 길이
    position = [int(input()) for _ in range(M)] + [L]  # 자르는 위치 배열

    # bisect
    for _ in range(N):
        answer = 0
        sub = int(input())  # 자르는 횟수
        l, r = 1, L  # 조각 길이의 최소값
        while l <= r:
            mid = (l+r) // 2
            prev, cut = 0, 0
            for pos in position:
                if pos - prev >= mid:
                    cut += 1
                    prev = pos

            if cut > sub:  # 여기에 꼭 괄호를 쓸 필요가 없구나, 거의 습관처럼, 괄호 포함해서 저렇게 넣었는데, 이것도 디버깅 대상에 포함하자
                answer = mid
                l = mid + 1

            else:
                r = mid - 1

        print(answer)


if __name__ == "__main__":
    solution()
