import sys
"""
[풀이 시간]
01:55~02:55

[요약]
1) 주어지는 3개의 문자열에 대한 Longest Common Sub-Sequence 구하기
  - 즉 3개의 문자열에 공통으로 들어가는 문자 시퀀스 중에서 가장 긴 것의 길이를 출력
[전략]
1) O(n^3)까지는 허용이 안된다
2) 3개의 문자열 중에서 가장 작은 길이의 문자열을 선택
  -
"""
str_list = [sys.stdin.readline().rstrip() for _ in range(3)]
print(str_list)