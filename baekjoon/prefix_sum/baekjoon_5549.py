import sys


def solution():
    """ QlogM*N
    idea: prefix sum
        - 2차원 테이블의 누적합 응용
        - 정글. 바다, 얼음에 대한 각각의 누적합 배열 만들기
        - 쿼리에 대한 답하기
    """
    input = sys.stdin.readline
    M, N = map(int, input().split())
    Q = int(input())
    grid = [list(input().rstrip()) for _ in range(M)]
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    # init each type of prefix sum array
    jungle = [[0]*(N+1) for _ in range(M+1)]
    ocean = [[0]*(N+1) for _ in range(M+1)]
    ice = [[0]*(N+1) for _ in range(M+1)]
    for i in range(1, M+1):
        for j in range(1, N+1):
            cnt = grid[i-1][j-1]
            cnt_j, cnt_o, cnt_i = 0, 0, 0
            if cnt == "J": cnt_j += 1
            elif cnt == "O": cnt_o += 1
            else: cnt_i += 1

            jungle[i][j] = jungle[i-1][j] + jungle[i][j-1] - jungle[i-1][j-1] + cnt_j
            ocean[i][j] = ocean[i-1][j] + ocean[i][j-1] - ocean[i-1][j-1] + cnt_o
            ice[i][j] = ice[i - 1][j] + ice[i][j - 1] - ice[i - 1][j - 1] + cnt_i

    # answering the question
    for query in queries:
        y1, x1, y2, x2 = query
        answer_j = jungle[y2][x2] - jungle[y1-1][x2] - jungle[y2][x1-1] + jungle[y1-1][x1-1]
        answer_o = ocean[y2][x2] - ocean[y1-1][x2] - ocean[y2][x1-1] + ocean[y1-1][x1-1]
        answer_i = ice[y2][x2] - ice[y1-1][x2] - ice[y2][x1-1] + ice[y1-1][x1-1]
        print(answer_j, answer_o, answer_i)


if __name__ == "__main__":
    solution()
