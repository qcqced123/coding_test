import sys


def solution():
    """ 두 수의 합이 K에 가장 근접한, 백만... N
    가장 가까운 근접한 값을 나열하고, 이진 탐색으로 찾아야 빠를듯

    idea: binary search
        - 탐색 대상: 가장 근접한 값 배열, 0 to K
        - 탐색 기준: 현재 기준값이 반드시 가장 근접한 값이여야 함, 없으면...? 포인터 이동 시켜야겠지?
            - cnt < mid:
        - 두 숫자 찾는 알고리즘: two-pointer
            - 이게 정렬된 배열은 아니라서, 아 정렬하자
    """
    # loop for multiple test case
    input = sys.stdin.readline
    for _ in range(int(input())):
        # init the data structure, pointer position
        N, K = map(int, input().split())  # length of arr, 기준값
        S = list(map(int, input().split()))
        S.sort()  # 괜찮을까..? 터질거 같은데

        # do bisect
        answer = 0
        l, r = 0, K
        while l <= r:
            cache = 0
            mid = (l+r) // 2  # 현재 기준값
            left, right = 0, N - 1
            while left < right:
                cnt = abs(K - S[left] + S[right])
                if cnt > mid:
                    left += 1

                elif cnt == mid:
                    cache += 1
                    right -= 1

                else:
                    break

            else:
                if cache:
                    answer = cache
                    r = mid - 1

                else:
                    l = mid + 1

                continue

            r = mid - 1

        print(answer)


def solution2():
    # loop for multiple test case
    input = sys.stdin.readline
    for _ in range(int(input())):
        # init the data structure, pointer position
        N, K = map(int, input().split())  # length of arr, 기준값
        S = list(map(int, input().split()))
        S.sort()  # 괜찮을까..? 터질거 같은데

        # do bisect
        answer = 0
        l, r = 0, 200000000  # 문제에 있는대로 세팅해야지.. bisect 문제는 특히나 확인하고 풀자
        while l <= r:
            cache = 0
            mid = (l+r) // 2  # 현재 기준값
            left, right = 0, N-1
            while left < right:
                cnt = K - (S[left] + S[right])  # 부호....
                curr = abs(cnt)
                if curr > mid:
                    if cnt > 0:
                        left += 1
                    else:
                        right -= 1

                elif curr == mid:
                    cache += 1
                    left += 1

                else:
                    break
            else:
                if cache:
                    answer = cache
                    r = mid - 1

                else:
                    l = mid + 1

                continue

            r = mid - 1

        print(answer)


if __name__ == "__main__":
    solution2()
