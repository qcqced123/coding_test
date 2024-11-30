import sys
from collections import Counter


def solution():
    """ QlogN
    루프 밖에서, 누적합 구하는 방식을 그대로 써서 미리, 가능한 모든 l,r 조합에 대해 대응하자
    idea: 누적합
        - 2D Table 구성
        - prefix[i][j]:
            prefix[i]: i번째 위치의 문자를 시작으로 하는 부분 배열의 알파벳 누적합
    """
    # init data structure
    input = sys.stdin.readline
    seq = input().rstrip()
    size = len(seq)

    # make the prefix sum array
    count = Counter(seq)
    prefix = [[0]*26 for _ in range(size)]
    for k, v in count.items():
        prefix[0][ord(k) - ord("a")] = v

    for i in range(1, size):
        cnt = seq[i-1]
        count[cnt] -= 1
        for k, v in count.items():
            prefix[i][ord(k)-ord("a")] = v

    # answering the query
    queries = []
    for _ in range(int(input())):
        target, l, r = map(str, input().split())
        l = int(l)
        r = int(r)
        queries.append((target, l, r))

    for query in queries:
        target, l, r = query
        if r + 1 == size: answer = prefix[l][ord(target)-ord("a")]
        else: answer = prefix[l][ord(target)-ord("a")] - prefix[r+1][ord(target)-ord("a")]

        print(answer) if answer >= 0 else print(0)


if __name__ == "__main__":
    solution()
