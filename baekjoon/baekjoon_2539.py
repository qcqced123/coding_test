import sys


def solution():
    """ 주어진 색종이 장수대로 사용하되, 아직 사이즈는 미정, 가장 작은 색종이 크기 찾기
    모든 색종이는 반드시 도화지 밑변에 맞춰 붙여야 한다......

    idea: binary search
        - 생각하기 귀찮으니까, 색종이 크기 귀납적으로 추론하자
        - 탐색 대상/범위: 최소의 색종이 크기, 1 to max(row size)
        - 탐색 기준: 현재 기준 최소의 색종이 크기로 다 가리려면 몇장이 필요할까 (T)
            - if T >= S:
                현재 색종이 크기가 충분하다는 의미, r = mid - 1, 정답 기록
            - elif T < S:
                현재 크기가 부족하다는 의미!, l = mid + 1
    feedback:
        - 4%에서 틀림, 왜 틀리지...
            - 문제 조건좀 끝까지 읽자.... 멍충아
            - 색종이는 반드시 밑변에 붙어야 된다잖아
        - 22%에서 틀림... 이유를 모르겠어...
        - 처음 색종이 세팅이 틀림
            - 나는 아무 생각없이, 첫 색종이 세팅을 1 to mid로 뒀는데
            - 생각해보면, 첫 색종이는 가장 빨리나오는 구멍을 기준으로 세팅해야함
    """
    # init data structures
    input = sys.stdin.readline
    row, col = map(int, input().split())
    limit = int(input())  # S
    M = int(input())
    grid = [tuple(map(int, input().split())) for _ in range(M)]
    grid.sort(key=lambda x: x[1])

    # do bisect
    # 처음 x 세팅을 잘못함
    answer = 1
    l, r = 1, row
    while l <= r:
        cache = 1
        mid = (l + r) // 2  # current minimum
        end_y, end_x = mid, mid + grid[0][1] - 1  # current range of color paper
        for y, x in grid:
            if y <= end_y and x > end_x:
                cache += 1
                end_x = x + mid - 1

            if cache > limit or y > end_y:
                break

        else:
            answer = mid
            r = mid - 1
            continue

        l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
