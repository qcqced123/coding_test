import sys
from collections import defaultdict


def solution():
    """ 배열 크기 동일 (인덱스 동일)
    합이 0인 쌍의 개수, 입력이 세로네
    (쌍 카운트 기준: 인덱스)

    idea 1: N**2 + N**2 + N**2
        1) A & B 합의 쌍
        2) 1에서 구한 쌍이랑 C랑 쌍 구하기
        3) 2에서 구한 쌍이랑 D랑 쌍 구하기
            - 합이 0이면 카운트
        => 이렇게 하면 중간에 16,000,000*4,000 이 되고, 시간 터짐
        => 버려,,,,
    """
    input = sys.stdin.readline
    N = int(input())

    A, B, C, D = [], [], [], []
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        A.append(a), B.append(b), C.append(c), D.append(d)

    sum_vocab = defaultdict(lambda: 0)  # convert to dict
    for i in range(N):
        for j in range(N):
            cnt = A[i] + B[j]
            sum_vocab[cnt] += 1

    # 애초에 이렇게 구하면 터지네
    # 여기 안터지게 못함?
    first_arr = list(sum_vocab.keys())
    for i in range(len(first_arr)):  # 합이 하나도 안겹치면 여기가 16,000,000
        for j in range(N):  # 여기 4000
            cnt = first_arr[i] + C[j]
            sum_vocab[cnt] += 1

    result = 0
    for i in range(N):
        cnt = D[i]
        if sum_vocab[0-cnt] > 0:
            result += sum_vocab[0-cnt]

    print(result)


if __name__ == "__main__":
    solution()
