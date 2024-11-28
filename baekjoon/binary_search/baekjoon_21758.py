import sys


def solution():
    """
    idea: 누적합
        - 벌과 벌통을 두는 방법에 따라서 경우의 수 3개로 분할
            => 벌 - 벌 - 벌통
            => 벌통 - 벌 - 벌
            => 벌 - 벌통 - 벌
    """
    # init data structure
    answer = 0
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)

    # bee - bee - house
    first_bee = arr[0]
    not_eat = first_bee
    for i in range(1, N):
        not_eat += arr[i]  # 두 번째 벌이 못먹는 꿀의 양
        answer = max(answer, total - first_bee - arr[i] + total - not_eat)

    # house - bee - bee
    first_bee = arr[-1]
    not_eat = first_bee
    for i in range(N-2, -1, -1):
        not_eat += arr[i]  # 두 번째 벌이 못먹는 꿀의 양
        answer = max(answer, total - first_bee - arr[i] + total - not_eat)

    # bee - house - bee
    # 슬라이싱 때문에 시간 초과
    # 누적합으로 풀어야 함
    first_bee = arr[0]
    last_bee = arr[-1]
    for i in range(1, N-1):
        answer = max(answer, total - first_bee - last_bee + arr[i])

    print(answer)


if __name__ == "__main__":
    solution()
