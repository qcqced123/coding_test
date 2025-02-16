import sys
from collections import deque, defaultdict


def solution():
    """
    idea: convolution with hash
        - fixed window size

    limit: N
    structure: circular queue
    """
    # get input data
    input = sys.stdin.readline
    N, D, K, C = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    # init fixed window, data structure (circular queue)
    left, right = 0, K-1
    queue = arr + arr[:K-1]

    # init hash structure, answer value
    l = left
    cache = deque([])
    for i in range(K):
        cache.append(queue[l])
        l += 1

    curr = set(cache)
    answer = len(curr) + 1 if C not in curr else len(curr)
    curr.clear()
    # do sliding window
    while right < len(queue)-1:
        # move the pointer and update the cache
        right += 1
        cache.popleft()
        cache.append(queue[right])

        # update the answer value
        curr.update(cache)
        answer = max(answer, len(curr) + 1 if C not in curr else len(curr))
        curr.clear()

    print(answer)


def solution2():
    # get input data
    input = sys.stdin.readline
    N, D, K, C = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    # init fixed window, data structure (circular queue)
    left, right = 0, K - 1
    queue = arr + arr[:K-1]

    # init hash structure, answer value
    l = left
    window = deque([])
    cache = defaultdict(int)
    for _ in range(K):
        cache[queue[l]] += 1
        window.append(queue[l])
        l += 1

    curr = len(cache)
    answer = curr
    if not cache[C]:
        answer += 1

    # do two pointer
    while right < len(queue)-1:
        # move the left pointer
        cnt_l = window.popleft()
        cache[cnt_l] -= 1
        if not cache[cnt_l]:
            curr -= 1

        # move the right pointer
        right += 1
        cnt_r = queue[right]
        if not cache[cnt_r]:
            curr += 1

        cache[cnt_r] += 1
        window.append(cnt_r)

        # check if coupon is valid
        temp = curr
        if not cache[C]:
            temp += 1

        answer = max(answer, temp)

    print(answer)

if __name__ == "__main__":
    solution2()
