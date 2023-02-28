import sys
"""
[풀이 시간]
1) 12:45 ~ 01:45

[요약]
1) 주어지는 3개의 문자열에 대한 Longest Common Sub-Sequence 구하기
  - 즉 3개의 문자열에 공통으로 들어가는 문자 시퀀스 중에서 가장 긴 것의 길이를 출력
[전략]
1) O(n^3)까지는 허용이 안된다
2) Longest Common Sub-String Algorithm 사용
"""
# Input & Make 3D Array
str_1 = sys.stdin.readline().rstrip()
str_2 = sys.stdin.readline().rstrip()
str_3 = sys.stdin.readline().rstrip()

table = [[[0] * (len(str_3) + 1)] * (len(str_2) + 1)] * (len(str_1) + 1)
for i in range(1, (len(str_1)+1)):
    table[i][0][0] = str_1[i-1]
for j in range(1, (len(str_list[1])+1)):
    table[0][j][0] = str_list[0][j-1]
for k in range(1, (len(str_list[2])+1)):
    table[0][0][k] = str_list[0][k-1]
print(table)