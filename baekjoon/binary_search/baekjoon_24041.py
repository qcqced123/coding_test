import sys


def solution():
    """ 재료 마다 유통 기한 다름, 2N*logN
    밀키트 유통 기한: 포함된 재료 중에서 가장 빠른거
    재료 별로 세균수 합친 다음, 기준 이하면 먹자
    input:
        부패 속도, 유통 기한, 중요도 여부(1이면 안중요해서 빼도 괜찮음)

    idea: binary search
        - 탐색 대상/범위: '몇 일째', 0 to G
        - 탐색 기준: 현재값(mid)을 기준 날짜로 볼떄, 세균수를 넘기냐 안넘기냐 (S)
            - S > G: r = mid - 1
            - S <= g: l = mid + 1, 정답 기록

        - 의문: K...는 우째요..?
        - 이분 탐색전, 배열 정렬

    question:
        - 역시나 틀림 (1%)
            - 정확하게 하려면, 현재 날짜를 기준으로, 빼줄 밀키트를 골라야 되는데, 그걸 도대체 어떻게 하는걸까??
            - 다른 사람들은 세균 수로 짤라야 된다는데
            - 시간 복잡도 때문에 현재 날짜를 기준으로 계산해서 정렬하면 안될거라 생각했는데, 해도 되는구나!
    feedback:
        - 이분 탐색 배열 최대값 세팅:
            G = 1e+9, S = 1, L = 1e+9 라면, 최대 2e+9일까지 버틸 수 있음
            따라서 최대값을 2e+9로 세팅해줘야 한다
    """
    # init the data structure
    input = sys.stdin.readline
    N, G, K = map(int, input().split())  # 재료, 기준 세균, 뺄 수 있는 친구들
    important, no_important = [], []
    for _ in range(N):
        s, l, o = map(int, input().split())
        if not o: important.append((s,l,o))
        else: no_important.append((s,l,o))

    # do bisect
    answer = 0
    l, r = 1, int(2e+9)
    while l <= r:
        cnt = 0
        mid = (l + r) // 2  # 현재 기준 일수
        for ms, ml, mo in important:  # linear search for must included kits
            cnt += ms * max(1, mid - ml)

        # 이게 시간 복잡도 때문에 안될거라 생각했는데
        no_important.sort(key=lambda x: (-x[0] * max(1, mid-x[1])))
        for i in range(K, len(no_important)):
            nms, nml, nmo = no_important[i]
            cnt += nms * max(1, mid - nml)

            if cnt > G:
                break

        if cnt > G:
            r = mid - 1
        else:
            answer = mid
            l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
