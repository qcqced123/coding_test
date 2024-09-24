def solution():
    """ G킬로그램: 현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀, NlogN
    살이 찐거면 항상 현재가 더 커야지

    idea: two pointer
        1) 배열 초기화:
        2) 포인터 초기화:
            - 포인터 위치: 나란히
            - 포인터 방향: forward
            - 포인터 이동 조건:
                - < G: right forward
                - >= G: left forward
                    - 같으면 기록
    """
    N = int(input())
    arr = [i for i in range(1, N+1)]
    if N == 1:
        print(-1)
        exit()

    cache = []
    l, r = 0, 1
    while l < r:
        cnt = pow(arr[r], 2) - pow(arr[l], 2)
        if cnt < N:
            r += 1
        else:
            if cnt == N:
                cache.append(arr[r])
            l += 1
    if cache:
        for i in cache:
            print(i, end='\n')
    else:
        print(-1)


if __name__ == "__main__":
    solution()
