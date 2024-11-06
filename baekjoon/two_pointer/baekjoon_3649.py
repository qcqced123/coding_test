import sys


def solution():
    """
    1, 2, 9999998, 99999999
    idea: two pointer
        - 단위 통일
        - 정렬
        - 포인터 위치: 양끝
        - 포인터 이동 조건: X와 포인터가 가리키는 원소들의 합(S) 비교
    feedback:
        - 입력은 여러개의 테스트 케이스로 이뤄져 있다잖아요... 미친
        - 근데 이런 입력은 어떻게 받아야 함??
    """
    input = sys.stdin.readline
    while True:
        try:
            X = int(input())*10000000
            N = int(input())
            arr = [int(input()) for _ in range(N)]
            arr.sort()

            cache, record = -sys.maxsize, []
            l, r = 0, len(arr) - 1
            while l < r:
                cnt = arr[l] + arr[r]
                if cnt > X:
                    r -= 1
                else:
                    if cnt == X:  # 기록은 같을 때만 해야지
                        curr = abs(arr[l] - arr[r])
                        if cache < curr:
                            cache = curr
                            record = [arr[l], arr[r]]
                    l += 1

            print(f"yes {record[0]} {record[1]}" if cache != -sys.maxsize else "danger")

        except:
            break


if __name__ == "__main__":
    solution()
