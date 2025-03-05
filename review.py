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
    """ solution func of baekjoon
    idea: dynamic programming with dfs, tree structure
        - 본인이 얼리 어답터가 되거나, 아니거나
        - dp[i][j]: i번째 노드가 얼리 어답터 이거나, 아니거나 최소의 얼리 어답터 숫자
    """
    from collections import defaultdict

    # dfs func
    sys.setrecursionlimit(10**6)
    def dfs(x: int):
        visited[x] = 1
        if len(graph[x]) == 1 and visited[graph[x][0]]:
            dp[x][0] = 0
            dp[x][1] = 1
            return

        for nx in graph[x]:
            if not visited[nx]:
                dfs(nx)
                dp[x][0] += dp[nx][1]
                dp[x][1] += min(dp[nx])

        dp[x][1] += 1


    # init data structure
    N = int(input())
    visited = [0]*(N+1)
    graph = defaultdict(list)
    dp = [[0]*2 for _ in range(N+1)]
    for _ in range(N-1):
        src, end = map(int, input().split())
        graph[src].append(end), graph[end].append(src)

    # update dp cache with dfs
    dfs(1)
    print(min(dp[1]))

    return


def sol_baekjoon_17142():
    """ solution func of baekjoon 17142
    idea: backtracking with bfs
        - 활성 바이러스 조합 뽑기
        - 조합 경우의 수마다 bfs 수행
        - 0 개수를 미리 세어주기
    feedback:
        - 비활성 바이러스 방문, 시간 처리:
            - 방문 X 방식: 비활성 바이러스 건너편에 빈 칸이 있으면, 도달할 수 없게 되어 틀림
            - 비활성 바이러스 시간 처리 x: 값 자체가 틀리게 나옴
            - 비활성 바이러스 시간 처리 0: 빈칸 없고 전부 비활성 바이러스인 경우 답이 틀림
            => 따라서, 비활성 바이러스를 만나면 시간 처리는 하되, 비활성 바이러스로부터 나오는 "시간값은 정답값 업데이트에 활용하지 않도록 만들자"
            => 이렇게 무시할 수도 있구나 싶어서... 참... 개어럽네...
    """
    from collections import deque
    from itertools import combinations

    # init data structure
    N, M = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # get virus position list, count how many empty space in current state of grid
    virus = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 2]
    zeros = 0
    for i in range(N):
        zeros += grid[i].count(0)

    # do backtrack with bfs, combinations
    answer = INF
    for comb in combinations(virus, M):
        # do bfs
        cache = 0
        zero_cache = zeros
        q = deque([])
        visited = [[0] * N for _ in range(N)]
        for y, x in comb:
            q.append((y, x, 0))
            visited[y][x] = 1

        while q:
            vy, vx, vc = q.popleft()
            if not grid[vy][vx]:
                cache = max(cache, vc)

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N and not visited[ny][nx] and grid[ny][nx] != 1:
                    nc = vc + 1
                    if not grid[ny][nx]:
                        zero_cache -= 1

                    visited[ny][nx] = 1
                    q.append((ny,nx,nc))

        if not zero_cache:
            answer = min(answer, cache)

    print(answer) if answer != INF else print(-1)


def sol_baekjoon_2613():
    """ solution func of baekjoon 2613
    idea: binary search
        - 탐색 대상/범위: 그룹 최대값 배열, min(arr) to max(arr)
        - 탐색 기준: 그룹 개수 조건을 하나 더 추가
            - 남은 원소 개수 == 그룹 개수
    """
    return


