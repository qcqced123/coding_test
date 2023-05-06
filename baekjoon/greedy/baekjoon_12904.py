import sys
"""
[풀이 시간]
1) 19:15 ~ 19:45

[요약]
1) 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임
    - 문자열의 뒤에 A를 추가한다.
    - 문자열을 뒤집고 뒤에 B를 추가한다.
    - S를 T로 변환하는 것이 가능한지 출력하기
[전략]
1) 서로 이웃한 알파벳 사이의 관계가 중요함
    - 각 단계 마다 문자열 T동일한 관계성을 갖게 되는지 판정 여부 따져 보기
    - 자료 구조는 리스트 활용!
"""
S = list(sys.stdin.readline().rstrip())
T = list(sys.stdin.readline().rstrip())

print(S, T)
