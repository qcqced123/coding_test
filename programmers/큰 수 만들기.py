import sys


def solution(number, k):
    """ k개 제거후 최대값, 값을 빼야 하는 특정 시점을 알아내야 하기 때문에 스택 사용
    idea: stack
    """
    stack = []
    cache, pointer = 0, sys.maxsize
    arr = list(map(str, number))

    for num in arr:
        cnt = int(num)
        while stack and cache < k and cnt > pointer:
            stack.pop()
            cache += 1
            pointer = stack[-1] if stack else 0

        stack.append(cnt)
        pointer = cnt

    return "".join(list(map(str, stack[:len(stack) - (k - cache)])))


if __name__ == '__main__':
    solution("9876543214", 4)
