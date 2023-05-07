import sys
"""
[풀이 시간]
1) 19:45 ~ 20:15

[요약]
1) 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임
    - 문자열의 뒤에 A를 추가한다.
    - 문자열을 뒤집고 뒤에 B를 추가한다.
    - S를 T로 변환하는 것이 가능한지 출력하기
[Solution]
1) S를 T에 맞게 만드는 것은 경우의 수가 너무 많아지기 때문에, T를 S로 만들자!
"""
S = list(sys.stdin.readline().rstrip())
T = list(sys.stdin.readline().rstrip())
result = 0

for i in range(len(T)-1, -1, -1):
    if S == T:
        result = 1
        break

    if T[i] == 'A':
        T.pop()

    else:
        T.pop()
        T.reverse()
print(result)



