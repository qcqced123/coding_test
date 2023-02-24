import sys
"""
앞면/뒷면 뒤집는 행위를 이진수, 비트 마스킹으로 표현하기
local optimal solution은 맞은듯
"""

N = int(sys.stdin.readline())
coins = [] # 뒤집기 전 코인
reverse_coins = [] # 뒤집은 코인

for _ in range(N):
    i = N-1 # 기본 시작이 1의 자리에 1을 넣고 시작 하니까 1을 빼줘야 원하는 자리수에 딱 숫자를 넣게 되는거구나
    bit = 0
    for curr in sys.stdin.readline().rstrip(): # 이진수 자리에 맞춰서 동전의 앞면/뒷면 여부를 표현
        if curr == 'T':
            bit += 1 << i
        i -= 1
    coins.append(bit) # 안뒤집은 코인 추가
    reverse_coins.append(~bit) # 뒤집은 코인 추가

# 여기부터 로직 이해 안감
ans = N**2
for bit in range(1 << N): # 이진수에서 자리수 N으로 표현 가능한 모든 경우의 수를 for-loop
    tmp_coins = []
    for i in range(N):
        if bit & 1 << i:
            tmp_coins.append(coins[i])
        else:
            tmp_coins.append(reverse_coins[i])

    total_t_cnt = 0
    for i in range(N):
        t_cnt = 0
        for coin in tmp_coins:
            if 1 << i & coin:
                t_cnt += 1
        total_t_cnt += min(t_cnt, N-t_cnt)
    ans = min(ans, total_t_cnt)
print(ans)

