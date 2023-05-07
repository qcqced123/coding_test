import sys
"""
[풀이 시간]
1) 21:00 ~ 21:30

[요약]
1) 이진수 중에서 특별한 성질을 갖는 수: 이친수
    - 이친수는 0으로 시작 X
    - 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
    - 자리수에 해당되는 모든 숫자 중에서 이친수의 개수를 판정.
[전략]
1) 이전 자리수에 대한 판정 결과 및 현재 자리수에 대한 판정 결과를 동시에 사용 해야 해서 DP
    - Recursive Call, 근데 DP Memorization 한 번도 구현 안해봤는데 어케하지
    - 노가다를 통해서 점화식을 발견할 수 있었다.
"""
N = int(sys.stdin.readline())  # 숫자의 자리수
result_table, result = [0] * (N + 1), 0
result_table[1] = 1

if N >= 2:
    result_table[2] = 1

if N >= 3:
    for i in range(3, N+1):
        result_table[i] = result_table[i-1] + result_table[i-2]
print(result_table[N])
