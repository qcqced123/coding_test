import sys
from typing import List


def solution() -> None:
    """
    idea:
        1) 회문: 슬라이싱 이용
        2) 유사회문: forward, backward 나눠서 판정

    optimization point:
        1) using in-place function for not calling kernel
    """
    N = int(sys.stdin.readline())
    for _ in range(N):
        forward = sys.stdin.readline().rstrip()
        backward = forward[::-1]  # reverse
        if forward == backward:
            print(0)
            continue

        activation, gradient = "", ""
        for i in range(len(forward)):
            if forward[i] != backward[i]:
                activation += forward[i+1:]
                gradient += backward[i+1:]
                break

            activation += forward[i]
            gradient += backward[i]

        if activation == activation[::-1] or gradient == gradient[::-1]:
            print(1)
            continue

        else:
            print(2)


if __name__ == '__main__':
    solution()



