import sys
INF = sys.maxsize
input = sys.stdin.readline


def solution1():
    """ baekjoon 3020
    idea: binary search
        - 탐색 대상/범위: 높이구간
    """
    from bisect import bisect_left

    input = sys.stdin.readline
    N, H = map(int, input().split())  # 장애물 개수,

    # make the 석순, 종유석 리스트
    # bisect 방식을 통일 하기 위해, 종유석 리스트는 천장 높이값에서 뺀 값을 저장
    up_list, down_list = [], []
    for i in range(N):
        cnt = int(input())
        if not i % 2: up_list.append(cnt)
        else: down_list.append(H-cnt)

    up_list.sort(), down_list.sort()

    # linear search by each height range
    # 파괴 해야 하는 석순 개수: 전체 석순 개수 - 인덱스
    # 파괴 해야 하는 종유석 개수: 인덱스
    answer, cache = sys.maxsize, 0
    for h in range(1, H+1):
        up, down = bisect_left(up_list, h), bisect_left(down_list, h)
        curr = N // 2 - up + down
        if curr < answer:
            answer = curr
            cache = 1

        elif curr == answer:
            cache += 1

    print(answer, cache)


def solution2():
    """ baekjoon 8983
    idea: binary search
        - "잡을 수 있는 동물 카운트" 기준: 주어진 사로들 중에서 한 곳에서라도, 잡을 수 있다면 카운트
        - 탐색 대상/범위:
            - 겉루프: 동물
            - 이진 탐색용 속루프: 사로 배열 (인덱스)
        - 탐색 기준: 현재 사로가, 현재 동물을 잡을 수 있는 범위에 포함되는지
            - 포함되지 않을 떄 & 더 크다면: R backward
            - 포함되지 않을 떄 & 더 작으면: l forward
    """
    # get input and make data structure for problem solving
    input = sys.stdin.readline
    M, N, L = map(int, input().split())  # 사로 개수, 동물 숫자, 최대 사정거리
    guns = list(map(int, input().split()))
    animals = [map(int, input().split()) for _ in range(N)]
    guns.sort()

    # for-loop of animals
    answer = 0
    for x, y in animals:
        l, r = 0, M - 1
        mini = x + y - L
        maxi = x - y + L
        while l <= r:
            mid = (l+r) // 2
            if mini <= guns[mid] <= maxi:
                answer += 1
                break

            elif guns[mid] > maxi:
                r = mid - 1

            else:
                l = mid + 1

    print(answer)


def solution3():
    """ baekjoon 1939
    idea: binary search with bfs, dfs
    """
    from collections import deque, defaultdict
    def bfs(x:int, y: int, weight: int) -> int:
        q = deque([(x, INF)])
        visited = [0]*(N+1)
        visited[x] = 1

        while q:
            vx, vl = q.popleft()
            for nx, nl in graph[vx]:
                if not visited[nx] and nl >= weight:
                    visited[nx] = 1
                    q.append((nx, nl))

        if visited[y]: return 1
        else: return 0

    # get the input and make the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 노드, 엣지
    graph = defaultdict(list)

    l, r = 0, 0
    for _ in range(M):
        s, e, limit = map(int, input().split())
        graph[s].append((e, limit)), graph[e].append((s, limit))
        r = max(r, limit)

    answer = 0
    src, end = map(int, input().split())
    while l <= r:
        mid = (l+r) // 2
        if bfs(src, end, mid):
            answer = mid
            l = mid + 1

        else:
            r = mid - 1

    print(answer)


