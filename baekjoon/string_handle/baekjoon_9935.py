import sys
"""
[요약]
1) 폭발 문자열: 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다
    - 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열
    - 새로 생긴 문자열에 다시 폭발 문자열이 포함될 수도 있다
    - 폭발은 문자열에 폭발 문자열이 없을 때까지
    - 중복 없음, 영어의 대소문자, 숫자
    - 남은 문자열이 없는 경우: 'FRULA'
[전략]
1) while + if ~ in + replace
    - 입력 길이: 100만 (설계 알고리즘 < O(n^2))
    - replace: O(n)
    => 이거보다 더 빠른게 필요
2) stack + linear search + del
    - 문자열을 순차적으로 스택에 할당
"""
text, bomb = sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip()
stack = []

for char in text:
    stack.append(char)
    if ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]
print(''.join(stack) if len(stack) else "FRULA")
