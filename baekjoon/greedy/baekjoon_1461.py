import sys
"""
[풀이 시간]
1) 22:40 ~ 23:10

[요약]
1) 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 위치
    - 모든 책을 원위치 시킬 때, 필요한 최소 걸음 수
    - N: 책 개수
    - M: 세준이가 한 번에 들 수 있는 책 개수
    - 책의 위치는 절대 0이 아님, 한 걸음에 한 칸
[전략]
1) 옵션이 여러 개, 최소값 구하기: Greedy
    - 정렬, 경우의 수 최소화 방법 생각
    - 절대값 기준 오름 차순 정렬
    - N, M 크기에 따라서 케이스 분류
        1-1) M >= N
            - 리스트 마지막 두 개의 원소 이용
        1-2) N > M
            - N 값을 down, 1-1 상황이 되도록 만들자
    - 나는 가장 작은 것부터 처리 해야 한다고 생각 했는데 오히려 가장 큰 것부터 처리를 해야 한다고 하는 구나..?
    - 해보니까 작은 것부터 처리 하는게 틀린게 아니라 양수, 음수를 나눠서 저장하는게 포인트 같음
"""
N, M = map(int, sys.stdin.readline().split())
position_list = sorted(list(map(int, sys.stdin.readline().split())), key=lambda x: abs(x))  # abs(): built-in
total_distance, idx, tmp, tmp_i = 0, 0, 0, 0
while True:
    if M >= N:
        for i in range(idx, len(position_list)):
            if position_list[-1] * position_list[i] < tmp:
                tmp = position_list[-1] * position_list[i]
                tmp_i = i
        if tmp >= 0:
            total_distance += abs(position_list[-1])
            break
        if tmp < 0:
            total_distance += (abs(position_list[tmp_i]) * 2) + abs(position_list[-1])
            break
    else:
        total_distance += abs(position_list[idx]) * 2
        idx += 1
        N -= 1
    print(total_distance)
print(total_distance)
