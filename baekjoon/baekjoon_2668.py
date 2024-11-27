import sys


def solution():
    """
    idea: backtrack
        - 탐색 후보군 선정: set(line2)
        - line1, line2에 대한 추가 배열 생성
        - 스택 종료 조건:
        - 스택 호출 조건:
        - 인자 정의: 현재 탐색 대상 번호
        - 탐색 대상: line1 and line2 동시에
    """
    # backtrack func
    sys.setrecursionlimit(10**6)
    def backtrack(cnt: int) -> None:
        for i in range(cnt, N):
            cnt_line1 = line1[i]
            if cnt_line1 not in candidates:
                continue
            # 서로 같을 때
            cnt_line2 = line2[i]
            if cnt_line1 == cnt_line2:
                result.append(cnt_line1)
                backtrack(cnt+1)
            # 서로 다를 떄
            else:
                if not del_line1 or cnt_line2 not in del_line1:
                    del_line1.add(cnt_line2)


        return

    # init the data structure
    input = sys.stdin.readline
    N = int(input())
    line1 = list(range(1, N+1))
    line2 = [int(input()) for _ in range(N)]

    # get candidate
    candidates = set(line2)

    # do backtrack
    result = []
    del_line1, del_line2 = set(), set()
    backtrack(0)



if __name__ == "__main__":
    solution()
