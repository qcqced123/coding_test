import sys

for _ in range(int(sys.stdin.readline())):
    N, coin_list, money = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split())), int(sys.stdin.readline())
    table = [0 for _ in range(money+1)]
    table[0] = 1  # 제일 중요
    for i in coin_list:
        for j in range(1, money+1):
            if j - i >= 0:
                table[j] += table[j - i]
    print(table[-1])
