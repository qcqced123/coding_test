import sys


def solution2():
    """
    idea: union-find
    """
    # union-find func
    sys.setrecursionlimit(10**6)
    def find(x: int) -> int:
        if disjoint[x] != x:
            disjoint[x] = find(disjoint[x])
        return disjoint[x]

    def union(y: int, x: int) -> None:
        y = find(y)
        x = find(x)
        if y < x:
            disjoint[x] = y
        else:
            disjoint[y] = x

    # get input data
    num = 1
    input = sys.stdin.readline
    while True:
        N, M = map(int, input().split())
        if not N and not M:
            break

        # init the disjoint array, graph
        disjoint = [i for i in range(N+1)]
        for _ in range(M):
            src, end = map(int, input().split())
            if find(src) != find(end):
                union(src, end)
            else:
                for i in range(1, N+1):
                    if disjoint[i] == disjoint[src] or disjoint[i] == disjoint[end]:
                        disjoint[i] = 0
                disjoint[src] = 0
                disjoint[end] = 0

        # answering the question
        answer = 0
        for i,v in enumerate(disjoint):
            if i and i == v:
                answer += 1

        if not answer: print(f"Case {num}: No trees.")
        elif answer == 1: print(f"Case {num}: There is one tree.")
        else: print(f"Case {num}: A forest of {answer} trees.")

        # go to next case
        num += 1


if __name__ == "__main__":
    solution2()
