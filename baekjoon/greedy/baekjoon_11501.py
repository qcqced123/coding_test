import sys

"""
[시간]
1) 14:10 ~ 14:34
[요약]
1) 주식을 '하나' 사기/원하는 만큼 가지고 있는 주식을 팔기/아무것도 안하기
    - 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산하는 프로그램 작성
[전략]
1) max() 이용해 문제 해결
    - max - 현재 ≥ 0: 사기
    - max - 현재 ≤ 0: 팔기
    => 시간 초과 때문에 문제 해결 불가
2) 리스트 역순으로 접근
"""
for _ in range(int(sys.stdin.readline())):
    N, price_list = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))
    price_list.reverse()
    max_price, result = price_list[0], 0
    for i in range(1, N):
        profit = max_price - price_list[i]
        if profit >= 0:
            result += profit
        else:
            max_price = price_list[i]
    print(result)




