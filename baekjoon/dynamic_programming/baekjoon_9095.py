import sys
"""
[시간]
1) 02: 07 ~ 02:37
[요약]
1) 정수 N을 1, 2, 3의 합으로 나타낼 수 있는데, 모든 경우의 수를 세어 주는 프로그램 작성
[전략]
1) f(N) = f(N-1) + f(N-2) + f(N-3)
    - 시간 제한이나 입력의 길이가 여유로움
    - 일단 생각이 안나니까 죄다 써보자
"""


def fibonacci(x: int) -> int:
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    if x == 4:
        return 7
    if x == 5:
        return 13
    return fibonacci(x-1) + fibonacci(x-2) + fibonacci(x-3)


for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    result = fibonacci(N)
    print(result)