def sol_baekjoon_17471():
    """ solution func of baekjoon
    idea: bfs with backtrack
        - 조합 이용해 선거구 조합 구하기
        - 조합별 bfs 수행, 실제 가능한 선거구 조합인가 판정
            - 가능한 선거구 조합: 값 업데이트
            - 불가능한 선거구 조합: pass
    """
    from itertools import combinations
    from collections import deque, defaultdict

    # bfs func
    def bfs(curr: set) -> int:
        x = curr.pop()
        q = deque([x])
        visited = {x}
        people = population[x]
        while q:
            vx = q.popleft()
            for nx in graph[vx]:
                if nx in curr and nx not in visited:
                    q.append(nx)
                    visited.add(nx)
                    curr.remove(nx)
                    people += population[nx]

        if not curr: return people
        else: return -1

    N = int(input())
    population = [0] + list(map(int, input().split()))

    # init adj graph
    graph = defaultdict(list)
    for i in range(1, N+1):
        _, *temp = list(map(int, input().split()))
        graph[i].extend(temp)

    # make the combinations
    answer = INF
    sectors = set(range(1, N+1))
    for i in range(1, N//2+1):
        for comb in combinations(range(1, N+1), i):
            sector_a = set(comb)
            sector_b = sectors-sector_a
            X, Y = bfs(sector_a), bfs(sector_b)
            if X != -1 and Y != -1:
                answer = min(answer, abs(X-Y))

    print(answer if answer != INF else -1)


def sol_baekjoon_2688():
    """ solution func of baekjoon
    idea: dynamic programming
        - dp[i] = sum(dp[i:])
    """
    # outer loop for test case
    for _ in range(int(input())):
        N = int(input())
        cache = [1]*10
        for i in range(N-1):
            for j in range(10):
                cache[j] = sum(cache[j:])

        print(sum(cache))

    return


def sol_baekjoon_2515():
    """ solution func of baekjoon
    idea: binary search with binary search
        - sorting by height-benefit ascending
        - make the height array with bisect
        - update the dynamic programming cache
    """
    from bisect import bisect_right

    # init data structure
    N, S = map(int, input().split())
    pictures = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]

    # sorting by height-benefit ascending
    pictures.sort()

    # init height array
    uppers = [0]*(N+1)
    heights = [h for h, _ in pictures]
    for i in range(1, N+1):
        cnt = heights[i] - S
        idx = bisect_right(heights, cnt)
        uppers[i] = idx

    # update the dynamic programming cache
    dp = [0]*(N+1)
    for i in range(1, N+1):
        nh, nc = pictures[i]
        dp[i] = max(dp[i-1], dp[uppers[i]-1] + nc)

    print(max(dp))


def sol_baekjoon_2666():
    """ solution func of baekjoon
    idea: dynamic programming with 3d array, recursive call dp
        - dp[i][j][k]: i번째 오더에서 문이 현재 j,k에 위치할떄, 벽장문의 최소 이동 횟수
    """
    # search func
    sys.setrecursionlimit(10**6)
    def move(cnt, ny, nx) -> int:
        if cnt == K:
            return 0  # 이게 정확히 맞음

        curr = orders[cnt]
        dp[cnt][ny][nx] = min(
            abs(curr-ny) + move(cnt+1, curr, nx),
            abs(curr-nx) + move(cnt+1, ny, curr)
        )
        return dp[cnt][ny][nx]

    # init data structure
    N = int(input())
    sy, sx = map(int, input().split())
    K = int(input())
    orders = [int(input()) for _ in range(K)]

    # do update dynamic programming
    dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(K)]
    print(move(0, sy, sx))


def sol_baekjoon_2602():
    """ solution func of baekjoon
    idea: dynamic programming
        - if dp[i] or (not dp[i] and target[0]): 탐색 시작
    => 아니 이 방식은 현재 글자의 다음 글자가 뭔지 어떻게 알아, 그걸 알면 풀 수 있는데 그게 안되서 못해 이거

    feedback:
        - 3d cache, 축소 논리.........
    """
    target = input().rstrip()
    grid = [list(input().rstrip()) for _ in range(2)]
    size_target = len(target)
    size_bridge = len(grid[0])
    dp = [[[0]*2 for _ in range(size_target)] for _ in range(size_bridge)]

    # update dynamic programming cache
    for i in range(size_bridge):
        for j in range(size_target):
            for k in range(2):
                if grid[k][i] == target[j]:
                    if not j:
                        dp[i][j][k] = 1
                    else:
                        for z in range(i):
                            dp[i][j][k] += dp[z][j-1][1-k]
    # find answer
    answer = 0
    for i in range(size_bridge):
        for j in range(2):
            answer += dp[i][-1][j]
    print(answer)


