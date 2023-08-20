import sys

"""
[풀이 시간]
1) 15:45 ~ 16:15

[요약]
1) 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열
    - 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부름
    - 그냥 별거 없이 괄호만 제대로 양쪽에 있으면 되네
    - 주어진 입력이 VPS인지 아닌지 출력
[전략]
1) 
"""
for i in range(int(sys.stdin.readline())):
    left, right, checker = 0, 0, False
    ps = list(sys.stdin.readline().rstrip())
    for j in ps:
        if j == '(':
            left += 1
        else:
            right += 1
        if right > left:
            checker = True
            break
    if checker:
        print('NO')
        continue
    if left == right:
        print("YES")
    elif left != right:
        print("NO")
