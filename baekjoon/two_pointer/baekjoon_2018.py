def solution():
    """ 자연수 N을 "연속된" 다른 여러 자연수의 합으로 표현하기
    15 => [15], [1,2,3,4,5], [4,5,6], [7,8]

    idea: Two-Pointer
        1) search by two-pointer
            - 포인터 위치: 나란히
            - 포인터 이동 방향: 둘 다 forward
            - 포인터 이동 조건:
                - 목표값이랑 일치: 왼쪽 포인터 이동
                - 목표값보다 클떄: 왼쪽 포인터 이동
                - 목표값보다 작을 때: 오른쪽 포인터 이동

            - 탐색 종료 조건: 왼쪽 포인터가 배열의 끝을 넘는 경우
    1 2 3 ... 13 14 15
    """
    def is_valid():
        return left <= N

    N = int(input())
    left, right = 1, 1
    sum, result = 0, 0

    while is_valid():
        if sum == N:
            result += 1
            sum -= left
            left += 1

        elif sum > N:
            sum -= left
            left += 1

        elif sum < N:
            sum += right
            right += 1

    print(result)


if __name__ == "__main__":
    solution()
