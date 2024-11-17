import sys


def solution():
    """ 무게 C, 최대 3개 선택 (knapsack...?), 중복x, 무게는 다 다름
    idea: two pointer (세수의 합)
        - if 고정 == C
        - elif 고정 + arr[l] == C
        - elif 고정 + arr[r] == C
        - elif 고정 + arr[l] + arr[r] == C
    """
    input = sys.stdin.readline
    N, C = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    # do the two pointer search
    answer = 0
    for i in range(N-1):
        cnt = arr[i]
        if cnt == C:
            answer += 1
            break

        l = i+1
        r = N-1
        while l < r:
            curr = cnt + arr[l] + arr[r]
            if cnt + arr[l] == C or cnt + arr[r] == C or curr == C:
                answer += 1
                break

            if curr > C:
                r -= 1

            else:
                l += 1

        if answer:
            break

    print(answer)


if __name__ == "__main__":
    solution()
