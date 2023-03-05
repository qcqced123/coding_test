import sys
"""
[풀이 시간]
1) 12:00 ~ 12:45

[문제 요약]
1) LCS Problem
    - 모든 문자열은 대문자로 구성
    - 최대 1000글자
[Idea]
1) LCS: Dynamic Programming
    - 2D Array 구현 필요
    - 시간 제한도 여유로운 문제
"""
text1 = '%' + sys.stdin.readline().rstrip()
text2 = '%' + sys.stdin.readline().rstrip()

len_text1, len_text2 = len(text1), len(text2)
table = [[0]*len_text2 for _ in range(len_text1)]

for i in range(len_text1):
    for j in range(len_text2):
        if i == 0 or j == 0:
            table[i][j] = 0
        elif text1[i] == text2[j]:
            table[i][j] += table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])
print(table[-1][-1])


