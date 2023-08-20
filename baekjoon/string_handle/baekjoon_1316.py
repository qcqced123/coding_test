import sys

"""
[풀이 시간]
1) 16:30 ~ 17:50

[요약]
1) 그룹 문자: ccazzzzbb, kin
    - 아닌 경우: aabbbccb (b가 혼자 떨어져 있기 때문에 그룹 문자열이 아님)
[전략]
"""
N = int(sys.stdin.readline())
result = N
for i in range(N):
    word_set = {1}
    word = list(sys.stdin.readline().rstrip())
    for j in range(len(word)):
        if word[j] in word_set:
            result -= 1
            break

        if j+1 != len(word) and word[j] != word[j+1]:
            word_set.add(word[j])
print(result)
