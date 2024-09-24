import sys


def solution():
    """ "좋다": 어떤 수가 다른 두 수의 합으로 표현 가능한 상태, 배열 내부에 "좋다"가 몇 개?
    N^2: in ops 아니면, 내부에 있는지 없는지 판정 못해서, N^2이나 준 것 같음, 그래서 투 포인터에서 뭔가 변형이 크게 없을 것 같은데

    idea: two pointer with "in" ops
        포인터 위치가 변할 때마다 in 연산, 배열 내부에 값이 있는지 없는지
        포인터 이동 조건 잡는게 까다롭네
        1) 오름차순 정렬
        2) 포인터 초기화:
            - 포인터 위치: 양 끝
            - 포인터 이동 방향: forward, backward
            - 포인터 이동 조건:
                - > goal: right backward
                - <= goal: left forward
        3) cache structure: set

    Q1. 포인터 이동 조건 못잡겠음
    => 투 포인터 그대로 사용하되, 배열의 원소 하나 하나를 목표 값으로 잡고 그냥 그대로 풀면 되는구나

    """
    N = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()

    cache = 0
    for i in range(N):
        l, r = 0, N-1
        goal = nums[i]
        while l < r:
            cnt = nums[l] + nums[r]
            if cnt < goal:
                l += 1

            elif cnt == goal:
                if l == i:
                    l += 1
                elif r == i:
                    r -= 1
                else:
                    cache += 1
                    break

            else:
                r -= 1

    print(cache)


if __name__ == "__main__":
    solution()