def sol_baekjoon_21758():
    """ solution func of baekjoon
    idea: prefix sum
        - 경우의 수 세개로 분할
            1) 꿀 - 꿀 - 벌통
            2) 벌통 - 꿀 - 꿀
            3) 꿀 - 벌통 - 꿀
    """
    # init data structure
    N = int(input())
    arr = list(map(int, input().split()))

    # case 1. 벌 - 벌 - 벌통
    answer = 0
    total = sum(arr)
    bee1, bee2 = arr[0], arr[0]
    for i in range(1, N):
        bee2 += arr[i]
        answer = max(answer, total-bee1-arr[i] + total - bee2)

    # case 2. 벌통 - 벌 - 벌
    bee1, bee2 = arr[-1], arr[-1]
    for i in range(N-2, -1, -1):
        bee2 += arr[i]
        answer = max(answer, total-bee1-arr[i] + total - bee2)

    # case 3. 벌 - 벌통 - 벌
    bee1, bee2 = arr[0], arr[-1]
    for i in range(1, N-1):
        answer = max(answer, total-bee1-bee2+arr[i])

    print(answer)


def sol_baekjoon_10835():
    """ solution func of baekjoon
    idea: dynamic programming
        - 3가지 규칙 == 3가지 점화식 및 업데이트 방향
        - 왼쪽 카드 버리기: dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        - 왼쪽 오른쪽 카드 모두 버리기: dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
        - 오른쪽 카드 버리기:
            - 점수 카운트 가능한 경우: dp[i][j+1] += arr[j]
            - 점수 카운트 불가능한 경우: pass
    """
    N = int(input())
    left = list(map(int, input().split())) + [0]
    right = list(map(int, input().split())) + [0]
    dp = [[-1]*(N+1) for _ in range(N+1)]

    # update dp cache
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            # dump left card
            if dp[i][j] > -1:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])

                # dump left and right card
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])

                # dump right card
                cnt_left, cnt_right = left[i], right[j]
                if cnt_left > cnt_right:
                    dp[i][j+1] = max(
                        dp[i][j+1],
                        cnt_right+dp[i][j]
                    )
    # answering the question
    answer = 0
    for i in range(N+1):
        answer = max(answer, max(dp[i]))

    print(answer)


def sol_baekjoon_2585():
    """ solution func of baekjoon 2585
    idea: parametric search + bfs
        - 최적화 대상/범위: 최소 연료통 크기, 0 to (sqrt(2*10000**2) // 10) + 1
        - 최적화 기준:
        - grid[i][j]: i번째 노드에서 j번째 노드까지의 거리

    """
    from collections import deque

    # helper func
    def cal_energy(sy, sx, ey, ex) -> int:
        """ calculate the necessary energy between input two difference node by using distances
        """
        distance = pow((sy-ey)**2+(sx-ex)**2, 1/2)
        divisor, remain = divmod(distance, 10)
        return int(divisor) + 1 if remain else int(divisor)

    # bfs func
    def bfs(limit: int):
        visited = set()
        visited.add(0)
        q = deque([(0,0)])  # 노드 번호, 경유 0회
        while q:
            vy, vx = q.popleft()

            # end point of stack
            if grid[vy][n+1] <= limit:
                return 1

            # exception handling
            if vx >= k:
                continue

            for nx in range(1, n+2):
                if nx not in visited and grid[vy][nx] <= limit:
                    visited.add(nx)
                    q.append((nx, vx+1))

        return 0

    # input data structure
    n, k = map(int, input().split())
    position = [(0,0)] + [tuple(map(int, input().split())) for _ in range(n)] + [(10000,10000)]

    # make the distance table
    grid = [[0]*(n+2) for _ in range(n+2)]
    for i in range(n+2):
        src_y, src_x = position[i]
        for j in range(n+2):
            end_y, end_x = position[j]
            grid[i][j] = cal_energy(src_y, src_x, end_y, end_x)

    # do parametric search with bfs
    answer = 0
    l, r = 0, cal_energy(0,0, 10000, 10000)
    while l <= r:
        mid = (l+r) // 2
        if bfs(mid):
            r = mid - 1
            answer = mid
        else:
            l = mid + 1

    print(answer)


