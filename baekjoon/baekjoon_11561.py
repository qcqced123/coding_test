import sys


def solution():
    """
    idea: binary search
        - 탐색 대상/범위: 밟아야 하는 다리 개수, 1 to N
        - 탐색 조건
    """
    input = sys.stdin.readline
    test = [int(input()) for _ in range(int(input()))]
    for t in test:
        answer = 0
        l, r = 1, int(pow(2*t, 1/2))
        while l <= r:
            mid = (l+r) // 2
            prev, jump = 0, 0
            for i in range(1, t+1):
                prev += i
                if prev > t:
                    break

                jump += 1
                if jump >= mid:
                    break


            if jump >= mid:
                answer = mid
                l = mid + 1

            else:
                r = mid - 1

        print(answer)


if __name__ == "__main__":
    solution()
