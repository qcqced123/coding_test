import sys

"""
[풀이 시간]
1) 11:15 ~ 11:35

[규칙]
1) 2를 곱한다
2) 숫자 1을 가장 오른쪽 자리에 추가
=> 2개의 연산만 사용 가능

[목표]
1) A를 B로 바꾸는데 필요한 연산의 최소 횟수 + 1 출력, 없으면 -1

[아이디어]
1) B -> A 역 연산을 진행하면 되겠다!
=> 만약 끝자리가 1이라면, 1을 빼주고
=> 끝자리가 1이 아니라면, 나누기 2를 해주고!
"""

# Input
A, B = map(int, sys.stdin.readline().split())
counter = 0 # 연산 횟수 저장용
checker = True
while checker:
    # B의 끝자리가 1인 경우
    if B % 10 == 1:
        B = (B -1)/10
        counter += 1
    # B의 끝자리가 1이 아닌 경우
    else:
        B = B / 2
        counter += 1

    if B == A:
        counter += 1
        checker = False
    if B < A:
        counter = -1
        checker = False

print(counter)


