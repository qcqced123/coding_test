import sys
"""
[풀이 시간]
1) 22:30 ~ 23:10

[규칙] 
1) 인덱스가 a이상 b이하에서 남은 책 한 권 골라 주기, 해당 범위에 남은 책이 없으면 그 학생에게는 책 안준다
2) 책을 줄 수 있는 최대 학생 수

[전략]
1) 책 개수, 학생 수 모두 최대 1000 => 크게 시간 초과 부담은 없는 듯, 이중 루프 해봐야 백만이라
2) 최대 학생 수 => 내림차순 정렬, 최대 힙정렬 고려
=> 근데 이게 그럼 쫙 펼쳐 두고 접근 해서 빼줘야 하는데, 아무래도 받으면서 빼는게 좋지 않을까??
=> 받으면서 뺄 수 있는 탁월한 방법이 없을까
=> 일단 책 개수가 사람이랑 같거나 작은 경우 무조건 책 개수를 최대 사람으로 표현하는게 불가능하네
=> 케이스를 생각해보자
4, 3인 경우
[1,2,3,4]
(1,4) => +1
(3,4) => +1
(2,4)
(2,3) => 
(1,2)
저장해두고 두 케이스를 지속적으로 비교하면서 루프를 돌려주면 되겠다. 일단 추가하고 추가 한거랑 추가 안한 거 변수로 두고 뭐가 더 클지
저 인덱스 개수를 세면 될 거 같은데?? 
1 => 2
2 => 2
3 => 2
4 => 2
숫자가 1또는 2인거 개수만 세면 되겠네
"""
G = int(sys.stdin.readline())
result_list = []
for i in range(G):
    N, M = map(int, sys.stdin.readline().split())
    book, result = [[value, 0] for value in range(1, N + 1, 1)], 0

    for j in range(M):
        a, b = map(int, sys.stdin.readline().split())
        if book[a-1][1] != 2:
            book[a-1][1] += 1

        if book[b-1][1] != 2:
            book[b-1][1] += 1

    for count in book:
        if count[1] > 0 and count[1] < 3:
            result += 1

    result_list.append(result)

for value in result_list:
    print(value)



