import sys

"""
[시간]
1) 15:20 ~ 16:00

[요약]
1) 주어진 전화번호 목록을 보고, 일관성이 여부 판단
    - 하나의 번호가 다른 번호의 접두어 X
    - 주어진 모든 번호에 동일하게 연락할 수 있어야 일관성 있다고 판단
[전략]
1) 전화번호 앞자리를 최우선 기준으로 정렬
    - 시간 제한 & 입력의 길이: 이중 루프 커버 불가능
    - 숫자처럼 생긴 '문자열'을 정렬, 길이와 관계 없이 자리수에 채워진 숫자가 비슷한 번호끼리 뭉침
        => 그래서 굳이 이중 루프를 이용해 전체를 탐색할 필요가 없음
        => 애초에 비슷한 것끼리 뭉쳐 있는 상태라서, local optimal ~ global optimal 기대 가능
        => 다만, 길이를 기준으로 정렬한게 아니라서, 슬라이싱 기준을 길이로 정해 줘야 한다.
"""
for _ in range(int(sys.stdin.readline())):
    checker, result = False, 'YES'
    num_list = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))]
    num_list.sort()
    for i in range(0, len(num_list)-1):
        if num_list[i][:min(len(num_list[i]), len(num_list[i+1]))] == num_list[i+1][:min(len(num_list[i]), len(num_list[i+1]))]:
            print('NO')
            checker = True
            break
    if not checker:
        print(result)
