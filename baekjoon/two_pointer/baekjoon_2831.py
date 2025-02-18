import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: two pointer
        - 룹 분할
        - 그룹별 매칭 시작
            - 투 포인터 이용해서, 매칭
    limit: NlogN
    """
    # get input data
    N = int(input())
    man = list(map(int, input().split())) if N > 1 else [int(input())]
    woman = list(map(int, input().split())) if N > 1 else [int(input())]
    man.sort(), woman.sort()

    # split into two groups
    prev_m, cnt_m = [], []
    prev_w, cnt_w = [], []
    for i in range(N):
        cnt_man, cnt_woman = man[i], woman[i]
        if cnt_man < 0: prev_m.append(cnt_man)
        else: cnt_m.append(cnt_man)

        if cnt_woman < 0: prev_w.append(cnt_woman)
        else: cnt_w.append(cnt_woman)

    # do two pointer
    answer = 0
    group = [(prev_m, cnt_w), (prev_w, cnt_m)]
    for i in range(2):
        curr = group[i]
        if not curr[0] or not curr[1]:
            continue

        cnt = curr[0] + curr[1]
        man_size, woman_size = len(curr[0]), len(curr[1])

        # init two pointer
        left, right = 0, len(cnt)-1
        while left < man_size and right > len(cnt) - woman_size - 1:
            if not i:
                cnt_man, cnt_woman = cnt[left], cnt[right]
                if abs(cnt_man) > cnt_woman:
                    answer += 1
                    left += 1
                    right -= 1

                else:
                    right -= 1

            else:
                cnt_woman, cnt_man = cnt[left], cnt[right]
                if abs(cnt_woman) > abs(cnt_man):
                    answer += 1
                    left += 1
                    right -= 1

                else:
                    right -= 1
    print(answer)


if __name__ == "__main__":
    solution()
