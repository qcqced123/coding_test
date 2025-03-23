import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: prefix sum
        - ascending sort by position value

    limit: NlogN
    """
    # get input data
    N, Q = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(N)]  # population, position
    cities.sort()


def solution2():
    # get input data
    N, Q = map(int, input().split())
    towns = [list(map(int, input().split())) for _ in range(N)]  # population, position
    towns.sort(key=lambda x: (x[1], x[0]))

    cnt = [-sum(towns[i][0] for i in range(N))]
    for i in range(N):
        cnt.append(cnt[-1] + towns[i][0]*2)


    print(towns)
    print(cnt)
    return


if __name__ == "__main__":
    solution2()
