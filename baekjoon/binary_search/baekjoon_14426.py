import sys


def solution():
    """ N*M*S
    idea:
        - 역시 N**2 풀이는 터짐
    """
    input = sys.stdin.readline
    N, M = map(int, input().split())
    vocab = [input().rstrip() for _ in range(N)]
    prefix = [input().rstrip() for _ in range(M)]

    # prefix sum
    arr = set()
    for v in vocab:
        cnt = ""
        for i in range(len(v)):
            cnt += v[i]
            arr.add(cnt)

    # answering the question with hashing
    answer = 0
    for p in prefix:
        if p in arr:
            answer += 1
    print(answer)


if __name__ == "__main__":
    solution()
