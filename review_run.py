import sys


INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    insert your solution here
    """
    # disjoint-set
    def find(x: int) -> int:
        if x != disjoint[x]:
            disjoint[x] = find(disjoint[x])

        return disjoint[x]

    def union(y: int, x: int) -> None:
        y = find(y)
        x = find(x)
        if y < x:
            disjoint[x] = y
        else:
            disjoint[y] = x

    for _ in range(int(input())):
        # get input data
        # init data structure
        V, E = map(int, input().split())

        flag = 0
        disjoint = [i for i in range((V+1))]
        for _ in range(E):
            src, end = map(int,input().split())
            if find(src) != find(end):
                union(src, end)

            else: flag += 1

        multiple = 0
        for i in range(1, V+1):
            if i == disjoint[i]:
                multiple += 1

        if multiple > 1:
            print("YES")
        elif multiple == 1 and not flag:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solution()