def sol_baekjoon_16139():
    """ solution func of baekjoon
    idea: prefix sum
        - 2d prefix array
            - prefix[i]: i번째 인덱스를 시작으로 하는 서브 시퀀스에 대한 알파벳 개수 세어주기
    """
    target = input().rstrip()
    size = len(target)
    N = int(input())

    # init queries list
    queries = []
    for _ in range(N):
        t, s, e = map(str, input().split())
        queries.append((t, int(s), int(e)))

    # init prefix sum array
    prefix = [[0]*26 for _ in range(size)]
    for char in target:
        prefix[0][ord(char) - ord("a")] += 1

    for i in range(1, size):
        for j in range(26):
            prefix[i][j] += prefix[i-1][j]

        cnt = target[i-1]
        prefix[i][ord(cnt) - ord("a")] -= 1

    # answering the questions
    for query in queries:
        t, s, e = query
        if e < size-1:
            print(prefix[s][ord(t)-ord("a")] - prefix[e+1][ord(t)-ord("a")])
        else:
            print(prefix[s][ord(t)-ord("a")])


def sol_baekjoon_19951():
    """ solution func of baekjoon
    idea: prefix sum
        - caching strategy
    """
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(M)]

    # init prefix sum
    cnt = 0
    cache = [0]*(N+1)
    for query in queries:
        start, end, weight = query
        cache[start-1] += weight
        cache[end] -= weight

    # do prefix sum
    for i in range(N):
        cnt += cache[i]
        arr[i] += cnt

    print(*arr)


def sol_baekjoon_16973():
    """ solution func of baekjoon
    idea: bfs with prefix sum
        - bfs로 출발지부터 목적지까지 최단거리 탐색을 하되, 해당 경로가 규칙에 맞는지 여부를 prefix sum 판정
        - prefix sum 수행해서, 현재 경로의 영역에 벽이 존재하는가 판정
            - 존재하면, 불가능한 경로 처리
            - 없다면, 가능한 경로 처리
            - prefix sum 점화식으로 판정하면 상수 시간 내에 판정이 가능함
            - 아니면, 부분 영역마다 루프를 돌려서 찾아야 되는데, 그리드 사이즈가 최대 1만 이라서, 탐색마다 1만을 탐색해야 할 수도 있음
    """
    from collections import deque
    def is_valid(y1, x1, y2, x2) -> int:
        result = 0
        if not grid[y1][x1] and not visited[y1][x1]:
            cnt = prefix[y2+1][x2+1] - prefix[y1][x2+1] - prefix[y2+1][x1] + prefix[y1][x1]
            if not cnt:
                result += 1
        return result

    # get input data
    N, M = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]
    row_size, col_size, y1, x1, end_y, end_x = map(int, input().split())

    # init grid, prefix
    prefix = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i-1][j-1]

    # do bfs
    y1 -= 1
    x1 -= 1
    end_y -= 1
    end_x -= 1

    q = deque([(y1, x1, 0)])
    visited = [[0]*M for _ in range(N)]
    visited[y1][x1] = 1
    while q:
        vy, vx, vc = q.popleft()
        for i in range(4):
            ny, nx = vy + dy[i], vx + dx[i]
            ny2 = ny + row_size - 1
            nx2 = nx + col_size - 1
            if -1 < ny < N and -1 < nx < M and -1 < ny2 < N and -1 < nx2 < M and is_valid(ny, nx, ny2, nx2):
                nc = vc + 1
                if ny == end_y and nx == end_x:
                    print(nc)
                    return
                visited[ny][nx] = 1
                q.append((ny, nx, nc))
    print(-1)


def sol_baekjoon_2251():
    """ solution func of baekjoon
    idea: bfs
    """


def sol_baekjoon_15684():
    """ solution func of baekjoon
        idea:
    """
    return


def sol_baekjoon_14226():
    """ solution func of baekjoon
    idea: bfs
    """
    return


def sol_baekjoon_5710():
    """ solution func of baekjoon
        idea:
    """
    return


