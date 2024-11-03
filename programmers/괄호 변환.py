import sys


def solution(p):
    """ 문제가 제시하는 순서대로 구현
    idea: stack, recursive call
    """
    answer = ""
    sys.setrecursionlimit(10 ** 6)

    def is_balanced(s) -> bool:
        return s.count("(") == s.count(")")

    def is_correct(s) -> int:
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif stack:
                stack.pop()
            else:
                return 0

        return not stack

    def make_correct(s) -> str:
        result = ""
        for c in s:
            if c == "(":
                result += ")"
            else:
                result += "("
        return result

    def recursive_func(arr) -> str:
        if len(arr) == 0:
            return ""

        # split current stack's array into two apart
        for i in range(2, len(arr) + 1, 2):
            u, v = arr[:i], arr[i:]
            if is_balanced(u):
                break
        # check current u is correct string
        if is_correct(u):
            return u + recursive_func(v)

        else:
            new = make_correct(u)
            return "(" + recursive_func(v) + ")" + new[1:-1]

    return recursive_func(p)


if __name__ == '__main__':
    solution("()))((()")
