import sys


def solution():
    """ NlogN, 카드 분배자 먼저 할당, 짝수
    idea:
        - 인덱스 == 짝수, 원소만 걸러내고, 거기서 가장 마지막 밑장보다 작은거 있으면 그거만 바꿔주면 되는거 아닌가??
        - 일단 문제 자체가 좀 이해가 안감

    question:
        - 문제 자체가 이해가 안감... 국어...
    """
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))

    player = [e for i, e in enumerate(arr) if not (i % 2)]
    player.sort(reverse=True)
    if player[-1] < arr[-1]:
        player[-1] = arr[-1]

    print(sum(player))


if __name__ == "__main__":
    solution()