def sol_baekjoon_2624():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_1451():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_2229():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_3067():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_1563():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_4781():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_28127():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_15573():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_13302():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_1707():
    """ solution func of baekjoon 1707
    idea: union-find
        - 복수개의 그래프: 무조건 이분 그래프
        - 단일 그래프: 내부에 사이클이 없어야 이분 그래프
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


def sol_baekjoon_6209():
    """ solution func of baekjoon 6209
    idea: parametric search
        - 최적화 대상/범위: 점프한 거리의 최소, 0 to D
        - 최적화 기준: 점프 최소 거리를 mid로 가정할 떄, 계산된 빼야할 돌의 개수와 기준값 M 사이의 비교
    """
    # get input data
    D, N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)] + [D] # element of stones
    arr.sort()

    # do parametric search
    answer = 0
    l, r = 0, D
    while l <= r:
        mid = (l+r) // 2
        prev, del_stones = 0, 0
        for stone in arr:
            cnt = stone - prev
            if cnt < mid:
                del_stones += 1

            else:
                prev = stone

            if del_stones > M:
                break

        if del_stones > M:
            r = mid - 1

        else:
            answer = mid
            l = mid + 1

    print(answer)


def sol_baekjoon_1941():
    """ solution func of baekjoon 1941
    idea: backtrack + bfs
        - queue:
        - direction:
        - combination 이용

    limit: 14!
    """
    from itertools import combinations
    from collections import deque, defaultdict

    # bfs func
    def bfs(y: int, x: int):
        # init data structure
        result = 0
        visited = set()
        visited.add((y,x))
        q = deque([(y, x)])

        # init cache
        cache = defaultdict(int)
        cache[grid[y][x]] += 1
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < 5 and -1 < nx < 5 and (ny,nx) not in visited and (ny*5+nx) in candidate:
                    q.append((ny, nx))
                    visited.add((ny, nx))
                    cache[grid[ny][nx]] += 1

        # check the current stack would be satisfied the limit condition
        if len(visited) == 7 and cache["S"] >= 4:
            result += 1

        return result

    answer = 0
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(input().rstrip()) for _ in range(5)]

    # linear search by combinations
    for candidate in combinations(range(25), 7):
        r, c = divmod(candidate[0], 5)
        candidate = set(candidate)
        answer += bfs(r,c)

    print(answer)

def sol_baekjoon_20183():
    """ solution func of baekjoon 20183
    idea: parametric search + bfs
        - 최적화 대상/범위: 내야 하는 최대 금액, min(edge) to max(edge)
        - 최적화 조건: mid를 지킬 떄, 계산된 total 값과 가진 돈 비교

        - queue: 좌표, 경로 전체 비용,
        - visited: 이게 문제네
    """
    from collections import deque, defaultdict

    # bfs func
    def bfs(limit: int) -> int:
        result = INF
        visited = dict()
        visited[A] = 0
        q = deque([(A, 0)])
        while q:
            vx, vc = q.popleft()
            if vc > visited[vx]:
                continue

            for nw, nx in graph[vx]:
                nc = vc + nw
                if nw <= limit:
                    if nx == B:
                        result = min(result, nc)

                    elif nx not in visited or nc < visited[nx]:
                        visited[nx] = nc
                        q.append((nx, nc))

        return result

    # get input data
    graph = defaultdict(list)
    N, M, A, B, C = map(int, input().split())

    # init graph, pointer
    answer = INF
    l, r = INF, 0
    for _ in range(M):
        src, end, cost = map(int, input().split())
        graph[src].append((cost, end)), graph[end].append((cost, src))
        l = min(l, cost)
        r = max(r, cost)

    # do bfs with parametric search
    while l <= r:
        mid = (l + r) // 2
        if bfs(mid) <= C:
            r = mid - 1
            answer = mid

        else:
            l = mid + 1

    print(answer if answer != INF else -1)


def sol_baekjoon_1800():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_9370():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_10800():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_1561():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_2878():
    """ solution func of baekjoon 2878
    idea:

    loss: squared error
        - (expectation - real)**2

    limit: NlogN
    """
    M, N = map(int, input().split())
    arr = [(int(input())) for _ in range(N)]
    arr.sort()

    return


def sol_baekjoon_2015():
    """ solution func of baekjoon 2015
    idea: prefix sum & hash
        - 투 포인터 x: 포인터 이동 조건이 없기 때문에
        - 대신 캐싱은 필요: 해시를 사용
    """
    from collections import defaultdict

    # get input data
    cache = defaultdict(int)
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # do prefix sum with hash
    cnt = 0
    answer = 0
    cache[0] = 1
    for element in arr:
        cnt += element
        curr = cache[cnt-K]
        if curr:
            answer += curr

        cache[cnt] += 1

    print(answer)


def sol_baekjoon_14948():
    """ solution func of baekjoon 11967
    idea: bfs with additional search direction
        - queue: 좌표, 경로상 가장 큰 타일값, 점프 횟수
        - visited: 여기 3차원 그리드로 표현
            - visited[i][j][k]: 현재 경로상 최대 블록값, 이거 기준으로 방문여부 판정
        - direction: 4방위로 구현, 루프 안쪽에 기본 거리, 뛰어넘기 거리도 포함해서 구현
    """
    from collections import deque

    # bfs func
    def bfs():
        visited[0][0][0] = grid[0][0]
        q = deque([(0, 0, 0)])
        while q:
            vy, vx, vj = q.popleft()
            vb = visited[vy][vx][vj]

            for i in range(4):
                # for common case
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < M:
                    nb = max(vb, grid[ny][nx])
                    if nb < visited[ny][nx][vj]:
                        visited[ny][nx][vj] = nb
                        q.append((ny,nx,vj))

                # for jumping case
                if not vj:
                    ny += dy[i]
                    nx += dx[i]
                    if -1 < ny < N and -1 < nx < M:
                        nb = max(vb, grid[ny][nx])
                        if nb < visited[ny][nx][1]:
                            visited[ny][nx][1] = nb
                            q.append((ny, nx, 1))

        return min(visited[-1][-1])

    # get input data
    N, M = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    visited = [[[INF, INF] for _ in range(M)] for _ in range(N)]
    grid = [list(map(int, input().split())) for _ in range(N)]


    # do bfs
    print(bfs())

def sol_baekjoon_11967():
    """ solution func of baekjoon 11967
    idea: bfs + hash
        - 스위치 시작 to 도착 정보를 해시로 저장
            - key: 시작
            - value: 도착

        - queue:
        - visited:
        - direction:
    """
    from collections import deque, defaultdict

    # bfs func
    def bfs():
        answer = 1
        visited = set()
        visited.add((1, 1))
        q = deque([(1, 1)])
        while q:
            vy, vx = q.popleft()
            for sy, sx in switches[(vy, vx)]:
                if not grid[sy][sx]:
                    answer += 1
                    grid[sy][sx] = 1

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if 0 < ny < N + 1 and 0 < nx < N + 1 and grid[ny][nx] and (ny, nx) not in visited:
                    q.append((ny, nx))
                    visited.add((ny, nx))

            for r in range(1, N + 1):
                for c in range(1, N + 1):
                    if grid[r][c] and (r, c) not in visited:
                        for i in range(4):
                            nr, nc = r + dy[i], c + dx[i]
                            if 0 < nr < N + 1 and 0 < nc < N + 1 and grid[nr][nc] and (nr, nc) in visited:
                                q.append((r, c))
                                visited.add((r, c))
                                break
        return answer

    # get input data
    N, M = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [[0] * (N + 1) for _ in range(N + 1)]

    # initialize hash
    switches = defaultdict(list)
    for _ in range(M):
        x, y, a, b = map(int, input().split())
        switches[(y, x)].append((b, a))

    # do bfs
    grid[1][1] = 1
    print(bfs())


def sol_baekjoon_5214():
    """ solution func of baekjoon 5214
    idea: bfs
        - queue:
        - visited:
        - direction:
    """
    from collections import deque, defaultdict

    # bfs func
    def bfs():
        visited = set()
        visited.add(1)
        q = deque([(1,1)])
        while q:
            vx, vc = q.popleft()
            for nx in graph[vx]:
                nc = vc
                if nx == N:
                    return nc + 1

                if nx not in visited:
                    if nx <= N:
                       nc += 1

                    visited.add(nx)
                    q.append((nx, nc))
        return -1

    # get input data
    graph = defaultdict(list)
    N, K, M = map(int, input().split())

    # init graph structure
    for i in range(1, M+1):
        cnt = list(map(int, input().split()))
        graph[N+i].extend(cnt)  # add hyper-tube to graph structure
        for j in range(K):
            graph[cnt[j]].append(N+i)

    print(bfs() if N > 1 else 1)


def sol_baekjoon_1114():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_2616():
    """ solution func of baekjoon
    idea: dynamic programming + prefix sum
        - structure: 3*N
        - dp[i][j]: ith 기관차 선택, jth 차량까지 고려, 최대 승객 숫자
    """
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    K = int(input())

    # init prefix sum array
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + arr[i]

    # update the dynamic programming cache
    dp = [[0] * (N + 1) for _ in range(4)]
    for i in range(1, 4):
        for j in range(K, N + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - K] + prefix[j] - prefix[j - K])

    print(dp[3][-1])


def sol_baekjoon_1525():
    """ solution func of baekjoon 1525
    idea: bfs with hash
        - visited: 이미 만들어 봤던 그리드 상태
        - queue:
    """
    from collections import deque

    # bfs func
    def bfs(y: int, x: int, path: str):
        visited.add(path)
        q = deque([(path, y, x, 0)])
        while q:
            vp, vy, vx, vc = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < 3 and -1 < nx < 3:
                    cnt = list(vp)
                    cnt[vy*3+vx], cnt[ny*3+nx] = cnt[ny*3+nx], "0"
                    np = "".join(cnt)
                    if np == result:
                        return vc+1

                    if np not in visited:
                        visited.add(np)
                        q.append((np, ny, nx, vc+1))
        return -1

    # init data structure
    result = "123456780"
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(3)]

    # find the starting point
    sy, sx = None, None
    for i in range(3):
        for j in range(3):
            if not grid[i][j]:
                sy, sx = i, j
                break

    # do bfs
    visited = set()
    sp = ""
    for i in range(3):
        sp += "".join(map(str,grid[i]))

    print(bfs(sy, sx, sp) if result != sp else 0)


def sol_baekjoon_20181():
    """ solution func of baekjoon 20181
    idea: dynamic programming + two-pointer
    """
    # get input data
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    # init dp cache, pointer position
    dp = [0]*(N+1)
    left, right, cnt = 0, 1, 0
    while right <= N:
        cnt += arr[right]
        dp[right] = dp[right-1]
        while cnt >= M:
            dp[right] = max(dp[right], dp[left-1] + cnt - M)
            cnt -= arr[left]
            left += 1

        right += 1

    print(dp[N])


def sol_baekjoon_15823():
    """ solution func of baekjoon 15823
    idea: parametric search, caching, hash
    """
    # get input data
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # do parametric search
    answer = 0
    l, r = 1, int(N//M)
    while l <= r:
        mid = (l+r) // 2
        cnt, starting = 0, 0
        while starting + mid <= N:
            cache = dict()
            for i in range(starting, starting+mid):
                curr = arr[i]
                if curr not in cache:
                    cache[curr] = i

                else:
                    starting = cache[curr] + 1
                    break
            else:
                cnt += 1
                starting += mid


        # determine the next searching element
        if cnt >= M:
            answer = mid
            l = mid + 1

        else:
            r = mid - 1

    print(answer if answer != INF else -1)


def sol_baekjoon_20159():
    """ solution func of baekjoon 20159

    limit: NlogN
    idea: prefix sum
        - my turn
        - enemy turn
    """
    # get input data
    N = int(input())
    arr = list(map(int, input().split()))

    # init cache value
    cache = sum(arr[::2])
    enemy = cache
    answer = cache  # not change

    # case 1
    for i in range(N-1, 0, -2):
        enemy += arr[i]
        enemy -= arr[i-1]
        answer = max(answer, enemy)

    # case 2
    enemy = cache
    for j in range(N-2, 1, -2):
        enemy -= arr[j]
        enemy += arr[j-1]
        answer = max(answer, enemy)

    print(answer)


def sol_baekjoon_13144():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_20366():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_22945():
    """ solution func of baekjoon
    idea:
    """
    return


def sol_baekjoon_10713():
    """ solution func of baekjoon 10713
    idea:
    """
    return


def sol_baekjoon_2208():
    """ solution func of baekjoon 2208
    idea:
    """
    return


def sol_baekjoon_2560():
    """ solution func of baekjoon 2560
    idea:
    """
    return

def sol_baekjoon_22345():
    """ solution func of baekjoon 22345
    idea:
    """
    return


if __name__ == '__main__':
    # sol_baekjoon_2533()
    # sol_baekjoon_17142()
    # sol_baekjoon_17471()
    # sol_baekjoon_2688()
    # sol_baekjoon_2666()
    # sol_baekjoon_2602()
    # sol_baekjoon_21758()
    # sol_baekjoon_2251()
    # sol_baekjoon_19951()
    # sol_baekjoon_16139()
    # sol_baekjoon_16973()
    # sol_baekjoon_10835()
    sol_baekjoon_1707()
