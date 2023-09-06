import sys
"""
[요약]
1) 동전을 최소로 사용해서 합이 K가 되도록 하는 프로그램 작성
    - 시간 제한: 1초
    - 메모리: 넉넉함
    - 입력 크기: 동전 100개, 가격 
    - 가치가 같은 동전이 여러 번 등장
[전략]
1) Tabulation with 2D
    - 중복 제거, K 넘어가는 값 처리
    => 루프 다 돌고 세트 쓰자. 그래도 시간은 똑같을 것 같다
"""
N, K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coin = int(sys.stdin.readline())
    if coin <= K:
        coins.append(coin)
coins = sorted(list(set(coins)))  # excepting overlapping coins, sort by Ascending
result = -1
if len(coins):
    money = [0] * (K+1)
    for i in range(len(coins)):
        for j in range(1, K+1):
            checker, divisor = j - coins[i], j % coins[i]
            if not checker:
                money[j] = 1
            elif money[checker]:
                if not money[j]:
                    money[j] = money[checker] + 1
                elif money[j]:
                    money[j] = min(money[j], money[checker] + 1)
    if money[-1]:
        result = money[-1]
print(result)


