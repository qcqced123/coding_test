import sys
from collections import defaultdict


def solution2():
    """
    idea: dynamic programming, prefix sum
        - 공 색깔별, 합산값 캐싱
        - 공 크기별, 개수값 캐싱
            - 본인 이상의 공 크기 개수만큼 빼줘야
    """
    # get input data, sort the arr by ascending
    input = sys.stdin.readline
    N = int(input())
    arr = [[i+1] + list(map(int, input().split())) for i in range(N)]  # player, color, size
    arr.sort(key=lambda x: (x[2], x[1]))

    # do prefix sum
    total = 0
    temp1, temp2 = (0,0), 0
    cache = [0]*(N+1)
    size_vocab = defaultdict(int)
    color_vocab = defaultdict(int)
    for player, color, size in arr:
        if temp1 == (color, size):
            cache[player] = temp2
        else:
            cache[player] = total - color_vocab[color] - size_vocab[size]*size

        color_vocab[color] += size
        size_vocab[size] += 1
        total += size  # 마지막에 업데이트, 본인 공은 빼야지
        temp1 = (color, size)
        temp2 = cache[player]

    # answering the question
    for i in range(1, N+1):
        print(cache[i], end="\n")

if __name__ == "__main__":
    solution2()
