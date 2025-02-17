import sys


def solution():
    """
    idea: two-pointer
        - 포인터 위치: 나란히
        - 포인터 방향: forward
        - 포인터 이동 조건:
            - left: 중복 원소 발생 시점
            - right: 중복 원소가 없는 경우
    feedback:
        - 내 풀이는 1개 짜리가 중복으로 정답에 들어가서 정확하게 구할 수 없음

    limit: NlogN
    """
    # get input data
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))

    # do two pointer
    answer = 0
    cache = set()
    left, right = 0, 0
    while right < N:
        cnt = arr[right]
        if cnt in cache:
            while cnt in cache:
                answer += right - left
                prev = arr[left]
                cache.remove(prev)
                left += 1

        right += 1
        cache.add(cnt)

    print(answer + (right-left)*(right-left+1) // 2)


def solution2():
    # get input data
    input = sys.stdin.readline
    N = int(input())
    cache = [0]*100001
    arr = list(map(int, input().split()))

    # do two pointer search
    answer = 0
    left, right = 0, 0
    while right < N:
        cnt = arr[right]
        prev = arr[left]
        if not cache[cnt]:
            cache[cnt] += 1
            right += 1

        else:
            answer += (right-left)
            cache[prev] -= 1
            left += 1

    answer += (right-left)*(right-left+1) // 2
    print(answer)


if __name__ == "__main__":
    solution()
