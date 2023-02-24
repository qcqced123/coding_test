import sys
"""
[저자 아이디어]
1) 문제 목적이 주어진 문자열을 같은 숫자로 통일하는 것이기 때문에, 0으로 통일하는 경우 혹은 1로 통일하는 경우에 필요한 횟수를 비교하자 
"""

# Input
S = input()
zero_count = 0 # 모두 0으로 통일 하는 경우
one_count = 0 # 모두 1로 통일 하는 경우

# 첫번째 문자열 처리
if S[0] == '1':
    zero_count += 1
else:
    one_count += 1

for idx in range(len(S)-1):
    if S[idx] != S[idx + 1]:
        if S[idx + 1] == '1':
            zero_count += 1

        if S[idx + 1] == '0':
            one_count += 1

print(min(zero_count, one_count))

