import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: two pointer with hash, prefix sum
        - 오름 차순 정렬
        - 포인터 위치: 양 끝
        - 포인터 이동 방향:
            - left: forward
            - right: backward

        - 포인터 이동 조건:
            - left: forward
            - right: backward

    limit: N**3
    """
    # get input data
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    # init hash
    cache = dict()
    for i in range(N):
        for j in range(i+1, N):
            cache[(i,j)] = arr[i] + arr[j]

    # do two pointer
    answer = INF
    left, right = 0, N-1
    while left < right:
        temp = 0
        cnt = arr[left] + arr[right]
        for k,v in cache.items():
            if left not in k and right not in k:
                if abs(v-cnt) < answer:
                    answer = abs(v-cnt)
                    temp = v-cnt

        if temp >= 0:
            right -= 1

        else:
            left += 1

    print(answer)


def solution2():
    # get input data
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    # do two pointer
    answer = INF
    for i in range(N-3):
        for j in range(i+3, N):
            cnt = arr[i] + arr[j]
            left, right = i+1, j-1
            while left < right:
                temp = arr[left] + arr[right]
                answer = min(answer, abs(cnt-temp))
                if temp < cnt:
                    left += 1
                else:
                    right -= 1
    print(answer)

if __name__ == "__main__":
    solution2()
