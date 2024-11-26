import sys


def solution():
    """ 조합 찾아서, 여러 제약 조건 만족 시키기!, 비용도 최소....!
    약간 스쿼드 만드는 문제랑 비슷해!

    idea: backtracking
        - 제약 조건: 개별 영양소들의 합
        - 최소 비용이 되는 경우의 수 찾기
        - 스택 종료 조건: 개별 영양 성분 조건을 만족 하는 경우
        - 인자 정의: 현재 탐색할 재료의 번호(인덱스), 현재 배열의 cost
        - 탐색 대상: 개별 재료의 영양분 성분 배열

    point:
        - N 크기가 매우 작아서, backtracking 으로 풀라는 의도 같음
        - 1%에서 틀리는데, 왜 틀리지..?
        - 아니 진심 이해가 안감.......
        - 아니 진짜 개멍청하네...... 하
        - 아니 저거 오타 하.... ㄱ하 ㅏ진짜

    """
    # backtrack func
    sys.setrecursionlimit(10**6)
    def is_enough() -> bool:
        return nutrients[0] >= minimum[0] and nutrients[1] >= minimum[1] and nutrients[2] >= minimum[2] and nutrients[3] >= minimum[3]

    def backtrack(cnt: int, curr: int) -> None:
        nonlocal cost, cost_seq
        if is_enough():
            if curr < cost:
                cost = curr
                cost_seq.append((curr, seq[:]))
            return

        for i in range(cnt, N):
            np, nf, ns, nv, nc = ingredients[i]
            if curr + nc < cost:
                nutrients[0] += np
                nutrients[1] += nf
                nutrients[2] += ns
                nutrients[3] += nv
                seq.append(i+1)

                backtrack(i+1, curr+nc)

                nutrients[0] -= np
                nutrients[1] -= nf
                nutrients[2] -= ns
                nutrients[3] -= nv
                seq.pop()

    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())  # number of ingredient
    nutrients = [0]*4  # cache
    minimum = list(map(int, input().split()))
    ingredients = [tuple(map(int, input().split())) for _ in range(N)]  # 0~3: 영양성분, 4: 가격

    # do backtrack
    cost = INF

    seq, cost_seq = [], []
    backtrack(0, 0)
    if cost != INF:
        cost_seq.sort()
        print(cost)
        print(*cost_seq[0][1])

    else:
        print(-1)
        print()

if __name__ == "__main__":
    solution()
