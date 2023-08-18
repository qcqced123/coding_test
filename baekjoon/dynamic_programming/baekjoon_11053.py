import sys
"""
[풀이 시간]
1) 21:00 ~ 21:30

[요약]
1) 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열의 길이 출력

[전략]
1) 전체 수열에서 하위 몇가지 수열의 증가 추이  비교가 필요함
    - 전형적인 DP
    - 테이블 구성을 어떻게 할 것인가??
    - 이중 루프 살짝 애매하지만 가능할 것 같음
"""
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
table = [1] * N

for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            table[i] = max(table[j] + 1, table[i])
print(max(table))