def sol_baekjoon_1939():
    """ baekjoon 1939 with dfs & binary search
    """
    from collections import defaultdict
    # dfs function
    sys.setrecursionlimit(10**6)
    def dfs(x: int):
        """ 스택 종료 조건: 도착지점 도착 그리고 제약 사항 통과
        """
        if x == end:
            return 1

        for nx, nl in graph[x]:
            if not visited[nx] and nl >= mid:
                visited[nx] = 1
                cnt = dfs(nx)
                if cnt:
                    return 1
        return 0

    # get the input and make the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 노드, 엣지
    graph = defaultdict(list)

    l, r = 0, 0
    for _ in range(M):
        s, e, limit = map(int, input().split())
        graph[s].append((e, limit)), graph[e].append((s, limit))
        r = max(r, limit)

    answer = 0
    src, end = map(int, input().split())
    while l <= r:
        mid = (l+r) // 2
        visited = [0]*(N+1)
        if dfs(src):
            answer = mid
            l = mid + 1

        else:
            r = mid - 1

    print(answer)


def sol_baekjoon_2302():
    """ solution func of baekjoon 2302
    idea: dynamic programming
        - 주어진 좌석 N개에 대한 경우의 수 계산 (VIP 좌석 고려 X)
        - dp[i] = dp[i-1] + dp[i-2]
        - VIP 좌석 배치 이후, 구간별 경우의 수끼리 곱하기
        - exception handling:
            - M == 0일때는 VIP 좌석이 없기 때문에, 캐시 배열에서 곧바로 경우의 수 리턴해야 한다
    """
    N = int(input())
    M = int(input())
    cache = [0]*(N+1)
    seats = [int(input()) for _ in range(M)]

    # do dynamic programming
    cache[0], cache[1] = 1, 1
    for i in range(2, N+1):
        cache[i] = cache[i-1] + cache[i-2]

    # do assign the VIP seats
    answer = 1
    if M > 0:
        prev = 0
        for i in seats:
            answer *= cache[i-prev-1]
            prev = i
            if i == seats[-1]:
                answer *= cache[N-i]
    else: answer = cache[N]
    print(answer)


def sol_baekjoon_2631():
    """ solution func of baekjoon 2631
    idea: dynamic programming
        - 현재 제대로 배치된 애들 빼고 다 재배치 필요
        - 그래서 제대로 배치된 애들 길이 중에 제일 긴거 구하기
        - 가장 긴 증가하는 수열 길이를 구하고 전체 수열 길이에서 빼주기
        - 시간 복잡도가 매우 여유로워서 N**2인 dynamic programming으로 해결 가능함
    """
    # init the data structure
    N = int(input())
    cache = [1]*N
    children = [int(input()) for _ in range(N)]

    # do the dynamic programming
    for i in range(1, N):
        for j in range(i):
            if children[i] > children[j]:
                cache[i] = max(cache[i], cache[j] + 1)

    print(N-max(cache))


def sol_baekjoon_2458():
    """ solution func of baekjoon 2458
    idea: floyd-warshall (dynamic programming)
        - "자신의 순서를 알 수 있다" == "모든 노드와 연결 되어 있다"
            - "연결": in-bound, out-bound 노드 개수 합산

        - 다른 노드를 경유해서 자신에게 오는 in-bound 노드까지 세어주려면 floyd-warshall 사용
        - 연결 되는 모든 노드 판정용으로 플루이드 워셜을 사용할 수 있다는 것을 반드시 기억하자

    """
    # init the data structure
    N, M = map(int, input().split())
    cache = [[0]*(N+1) for _ in range(N+1)]  # for floyd-warshall
    for _ in range(M):
        src, end = map(int, input().split())
        cache[src][end] = 1

    # do the dynamic programming
    for k in range(1, N+1):
        for y in range(1, N+1):
            for x in range(1, N+1):
                if cache[y][k] and cache[k][x]:
                    cache[y][x] = 1

    # calculating the in-bound and out-bound nodes
    answer = 0
    for y in range(1, N+1):
        cnt = 0
        for x in range(1, N+1):
            cnt += cache[y][x] + cache[x][y]

        if cnt == N-1:
            answer += 1

    print(answer)


def sol_baekjoon_15989():
    """ solution func of baekjoon 15989
    idea: dynamic programming
    """
    N = int(input())
    cache = [1]*10001
    test = [int(input()) for _ in range(N)]

    # do the dynamic programming
    # case of adding the number "2"
    for i in range(2, 10001):
        cache[i] += cache[i-2]

    # case of adding the number "3"
    for i in range(3, 10001):
        cache[i] += cache[i-3]

    # answering the question
    for t in test:
        print(cache[t])


