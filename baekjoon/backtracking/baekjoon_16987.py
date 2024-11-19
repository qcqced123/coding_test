import sys


def solution():
    """ 틀릴 때마다 턱걸이 5회 (이럼 난 근육맨이 되어 있겠군), 가장 많은 계란 깨기
    내구도: 체력, 무게: 공격력
    idea: backtracking
        - 스택 종료 조건: 계란 번호 == 마지막 인덱스 + 1
        - 스택 호출 조건:
        - 인자 정의: 현재 공격자 계란 번호, 계란이 깨진 개수
    """
    # init the data structure
    input = sys.stdin.readline
    N = int(input())
    eggs = [list(map(int, input().split())) for _ in range(N)]  # 체력, 공격력

    # do the backtracking
    answer = 0
    sys.setrecursionlimit(10**6)
    def backtracking(cnt: int) -> None:
        nonlocal answer
        # end point of stack
        if cnt <= N:
            count = 0
            for i in range(N):
                if eggs[i][0] <= 0:
                    count += 1
            answer = max(answer, count)

        if cnt == N:
            return

        # init the state of current attacker
        hp, attack = eggs[cnt][0], eggs[cnt][1]
        if hp <= 0:
            backtracking(cnt+1)
            return

        # find the defender
        for i in range(N):
            d_hp, d_attack = eggs[i][0], eggs[i][1]
            if i == cnt or d_hp <= 0:
                continue

            # let's battle
            eggs[cnt][0] -= d_attack
            eggs[i][0] -= attack
            backtracking(cnt+1)

            eggs[cnt][0] += d_attack
            eggs[i][0] += attack

    backtracking(0)
    print(answer)


if __name__ == "__main__":
    solution()
