import sys
INF = sys.maxsize
input = sys.stdin.readline


def sol_baekjoon_3020():
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


def sol_baekjoon_8983():
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
    idea: bfs with graph search
        - visited는 배열 인덱싱으로 구현하는게 시간 복잡도 측면에서 더 빠름
        - 세트가 공간 복잡도 측면에서 좀 더 효율적이지만, 인덱싱 연산보다 느림
    """
    from collections import deque, defaultdict

    # init the data structure
    N, M = map(int, input().split())  # nums of nods, nums of edge
    cache = [1] * (N+1)
    graph = defaultdict(list)
    for _ in range(M):
        child, parent = map(int, input().split())
        graph[parent].append(child)

    # do bfs
    for node in range(1, N+1):
        count = 0
        q = deque([node])
        visited = [0]*(N+1)
        visited[node] = 1
        while q:
            vx = q.popleft()
            for nx in graph[vx]:
                if not visited[nx]:
                    count += 1
                    q.append(nx)
                    visited[nx] = 1

        cache[node] += count

    answer, value = [], 0
    for i in range(1, N+1):
        if cache[i] > value:
            answer = [i]
            value = cache[i]

        elif cache[i] == value:
            answer.append(i)

    print(*answer)


def sol_baekjoon_2502():
    """ solution func of baekjoon 2502
    idea: dynamic programming
        - 1, 2일차를 규칙, 제약 조건에 의해서 무언가 예쁘게 찾을 수 없어서 완전 탐색 해야 하는 문제
        - 1, 2일차 값만 완전 탐색 시키고, 이후 계산은 dynamic programming 접근
        - 처음에 이 방법을 안썼던 이유가, 표면적으로 시간 복잡도 계산 하면 10만**2 이라서...
            - 1,2일차가 근데 10만 까지 갈 수가 없어서 시간 복잡도를 초과 하지 않음
    """
    N, D = map(int, input().split())
    cache = [0]*(N+1)

    # find the day 1, 2 value with brute force
    for i in range(1, D+1):
        for j in range(i, D+1):  # 1 <= A <= B
            cache[1] = i
            cache[2] = j
            for k in range(3, N+1):
                cache[k] = cache[k-1] + cache[k-2]

            if cache[N] == D:
                print(i)
                print(j)
                return


def sol_baekjoon_11561():
    """ solution func of baekjoon 11561
    idea: binary search
        - 첫 점프의 위치 값이 클수록, 최대 징검 다리 개수는 줄어듦
        - 따라서 첫 점프의 위치는 반드시 1이라고 가정 하고, 다음 점프 거리는 +1씩 늘리는게 맞음
        - 탐색 대상/범위: 최대 점프 거리 배열, 0 to N
        - 탐색 조건: 현재 기준 최대 점프 거리 까지의 합산 위치(T)가 N보다 크냐 작냐
            - T > N: r = mid - 1
            - T <= N: l = mid + 1, answer 기록
    """
    T = int(input())
    test = [int(input()) for _ in range(T)]

    # do bisect
    for t in test:
        answer = 0
        l, r = 1, t
        while l <= r:
            mid = (l+r) // 2
            if mid*(mid+1) // 2 <= t:
                answer = mid
                l = mid + 1

            else:
                r = mid - 1

        print(answer)


def sol_baekjoon_24041():
    """ solution func of baekjoon 24041
    idea: binary search
        - 제약 조건 k 해결이 관건인 문제
        - 뺄 수 있는 밀키트, 뺄 수 없는 밀키트 분리
        - 뺄 수 있는 밀키트 경우, 주어진 수식에 따라서 밀키트마다 가중치 값 계산하고, 정렬
        - 가중치 값 상위 K개의 밀키트를 빼고 이분 탐색 수행
        - 탐색 대상/범위: 최대일수, 1 to 2e+9
            - 범위의 최대값: 모든 입력이 최악의 경우라고 가정하면 저렇게 나옴
                - G = 1e+9, s = 1, L = 1e+9
                => 저런 경우, 최대 일수가 2e+9가 되기 때문
        - 탐색 기준: 현재 기준 일수 세균값(T)와 기준 세균값 G 비교
            - T <= G: 먹을 수 있는 경우, 정답 기록, 기준일수 늘리기
                - l = mid + 1

            - T > G: 먹을 수 없는 경우, 기준 일수 줄이기
                - r = mid - 1
    """
    # init the data structure
    N, G, K = map(int, input().split())
    important, not_important = [], []
    for _ in range(N):
        s, l, o = map(int, input().split())
        if not o: important.append((s,l,o))
        else: not_important.append((s,l,o))

    # do bisect with sorting
    answer = 0
    l, r = 1, int(2e+9)
    while l <= r:
        cnt = 0
        mid = (l+r) // 2
        for ms, ml, mo in important:
            cnt += ms*max(1, mid-ml)

        not_important.sort(key=lambda x: (-x[0]*max(1, mid-x[1])))
        for i in range(K, len(not_important)):
            nms, nml, _ = not_important[i]
            cnt += nms*max(1, mid-nml)

            if cnt > G:
                break

        if cnt > G:
            r = mid - 1

        else:
            answer = mid
            l = mid + 1

    print(answer)


def sol_baekjoon_15732():
    """ solution func of baekjoon 15732
    idea: binary search
        - 탐색 대상/범위: 마지막 상자의 번호, min(주어진 규칙) to max(주어진 규칙)
        - 탐색 기준: 현재 기준값을 마지막 상자의 번호로 만드는데 필요한 도토리 개수(T)와 기준 도토리 개수(D) 비교
            - T > D: 현재 상자 너무 많음!, r = mid - 1
            - T <= D: 현재 상자보다 더 필요함!, l = mid + 1, 정답 기록
    """
    N, K, D = map(int, input().split())

    mini = INF
    maxi = -INF
    rules = []
    for _ in range(K):
        src, end, steps = map(int, input().split())
        rules.append((src, end, steps))
        mini = min(mini, src, end)
        maxi = max(maxi, end)

    # do bisect
    answer = 0
    l, r = mini, maxi
    while l <= r:
        cnt = 0
        mid = (l+r) // 2
        for rule in rules:
            last_box = mid
            vs, ve, step = rule
            if vs > mid:
                continue

            if ve < mid:
                last_box = ve

            cnt += (last_box - vs) // step + 1
            if cnt >= D:
                break

        if cnt >= D:
            r = mid - 1
            answer = mid

        else:
            l = mid + 1

    print(answer)


def sol_baekjoon_1062():
    """ solution func of baekjoon 1062
    feedback:
        - 나는 처음에 주어진 단어를 기준으로 vocab을 업데이트 했음
            - N이 최대 50이라서, 최악의 경우면 시간 초과가 발생함
            - 그니까 단어 기준으로 백트래킹 하지 말고, 알파벳 기준으로 백트래킹 하면서, 주어진 단어들을 커버 가능한지 세는게 더 빠름
    idea: backtracking (combinations)
        - 전체 알파벳 중에서, 기본 vocab 포함 되는 애들 제외, 나머지 조합의 경우의 수 뽑기
        - 경우의 수마다, 최대 몇개의 글자 커버가 되는지 기록
    """
    from itertools import combinations

    N, K = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]

    # edge handling
    if K < 5:
        print(0)
        return

    elif K == 26:
        print(N)
        return

    # init the data structure
    vocab = [0]*26
    new_arr = [set(seq[4:-4]) for seq in arr]
    for c in ["a", "t", "n", "i", "c"]:
        vocab[ord(c) - ord("a")] = 1

    # do backtracking
    answer = 0
    iterator = [i for i in range(26) if not vocab[i]]
    combs = combinations(iterator, K-5)
    for comb in combs:
        for c in comb:
            vocab[c] = 1

        cache = 0
        for seq in new_arr:
            for s in seq:
                if not vocab[ord(s)-ord("a")]:
                    break
            else:
                cache += 1

        # record the answer and backtracking
        answer = max(answer, cache)
        for c in comb:
            vocab[c] = 0

    print(answer)


def sol_baekjoon_1038():
    """ solution func of baekjoon 1038
    idea: backtracking (combinations)
    """
    from itertools import combinations

    N = int(input())
    answer = []
    for i in range(1, 11):  # 자리수
        for comb in combinations(range(10), i):  # 숫자 경우의 수
            comb = list(map(str, sorted(comb, reverse=True)))
            answer.append(int("".join(comb)))

    answer.sort()
    try: print(answer[N])
    except: print(-1)


def sol_baekjoon_12869():
    """ solution func of baekjoon 12869
    idea: dynamic programming
        - 제약 조건: 주어진 SCV들 체력
            - 주어진 애들의 가능한 체력을 축으로 사용하자
            - 최대 3마리까지 가능 하니까, 3차원 dp cache 사용
            - 예외 처리 귀찮으니까 그냥 다 3마리 들어온다고 가정하자
            - 체력도 귀찮으니까 60으로 통일 시켜놓고 구하자
    """
    # init the data structure
    N = int(input())
    arr = list(map(int, input().split()))
    arr.extend([0, 0])  # for unified the scv count
    cache = [[[0]*61 for _ in range(61)] for _ in range(61)]  # init the 3d dp array cache

    # update the dp cache
    combs = (
        (9, 3, 1),
        (9, 1, 3),
        (3, 9, 1),
        (3, 1, 9),
        (1, 3, 9),
        (1, 9, 3),
    )
    cache[arr[0]][arr[1]][arr[2]] = 1
    for i in range(60, -1, -1):
        for j in range(60, -1, -1):
            for k in range(60, -1, -1):
                if cache[i][j][k]:
                    cnt = cache[i][j][k]
                    for comb in combs:
                        first, second, third = comb
                        ni = i-first if i-first > 0 else 0
                        nj = j-second if j-second > 0 else 0
                        nk = k-third if k-third > 0 else 0
                        if not cache[ni][nj][nk] or cnt + 1 < cache[ni][nj][nk]:
                            cache[ni][nj][nk] = cnt + 1
    print(cache[0][0][0]-1)


def sol_baekjoon_2632():
    """ solution func of baekjoon 2632
    idea: 부분합 && binary search
        - 원형큐 처리
            - 마지막 원소는 n-1개 처리
            - 마지막 원소도 n개 처리하면, 부분합 구할 때 중복 발생
        - A 배열의 가능한 모든 부분합 경우의 수 도출
            - 여기서 도출 되는 배열의 길이가 10만이라면, 무무무무조건 부분합 + 이분 탐색
            - 그래서 처음 원본 배열의 크기가 1000이면, 부분합 쓰는 문제라고 의심을 해봐야
        - 정렬
        - 이분 탐색
    """
    from bisect import bisect_left, bisect_right

    # init data structure
    input = sys.stdin.readline
    size = int(input())  # size of ordered pizza
    a_size, b_size = map(int, input().split())  # save size cache

    pizza_a = [int(input()) for _ in range(a_size)]
    pizza_b = [int(input()) for _ in range(b_size)]

    # make circular queue
    pizza_a += pizza_a[:-1]
    pizza_b += pizza_b[:-1]

    # make the sub seq sum array for each pizza type
    subseq_a, subseq_b = [], []
    for i in range(a_size):
        for j in range(1, a_size + 1):
            if i and j == a_size:
                continue

            subseq_a.append(sum(pizza_a[i:i + j]))

    for i in range(b_size):
        for j in range(1, b_size + 1):
            if i and j == b_size:
                continue

            subseq_b.append(sum(pizza_b[i:i + j]))

    subseq_a.sort()
    subseq_b.sort()

    # parametric search logic
    answer = subseq_a.count(size) + subseq_b.count(size)
    for i in subseq_a:
        cnt = size - i
        l_idx, r_idx = bisect_left(subseq_b, cnt), bisect_right(subseq_b, cnt)
        answer += r_idx - l_idx

    print(answer)


def sol_baekjoon_2533():
    return


def sol_baekjoon_17142():
    return


def sol_baekjoon_2613():
    return


def sol_baekjoon_17471():
    return


def sol_baekjoon_2688():
    return


def sol_baekjoon_2515():
    return


def sol_baekjoon_2666():
    return


def sol_baekjoon_2251():
    return


def sol_baekjoon_2602():
    return


def sol_baekjoon_21758():
    return


def sol_baekjoon_14226():
    return


def sol_baekjoon_10835():
    return


def sol_baekjoon_2585():
    return


def sol_baekjoon_15684():
    return


def sol_baekjoon_2616():
    return


def sol_baekjoon_16139():
    return


def sol_baekjoon_16973():
    return


if __name__ == '__main__':
    sol_baekjoon_2533()
