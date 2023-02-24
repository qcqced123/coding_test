import sys
"""
[풀이 시간]
1) 15:30 ~ 15:50 

[문제]
N^2 => 전체 동전의 개수
H => 동전의 앞면
T -> 동전의 뒷면
1) 임의의 한 행 또는 한 열에 놓인 N개의 동전을 모두 뒤집는 작업 
=> 행이나 열단위 작업 수행, 뒷면(T) 값 갖는 동전의 개수를 최소로 만들기

[전략]
- 일단 N^2의 최대 상한선 == 400, 시간 제한도 6초 ㅎㅎ 틀리면 등신
- 일단 입력 받는 것부터 구현 해보자
- 뒷면 동전이 가장 많은 줄을 찾아서 뒤집는데 뒤집고 난 결과랑 이전 결과랑 비교 해서 개수
  구현은 while & for-loop 섞어서 쓰자
"""
# 동전 초기 상태, 행 & 열마다 뒷면 개수(1행, 1열, 2행, 2열, 3행, 3열)
N, min_value = int(sys.stdin.readline()), 0
coin_list, t_number, checker = [[j for j in sys.stdin.readline().strip()]for i in range(N)], [], True

# Coin Table 접근
while checker:
    all_counter, counter, temp = 0, [0] * (2*N), 0
    # Row & Col => 이중 루프 하나로 처리가 가능
    for i in range(N):
        temp_1, temp_2 = [], []  # row, col
        for j in range(N):
            # row => 여기서 어차피 전체 루프를 돌기 때문에 all_counter를 여기서 세어주면 될 것 같다.
            if coin_list[i][j] == 'T':
                counter[2*i] += 1
                all_counter += 1
            # col
            if coin_list[j][i] == 'T':
                counter[2*i+1] += 1
            temp_1.append(coin_list[i][j]) # row
            temp_2.append(coin_list[j][i]) # col

        t_number.append(temp_1)
        t_number.append(temp_2)

    change_idx = counter.index(max(counter))
    value, rest = int(change_idx / 2), change_idx % 2

    if rest == 0:  # row
        for i in range(N):
            if coin_list[value][i] == 'T':
                coin_list[value][i] = 'H'
            else:
                coin_list[value][i] = 'T'
    else:  # col
        for i in range(N):
            if coin_list[i][value] == 'T':
                coin_list[i][value] = 'H'
            else:
                coin_list[i][value] = 'T'

    # 뒤집고 난 결과랑 이전 결과랑 비교 => 이전 결과가 더 클때만 다음 루프 수행
    for i in range(N):
        for j in range(N):
            if coin_list[i][j] == 'T':
                temp += 1
    if all_counter > temp:
        min_value = temp
    else:
        checker = False

print(min_value)

