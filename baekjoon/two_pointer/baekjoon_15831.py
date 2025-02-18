import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: two pointer
        - 배열 원소 전처리: 문자열 to 정수
        - 조건을 만족하는 연속 부분 배열 찾기
        - 포인터 위치: 나란히
        - 포인터 이동 방향: forward
        - 포인터 이동 조건: 주어진 조건 만족 여부

    limit: NlogN
    """
    # get input data
    N, B, W = map(int, input().split())
    arr = list(map(str, input().rstrip()))

    # preprocess: string to int
    path = []
    for v in arr:
        if v == "B": path.append(0)
        else: path.append(1)

    # caching the current state of path
    cache = [0]*2

    # do two pointer
    answer = 0
    left, right = 0, 0
    while right < N:
        cnt = path[right]
        cache[cnt] += 1
        if cache[0] > B:
            while cache[0] > B:
                temp = path[left]
                cache[temp] -= 1
                left += 1

        if cache[1] >= W:
            answer = max(answer, right-left+1)

        right += 1

    print(answer)


if __name__ == "__main__":
    solution()
