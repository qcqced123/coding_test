import sys


def solution():
    expr = list(map(str, sys.stdin.readline().rstrip()))
    stack, ops, result = [], {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1}, ''
    for char in expr:
        if char.isalpha():
            result += char
            continue

        elif char == '(':  # 애초에 그냥 이렇게 넣고 다음 루프로 넘어가게 만들면 훨씬 간결하게 코드 작성이 가능하다...
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':  # 진짜 훨씬 간단하네 이렇게 코드 쓰는게... 하
                result += stack.pop()
            stack.pop()  # for pop (

        else:
            while stack and ops[stack[-1]] >= ops[char]:
                result += stack.pop()
            stack.append(char)

    while stack:
        result += stack.pop()
    print(result)


if __name__ == "__main__":
    solution()
