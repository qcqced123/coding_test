import sys
"""
[풀이 시간]
1) 19:45 ~ 20:15

[요약]
1) 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임
    - 문자열의 뒤에 A를 추가한다.
    - 문자열을 뒤집고 뒤에 B를 추가한다.
    - S를 T로 변환하는 것이 가능한지 출력하기
[전략]
1) 서로 이웃한 알파벳 사이의 관계가 중요함
    - 각 단계 마다 문자열 T동일한 관계성을 갖게 되는지 판정 여부 따져 보기
    - 자료 구조는 리스트 활용!
=> 모르겠다 답지를 보자
=> 알고리즘에서 리스트를 뒤집겠다는 것은 값을 죄다 반전 시키는게 아니라 진짜 그냥 순서를 뒤집겠다는 의미
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
        T.reverse()  # list를 거꾸로
print(result)


