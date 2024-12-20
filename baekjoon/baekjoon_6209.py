import sys


def solution():
    """
    idea: parametric search
        - 탐색 대상/범위: 점프 최소 거리 배열, 1 to d
        - 탐색 기준: mid 값을 현재 경우의 수에서 거리의 최소로 만들기 위해서 몇 개의 돌을 빼야 하는가

    question:
        - 기존 파라매트릭 서치랑 똑같이 풀되, 뺀 돌의 개수가 정확히 m이랑 같을 때만, 정답값을 업데이트 하도록 했는데, 왜 틀릴까..ㅠ
    """
    # get input data
    input = sys.stdin.readline
    d, n, m = map(int, input().split())
    stones = [int(input()) for _ in range(n)] + [d]
    stones.sort()

    # do parametric search
    answer = 0
    l, r = 1, d
    while l <= r:
        mid = (l+r) // 2
        prev, del_stones = 0, 0
        for stone in stones:
            cnt = stone-prev
            if cnt < mid:
                del_stones += 1
            else:
                prev = stone

            if del_stones > m:
                break

        if del_stones > m:
            r = mid - 1

        else:
            if del_stones == m: answer = mid
            l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
