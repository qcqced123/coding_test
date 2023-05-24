import sys
"""
[풀이 시간]
1) 04:30 ~ 05:00

[요약]
1) 주사위의 여섯 면에는 수가 쓰여 있고, 수가 밖으로 나오게 접는다
    - 같은 주사위 N**3개, 이걸로 정육면체를 만드려고 함
    - 정육면체는 탁자위에 있으므로, 5개의 면만 보임
    - 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값
[전략]
1) 여러 선택 옵션과 최소값을 찾아야 하는 전형적인 Greedy
    - 밖으로 보이는 면의 값이 제일 작아야 하는데, 바닥쪽 제외한 나머지 가장자리 위치한 주사위가 중요함
    - 어차피 정육면체 당 최대 노출면은 3개, 노출면의 개수에 따라서 규칙을 찾아보자
    - 1면 노출: 4(n-1)(n-2) + (n-2)**2
    - 2면 노출: 2(n-1) + 2(n-2)
    - 3면 노출: 4개
    => N = 1일 때 예외처리
    => 3면 노출의 경우 그냥 그대로 합을 구하는게 불가능하네
    => 각 면을 중심으로 옆에 면 2개 뽑기를 해야겠네
"""
N = int(sys.stdin.readline())
value_list = sorted(list(map(int, sys.stdin.readline().split())))
tmp3, tmp2, tmp1 = sum(value_list[0:3]), sum(value_list[0:2]), sum(value_list[0:1])

if N == 1:
    print(sum(value_list))
else:
    three = tmp3 * 4
    two = tmp2 * (2*(N-1) + 2*(N-2))
    one = tmp1 * (4 * (N-1)*(N-2) + (N-2)*(N-2))

    print(three + two + one)
