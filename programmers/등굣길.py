def solution(m, n, puddles):
    """ 웅덩이 피하기, 입력 인덱스 != 구현 인덱스
    rule:
        1) 방향 2개
        2) 웅덩이 피하기
            - 원소값: 1

    idea: dynamic programming
        1) 그리드 초기화
        2) 캐시 초기화
            - 첫번쨰 행, 열 초기화: 웅동이 떄문에 막혀있지만 않다면 ~
    review:
        1) y, x 인덱스 순서 조심 하기!

    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42898?language=python3
    """
    # initialize the grid for setting the puddles
    modular = 1000000007
    grid = [[0] * m for _ in range(n)]  # 원소값 0 == 이동 가능, 원소값 1 == 이동 불가
    if len(puddles) > 0:
        for puddle in puddles:
            r, c = puddle
            grid[c - 1][r - 1] = 1

    # init cache array
    cache = [[0] * m for _ in range(n)]
    cache[0][0] = 1
    for i in range(1, n):
        if not grid[i - 1][0] and not grid[i][0] and cache[i - 1][0]:
            cache[i][0] = 1

    for j in range(1, m):
        if not grid[0][j - 1] and not grid[0][j] and cache[0][j - 1]:
            cache[0][j] = 1

    # do dynamic programming
    for y in range(1, n):
        for x in range(1, m):
            if not grid[y][x]:
                cache[y][x] = (cache[y - 1][x] + cache[y][x - 1]) % modular

    answer = cache[-1][-1] % modular
    return answer


if __name__ == '__main__':
    solution()