def solution():
    """ 구멍과 레고조각 2개: 구멍 길이 == 조각의 길이 합, (NlogN)
    idea: two-pointer
        1) 배열 단위 통일, 정렬
        2) 포인터 초기화
            - 포인터 위치: 양 끝
            - 포인터 이동 방향: forward, backward
            - 포인터 이동 조건:
                - > X: left forward
                - =< X: right forward
    """
    x = int(input())*10000000
    lego = [int(input()) for _ in range(int(input()))]
    lego.sort()

    result = None
    l, r, cache = 0, 0, 0
    while r < len(lego) - 1:
        r += 1
        cnt = lego[l] + lego[r]

        if cnt > x:
            l += 1

        else:
            if cnt == x:
                curr = abs(lego[l] - lego[r])
                if cache < curr:
                    cache = curr
                    result = (lego[l], lego[r])

    print(f"yes {result[0]} {result[1]}") if result is not None else print('danger')


if __name__ == "__main__":
    solution()
