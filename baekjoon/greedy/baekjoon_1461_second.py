import sys

N, M = map(int, sys.stdin.readline().split())
position_list = sorted(list(map(int, sys.stdin.readline().split())))  # abs(): built-in

pos = [num for num in position_list if num > 0]  # 양수 리스트
neg = [num for num in position_list if num < 0]  # 음수 리스트
move = []  # 이동 대상 책의 위치를 별도로 저장
for i in range(-1, -len(pos)-1, -M):  # range 단위를 M으로
    move.append(pos[i])
for i in range(0, len(neg), M):
    move.append(-neg[i])
move.sort(key=lambda x: abs(x))
print(move[-1] + sum(move[:-1]) * 2)
