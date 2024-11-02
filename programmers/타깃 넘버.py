import sys


def solution(numbers, target):
    """ 음이 아닌 정수, 더하거나 빼서 타겟값 만들기
    연산자 숫자 == 피연산자 숫자, 2**N
    idea: stack, recursive call, bf
        - number 배열 전처리
        - 인자 정의: (현재 수식, 현재 값)
        - 스택 종료 조건: 현재값 == 타겟값
        - 스택 호출 조건:
    """
    # preprocess numbers array
    arr = []
    ops = ["+"] * len(numbers)
    for i, j in zip(ops, numbers):
        arr.append(i)
        arr.append(j)

    # recursive call
    answer = 0
    sys.setrecursionlimit(10 ** 6)

    def recursive_func(cnt: list, curr: int) -> None:
        nonlocal answer
        if curr == target:
            answer += 1
            return

        for i in range(0, len(cnt), 2):  # search for only calc ops
            future = cnt[i + 2:]
            recursive_func(
                future,
                curr - 2 * cnt[i + 1]
            )
        return

    recursive_func(arr, sum(numbers))
    return answer


if __name__ == "__main__":
    solution([1, 1, 1, 1, 1], 3)

