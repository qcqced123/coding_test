import sys


def solution():
    """ 뭐부터 때리는지에 따라서, 공격 횟수가 달라짐
    idea: dynamic programming
        - 3D dp cache
    feedback:
        - 제약 조건: SCV 체력
            - 그니까 각 차원을 가능한 SCV 체력 값으로 나열
            - 이걸 알아도 어렵다...;;;;
    """
    input = sys.stdin.readline
    N = int(input())
    scv = list(map(int, input().split()))
    scv.extend([0, 0])  # 3개보다 적게 들어왔을 때, 개수 맞춰주기
    cache = [[[0]*61 for _ in range(61)] for _ in range(61)]  # 3D dp cache
    cache[scv[0]][scv[1]][scv[2]] = 1  # 초기화, 원래 0으로 시작해야 되는데 캐시값 자체를 0으로 초기화해서 1로 초기화

    attack_comb = ((9, 3, 1), (9, 1, 3), (3, 1, 9), (3, 9, 1), (1, 3, 9), (1, 9, 3))
    for i in range(60, -1, -1):
        for j in range(60, -1, -1):
            for k in range(60, -1, -1):
                # start to updating the cache
                if cache[i][j][k]:
                    for c in attack_comb:
                        first, second, third = c
                        ni = i-first if i-first >= 0 else 0
                        nj = j-second if j-second >= 0 else 0
                        nk = k-third if k-third >= 0 else 0

                        cnt = cache[i][j][k] + 1
                        if not cache[ni][nj][nk] or cnt < cache[ni][nj][nk]:
                            cache[ni][nj][nk] = cnt
    print(cache[0][0][0] - 1)  # 초기에 1을 임의로 더했기 때문에 빼줘야 정확함



if __name__ == "__main__":
    solution()
