import sys


def solution():
    """ NlogN
    idea: prefix sum, sliding window
        - prefix[i]: number of ice in ith index
        - 윈도우 사이즈를 무조건 고정해두면 안될 듯,
        - 양 끝의 경우는 오른쪽만 크기 그대로 살리고 혹은 왼쪽만 크기 그대로 살리고, 이런 식으로 가야 함
    """
    input = sys.stdin.readline
    N, K = map(int, input().split())
    ice = [tuple(map(int, input().split())) for _ in range(N)]
    ice.sort(key=lambda x: x[1])

    # init prefix array
    prefix = [0]*(ice[-1][1]+1)
    for v, p in ice:
        prefix[p] += v

    # find the optimal position
    window = K*2+1
    answer = sum(prefix[1:window+1])
    curr = answer
    for i in range(2, len(prefix)-window+1):
        cnt = curr - prefix[i-1]
        cnt += prefix[i+window-1]
        answer = max(answer, cnt)
        curr = cnt

    print(answer)



if __name__ == "__main__":
    solution()
