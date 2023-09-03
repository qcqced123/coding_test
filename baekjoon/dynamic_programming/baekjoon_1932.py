import sys
"""
[요약]
1) 각 변의 길이가 N인 정수 삼각형
    - 선택된 수의 합이 최대가 되는 경로
    - 왼쪽 대각선 혹은 오른쪽 대각선 선택 가능
    - 입력 길이: 500
    - 시간: 2초
    => 여유로움
"""
N = int(sys.stdin.readline())
tri_list, answer = [], []
for _ in range(N):
    tmp_tri = list(map(int, sys.stdin.readline().split()))
    tri_list.append(tmp_tri), answer.append([0] * len(tmp_tri))

answer[0] = tri_list[0]
for i in range(1, N):
    answer[i][0], answer[i][-1] = answer[i-1][0] + tri_list[i][0], answer[i-1][-1] + tri_list[i][-1]
    for j in range(1, len(answer[i])-1):
        answer[i][j] = max(answer[i-1][j-1], answer[i-1][j]) + tri_list[i][j]
print(max(answer[N-1]))