def sol_baekjoon_4811():
    """ solution func of baekjoon 15989
    idea: dynamic programming
        - 제약 조건: w 개수, h 개수
            - 행: w 개수 나열
            - 열: h 개수 나열
        - dp[i][j] = dp[i-1][j] + dp[i][j-1] (w추가 경우의 수 + h추가 경우의 수)
    """
    arr = []
    while True:
        t = int(input())
        if not t:
            break
        arr.append(t)

    cache = [[0]*31 for _ in range(31)]

    # do update the dp cache
    cache[1][0], cache[1][1] = 1, 1
    for i in range(2, 31):
        for j in range(i+1):
            cache[i][j] = cache[i-1][j] + cache[i][j-1]

    for i in arr:
        print(cache[i][i], end='\n')

    return


def sol_baekjoon_5557():
    """ solution func of baekjoon 5557
    idea: dynamic programming
        - 제약 조건: 모든 중간 계산 결과는 0 이상, 20 이하
        - 행: 피연산자 (마지막 원소 제외)
        - 열: 제약 조건 나열
        - 기타 리스트 문제랑 논리 구조가 똑같음

    """
    # init the data structure
    N = int(input())
    arr = list(map(int, input().split()))
    cache = [[0]*21 for _ in range(N-1)]

    src = arr[0]
    last = arr[-1]
    arr = arr[:-1]

    # do update the dp cache
    cache[0][src] = 1
    for i in range(1, N-1):
        cnt = arr[i]
        for j in range(21):
            if j+cnt <= 20:
                cache[i][j] += cache[i-1][j+cnt]

            if j-cnt >= 0:
                cache[i][j] += cache[i - 1][j-cnt]

    print(cache[-1][last])


def sol_baekjoon_15990():
    """ solution func of baekjoon 15990
    idea: dynamic programming
        - 제약 조건: 같은 숫자 연속 사용 불가
        - 1로 끝난 경우: 2 또는 3을 이어 붙일 수 있음
        - 2로 끝난 경우: 1 또는 3을 이어 붙일 수 있음
        - 3으로 끝난 경우: 1 또는 2를 이어 붙일 수 있음

    => 도둑질 문제랑 똑같다
    """
    # init the data structure
    N = int(input())
    size = 100001
    test = [int(input()) for _ in range(N)]
    cache = [[0]*3 for _ in range(size)]

    # do update the dp cache
    cache[1], cache[2], cache[3] = [1, 0, 0], [0, 1, 0], [1, 1, 1]
    for i in range(4, size):
        cache[i][0] = (cache[i-1][1] + cache[i-1][2]) % 1000000009
        cache[i][1] = (cache[i-2][0] + cache[i-2][2]) % 1000000009
        cache[i][2] = (cache[i-3][0] + cache[i-3][1]) % 1000000009

    # answering the question
    for t in test:
        print(sum(cache[t]) % 1000000009)


def sol_baekjoon_1325():
    """ solution func of baekjoon 1325
    idea:
    """


def sol_baekjoon_2502():
    """ solution func of baekjoon 2502
    idea:
    """


def sol_baekjoon_11561():
    """ solution func of baekjoon 11561
    idea:
    """


def sol_baekjoon_24041():
    """ solution func of baekjoon 24041
    idea:
    """


def sol_baekjoon_15732():
    """ solution func of baekjoon 15732
    idea:
    """


def sol_baekjoon_1062():
    """ solution func of baekjoon 1062
    idea:
    """


def sol_baekjoon_1038():
    """ solution func of baekjoon 1038
    idea:
    """


def sol_baekjoon_12869():
    """ solution func of baekjoon 12869
    idea:
    """


def sol_baekjoon_2632():
    """ solution func of baekjoon 2632
    idea:
    """


if __name__ == '__main__':
    sol_baekjoon_1325()
