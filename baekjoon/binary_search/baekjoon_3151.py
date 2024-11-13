import sys
from bisect import bisect_left, bisect_right


def solution():
    """ 3명 팀, 코딩값 0이 되는 팀의 개수 찾기, N**2
    idea: two-pointer, binary-search
        - 하나 고정하고, 나머지 투포인터
    반레:
    8
    -10 5 5 5 5 5 5 5
    ans=21

    6
    -8 3 3 5 5 5
    ans=6
    => 중복되는 값이 여러개 있을 때 문제가 됨

    feedback:
        - 세용액 문제랑 큰 틀에서 같은데, 그떄는 원소 중복 허용 X였고, 이번 문제는 허용 0
        - 원소 중복 되는 경우, 처리하는 방빕 구현하는게 관건
    """
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    # two pointer search
    # 세 용액 문제랑 다른게, 중복 원소가 있음
    answer = 0
    for i in range(N-1):
        cnt = arr[i]
        l, r = i+1, N-1
        while l < r:
            curr = cnt + arr[l] + arr[r]
            if curr < 0:
                l += 1

            elif curr == 0:
                if arr[l] == arr[r]:
                    answer += (r-l+1)*(r-l) // 2
                    break
                else:
                    next_l, next_r = bisect_right(arr, arr[l]), bisect_left(arr, arr[r])
                    answer += (next_l - l) * (r+1 - next_r)
                    l, r = next_l, next_r
            else:
                r -= 1

    print(answer)


if __name__ == "__main__":
    solution()
