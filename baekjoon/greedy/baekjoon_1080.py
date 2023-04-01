import sys
"""
[풀이 시간]
1) 17:25 ~ 18:10

[요약]
1) 행렬 A to B 변환에 필요한 연산의 최소 횟수
    - 주어진 행렬의 부분 행렬 [3,3]의 모든 원소를 뒤집기
    - CNN 필터 혹은 커널 연산과 비슷한듯
[전략]
1) 시간 압박 낮음
2) 최소값 구하기 문제: Greedy, 정렬 대상 및 방식 정의
    - 커널이 지나가는 영역의 1열 1행이 서로 같은지 주목하기
    - 어차피 커널이 행렬의 모든 원소를 1열 1행 위치로 한 번씩 지나는 점을 이용
"""


def flip(x, y):
    for i in range(x, x+3, 1):
        for j in range(y, y+3, 1):
            A_matrix[i][j] = 1 - A_matrix[i][j]


N, M = map(int, sys.stdin.readline().split())
A_matrix = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(N)]
B_matrix = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(N)]
result = 0

for i in range(N-2):
    for j in range(M-2):
        if A_matrix[i][j] != B_matrix[i][j]:
            """ A 행렬에 flip 연산 적용 필요 """
            flip(i, j)
            result += 1

for i in range(N):
    for j in range(M):
        if A_matrix[i][j] != B_matrix[i][j]:
            result = -1

print(result)

