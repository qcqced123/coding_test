import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: two pointer
        - 포인터 위치: 나란히
        - 포인터 방향: forward
        - 포인터 이동 조건: D 만족 여부

    limit: NlogN
    """
    N, D = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort()

    # do two pointer
    answer, temp = 0, 0
    left, right = 0, 0
    prev, prev_v = arr[left][0], arr[left][1]
    while right < N:
        # index for updating the cache
        cnt = arr[right][0]
        cnt_v = arr[right][1]
        temp += cnt_v

        if cnt - prev >= D:
            while cnt - prev >= D:
                temp -= prev_v
                left += 1
                prev = arr[left][0]
                prev_v = arr[left][1]

        right += 1
        answer = max(answer, temp)

    print(answer)

if __name__ == "__main__":
    solution()
