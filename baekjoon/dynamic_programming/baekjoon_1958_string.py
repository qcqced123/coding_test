import sys
"""
[풀이 시간]
1) 12:45 ~ 01:45

[요약]
1) 주어지는 3개의 문자열에 대한 Longest Common Sub-Sequence 구하기
  - 즉 3개의 문자열에 공통으로 들어가는 문자 시퀀스 중에서 가장 긴 것의 길이를 출력
[전략]
1) O(n^3)까지는 허용 가능
2) Longest Common Sub-String Algorithm 사용
    - 우리가 흔히 아는 LCS는 2개의 문자열을 비교
    - 여기 경우는 3개를 비교 해야 하기 때문에, 3차원 배열이 필요
    - 문자열의 최대 길이가 100이라서 3중 루프도 가능함
"""
# Input & Make 3D Array
str_1 = "%" + sys.stdin.readline().rstrip()
str_2 = "%" + sys.stdin.readline().rstrip()
str_3 = "%" + sys.stdin.readline().rstrip()

max_num = 0
table = [[([0] * len(str_3)) for _ in range(len(str_2))] for _ in range(len(str_1))] # 실제 테이블에 진짜 문자를 맵핑할 필요는 없음
for i in range(len(str_1)):
    for j in range(len(str_2)):
        for k in range(len(str_3)):
            if i == 0 or j == 0 or k == 0:
                table[i][j][k] = 0
            elif str_1[i] == str_2[j] and str_2[j] == str_3[k]:
                table[i][j][k] = table[i-1][j-1][k-1] + 1 # 대각선 + 1
                if max_num < table[i][j][k]:
                    max_num = table[i][j][k]
            else:
                continue
#                 table[i][j][-k] = max(table[i-1][j][k], table[i][j-1][k], table[i][j][k-1])
# print(table[len(str_1)-1][len(str_2)-1][len(str_3)-1])
print(max_num)
