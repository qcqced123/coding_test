import sys


def solution():
    """ 능력치 합 최대 스쿼드 찾기
    idea: backtracking
        - 스택 종료:
        - 스택 호출: 현재 플레이어의 포지션 값이 0이 아니고, 스쿼드의 해당 포지션이 비어있는 경우
        - 인자 정의: 현재 탐색 대상 플레이어 번호
        - 탐색 대상: 플레이어의 포지션 오버롤 리스트
    """
    # init the data structure
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    for _ in range(int(input())):
        answer = 0
        squad = [0]*11
        info = [list(map(int, input().split())) for _ in range(11)]

        # backtrack func
        def backtrack(number: int):
            nonlocal answer
            # end point of stack call
            if number == 11:
                answer = max(answer, sum(squad))
                return

            for i in range(11):
                cnt = info[number][i]
                if cnt and not squad[i]:
                    squad[i] = cnt
                    backtrack(number+1)
                    squad[i] = 0  # backtrack

        backtrack(0)
        print(answer)


if __name__ == "__main__":
    solution()
