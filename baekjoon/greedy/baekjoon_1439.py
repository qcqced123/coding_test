import sys

"""
[풀이 시간]
1) 00:20 ~ 00:40

[변수 설명]
S => 0 또는 1로 구성된 문자열

[목표 & 규칙]
1) 최소 시도로 숫자를 적절하게 뒤집어 모두 같은 숫자가 되도록
2) 연속된 같은 숫자만 한 번에 뒤집는 것이 가능함

[아이디어]
1) 0 또는 1의 개수를 비교해서 적은 쪽을 뒤집으면 되는 것 아닌가
=> 단순 개수를 세지 말고 덩어리 수를 세자
2) 내가 세운 식이 항상 지역 최소라고 보장할 수가 없구나..
"""

# Input
S = input()
zero_count = 0 # 0 뭉탱이 개수
one_count = 0 # 1 뭉탱이 개수

for idx, value in enumerate(S):
    if idx == len(S)-1:
        if value != S[idx - 1]:
            if value == "0":
                zero_count += 1
            if value == "1":
                one_count += 1
        break

    if value == S[idx+1]:
        continue

    if value != S[idx+1]:
        if value == "0":
            zero_count += 1
        if value == "1":
            one_count += 1

