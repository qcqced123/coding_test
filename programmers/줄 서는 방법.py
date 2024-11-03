from math import factorial


def solution(n, k):
    """ 줄 세우기, 사전순 나열에서 K번쨰 배열 리턴
    idea: implementation
        - 20!이라서 backtracking 불가능
    """
    k -= 1
    answer = []
    numbers = list(range(1, n + 1))
    while numbers:
        idx, k = divmod(k, factorial(len(numbers) - 1))  # 남은 것 중에서 idx 번째 숫자를 append
        answer.append(numbers.pop(idx))

    return answer


if __name__ == '__main__':
    print(solution(4, 11))
