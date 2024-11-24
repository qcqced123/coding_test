import sys


def solution():
    """
    idea: dynamic programming
        - "정수배" 라는 언급
        - 제약 조건: 고객
            - 최소 비용 구하기
            - 행: 도시
            - 열: 고객 숫자
    """
    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    C, N = map(int, input().split())
    cache = [[INF]*(C+1) for _ in range(N+1)]
    costs, people = [], []
    for _ in range(N):
        c, p = map(int, input().split())
        costs.append(c), people.append(p)

    # update the cache
    for y in range(1, N+1):
        cost = costs[y-1]
        person = people[y-1]
        for x in range(1, C+1):
            cache[y][x] = min(cache[y-1][x], cache[y][x])
            i, j = divmod(x, person)
            if not j:
                cache[y][x] = min(cache[y][x], cost*i)

            cache[y][x] = min(cache[y][x], cache[y-1][x-person] + cost)

    for i in range(N+1):
        print(cache[i], end='\n')


    print(cache[-1][-1])


if __name__ == "__main__":
    solution()
