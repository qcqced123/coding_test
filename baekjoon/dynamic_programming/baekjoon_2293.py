import sys
"""
[요약]
1) n가지 종류의 동전, 가격은 모두 다름
    - 합이 K원이 되도록 만드는 경우의 수
    - 개별 동전은 몇개 라도 사용 가능, 다만 조합만 인정
    - 시간 제한: 0.5
    - 길이: 동전 종류 100, 가격 10000

[전략]
1) 시간 제한과 메모리 고려하면 Tabulation
    -
"""
N, K = map(int, sys.stdin.readline().split())
coins = []
for i in range(N):
    coin = int(sys.stdin.readline())
    if coin <= K:
        coins.append(coin)

result = 0
if len(coins):
    coins.sort()
    money = [0] * (K+1)
    for i in range(len(coins)):
        for j in range(1, K+1):
            checker = j - coins[i]
            if checker == 0:
                money[j] += 1  # 주의!!!
            elif checker > 0:
                money[j] += money[checker]
    result = money[-1]
print(result)

