import sys
INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    insert your solution here
    """
    # get input data
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # do parametric search
    answer = 0
    l, r = 1, int(N//M)
    while l <= r:
        mid = (l+r) // 2
        cnt, starting = 0, 0
        while starting + mid <= N:
            cache = dict()
            for i in range(starting, starting+mid):
                curr = arr[i]
                if curr not in cache:
                    cache[curr] = i

                else:
                    starting = cache[curr] + 1
                    break
            else:
                cnt += 1
                starting += mid


        # determine the next searching element
        if cnt >= M:
            answer = mid
            l = mid + 1

        else:
            r = mid - 1

    print(answer)
    return

if __name__ == '__main__':
    solution()