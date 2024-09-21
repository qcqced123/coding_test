import sys


def solution():
    """ sliding window solution
    """
    def expand(right: int, state: set):
        candidate = 1
        while right < len(candies):
            state.add(candies[right])
            if len(state) >= 3:
                break

            right += 1
            candidate += 1
        return candidate

    N = int(sys.stdin.readline())
    candies = list(map(int, sys.stdin.readline().split()))

    result = 0
    for i in range(len(candies)):
        cnt_dict = {candies[i]}
        result = max(
            result,
            expand(i+1, cnt_dict)
        )
    print(result)


def review_solution():
    """ Three pointer solution
    1) 세트 길이가 1일 때: 오른쪽 포인터가 가리키는 값 추가, 오른쪽 포인터 한 칸 이동
    2) 세트 길이가 2일 때:
        현재 원소 == 세트 원소: 오른쪽 포인터 한 칸 이동
        현재 원소 != 세트 원소
    """
    N = int(sys.stdin.readline())
    candies = list(map(int, sys.stdin.readline().split()))

    result = 0
    fruits = [candies[0]]
    left, next_left, right = 0, 0, 1

    while right < N:
        if len(fruits) == 1 and candies[right] not in fruits:
            fruits.append(candies[right])

        else:
            if candies[right] not in fruits:
                result = max(result, right - left)
                for i in range(len(fruits)):
                    if fruits[i] != candies[next_left]:
                        fruits.pop(i)
                        break

                fruits.append(candies[right])
                left = next_left

        if candies[right-1] != candies[right]:
            next_left = right

        right += 1

    print(max(result, N-left))  # 그 경우는 여기서 처리하는구나


if __name__ == "__main__":
    review_solution()
