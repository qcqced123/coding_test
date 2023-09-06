import sys
"""
[풀이]
1) 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램 작성
    - 시간 제한: 2초
    - 메모리 제한: 넉넉함
    - 길이: 200, 200
    - 덧셈 순서 바뀌는 거 인정, 한 개를 여러 번 사용하는 것도 인정
[전략]
1) 주어진 조건이 넉넉, 재귀나 테이블 둘 다 가능할 듯
    - N: f(k) = N: f(k-1) + N-1: f(k-1) + ...  + 0: f(k-1) 
"""
N, K = map(int, sys.stdin.readline().split())
num_table = [[1] * (N+1) for _ in range(K)]  # must match index
for i in range(1, K):  # i+1 is real
    for j in range(1, N+1):
        num_table[i][j] = num_table[i-1][j] + num_table[i][j-1]
print(num_table[-1][-1] % 1000000000)
