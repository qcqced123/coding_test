import sys


def solution():
    """
    idea: dynamic programming
    feedback:
        - 다른 사람 풀이를 보니, 숫자 만들기 문제랑 같다는걸 알 수 있었음 (over-lapping 구조가 잘 보임...)
    """
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    cache = [0]*(N+1)
    vips = [int(input()) for _ in range(M)]

    # init dynamic programming cache array
    cache[0] = 1
    for i in range(1, N+1):
        if i < 3:
            cache[i] = i
            continue

        cache[i] = cache[i-1] + cache[i-2]

    # calculate the VIP case
    # M == 0 이면, answer는 그냥 cache 바로 출력
    if M > 0:
        prev = 0
        answer = 1
        for vip in vips:
            answer *= cache[vip - prev - 1]
            prev = vip
            if vip == vips[-1]:
                answer *= cache[N - prev]

    else:
        answer = cache[-1]

    print(answer)


if __name__ == "__main__":
    solution()
