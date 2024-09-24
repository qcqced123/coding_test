import sys


def solution():
    """ 목재 절단기로 나무 자르기, 높이 최대값 리턴, ~O(N)

    idea: two-pointer
        1) 정렬
        2) 초기 연속 구간 합 구하기
        3) 원 포인터 초기화:
            - 포인터 위치: 시작
            - 포인터 방향: forward
            - 포인터 이동 조건:
                - >= M: left forward

        4) 그리고 추가로 높이 더 높일 수 있는지 계산
            - iteration break point: 합산 < M
            - index == 0, 나눌 떄 개수 다시 세기
    """
    N, M = map(int, sys.stdin.readline().split())
    trees = list(map(int, sys.stdin.readline().split()))
    trees.sort()

    l = 0
    cache = sum(trees) - trees[l]*N
    while l < N-1:
        next_tree = trees[l+1]
        cnt = cache - (next_tree - trees[l])*(N-l-1)
        if cnt >= M:
            l += 1
            cache = cnt
            continue

        break

    divisor = N if not l else N-l-1  #
    result = trees[l] + (cache - M) // divisor
    print(result)


if __name__ == "__main__":
    solution()
