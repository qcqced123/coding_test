import sys
from collections import deque


def solution():
    """ 십진수 저장 (최대 4자리)
    주어진 규칙에 맞게 숫자 변환

    A to B, 최소 명령어 나열 (명령어 시퀀스 길이 기준 업데이트)

    idea: BFS
        1000000 (가수), value (실제값)
        1) 더미값 준비: 자리수 유지
    """

    N = int(input())
    commands = ['D', 'S', 'L', 'R']
    for _ in range(N):
        src, end = map(int, sys.stdin.readline().split())  # dtype must be int

        # double queues
        visited = [0]*10000  # 좋은 방법인듯
        value_q = deque([src])
        sequence_q = deque([""])

        while value_q:
            vx = value_q.popleft()
            vs = sequence_q.popleft()

            # return the result
            if vx == end:
                print(vs, end='\n')
                break

            for i in commands:
                if i == 'D':
                    nx = (2*vx) % 10000

                elif i == 'S':
                    nx = vx - 1 if vx else 9999

                elif i == 'L':
                    nx = (vx % 1000)*10 + vx // 1000  # 이거 수식 떄문에 복습

                else:
                    nx = (vx % 10)*1000 + vx // 10

                if not visited[nx]:  # visited set
                    visited[nx] = 1
                    value_q.append(nx)
                    sequence_q.append(vs+i)


if __name__ == "__main__":
    solution()
