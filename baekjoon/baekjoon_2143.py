import sys
from collections import defaultdict


def solution():
    """ 부배열: 연속된 부분 수열
    부 배열 합의 쌍 개수

    - 메모리 제한, 목표 합계가 너무 커서 DP x
    - 주어진 수열 두개는 최대 1000 (A*B, 1,000,000, A*BlogA*B)

    idea 1: N**2 + N**2
        1) A 배열 N**2
        2) B 배열 N**2
        => 골드 3인데 안될줄
    """
    input = sys.stdin.readline

    T = int(input())

    N = int(input())  # end index of array A
    A = list(map(int, input().split()))

    M = int(input())  # end index of array B
    B = list(map(int, input().split()))

    # get sum dictionary of array A
    a_dict = defaultdict(lambda: 0)  # 이런 문법이 되는구나
    for i in range(N):
        cnt = 0
        for j in range(i, N):
            cnt += A[j]
            a_dict[cnt] += 1

    # get answer with linear searching of array b
    result = 0
    for i in range(M):
        curr = 0
        for j in range(i, M):
            curr += B[j]
            # a_dict[T-curr]가 호출되는 시점에, T-curr가 사전의 키값에 없으면 그 때 초기화, 메모리 상으로 훨씬 유리함
            # 0도 포함해도 되는데, 빼는게 그래도 속도가 빨라짐
            if a_dict[T-curr] > 0:
                result += a_dict[T-curr]
    print(result)


def solution2() -> None:
    """
    idea 2: binary search (이렇게 풀라는데 전혀 감이 안옴)
        풀이를 보니까 N**2 + N**2인건 똑같음
        1) bisect_left, bisect_right 하면 중복된 값들의 시작, 끝 인덱스가 나오니까, 그걸로 개수를 세겠다

        => 근데 결국은 이게 더 느림, 어쩔 수 없음
        => 내가 짠 bisect 쓰면 더 느림.... 왜이리 느리냐...?
    """
    def bisect_left(arr, x) -> int:
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r) // 2
            if x > arr[mid]:
                l = mid + 1
            else:
                r = mid

        return l

    def bisect_right(arr, x) -> int:
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if x < arr[mid]:
                r = mid
            else:
                l = mid + 1
        return l

    input = sys.stdin.readline
    T = int(input())

    N = int(input())  # end index of array A
    A = list(map(int, input().split()))

    M = int(input())  # end index of array B
    B = list(map(int, input().split()))

    # get sum dictionary of array A
    cache_a = []
    for i in range(N):
        cnt = 0
        for j in range(i, N):
            cnt += A[j]
            cache_a.append(cnt)

    # get sum dictionary of array B
    cache_b = []
    for i in range(M):
        cnt = 0
        for j in range(i, M):
            cnt += B[j]
            cache_b.append(cnt)

    cache_a.sort()
    cache_b.sort()

    result = 0
    for i in range(len(cache_a)):
        l = bisect_left(cache_b, T-cache_a[i])
        r = bisect_right(cache_b, T-cache_a[i])
        result += r-l

    print(result)

    return


if __name__ == "__main__":
    solution2()
