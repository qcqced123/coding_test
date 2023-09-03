import sys
import heapq

"""
[요약]
1) 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없어서 점수의 합이 최대가 되게 스티커를 떼어내는 방법
    - 시간 제한: 1초
    - 길이: 10만
    => 살짝 빡센,,,
    => 행과 열을 뒤집어서 접근해야 한다.
"""
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    sticker, answer = [list(map(int, sys.stdin.readline().split())) for _ in range(2)], [[0] * N for _ in range(2)]
    answer[0][0], answer[1][0] = sticker[0][0], sticker[1][0]
    for j in range(1, N):
        for i in range(2):
            if j == 1:
                answer[i][j] = answer[i-1][0] + sticker[i][j]
                continue
            answer[i][j] = max(answer[i-1][j-1], answer[i-1][j-2]) + sticker[i][j]
    print(max(answer[0][N-1], answer[1][N-1]))

