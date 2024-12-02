import sys


def solution():
    """ NlogN
    idea: prefix sum, sliding window
        - prefix[i]: number of ice in ith index

    feedback:
        - x 값이 어차피 양수라서, 윈도우 사이즈를 유동적으로 가져가야 하는 상황은 고려할 필요가 없음
        - 다만, 좌표 시작이 0부터 라는 걸 간과함
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
    answer = sum(prefix[:window])
    curr = answer
    for i in range(1, len(prefix)-window+1):
        cnt = curr - prefix[i-1]
        cnt += prefix[i+window-1]
        answer = max(answer, cnt)
        curr = cnt

    print(answer)



if __name__ == "__main__":
    solution()
