import sys
from typing import List


def solution():
    """ 연속된 숫자의 부분합, N^2
    투 포인터를 쓰되, 부분의 합을 구해야 해서 N^2을 준듯

    idea: 투 포인터
        포인터 위치: 나란히
        포인터 이동 조건: 부분의 합이 M이거나, 아니면
            - 합이 M일 때: 왼쪽 움직이기
            - 합이 M보다 작을떄: 오른쪽 움직이기
            - 합이 M보다 클때: 왼쪽 움직이기

        탐색 종료 조건: 둘 다 배열 끝일 때

    solution:
    """
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    result = 0
    left, right = 0, 0  # 겹치는걸 고려해서 코드를 짰으면, 맨처음에 겹칠수도 있는걸 왜 생각못하냐
    while left < N and right < N:
        cnt = sum(nums[left:right+1])
        if cnt == M:
            result += 1
            left += 1

        elif cnt < M:
            right += 1

        else:
            left += 1

    print(result)


if __name__ == "__main__":
    solution()
