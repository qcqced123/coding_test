import sys

"""
[시간]
1) 01:40 ~ 02:10
[요약]
1) S: 서로 다른 N개의 자연수들의 합
    => 이 때, 자연수 N의 최대값
[전략]
1) 자연수 개수가 최대가 되도록 만들 어야 하기 때문에 최대한 작은 수들의 합으로 S를 구성
    - 10: 1,2,3,4 => 4개
"""
S = int(sys.stdin.readline())

if S < 3:
    print(1)
else:
    result, tmp_sum = 0, 0
    for num in range(1, S):
        if S - tmp_sum >= num:
            tmp_sum += num
            result += 1
        else:
            break
    print(result)
